from typing import *
from .codetoken import TOKENISED


class LEXER:
    def __init__(self,file: IO):
        self.interpeted_code: List[TOKENISED] = []