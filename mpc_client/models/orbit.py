from astropy.time import Time
from astropy import units
from mpc_client.models.mpc_object import MpcObject


class Orbit(MpcObject):
    """Orbit object for an asteroid; contains all orbit related parameters"""

    @property
    def updated(self):
        """Date/time when the orbits-table was last updated.

        Returns:
            astropy.time.Time object, the last time this orbit was udpated
        """
        timestamp = self._data.get('orbit_updated_at', None)
        return Time(timestamp, format='isot')

    @property
    def epoch(self):
        """The date/time of reference for the current orbital parameters.

        Returns:
            astropy.time.Time object, the current epoch
        """
        timestamp = self._data.get('epoch_jd', None)
        return Time(float(timestamp), format='jd') if timestamp else None

    @property
    def period(self):
        """The time, in years, it takes for this asteroid to orbit the Sun.

        Returns:
            Decimal number of years of period, or None if the data is not a
            valid number
        """
        return self._get_as_decimal('period') * units.yr

    @property
    def semimajor_axis(self):
        """One half of the longest diameter of the orbital ellipse.

        Returns:
            Decimal, the length of the semimajor axis in Astronomical Units
        """
        return self._get_as_decimal('semimajor_axis') * units.AU

    @property
    def aphelion_distance(self):
        """The distance when the asteroid is farthest from the Sun in its
        orbit.
        """
        return self._get_as_decimal('aphelion_distance')

    @property
    def perihelion_distance(self):
        """The distance when the asteroid is nearest to the Sun in its orbit.

        Returns:
            Decimal, the perihelion distance in Astronomical Units
        """
        return self._get_as_decimal('perihelion_distance')

    @property
    def perihelion_date(self):
        """The date when the asteroid is at perihelion (its closest point
        to the Sun).

        Returns:
            astropy.time.Time object
        """
        timestamp = self._data.get('perihelion_date_jd', None)
        return Time(float(timestamp), format='jd') if timestamp else None

    @property
    def argument_of_perihelion(self):
        """The orientation of the ellipse in the orbital plane and is
        the angle from the asteroid's ascending noe to its perihelion,
        measured in the direction of motion.

        Returns:
            Decimal, an angle in Degrees (Range 0-360)
        """
        return self._get_as_decimal('argument_of_perihelion')

    @property
    def ascending_node(self):
        """The longitude of the ascending node, it defines the horizontal
        orientation of the ellipse with respect to the ecliptic, and is the
        angle measured counterclockwise (as seen from North of the ecliptic)
        from the First Point of Aires to the ascending node.

        Returns:
            Decimal, an angle in Degrees (Range 0-360)
        """
        return self._get_as_decimal('ascending_node')

    @property
    def inclination(self):
        """The angle between the asteroid's orbit and the ecliptic

        Returns:
            Decimal, an angle in Degrees (Range 0-180)
        """
        return self._get_as_decimal('inclination')

    @property
    def eccentricity(self):
        """Measure of how far the orbit shape departs from a circle where
        0 is a perfect circle and 1 is a parabola

        Returns:
            Decimal between 0 and 1
        """
        return self._get_as_decimal('eccentricity')

    @property
    def mean_anomoly(self):
        return self._get_as_decimal('mean_anomoly')

    @property
    def mean_daily_motion(self):
        return self._get_as_decimal('mean_daily_motion')

    @property
    def phase_slope(self):
        return self._get_as_decimal('phase_slope')

    @property
    def orbit_type_id(self):
        return self._data.get('orbit_type', None)

    @property
    def orbit_type(self):
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
        }.get(self.orbit_type_id, None)

    @property
    def delta_v(self):
        return self._get_as_decimal('dalta_v')

    @property
    def tisserand_jupiter(self):
        return self._get_as_decimal('tisserand_jupiter')


