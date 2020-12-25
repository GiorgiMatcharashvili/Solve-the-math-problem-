import random

lst = [1, 2, 3]
win = 0
lose = 0
x = 0
print('''
The Monty Hall Problem solution and probabilitys for both option:
stay and change.

Puzzle is simple:

Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car;
behind the others, goats. You pick a door, say No. 1, and the host,
who knows what's behind the doors, opens another door, say No. 3,
which has a goat. He then says to you, "Do you want to pick door No. 2?"

Is it to your advantage to switch your choice?

''')

while True:
    car = random.randint(1, 3)  # Behind one door is a car; behind the others, goats.
    choise = random.randint(1, 3)  # You pick a door.

    lst.remove(car)
    try:
        lst.remove(choise)  # and the host, who knows what's behind the doors, opens another door,
    except:
        pass
    goat = random.choice(lst)  # which has a goat.

    # He then says to you, "Do you want to pick door another door?"

    lst = [1, 2, 3]
    lst.remove(choise)  # find the number of the door, which you think to change.
    lst.remove(goat)
    change = random.choice(lst)

    lst = [1, 2, 3]

    if int(change) == int(car):
        win = int(win) + 1  # if your new choise has a car, you win.

    else:
        lose = int(lose) + 1  # else you lose.

    x = int(x) + 1  # Count numbers of cases

    if int(x) == 1000000:
        result = int(win) - int(lose)

        print("""
If we play this game a million times and we always change our first choise,
We will win """ + str(win) + """ times and lose """ + str(lose) + """ times.
              """)

        x = 0
        win = 0
        lose = 0
        p = input("Press any key to try again...")