import numpy as np

arr = []
app_name = input('What app are you using > ')
array_size = int(input('Days to calculate > '))

for value in range(array_size):
    arr.append(input('Enter daily minute value > '))

arr = np.array(arr).astype(int)
print(f'Your average screentime for {app_name} is {np.mean(arr)} minutes')
