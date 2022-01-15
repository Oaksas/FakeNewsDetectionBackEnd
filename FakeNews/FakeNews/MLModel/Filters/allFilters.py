from .makeAllLowerCaseFilter import makeLowerCase
from .otherFilters import OtherFilters
from .websiteFilter import WebsiteFilter


class allFilters:
    def __init__(self,text) -> None:
        self.text=text
    def filter(self):
        return  OtherFilters(WebsiteFilter(makeLowerCase(self.text).filter()).filter()).filter()