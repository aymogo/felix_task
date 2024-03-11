from rest_framework import generics
from warehouse import models, serializers


class OrderProductView(generics.ListAPIView):
    queryset = models.OrderProduct.objects.all()
    serializer_class = serializers.OrderProductSerializer
