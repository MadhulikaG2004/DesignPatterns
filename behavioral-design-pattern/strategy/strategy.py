from abc import ABC,abstractmethod

class TextEditorStrategy(ABC):
    def format_text(self,text):
        pass
class UpperCaseEditor(TextEditorStrategy):
    def format_text(self, text):
        return "Upper editor!"
class LowerCaseEditor(TextEditorStrategy):
    def format_text(self, text):
        return "Lower editor!"
class TextEditor:
    def __init__(self,strategy:TextEditorStrategy):
        self.strategy=strategy
    def format_text(self,text):
        return self.strategy.format_text(text)

if __name__=="__main__":
    text_edit=TextEditor(UpperCaseEditor())
    print(text_edit.format_text("hi"))
