from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.car_list = []
        self.car_generate()

    def car_generate(self):
        num = random.randint(1, 6)
        if num == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.setheading(180)
            new_car.penup()
            y_position = self.set_y_position()
            new_car.goto(300, y_position)
            self.car_list.append(new_car)

    def set_y_position(self):
        if self.car_list == []:
            y_position = random.randint(-270, 270)
        else:
            create_position = True
            while create_position:
                y_position = random.randint(-270, 270)
                if abs(y_position - self.car_list[-1].ycor()) > 25:
                    create_position = False
        return y_position

    def move(self):
        for car in self.car_list:
            car.forward(MOVE_INCREMENT)
            if car.xcor() < -300:
                car.hideturtle()
                self.car_list.remove(car)



