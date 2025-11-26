import turtle


def koch_curve(t, length, level):
    """Рекурсивна функція для малювання кривої Коха."""
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)
        t.right(120)
        koch_curve(t, length, level - 1)
        t.left(60)
        koch_curve(t, length, level - 1)


def koch_snowflake(level, size=300):
    """Малює сніжинку Коха із заданим рівнем рекурсії."""
    window = turtle.Screen()
    window.title("Сніжинка Коха")   
    window.bgcolor("white")          

    t = turtle.Turtle()
    t.speed(0)

    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    for _ in range(3):
        koch_curve(t, size, level)
        t.right(120)

    window.exitonclick()


if __name__ == "__main__":
    try:
        level = int(input("Введіть рівень фракталу (0 або більше): "))
        if level < 0:
            raise ValueError("Рівень повинен бути 0 або більше.")
        koch_snowflake(level)
    except ValueError as e:
        print(
            "Неправильне введення:"
            f" {e}, будь ласка, введіть ціле число 0 або більше."
        )
