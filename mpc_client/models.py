from mpc_client.properties import (
    Time, Quantity, UnitlessQuantity, BooleanFlag
)
from astropy import units


class Asteroid(object):
    """The asteroid object"""

    def __init__(self, data):
        self.name = data.get('name', None)
        self.number = data.get('number', None)
        self.designation = data.get('designation', None)
        self.absolute_magnitude = UnitlessQuantity(
            data, 'absolute_magnitude')
        self.orbit = Orbit(data)


class Orbit(object):
    """The orbit object, belonging to a asteroid"""

    def __init__(self, data):
        """Initialize the orbit instance by passing the parent asteroid data

        Args:
            data: the parent Asteroid object data
        """
        self.updated = Time(data, 'orbit_updated_at', 'isot')
        self.epoch = Time(data, 'epoch_jd', 'jd')
        self.period = Quantity(data, 'period', 'yr')
        self.semimajor_axis = Quantity(data, 'semimajor_axis', 'AU')
        self.aphelion_distance = Quantity(data, 'aphelion_distance', 'AU')
        self.perihelion_distance = Quantity(data, 'perihelion_distance', 'AU')
        self.perihelion_date = Time(data, 'perihelion_date_jd', 'jd')
        self.argument_of_perihelion = Quantity(
            data, 'argument_of_perihelion', 'deg')
        self.ascending_node = Quantity(data, 'ascending_node', 'deg')
        self.inclination = Quantity(data, 'inclination', 'deg')
        self.eccentricity = UnitlessQuantity(data, 'eccentricity')
        self.mean_anomoly = Quantity(data, 'mean_anomoly', 'deg')
        self.mean_daily_motion = Quantity(
            data, 'mean_daily_motion', 'deg/day')
        self.phase_slope = UnitlessQuantity(data, 'phase_slope')
        self.type_id = data.get('orbit_type', None)
        self.type = self._get_orbit_type(self.type_id)
        self.delta_v = Quantity(data, 'delta_v', 'km/sec')
        self.tisserand_jupiter = UnitlessQuantity(data, 'tisserand_jupiter')
        self.neo = BooleanFlag(data, 'neo')
        self.km_neo = BooleanFlag(data, 'km_neo')
        self.pha = BooleanFlag(data, 'pha')
        self.moid = MoidCollection(data)

    @staticmethod
    def _get_orbit_type(type_id):
        """Return the named orbit type"""
        return {
            0: "Unclassified",
            1: "Atiras",
            2: "Atens",
            3: "Apollos",
            4: "Amors",
            5: "Mars Crossers",
            6: "Hungarias",
            7: "Phocaeas",
            8: "Hildas",
            9: "Jupitar Trojans",
            10: "Distant Objects"
        }.get(type_id, None)


class MoidCollection(object):
    """Minimum Orbit Intersection Distances collection"""

    def __init__(self, data):
        """Initialize the Moid collection using data from the parent asteroid

        Args:
            data: a dictionary containing all asteroid data
        """
        self.mercury = Quantity(data, 'mercury_moid', 'AU')
        self.venus = Quantity(data, 'venus_moid', 'AU')
        self.earth = Quantity(data, 'earth_moid', 'AU')
        self.mars = Quantity(data, 'mars_moid', 'AU')
        self.jupiter = Quantity(data, 'jupiter_moid', 'AU')
        self.saturn = Quantity(data, 'saturn_moid', 'AU')
        self.uranus = Quantity(data, 'uranus_moid', 'AU')
        self.neptune = Quantity(data, 'neptune_moid', 'AU')