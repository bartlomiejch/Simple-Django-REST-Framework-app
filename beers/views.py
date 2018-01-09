from rest_framework import viewsets
from django.db.models import Q

from beers.models import Bar, Beer, Producer
from beers.serializers import BeerSerializer, ProducerSerializer, BarSerializer


class BeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer


class BarViewSet(viewsets.ModelViewSet):
    queryset = Bar.objects.all().order_by('beers')
    serializer_class = BarSerializer


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all().order_by('prizes')
    serializer_class = ProducerSerializer
    lookup_field = 'name'


class SpecialBeerViewSet(viewsets.ModelViewSet):
    queryset = Beer.objects.filter(Q(power__gt=2, power__lt=5, producer=Producer.objects.get(name='Browar Rodzinny')) | Q(power__gt=5, power__lt=9, producer=Producer.objects.get(name='Browar Lomza')))
    serializer_class = BeerSerializer
