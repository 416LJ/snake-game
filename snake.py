from turtle import Turtle


UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.position = None
        self.the_snake = []
        self.x_cord =0

        for i in range(3):
            self.add_segment(i)
        self.head = self.the_snake[0]

    def move(self):
        # ge the snake to follower each other
        for bit in range(len(self.the_snake) - 1, 0, -1):
            new_x = self.the_snake[bit - 1].xcor()
            new_y = self.the_snake[bit - 1].ycor()
            self.the_snake[bit].goto(x=new_x, y=new_y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


    def add_segment(self,position):
        self.position = Turtle(shape="square")
        self.position.penup()
        self.position.speed("fastest")
        self.x_cord -= 20
        self.position.color("white")
        self.position.goto(x=self.x_cord, y=0)
        self.the_snake.append(self.position)

    def extend(self):
        self.add_segment(self.the_snake[-1].position())

    def check_margins(self):
        if 280 >= self.head.xcor() >= -280 and 280 >= self.head.ycor() >= -280:
            return True
        else:
            return False
