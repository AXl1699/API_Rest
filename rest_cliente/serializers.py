from rest_framework import serializers
from core.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields =['id_cliente','nombre_cliente','correo_cliente','telefono_cliente','direccion_cliente']
