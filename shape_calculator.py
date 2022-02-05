class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle(width={}, height={})'.format(self.width, self.height)

    def set_width(self, width):
        self.width = width
        return self.width

    def set_height(self, height):
        self.height = height
        return self.height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        pic_str = ''
        for i in range(self.height):
            if i < self.height:
                pic_str += ('*' * self.width)
                pic_str += '\n'
        if self.height or self.width < 50:
            return pic_str
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        height_fit = self.height // shape.height
        width_fit = self.width // shape.width
        return height_fit * width_fit


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)

    def __str__(self):
        return 'Square(side={})'.format(self.width)

    def set_side(self, length):
        super().set_width(length)
        super().set_height(length)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(2)
print(sq.get_diagonal())
print(sq)
print(rect)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
