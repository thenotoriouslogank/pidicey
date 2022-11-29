import random


dice = input("what do you want to roll? [xdy]")
drop = int(input("drop how many? [int] "))
s = dice.rsplit("d", 1)
times = int(s[0])
die = int(s[1])
results = []
hilo = ''

def Roll(die, times):
    for _ in range(times):
        results.append(random.randint(1, die))
    print("Rolls: " + str(results))

def Total(results):
    print("Total: " + str(sum(results)))

def HiLow(drop):
    if int(drop) > 0:
        hilo = input("Drop highest or lowest? [H/L]")
        if hilo == "L":
            results.sort()
            for _ in range(drop):
                results.pop(0)
            print("Dropped Lowest " + str(drop) + ": " + str(results))
        elif hilo == "H":
            results.sort(reverse=True)
            for _ in range(drop):
                results.pop(0)
            print("Dropped Highest " + str(drop) + ": " + str(results))

    else:
        Total(results)

Roll(die, times)
HiLow(drop)