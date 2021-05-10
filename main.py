import numpy as np
import matplotlib.pyplot as plt
import math
import random

num_of_cities = 200
skip = 2000

def generateCoordinates():
    coords = []
    for i in range(num_of_cities):
        coords.append(random.randint(0, num_of_cities - 1))
    return coords

def distance(xCoords, yCoords, i, j):
    return math.sqrt((xCoords[i] - xCoords[j]) ** 2 + (yCoords[i] - yCoords[j]) ** 2)

def totalDistance(xCoords, yCoords):
    dist = 0
    for i in range(num_of_cities - 1):
        dist += distance(xCoords, yCoords, i , i + 1)
    dist += distance(xCoords, yCoords, 0, num_of_cities - 1)
    return dist

def reverse_sublist(xTemp, yTemp):
    i = 0
    j = 0
    while i == j:
        i = random.randint(0, num_of_cities - 2)
        j = random.randint(i + 1, num_of_cities - 1)

    xTemp[i:j] = xTemp[i:j][::-1]
    yTemp[i:j] = yTemp[i:j][::-1]

def swap_random_cities(xTemp, yTemp):
    i = 0
    j = 0
    while i == j:
        i = random.randint(0, num_of_cities - 1)
        j = random.randint(0, num_of_cities - 1)
    swap_cities(xTemp, yTemp, i, j)

def swap_cities(xTemp, yTemp, i, j):
    tempX = xTemp[i]
    tempY = yTemp[i]
    xTemp[i] = xTemp[j]
    yTemp[i] = yTemp[j]
    xTemp[j] = tempX
    yTemp[j] = tempY

def random_shuffle(xTemp, yTemp):
    xTemp = np.array(xTemp)
    yTemp = np.array(yTemp)
    order = np.arange(num_of_cities)
    np.random.shuffle(order)
    xTemp = xTemp[order]
    yTemp = yTemp[order]
    
def perturb(xTemp, yTemp):
    reverse_sublist(xTemp, yTemp)
    #swap_random_cities(xTemp, yTemp)
    #random_shuffle(xTemp, yTemp)

def make_copies(xTemp, yTemp):
    x = []
    y = []
    for i in range(num_of_cities):
        x.append(xTemp[i])
        y.append(yTemp[i])

    return x, y

def isAcceptable(x_new, x, T):
    delta = x_new - x
    return random.uniform(0, 1) < np.exp((x - x_new) / T)
    p = np.exp(delta / T)
    c = random.random()
    if (c >= p):
        return True
    return False

def plotGraph(xCoords, yCoords):
    plt.plot(xCoords, yCoords, '--b')
    plt.scatter(xCoords, yCoords, marker='o')
    plt.show()
    plt.pause(0.001)
    plt.clf()

def simulated_annealing(xCoords, yCoords):
    sim_values = []
    temperature_values = []
    iterations = []
    delta = []

    x = totalDistance(xCoords, yCoords)
    initial_x = x
    k = 0

    k_max = 100000
    T = 3000
    alpha = 0.9995
    while k < k_max and T > 1e-10:
        xTemp = xCoords[:]
        yTemp = yCoords[:]
        perturb(xTemp, yTemp)

        x_new = totalDistance(xTemp, yTemp)
        if isAcceptable(x_new, x, T):
            xCoords = xTemp[:]
            yCoords = yTemp[:]
            x = x_new
            delta.append(x - x_new)
        else:
            delta.append(0)

        sim_values.append(x_new)
        temperature_values.append(T)
        iterations.append(k)

        if k % skip == 0: plotGraph(xCoords, yCoords)

        T *= alpha
        k += 1


    plt.show()

def main():
    print('Cities: ', num_of_cities)
    xCoords = generateCoordinates()
    yCoords = generateCoordinates()
    plotGraph(xCoords, yCoords)
    plt.show()
    simulated_annealing(xCoords, yCoords)

if __name__ == "__main__":
    main()
