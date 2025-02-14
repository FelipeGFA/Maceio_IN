from rest_framework import generics
from .models import Pessoa
from .serializers import PessoaSerializer  

class PessoaListCreateAPIView(generics.ListCreateAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer

class PessoaRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pessoa.objects.all()
    serializer_class = PessoaSerializer
    lookup_field = 'pk'  
