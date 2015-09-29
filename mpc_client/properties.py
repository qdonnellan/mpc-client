import astropy
from decimal import Decimal, InvalidOperation

class Time(object):
    """An astropy time property"""

    def __init__(self, data, key, time_format):
        """Initialize a TimeProperty instance by saving the raw value of
        data[key] to this class. We will compute the actual time object only on
        demand.

        Args:
            data: a dictionary containing many keys including the expected key
            key: a string key expected to exist in data
            time_format: a string indicating format of the time anticipated in
                the data dictionary, see the astropy.time docs for appropriate
                time formats:
                http://docs.astropy.org/en/stable/api/astropy.time.Time.html
        """
        self.value = None
        self._raw_value = data.get(key, None)
        self._time_format = time_format

    def __get__(self, instance, owner):
        """Only when the value of the instance is requested do we attempt to
        calculate the time object

        Returns:
            an astropy.Time object
        """
        if not self.value:
            self.value = self._create_time()
        return self.value

    def _create_time(self):
        """Create an astropy.Time object from the _raw_value saved to this
        instance

        Returns:
            an astropy.Time object
        """
        return astropy.time.Time(self._raw_value, format=self._time_format)


class Quantity(object):
    """A Quantity property - something with value an units"""

    def __init__(self, data, key, units):
        """Initialize the Quantity property instance by saving the raw value
        of data[key] to this instance. We will calculate the actual Quantity
        only on demand

        Args:
            data: a dictionary containing many keys including the expected key
            key: a string key expected to exist in data
            unit_format: a string key denoting the appropriate units to use
        """
        self.value = None
        self._raw_value = data.get(key, None)
        self._units = units

    def __get__(self, instance, owner):
        if not self.value:
            self.value = self._create_quantity()
        return self.value

    def _create_quantity(self):
        """Create an astropy.Quantity instnace by multiplying a decimal
        representation of the raw value with the astropy.units object
        associated with this instance.

        Returns:
            an astropy.Quantity object or None if it cannot be created from
            the known values
        """
        try:
            return Decimal(self._raw_value) * self._get_astropy_units()
        except InvalidOperation:
            return None

    def _get_astropy_units(self):
        """Return the appropriate astropy units object"""
        valid_units = {
            'yr': astropy.units.yr,
            'AU': astropy.units.AU,
            'deg': astropy.units.deg,
            'deg/day': astropy.units.deg / astropy.units.d
        }
        return valid_units.get(self._units, None)


class UnitlessQuantity(object):
    """Returns a simple Decimal representation of a number"""

    def __init__(self, data, key):
        """Initialize the Quantity property instance by saving the raw value
        of data[key] to this instance. We will calculate the actual Decimal
        only on demand

        Args:
            data: a dictionary containing many keys including the expected key
            key: a string key expected to exist in data
        """
        self.value = None
        self._raw_value = data.get(key, None)

    def __get__(self, instance, owner):
        if not self.value:
            self.value = self._create_quantity()
        return self.value

    def _create_quantity(self):
        """Create a Decimal instnace from the known raw value

        Returns:
            a Decimal object or None if it cannot be created from the known
            values
        """
        try:
            return Decimal(self._raw_value)
        except InvalidOperation:
            return None


class BooleanFlag(object):
    """Returns a simple boolean value based on the raw input"""

    def __init__(self, data, key):
        self.value = None
        self._flag = data.get(key, None)

    def __get__(self, instance, owner):
        if self.value is None:
            self.value = self._flag == 1
        return self.value
