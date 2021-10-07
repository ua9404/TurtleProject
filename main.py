# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import turtle


def square():
   turtle.setheading(45)
   turtle.begin_fill()
   turtle.fillcolor("blue")
   turtle.forward(100)
   turtle.right(90)
   turtle.forward(100)
   turtle.right(90)
   turtle.forward(100)
   turtle.right(90)
   turtle.forward(100)
   turtle.end_fill()



def test_drive():
   turtle.forward(100)
   #turtle.left(87)
   turtle.setheading(127)
   turtle.up()
   turtle.goto(50, 50)
   turtle.down()
   turtle.home()
   turtle.circle(50)


def main():
   test_drive()
   square()


main()


turtle.done()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
