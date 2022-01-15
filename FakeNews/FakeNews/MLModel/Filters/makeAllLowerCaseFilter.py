#filters the text to all-Lower-case-letters
class makeLowerCase:
    def __init__(self,text) -> None:
        self.text =text
    def filter(self):
        text =self.text.lower()
        return text



