from django import template

registry = template.Library()

@registry.simple_tag()
def get_charging_points(charging_station):
    return charging_station.charging_point.all()