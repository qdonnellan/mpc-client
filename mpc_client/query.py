"""query.py - a query client used to access the mpc_client API
"""


import requests
from . import settings
from .models import Asteroid
import os
import json


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
        return self.all()

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

    def order(self, parameter, desc=False):
        """Order the results by the parameter given. Results are ascending
        unless desc=True

        Args:
            parameter (string): the name of the parameter that should be used
                to order the result set
            desc (boolean): True if the results should be in descending order

        Returns:
            this Query object
        """
        if desc:
            self._parameters['order_by_desc'] = parameter
            self._parameters.pop('order_by', None)
        else:
            self._parameters['order_by'] = parameter
            self._parameters.pop('order_by_desc', None)
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
            this Query object
        """
        self._results = self._request_data().json()
        return self

    def all(self):
        """Return the results as a collection of Asteroid objects

        Returns:
            a list of Asteroid objects
        """
        return (Asteroid(x) for x in self._results)

    def first(self):
        """"Return the first result as an Asteroid object

        Returns:
            a single Asteroid object if there is at least 1 result, None
            otherwise
        """
        if not self._results:
            self.run()
        if len(self._results) > 0:
            return Asteroid(self._results[0])

    def save_to_file(self, filename):
        """Save the current query results to a file, for use later"""
        filepath = os.path.join(settings.STORAGE_DIR, filename)
        if not self._results:
            self.run()
        with open(filepath, 'w+') as outfile:
            json.dump(self._results, outfile)

    def load_from_file(self, filename):
        """Load a previously saved results query from a file

        Returns:
            this Query object
        """
        filepath = os.path.join(settings.STORAGE_DIR, filename)
        with open(filepath, 'r') as infile:
            self._results = json.load(infile)
        return self

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
