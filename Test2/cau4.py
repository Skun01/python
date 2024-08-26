class TamThucBacHai:
    def __init__(self, a = 0, b = 0, c = 0) -> None:
        self.a = a
        self.b = b
        self.c = c
    def __str__(self) -> str:
        return f'{self.a}x2 + {self.b}x + {self.c}'
    def __add__(self, Another):
        return TamThucBacHai(self.a + Another.a, self.b + Another.b, self.c + Another.c)
    def __sub__(self, Another):
        return TamThucBacHai(self.a - Another.a, self.b - Another.b, self.c - Another.c)
    
tamThuc1 = TamThucBacHai(2, 3, 4)
tamThuc2 = TamThucBacHai(-3, 2, 1)
TongTamThuc = tamThuc1 + tamThuc2
HieuTamThuc = tamThuc1 - tamThuc2
print(TongTamThuc)
print(HieuTamThuc)