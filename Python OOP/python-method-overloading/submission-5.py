class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self, text1: str ,text2:str= None) -> str:
        if text2 is None:
            return text1.upper()
        else:
            return text1 + text2

    def format_text(self, *text: str) -> str:
        res: str | None = ""
        if len(text) == 1:
            return str(text[0]).upper()
        else:
            for word in text:
                res += str(word)
        return res
                



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
