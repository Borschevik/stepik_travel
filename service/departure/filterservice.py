# Filter service for departure


class FilterService:
    """
    Service for filtering tours by deaprture location
    """

    def __init__(self, data: dict):
        """
        :param data: dict with nested tours data
        """

        self.data = data

    def filter(self, value: str) -> dict:
        """
        Departure location

        :param value: string
        :return: filtered departure dict
        """

        return {k: v for k, v in self.data.items() if v["departure"] == value}
