
import uuid
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .choices import *
# Create your models here.


def getuuid():
    return uuid.uuid4()

class Route(models.Model):
    rid = models.CharField(max_length=255,primary_key=True,null=False)
    rname = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.rid

class Stops(models.Model):
    sname = models.CharField(max_length=255)
    sroute = models.ForeignKey(Route, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.sname


class Buses(models.Model):
    unq = models.CharField(max_length=255,unique=True)
    bnum = models.CharField(max_length=255)
    broute = models.ForeignKey(Route, on_delete=models.CASCADE)
    b_cur_stop = models.ForeignKey(Stops, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        self.unq = getuuid()
        super(Buses, self).save(*args, **kwargs)
        
    def __str__(self) -> str:
        return self.bnum

class BStop(models.Model):
    unq = models.CharField(max_length=255,default=getuuid())
    num = models.CharField(max_length=255)
    route = models.CharField(max_length=255,choices=BUS_ROUTES)

    def __str__(self) -> str:
        return self.num

@receiver(post_save, sender=Buses)
def sendIntoSock(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()

    async_to_sync(channel_layer.group_send)(
        "bus_%s" % instance.unq, 
        {
            "type": "update_stop",
            "value": instance.b_cur_stop
        }
    )

