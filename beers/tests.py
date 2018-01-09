import json
from django.test import TestCase

from .models import Beer, Producer, Bar
from .views import (BeerViewSet, BarViewSet,
    ProducerViewSet, SpecialBeerViewSet)


class AppTest(TestCase):
    """Test module for beers app"""

    def setUp(self):
        producer = Producer.objects.create(name='a', prizes=1)
        beer = Beer.objects.create(name='test_beer',
             power=3, producer=producer)
        bar = Bar.objects.create(name='test_bar')
        bar.beers.add(beer)

    def test_beer_view(self):
        response = self.client.get('/beers/')
        self.assertEqual(response.status_code, 200)
        expectedJSON = json.dumps({'count': 1,
                                    'next': None,
                                    'previous': None,
                                    'results': [{'name': 'test_beer',
                                    'power': '3.00',
                                    'producer': {'name': 'a', 'prizes': 1}}]})
        self.assertJSONEqual(str(response.content, encoding='utf8'), expectedJSON)

    def test_bar_view(self):
        response = self.client.get('/bars/')
        self.assertEqual(response.status_code, 200)
        expectedJSON = json.dumps({'count': 1,
                                    'next': None,
                                    'previous': None,
                                    'results': [{'beers': [{'name': 'test_beer',
                                    'power': '3.00',
                                    'producer': {'name': 'a', 'prizes': 1}}],
                                    'name': 'test_bar'}]})
        self.assertJSONEqual(str(response.content, encoding='utf8'), expectedJSON)


    def test_producer_view(self):
        response = self.client.get('/producers/')
        self.assertEqual(response.status_code, 200)
        expectedJSON = json.dumps({'count': 1,
                                    'next': None,
                                    'previous': None,
                                    'results': [{'name': 'a', 'prizes': 1}]})
        self.assertJSONEqual(str(response.content, encoding='utf8'), expectedJSON)

    def test_special_beer_view(self):
        response = self.client.get('/special_beers/')
        self.assertEqual(response.status_code, 200)
        expectedJSON = json.dumps({'count': 1,
                                    'next': None,
                                    'previous': None,
                                    'results': [{'name': 'test_beer',
                                    'power': '3.00',
                                    'producer': {'name': 'a', 'prizes': 1}}]})
        self.assertJSONEqual(str(response.content, encoding='utf8'), expectedJSON)
