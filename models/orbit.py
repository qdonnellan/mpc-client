from datetime import datetime

class Orbit(object):
    """Orbit object for an asteroid; contains all orbit related parameters"""

    def __init__(self, asteroid_data):
        """Initialize an orbit instance using parent asteroid data

        Args:
            asteroid_data: json-like data returned from a query of the MPC
                web service
        """
        self._data = asteroid_data

    @property
    def updated(self):
        """Date-time instance for when the orbits-table for the related
        asteroid was last updated.
        """
        timestamp = self._data.get('orbit_updated_at', None)
        # TODO: need to convert to actual datetime object...
