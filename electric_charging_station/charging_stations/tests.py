from django.test import TestCase

# Create your tests here.


from charging_stations.models import ChargingStation, ChargingPoint


def create_charging_station(name):
    return ChargingStation.objects.create(
        name=name,
        lat=0,
        long=0
    )


def create_charging_point(charging_station, p_no):
    return ChargingPoint.objects.create(
        port_number=p_no,
        charging_fee=1,
        status=ChargingPoint.STATUS_CHOICES[0][0],
        charging_station=charging_station
    )


class ModelTestCase(TestCase):
    def setUp(self):
        super(ModelTestCase, self).setUp()
        self.charging_station = create_charging_station(name='abc')
        self.charging_point1 = create_charging_point(charging_station=self.charging_station, p_no=1)
        self.charging_point2 = create_charging_point(charging_station=self.charging_station, p_no=2)
        self.charging_point3 = create_charging_point(charging_station=self.charging_station, p_no=3)

    def test_many_one_relation(self):
        self.assertEqual(self.charging_point1.charging_station, self.charging_station)
        self.assertEqual(self.charging_point2.charging_station, self.charging_station)
        self.assertEqual(self.charging_point3.charging_station, self.charging_station)

    def test_check_charging_point_exists(self):
        charging_station = create_charging_station(name='xyz')
        charging_point_exists = ChargingStation.objects.check_charging_point_exists(self.charging_point1)
        self.assertTrue(charging_point_exists)
