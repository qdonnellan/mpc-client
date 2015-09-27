from decimal import Decimal, InvalidOperation


class MpcObject(object):
    """The Base MPC Object class, contains many useful methods"""

    def __init__(self, data):
        """Initializing an MpcObject instance

        Args:
            data: a dictionary/JSON object contaning all information related
                to this MPC object
        """
        self._data = data

    def _get_as_decimal(self, paramter_name):
        """Get the key from the MPC object data source and return the value
        as a Decimal object if possible, otherwise return None

        Args:
            parameter_name: the name of the paramter in the astroid data

        Returns:
            the value of the parameter as a Decimal object
        """
        try:
            return Decimal(self._data.get(paramter_name, None))
        except InvalidOperation:
            return None
