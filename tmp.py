from random import randint
fruits = ["apple", "banana", "cherry", "kiwi", "mango","ros"]

def shuffle(list):
    l = len(list)-1
    for i in range(1,2*l):
        i1 = randint(0, l)
        i2 = randint(0, l)
        list[i1], list[i2] = list[i2], list[i1]
    return list

fruits = shuffle(fruits)
print(fruits)