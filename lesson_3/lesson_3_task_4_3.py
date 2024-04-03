from turtle import *
# нарисуем кошОчку :)

t = Turtle()
t.hideturtle()
screen = Screen()
t.screen.setup(1200, 800)
screen.title("Дымок с белыми пятнышками")
t.speed(0)

t.begin_fill()
t.color("black", "grey")

t.up()
t.goto(-258, 93)
t.down()

t.right(146)
t.fd(66)
t.right(89)
t.fd(94)
t.right(145)
t.fd(116)

t.left(14)
t.fd(92)

t.left(58)
t.fd(12)

t.right(52)
t.fd(69)

t.left(10)
t.fd(233)

t.right(32)
t.fd(150)

t.right(41)
t.fd(131)

t.left(27)
t.fd(74)

t.right(32)
t.fd(115)

t.right(40)
t.fd(54)

t.right(97)
t.fd(29)

t.right(66)
t.fd(30)

t.left(32)
t.fd(72)

t.left(40)
t.fd(117)

t.right(98)
t.fd(110)

t.left(44)
t.fd(84)

t.up()
t.goto(251, -99)
t.down()
# нога отрисована

t.right(220)
t.fd(11)

t.left(40)
t.fd(75)

t.right(61)
t.fd(108)

t.right(43)
t.fd(61)

t.right(105)
t.fd(28)

t.right(60)
t.fd(34)

t.left(37)
t.fd(56)

t.left(73)
t.fd(136)

t.right(44)
t.fd(206)

t.up()
t.goto(143, -100)
t.down()

t.left(95)
t.fd(268)

t.up()
t.goto(-35, -96)
t.down()

t.right(85+178)
t.fd(147)

t.right(95)
t.fd(68)

t.right(107)
t.fd(22)

t.right(43)
t.fd(24)

t.left(83)
t.fd(127)

#три ноги готово

t.up()
t.goto(-91, 93)
t.down()

t.right(101+107)
t.fd(169)

t.right(42)
t.fd(303)

t.right(37)
t.fd(64)

t.right(99)
t.fd(23)

t.right(61)
t.fd(34)

t.left(27)
t.fd(147)

t.left(31)
t.fd(53)

t.right(25)
t.fd(195)

#4 ноги готово

t.up()
t.goto(-237, -40)
t.down()

t.left(105)
t.fd(37)

t.left(43)
t.fd(53)

t.right(51)
t.fd(49)

t.right(78)
t.fd(32)

t.left(16)
t.fd(36)

t.right(40)
t.fd(58)

# рисуем хвост:

t.up()
t.goto(202, 108)
t.down()

t.right(25)
t.fd(143)

t.left(33)
t.fd(95)

t.right(19)
t.fd(54)

t.right(40)
t.fd(51)

t.right(137)
t.fd(71)

t.left(21)
t.fd(108)

t.right(28)
t.fd(120)

t.end_fill()

#рисуем глаз

t.begin_fill()
t.color("black", "blue")

t.up()
t.goto(-341, 26)
t.down()
t.circle(8, 360)
t.end_fill()

# и рот
t.up()
t.goto(-341, -44)
t.down()
t.color("red")
t.pensize(3)
t.right(180)
t.circle(100, 11)

# Необходимо, чтобы окно не закрывалось само, а только по клику
t.screen.exitonclick()
t.screen.mainloop()