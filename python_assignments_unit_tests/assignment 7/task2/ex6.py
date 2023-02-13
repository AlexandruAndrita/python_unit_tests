from ex4 import Rectangle


class Square(Rectangle):
    def __init__(self, x: int, y: int, length: int):
        super().__init__(x,y,length,length)

    def to_string(self) -> str:
        return Rectangle.to_string(self)

    def area(self) -> float:
        return Rectangle.area(self)
