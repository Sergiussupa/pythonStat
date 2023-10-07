import numpy as np
import matplotlib.pyplot as plt
import random
import math

n = int(input("Количество наборов "))
m = int(input("Количество элементов в наборе "))
p = float(input("Введите вероятность для каждого отдельного события в наборе. Формат .xxxxx "))

set_flips = []
summary = []
count_suc = [] # эмпирическое распределение
count_theor = [] # теоретическое распределение
def flip(a) :
    return int((random.uniform(0,1) - a < 0) if 1 else 0)
def flips(a, b) :
    arr = []
    for i in range(a) :
        arr.append(flip(b))
    return arr
def sum(a) :
    count = 0
    for i in range(len(a)) :
        count+=a[i]
    return count
def render() :
    for i in range(m+1) :
        count_suc.append(0)
        count_theor.append(math.comb(m, i)*math.pow(p,i)*math.pow(1-p,m-i))

    for i in range(n) :
        set_flips.append(flips(m, p))
        summary.append(sum(set_flips[i]))
        count_suc[summary[i]] += 1
        #print(set_flips[i], summary[i])
    for i in range(len(count_suc)) :
        count_suc[i] /= n

    print(count_suc)
    print(count_theor)


    x = np.arange(m+1)
    y = np.array(count_suc)
    plt.plot(x, y)
    x = np.arange(m+1)
    y = np.array(count_theor)
    plt.plot(x, y)
    plt.show()

if (p < 0 or p > 1) :
    print("Значение p может быть от 0 до 1")
else :
    render()