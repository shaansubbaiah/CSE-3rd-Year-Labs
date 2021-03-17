import csv

def updateHypothesis(x, h):
    if h == []:
        return x

    for i in range(0, len(h)):
        if x[i].upper()!=h[i].upper():
            h[i] = '?'

    return h


if __name__ == "__main__":
    data = []
    h = []

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        print("Data: ")
        for row in reader:
            data.append(row)
            print(row)

    if data:
        for x in data:
            if x[-1].upper() == "YES":
                x.pop() # removing last field
                h = updateHypothesis(x,h)

    print("\nHypothesis: ",h)
