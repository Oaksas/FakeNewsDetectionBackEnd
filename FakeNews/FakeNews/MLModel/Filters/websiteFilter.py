import re

#filters all website url realted contents from the text
class WebsiteFilter:
    def __init__(self,text) -> None:
        self.text =text
    def filter(self):
        text = re.sub('https?://\S+|www\.\S+', '', self.text)
        return text



