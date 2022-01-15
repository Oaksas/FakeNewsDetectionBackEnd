import re

#filters all website url realted contents from the text
class OtherFilters:
    def __init__(self,text) -> None:
        self.text=text
    def filter(self):
        text = re.sub('\[.*?\]', '', self.text)
        text = re.sub("\\W"," ",self.text) 
        text = re.sub('<.*?>+', '', self.text)
        text = re.sub('\n', '', self.text)
        text = re.sub('\w*\d\w*', '', self.text)   
        return text
   