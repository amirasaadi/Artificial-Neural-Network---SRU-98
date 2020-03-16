import numpy as np
from matplotlib import pyplot as plt
# constants
x_min = y_min = - 20
x_max = y_max = 20

numbers = [20,200,2000]

#functions
def data_generator(number_of_data):
    dataset = np.random.uniform(x_min,x_max,(number_of_data,2))
    return dataset

def data_augmentation(dataset):
    pass

# main
dataset1 = data_generator(numbers[0])
dataset2 = data_generator(numbers[1])
dataset3 = data_generator(numbers[2])

print(dataset1[19])

# ploting
# plt.plot(dataset1[0],dataset1[1],'ro')
# plt.axhline()
# plt.axvline()
# plt.savefig('2.png')