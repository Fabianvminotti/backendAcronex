from dataclasses import fields
from rest_framework import serializers
from .models import maquinas

class maquinasSerializer(serializers.ModelSerializer):
    class Meta:
        model = maquinas
        fields=('id' ,'nombre','clase','empresa','estado')

          