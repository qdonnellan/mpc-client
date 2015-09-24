import requests
import settings


class Query(object):
    """Query client the Minor Planet Center web service"""

    def __init__(self):
        """Initialize a query with the default parameters"""
        self.parameters = {"json": 1}

    def limit(self, number_of_results):
        """Add a limit parameter to this query

        Args:
            number_of_results: an integer representing the maximum number of
                objects that the web_servce should return

        Returns:
            this Query object
        """
        self.parameters['limit'] = number_of_results
        return self

    def filter(self, **kwargs):
        """Filter the query by adding additional parameters

        Returns:
            this Query object
        """
        self.parameters.update(kwargs)
        return self

    def _request_data(self):
        """Request data from the web service, return response

        Returns:
            requests.response object
        """
        return requests.post(
            url=settings.WEB_SERVICE_URL,
            params=self.parameters,
            auth=(settings.USRENAME, settings.PASSWORD)
        )
