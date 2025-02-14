from rest_framework import serializers
from .models import Pessoa

class PessoaSerializer(serializers.ModelSerializer):
    setor_display = serializers.CharField(source='get_setor_display', read_only=True) 
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'setor', 'setor_display', 'email']  
