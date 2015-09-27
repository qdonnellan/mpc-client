from models.orbit import Orbit
from models.mpc_object import MpcObject


class Asteroid(MpcObject):
    """The asteroid object"""

    def __init__(self, query_result):
        """Initialize the asteroid instance

        Args:
            query_result: a json result from a query of the MPC web service
        """
        super(Asteroid, self).__init__(query_result)
        self.orbit = Orbit(self._data)

    @property
    def name(self):
        """The asteroid's name; e.g., Eros.  If the asteroid has not yet been
        named, this field will be None
        """
        return self._data.get('name', None)

    @property
    def number(self):
        """The asteroid's number; e.g. 433. If the asteroid has not yet been
        numbered, this field witll be None
        """
        return self._data.get('number', None)

    @property
    def designation(self):
        """The asteroid's provisional designation (e.g. 2014 AA) if it has not
        been numbered yet. If ths asteroid has been numbered this number is its
        permanent designation (padded with leading zeroes for a total of 7
        digits).
        """
        return self._data.get('designation', None)
