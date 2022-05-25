import random

random_number = random.randint(1, 15)
tries = 1

emri = input("Pershendetje, si quheni ?")

print("Pershendetje", emri + '!')

pytja = input("""A deshironi ta luajme nje loje ?
                 Nese Po shtypni P, nese Jo shtyni J.""")

if pytja == "j":
    print("OK :(")

if pytja == "p":
    print("Ne rregull, atehere po e mendoj nje numer nga 1 deri 15")
    zgjedhja = int(input("Zgjedhe nje numer: "))
    if zgjedhja > random_number:
        print("Zgjedhe nje nr me te vogel...")
    if zgjedhja < random_number:
        print("Zgjedhe nje nr me te madh...")

    while zgjedhja != random_number:
        tries += 1
        zgjedhja = int(input("Provojeni prap: "))
        if zgjedhja < random_number:
            print("Zgjedhe nje nr me te madh...")
    if zgjedhja == random_number:
        print("Ju fituat :)! Numri i menduar ishte ", random_number, "dhe e gjetet vetem me", tries, "perpjekje!")

