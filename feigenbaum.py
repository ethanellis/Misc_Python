from collections import Counter
import matplotlib.pyplot as plt
import numpy as np

#while True:
    #pick = input('select a value of R between 0 and 4: ')
    #R = float(pick)
    #x_range = [1,2,3,4]
    #stable_points = []

R_jump = float(input('input step-size. Recommend 0.01-0.001: '))
r_range = []
stable_values = []
R = 0.000
while R < 4:
    x = .5
    count = 0
    outputs = []
    while count < 1000:
        x = R*x*(1-x)
        count += 1
        outputs.append(x)

    c = Counter(outputs)
    best_keys = []
    for key,i in c.items():
        if i > 50:
            best_keys.append(key)
        else:
            pass
    if len(best_keys) < 1:
        i = 0
        while i < 150:
            best_keys.append(outputs[len(outputs)-1-i])
            i += 1
        
    stable_values.append(best_keys)
    r_range.append(R)
    #print(R)
    R += R_jump

for xe, ye in zip(r_range,stable_values):
    plt.scatter([xe]*len(ye), ye, s = 0.5, c = 'black')

plt.xticks([1,2,3,4])
plt.title('bifurcation diagram')
#plt.savefig('bifurcate.png')
plt.show()


    #print(best_keys)

    
