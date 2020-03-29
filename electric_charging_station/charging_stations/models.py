from django.db import models

# Create your models here.


class ChargingStationQuerySet(models.QuerySet):

    def filter_by_name(self, name):
        return self.filter(name=name)

    def check_charging_point_exists(self, charging_point):
        return self.filter(charging_point__id=charging_point.id).exists()


class ChargingStation(models.Model):
    name = models.CharField(null=True, max_length=50, default='Sample Name', unique=True)
    addr = models.CharField(name='address', null=False, max_length=500)
    lat = models.IntegerField(null=False)
    long = models.IntegerField(null=False)
    parking_fee = models.PositiveIntegerField(null=True)

    class Meta:
        app_label = 'charging_stations'
        verbose_name = 'charging_station'
        verbose_name_plural = 'charging_stations'
        indexes = [models.Index(fields=['name'])]

    objects = ChargingStationQuerySet.as_manager()

    @property
    def lat_long(self):
        return self.lat, self.long


class ChargingPoint(models.Model):
    STATUS_CHOICES = (
        ('active', 'active'),
        ('occupied', 'occupied'),
        ('inactive', 'inactive'),
        ('free', 'free')
    )
    port_no = models.CharField(name='port_number', unique=True, null=False, max_length=15)
    charging_fee = models.PositiveIntegerField(null=False, default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=20)
    charging_station = models.ForeignKey('ChargingStation', related_name='charging_point',
                                         on_delete=models.DO_NOTHING)

    class Meta:
        app_label = 'charging_stations'
        verbose_name = 'charging_point'
        verbose_name_plural = 'charging_points'
        indexes = [models.Index(fields=['port_number'])]

    def natural_key(self):
        return self.port_no, self.charging_fee, self.status
