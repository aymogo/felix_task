from rest_framework import serializers
from warehouse import models


class OrderProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=128)
    product_materials = serializers.SerializerMethodField()
    empty_warehouses = {}

    class Meta:
        model = models.OrderProduct
        fields = ("product_name", "product_qty", "product_materials")

    def get_product_materials(self, obj):
        empty_warehouses = self.empty_warehouses
        result_list = []
        for item in models.ProductMaterial.objects.filter(product=obj.pk):
            material_name = item.material.title
            required_quantity = obj.product_qty * item.quantity

            queryset = models.Warehouse.objects.filter(material=item.material).order_by("remainder")

            for q in queryset:
                if q.pk not in empty_warehouses:
                    empty_warehouses[q.pk] = q.remainder

                if empty_warehouses[q.pk] == 0:
                    continue

                if (required_quantity >= empty_warehouses[q.pk] and q != queryset.last()):
                    data = {
                        "warehouse_id": q.pk,
                        "material_name": material_name,
                        "qty": empty_warehouses[q.pk],
                        "price": q.price,
                    }
                    required_quantity -= empty_warehouses[q.pk]
                    empty_warehouses[q.pk] = 0
                elif required_quantity <= empty_warehouses[q.pk]:
                    data = {
                        "warehouse_id": q.pk,
                        "material_name": material_name,
                        "qty": required_quantity,
                        "price": q.price,
                    }
                    empty_warehouses[q.pk] -= required_quantity
                    required_quantity = 0
                elif q == queryset.last():
                    if required_quantity - empty_warehouses[q.pk] > 0:
                        data = [
                            {
                                "warehouse_id": q.pk,
                                "material_name": material_name,
                                "qty": empty_warehouses[q.pk],
                                "price": q.price,
                            },
                            {
                                "warehouse_id": None,
                                "material_name": material_name,
                                "qty": required_quantity - empty_warehouses[q.pk],
                                "price": None,
                            },
                        ]
                    else:
                        data = {
                            "warehouse_id": q.pk,
                            "material_name": material_name,
                            "qty": required_quantity,
                            "price": q.price,
                        }
                        required_quantity -= empty_warehouses[q.pk]
                        empty_warehouses[q.pk] = 0

                result_list.extend(data) if isinstance(data, list) else result_list.append(data)

        return result_list
