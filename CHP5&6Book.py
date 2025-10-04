print(10%3)

if x == y:
    print('x and y are equal')
elif x < y:
    print('x is less than y')
else:
    print('x is greater than y')

    if a > 10 and b > 20:
        print("Hello")

if 0 < x < 10:
    print('x is a positive single-digit number.')

    from time import time

    now = time()  # Get the current time as seconds since the epoch (January 1, 1970)

    # Calculate the number of days
    seconds_in_day = 24 * 60 * 60
    days_since_epoch = int(now // seconds_in_day)

    # Calculate the remaining seconds within the current day
    remaining_seconds_today = now % seconds_in_day

    # Calculate hours, minutes, and seconds from the remaining seconds
    hours = int(remaining_seconds_today // (60 * 60))
    minutes = int((remaining_seconds_today % (60 * 60)) // 60)
    seconds = int(remaining_seconds_today % 60)

    print(f"Days since January 1, 1970: {days_since_epoch}")
    print(f"Current time of day: {hours:02d}:{minutes:02d}:{seconds:02d}")


def is_triangle(a, b, c):
     if a + b > c and a + c > b and b + c > a:
         print("Yes")
    else:
         print("No")

 6

Stack:

| recurse(n=0, s=6) | <--- Current active frame (prints 6)
|-------------------|
| recurse(n=1, s=5) |
|-------------------|
| recurse(n=2, s=3) |
|-------------------|
| recurse(n=3, s=0) |
|-------------------|
| __main__          |

from jupyturtle import forward, left, right, back, run


def draw(length):
    angle = 50
    factor = 0.6

    if length > 5:
        forward(length)
        left(angle)
        draw(factor * length)
        right(2 * angle)
        draw(factor * length)
        left(angle)
        back(length)


run(draw, 100)  # Calls draw with an initial length of 100

make_turtle(delay=0)
koch(120)

make_turtle(delay=0, height=200)

draw_sierpinski(100, 3)




