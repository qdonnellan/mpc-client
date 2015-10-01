from .properties import Time, Quantity, BooleanFlag


class BaseMpcObject(object):
    def __getattribute__(self, attr):
        obj = object.__getattribute__(self, attr)
        if hasattr(obj, '__get__'):
            return obj.__get__(self, type(self))
        return obj


class Asteroid(BaseMpcObject):
    """The asteroid object"""

    def __init__(self, data):
        self.name = data.get('name', None)
        self.number = data.get('number', None)
        self.designation = data.get('designation', None)
        self.absolute_magnitude = Quantity(data, 'absolute_magnitude')
        self.albedo = Quantity(data, 'albedo')
        self.albedo_uncertainty = Quantity(data, 'albedo_unc')
        self.diameter = Quantity(data, 'diameter', 'km')
        self.diameter_uncertainty = Quantity(data, 'diameter_unc', 'km')
        self.binary = data.get('binary_object', None)
        self.orbit = Orbit(data)
        self.neowise = Neowise(data)


class Orbit(BaseMpcObject):
    """The orbit object, belonging to a asteroid"""

    def __init__(self, data):
        """Initialize the orbit instance by passing the parent asteroid data

        Args:
            data: the parent Asteroid object data
        """
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
        self.eccentricity = Quantity(data, 'eccentricity')
        self.mean_anomoly = Quantity(data, 'mean_anomoly', 'deg')
        self.mean_daily_motion = Quantity(
            data, 'mean_daily_motion', 'deg/day')
        self.phase_slope = Quantity(data, 'phase_slope')
        self.type_id = data.get('orbit_type', None)
        self.type = self._get_orbit_type(self.type_id)
        self.delta_v = Quantity(data, 'delta_v', 'km/sec')
        self.tisserand_jupiter = Quantity(data, 'tisserand_jupiter')
        self.neo = BooleanFlag(data, 'neo')
        self.km_neo = BooleanFlag(data, 'km_neo')
        self.pha = BooleanFlag(data, 'pha')
        self.moid = MoidCollection(data)

    @classmethod
    def _get_orbit_type(cls, type_id):
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


class MoidCollection(BaseMpcObject):
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


class Neowise(BaseMpcObject):
    """A collection of calculations from the NEOWISE team"""

    def __init__(self, data):
        """Initialize the neowise collection object

        Args:
            data: a dictionary containing all asteroid data
        """
        self.absolute_magnitude = Quantity(data, 'h_neowise')
        self.phase_slope = Quantity(data, 'g_neowise')
        self.albedo = Quantity(data, 'albedo_neowise')
        self.albedo_uncertainty = Quantity(data, 'albedo_neowise_unc')
        self.diameter = Quantity(data, 'diameter_neowise', 'km')
        self.diameter_uncertainty = Quantity(
            data, 'diameter_neowise_unc', 'km')
