from . import Pricer, Router
from . import location_to_coords, coords_to_meters


class UberRouting(Pricer, Router):
    def __init__(self):
        Pricer.__init__(self)
        Router.__init__(self)

    def get_pricing(self, origin, destiny):
        origin_coord, destiny_coord = location_to_coords(origin, destiny)
        meters = coords_to_meters(origin_coord, destiny_coord)

        price = (meters/1000) * 1.4

        return price if price > 8 else 8

    def get_routing(self, origin, destiny):
        return origin, destiny

