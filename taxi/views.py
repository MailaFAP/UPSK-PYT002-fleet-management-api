
"""Este módulo contém as views da API para a aplicação de táxi."""
from rest_framework import viewsets
from .serializers import TaxiSerializer
from .models import Taxi

class TaxiViewSet(viewsets.ModelViewSet):
    """Viewset que fornece endpoints para operações CRUD na entidade Taxi.
    
    Atributos:
    serializer_class: Classe de serialização utilizada para transformar objetos Taxi em dados JSON.
    queryset: Queryset que retorna todos os objetos da classe Taxi.
    """
    serializer_class = TaxiSerializer
    queryset = Taxi.objects.all()
