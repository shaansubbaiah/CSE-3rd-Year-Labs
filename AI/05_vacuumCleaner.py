import random

environment = {"A": 0, "B": 0}  # assumed initial state


def checkDirt():
    return random.randint(0, 1)


def setEnvironment():
    environment["A"] = checkDirt()
    environment["B"] = checkDirt()

    print("\nNew environment: ", end="")
    print(environment)


def cleaned():
    print("\nBoth the locations are cleaned.")
    exit(0)


def newState():
    setEnvironment()

    if environment["A"] == 0 and environment["B"] == 0:
        cleaned()
    else:
        if environment["A"]:
            cleanAt(1)
        else:
            cleanAt(0)


def cleanAt(state):
    if state == 1:
        print("\nVaccum cleaner at A location.")
        dirt = environment["A"]  # 0-nodirt 1-dirt

        if dirt == 1:
            print("Location A is dirty.")
            print("Vaccum cleaner cleaned the dirt at A.")
            environment["A"] = 0
        else:
            print("Location A is clean.")

        if environment["B"]:
            print("Vaccum cleaner moving to B location.")
            cleanAt(0)

    else:
        print("\nVaccum cleaner at B location.")
        dirt = environment["B"]  # 0-nodirt 1-dirt

        if dirt == 1:
            print("Location B is dirty.")
            print("Vaccum cleaner cleaned the dirt at B.")
            environment["B"] = 0
        else:
            print("Location B is clean.")

        if environment["A"]:
            print("Vaccum cleaner moving to A location.")
            cleanAt(1)

    print("\nCurrent environment: ", end="")
    print(environment)
    newState()


def start():
    newState()


if __name__ == "__main__":
    start()