from requests import get
from bs4 import BeautifulSoup
import re

BASE_URL = "https://www.finn.no/"
def get_sort_opts(category, subcategory):
    """Get sorting options based on `category` and `subcategory`
    
    params:
    - `category`.
    - `subcategory`.
    """

    res = get(f"{BASE_URL}{category}/{subcategory}/search.html")
    
    soup = BeautifulSoup(res.content, "html.parser")
    return re.findall(r"value=\"(.*?)\"", str(soup.find(id="search-sorter")))


def get_subcategories(category):
    """Get valid subcategories for `category`.
    
    params:
    - `category`.
    """

    res = get(f"{BASE_URL}{category}/browse.html")
    
    soup = BeautifulSoup(res.content, "html.parser")
    return re.findall(r"\.no/(.*)search.html", str(soup.find(slot="links").find_all("a")))

