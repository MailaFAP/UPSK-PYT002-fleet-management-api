"""Módulo contendo os serializers para a API da aplicação taxi"""

from rest_framework import serializers
from .models import Taxi
from .models import Trajectories

class TaxiSerializer(serializers.ModelSerializer):
    """Serializador para objetos da classe Taxi do modelo Taxi"""
    class Meta:
        """ Classe Meta para definir metadados para o TaxiSerializer. 
        Aqui, configuramos o modelo a ser serializado (models.Taxi) e os campos que devem ser 
        incluídos na serialização. """
        model = Taxi
        fields = '__all__'
        
class TaxiLocationSerializer(serializers.ModelSerializer):
    """Serializador para objetos da classe Trajectories do modelo Trajectories"""
    class Meta:
        """ Classe Meta para definir metadados para o TaxiLocationSerializer. 
        Aqui, configuramos o modelo a ser serializado (models.TaxiLocation) e os campos que devem ser 
        incluídos na serialização. """
        model = Trajectories
        fields = '__all__'