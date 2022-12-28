from bs4 import BeautifulSoup
import re

from FinnAPI import *


class FinnRealEstate(FinnAPI):
    _category = "realestate"
    BASE_URL = "https://finn.no/"
    
    def __init__(self, subcategory=None):
        super().__init__()

        if subcategory:
            self._subcategory = subcategory

        self._opts = self._searchkeys[self._category]
        self._vertical = self._opts["vertical"]
        self._searchkey_opts = self._opts["searchkeys"]
        self._searchkey = self._searchkey_opts[0]


    @property
    def sort(self):
        return self._sort
    
    @sort.setter
    def sort(self, value):
        if value in self._sort_opts:
            self._sort = value  
        else:
            raise ValueError(f"{value} is an invalid sort option, check FinnRealEstate._sort_opts for all valid options")  

    
    @property
    def search_key(self):
        """search_key :)
        """
        return self._searchkey

    @search_key.setter
    def search_key(self, value):
        if value in self._searchkey_opts:
            self._search_key = value
        else:
            raise ValueError(f"{value} is an invalid search key option, check FinnRealEstate._sort_key_opts for all valid options")  
    
    def _subcategories(self):
        """WARNING: makes a HTTP request everytime it is called.
        
        Gets all the valid subcategories for this category.

        Should probably be hardcoded in a seperate file instead as a request is sent everytime a call is made.
        """
        res = get(f"{self.BASE_URL}/{self._category}/")
        soup = BeautifulSoup(res.content, "html.parser")
        return re.findall(r"\.no/(.*)search.html", str(soup.find(slot="links").find_all("a")))

    def _sort_opts(self, subcategory=None):
        """WARNING: makes a HTTP request everytime it is called.

        gets all valid sort options for the category and subcategory.

        Should be replaced by hardcoded values.
        """
        if not self._subcategory and not subcategory:
            raise AttributeError("subcategory must be specified in order to use this method.")
        
        subcategory = subcategory if subcategory else self._subcategory

        res = get(f"{self.BASE_URL}/{self._category}/{self._subcategory}/search.html")
        soup = BeautifulSoup(res.content, "html.parser")
        return re.findall(r"value=\"(.*?)\"", str(soup.find(id="search-sorter")))