from typing import *
from .codetoken import TOKENISED


class LEXER:
    def __init__(self):
        self.code: List[TOKENISED] = []
    
    @classmethod
    def lex(self,file: IO):
        with open(file,"r") as lexerfile:
            for kword in lexerfile:
                kword: str
                tobetokenised: list = []
                if kword == " ":
                    continue
                if kword.isalpha():
                    ...
                