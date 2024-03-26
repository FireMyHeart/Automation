from turtle import *

# Функция для рисования Снежинки Коха
def snowflake(t, order, size):
    if order == 0:
        t.fd(size)
    else:
        for angle in [60, -120, 60, 0]:
            snowflake(t, order-1, size/3)
            t.left(angle)

t = Turtle()
t.speed(0)
screen = Screen()
screen.setup(width=800, height=800)
screen.title("Снежинка Коха")

# Начальная позиция курсора
t.up()
t.goto(-150, 100)
t.down()

# Повторить рисование элемента трижды, поворачивая каждый следующий элемент на 120°, чтобы замкнуть в круг.
t.begin_fill()
t.color("black", "pink")
for i in range(3):
    snowflake(t, 4, 300)
    t.right(120)
t.end_fill()

t.screen.exitonclick()
t.screen.mainloop()