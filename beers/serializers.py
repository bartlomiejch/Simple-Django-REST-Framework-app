from rest_framework.serializers import ModelSerializer

from beers.models import Beer, Producer, Bar


class ProducerSerializer(ModelSerializer):
    class Meta:
        model = Producer
        fields = [
            'name',
            'prizes'
        ]
        lookup_field = 'name'
        extra_kwargs = {
            'url': {'lookup_field': 'name'}
        }


class BeerSerializer(ModelSerializer):
    producer = ProducerSerializer()
    class Meta:
        model = Beer
        fields = [
            'name',
            'power',
            'producer',
        ]


class BarSerializer(ModelSerializer):
    beers = BeerSerializer(many=True)
    class Meta:
        model = Bar
        fields = [
            'name',
            'beers'
        ]
