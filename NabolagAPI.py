import requests
import bs4
import json

URL = "https://profil.nabolag.no/"

def get_nabolag(finnkode: int) -> dict:
    """ Gets data about neighborhood near finnkode's location from "profil.nabolag.no"

    params:
    `finnkode` - valid finnkode
    """
    res = requests.get("".join((URL, str(finnkode))))

    if res.status_code == 200:
        soup = bs4.BeautifulSoup(res.content, "html.parser")

        return json.loads(soup.find(id="__NEXT_DATA__").text)