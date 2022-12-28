from requests import get, Response
from .search_key import SearchKey

from typing import Union, AnyStr

class FinnAPI:
    """The core of the API interface.

    Params:
    - `searchkey` - category to query.
    """

    API = "https://www.finn.no/api"

    def __init__(self, searchkey: Union[AnyStr, SearchKey]):
        self._vertical = "a"
        self._searchkey = searchkey.upper()

    def get_valid_filters(self) -> dict:
        valid_filters = self.__call__().json()["filters"]
        
        return {
            filter["name"]:filter["type"] 
            for filter in valid_filters
        }

    def __call__(self, **filters) -> Response:
        """
        Params:
        - `**filters` - filters for query, use `get_valid_filters` to get a list of valid filters.

        Returns:
        - `requests.response`.
        """

        return get(self._build_url(filters))


    def _build_url(self, filters: dict):
        """Builds the final url.

        Params:
        - `filters`
        """

        base = f"{self.API}/search-qf?searchkey={self._searchkey}&vertical={self._vertical}"
        
        if filters:
            for name, value in filters.items():
                base = f"{base}&{name}={value}"

        return base