from requests import get, HTTPError
from bs4 import BeautifulSoup
import re
from typing import Union

class FinnAd:
    """Scrapes data from a specific finn ad.

    The class represents a single ad and its contents.

    Params:
    - `finnkode` - a valid finnkode.
    """
    
    _BASE_URL = "https://finn.no/"
    
    def __init__(self, finnkode: Union[int, str]):
        self.finnkode = str(finnkode)
        self.ad_resp = get(
            self._BASE_URL + self.finnkode)

        if (s_c:=self.ad_resp.status_code) != 200:
            if s_c == 404:
                raise HTTPError(
                    f"Got 404. Valid finnkode?"
                )
            raise HTTPError(
                f"Something went wrong, status code: {s_c}."
            )
        self._soup = BeautifulSoup(self.ad_resp.content, "html.parser")


    @property
    def images(self) -> list:
        """ Extracts links and image titles for all images belonging to the ad.
        """

        if not hasattr(self, "_images"):
            self._images = []

            for img_tag in self._soup.find(id="main-carousel").find_all("img"):
                self._images.append(
                    {
                        "img_title": img_tag.attrs.get("title", ""),
                        "img_url": img_tag.attrs.get("data-srcset", "").split()[0]
                    }
                )

        return self._images


    @property 
    def ad_title(self):
        """ Title of the ad
        """

        if not hasattr(self, "_ad_title"):
            self._ad_title = self._soup.find("title").text
        
        return self._ad_title


    @property 
    def ad_short_description(self):
        """ Ad description
        """

        if not hasattr(self, "_ad_description"):
            try:
                self._ad_short_description = re.search(r"<meta content=\"(.*)\" name=\"description\"", str(self._soup.find("head"))).group(1)
            except: 
                self._ad_short_description = ""
        return self._ad_short_description


    @property
    def ad_description(self):
        """ Ad complete description"""
        raise NotImplementedError

    @property 
    def ad_map(self):
        """ Map-link to ad (or implement seperate instance of FinnkartAPI)
        """

        return self._ad_map

    @property
    def ad_details(self):
        """ Ad information
        """
        if not hasattr(self, "_ad_info"):
            self._ad_details = {}
            details = self._soup.find_all("dl")

            if details:
                for detail in details:
                    for label, value in zip(detail.find_all("div"), detail.find_all("dd")):
                        self._ad_details[label["data-testid"]] = str.replace(
                            str.replace(value.text, u"\xa0", ""), u"\n", "")
            
            bap_desc = self._soup.find(id="bapDescriptionContent")
            
            if bap_desc:
                self._ad_details["bap_description"] = re.sub(u"\r\n", " ", bap_desc.text.strip(u"\n").strip())

            facilities = self._soup.find("section", {"aria-labelledby":"facilities-heading"})

            if facilities:
                self._ad_details["facilities"] = []
                for facility in facilities.find_all("div", {"class":"py-4 break-words"}):
                    self._ad_details["facilities"].append(str.replace(facility.text,u"\n", " ").strip())

            price = self._soup.find("div", {"class":"panel make-offer-order"})
            
            if price:
                self._ad_details["price"] = price.contents
        
        return self._ad_details