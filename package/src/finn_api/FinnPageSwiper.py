from FinnAPI import FinnAPI
from requests import Response

class FinnPageSwiper:
    """ Quick and dirty implementation of a page swiper.
    Params:
    - `searchkey` - category to query.
    - `start_page` - starting page to request, defaults to `1`.
    - `end_page` - last page to request, maximum value is `50`, defaults to `1`.
    """

    def __init__(self, searchkey: str, start_page: int = 1, end_page: int = 1) -> None:
        self._finn_api = FinnAPI(searchkey)

        if end_page > 50:
            self._end_page = 50
        elif end_page > start_page:
            self._end_page = 1
            self._start_page = 1
        elif end_page < 1 > start_page:
            self._end_page = 1
            self._start_page = 1
        else:
            self._start_page = start_page
            self._end_page = end_page

    def __call__(self) -> Response:
        """ Makes requests to API.
        
        Yields:
        - `requests.Response`.
        """

        page = self._start_page
        max_pages = self._end_page
        
        while page <= max_pages:
            res = self._finn_api(page=page)
            
            if res.status_code != 200:
                yield res

            if page == self._start_page:
                json = res.json()
                if max_pages > (res_pages:=json["metadata"]["paging"]["last"]):
                    max_pages = res_pages

                print(
                    f"matches: {json['metadata']['result_size']['match_count']}",
                    f"pages: {res_pages}", sep="\n"
                )
            
            yield res
            page+=1