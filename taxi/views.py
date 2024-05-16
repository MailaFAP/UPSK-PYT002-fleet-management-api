
"""Este módulo contém as views da API para a aplicação de táxi."""
from rest_framework import viewsets
from .serializers import TaxiSerializer, TaxiLocationSerializer
from .models import Taxi, Trajectories


class TaxiViewSet(viewsets.ModelViewSet):
    """Viewset que fornece endpoints para operações CRUD na entidade Taxi.

    Atributos:
    serializer_class: Classe de serialização utilizada para transformar objetos Taxi em dados JSON.
    queryset: Queryset que retorna todos os objetos da classe Taxi.
    """
    serializer_class = TaxiSerializer
    queryset = Taxi.objects.all()


class TaxiLocationView(viewsets.ModelViewSet):
    """ Classe que representa a visualização de localização de táxi.Esta classe herda de ModelViewSet 
    e possui o método get para obter informações de localização de um táxi de determinada data.

    Parâmetros:
    taxi_id: ID do táxi desejado.
    date: Data da qual se deseja obter as informações de localização.

    Retorno:
    Retorna um Response com as informações de latitude, longitude e data da trajetória do táxi 
    correspondente ao ID informado na data especificada."""
    serializer_class = TaxiLocationSerializer
    queryset = Trajectories.objects.all()