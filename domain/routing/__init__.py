class Pricer:
    def __init__(self):
        pass

    def get_pricing(self, origin, destiny):
        raise "Pricer::get_pricing must not be called directly, please, extends this class and override this method."


class Router:
    def __init__(self):
        pass

    def get_routing(self, origin, destiny):
        raise "Router::get_routing must not be called directly, please, extends this class and override this method."

    def build_routing(self,  origin_location, origin_coord, destiny_location, destiny_coord):
        pass


def coords_to_meters(self, origin_coord, destiny_coord):
    pass


def location_to_coords(self, origin, destiny):
    origin_coords = []
    destiny_coords = []

    return origin_coords, destiny_coords
