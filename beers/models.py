import uuid
from django.db import models
from django.db.models.signals import post_save
from hashids import Hashids
hashids = Hashids(salt='thismysalt', min_length=4)


def update_producer_id_hash(sender, instance, created, **kwargs):
    instance.producer_id_hash = hashids.encode(instance.producer.id)


class Beer(models.Model):
    name = models.CharField(max_length=32, unique=True)
    power = models.DecimalField(max_digits=4, decimal_places=2)
    producer = models.ForeignKey('Producer')
    producer_id_hash = models.CharField(max_length=32, unique=False, default=uuid.uuid1)


class Producer(models.Model):
    name = models.CharField(max_length=32, unique=True)
    prizes = models.IntegerField(default=0)


class Bar(models.Model):
    name = models.CharField(max_length=32)
    beers = models.ManyToManyField('Beer')

post_save.connect(update_producer_id_hash, sender=Beer)
