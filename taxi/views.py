
"""Este módulo contém as views da API para a aplicação de táxi."""
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import TaxiSerializer , TaxiLocationSerializer
from .models import Taxi , Trajectories

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

    #@action(detail=True, methods= ['GET'])
    def list(self, request, pk=None):
 
        """
        Este método recebe o ID do táxi e a data como parâmetros e retorna as informações de 
        localização do táxi na data especificada.

        Parâmetros:
        request: Objeto de solicitação HTTP.
        pk: ID do táxi desejado.
        
        Retorno:
        Retorna um objeto Response com as informações de latitude, longitude e data da 
        trajetória do táxi, ou um objeto Response com status 404 se o táxi ou a data não 
        forem encontrados.
        """
 
        taxi = request.GET.get('taxi')
        date = request.GET.get('date')
        print(taxi)
        print(date)
        trajectories = Trajectories.objects.filter(taxi=taxi, date__date=date)
        print(trajectories.query)

        if not trajectories.exists():
            return Response({'error': 'Trajetórias não encontradas para o taxi na data especificada'}, status=404)
        serializer = TaxiLocationSerializer(trajectories, many=True)
        return Response(serializer.data)