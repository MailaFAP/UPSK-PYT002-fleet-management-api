"""modelagem de dados """
from django.db import models


class Taxi(models.Model):
    """
    Modelo que representa um táxi na aplicação.

    Atributos:
    - id: chave primária autoincrementada que identifica o táxi
    - plate: placa do táxi (máx. 10 caracteres)
    """
    id = models.AutoField('id', primary_key=True)
    plate = models.CharField('plate', max_length=10)

    class Meta:
        """classe para ordenar os dados de acordo com o id do taxi"""
        ordering = ['id']


class Trajectories(models.Model):
    """ Modelo para armazenar informações sobre trajetórias de táxis. Campos:

    id: identificador único da trajetória
    taxi_id: identificador do táxi
    date: data em que a trajetória foi registrada
    longitude: longitude do local da trajetória
    latitude: latitude do local da trajetória """

    id = models.AutoField('id', primary_key=True)
    taxi = models.ForeignKey(Taxi , on_delete=models.CASCADE)
    date = models.DateTimeField('date')
    longitude = models.FloatField('longitude')
    latitude = models.FloatField('latitude')

    class Meta:
        """classe para ordenar os dados de acordo com o id do taxi"""
        ordering = ['id']
