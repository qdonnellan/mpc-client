import requests
import settings
from models.asteroid import Asteroid


class Query(object):
    """Query client the Minor Planet Center web service"""

    def __init__(self):
        """Initialize a query with the default parameters"""
        self._parameters = {"json": 1}
        self._results = []

    def __iter__(self):
        """Return the results of the query if it has alredy been run, or
        run the query if it hasn't and then return

        Returns:
            an interable containing the results of this query
        """
        if not self._results:
            self.run()
        return (Asteroid(x) for x in self._results)

    def limit(self, number_of_results):
        """Add a limit parameter to this query

        Args:
            number_of_results: an integer representing the maximum number of
                objects that the web_servce should return

        Returns:
            this Query object
        """
        self._parameters['limit'] = number_of_results
        return self

    def filter(self, **kwargs):
        """Filter the query by adding additional parameters

        Args:
            kwargs: any number of arguments and their values, expected to match
                up with the published MPC parameters. For example:
                filter(eccentricity_min=0.95)

        Returns:
            this Query object
        """
        self._parameters.update(kwargs)
        return self

    def run(self):
        """Run this Query and save the results in _results

        Returns:
            a list, the result of running this query
        """
        self._results = self._request_data().json()
        return self._results

    def _request_data(self):
        """Request data from the web service, return response

        Returns:
            requests.response object
        """
        return requests.post(
            url=settings.WEB_SERVICE_URL,
            params=self._parameters,
            auth=(settings.USRENAME, settings.PASSWORD)
        )
