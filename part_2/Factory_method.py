class Draw:
    def Circle():
        return "Круг: ◯"
    def Square():
        return "Квадрат: □"
    def Triangle():
        return "Треугольник: △"
    def Star():
        return "Звезда: ☆"

class ShapeFactory:
    def create_shape(shape_type):
        if shape_type == "circle":
            return Draw.Circle()
        elif shape_type == "square":
            return Draw.Square()
        elif shape_type == "triangle":
            return Draw.Triangle()
        elif shape_type == "star":
            return Draw.Star()
        else:
            return(f"Неизвестный тип фигуры: {shape_type}")

circle = ShapeFactory.create_shape("circle")
square = ShapeFactory.create_shape("square")
triangle = ShapeFactory.create_shape("triangle")
twoangle = ShapeFactory.create_shape("twoangle")
star = ShapeFactory.create_shape("star")
print(circle)
print(square)
print(triangle)
print(star)
print(twoangle)
