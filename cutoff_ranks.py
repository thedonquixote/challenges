import math
instances=100000000
averageUtil=['30', '95', '4', '8', '19', '89']

for j in range(len(averageUtil)):
    if(int(averageUtil[j]) < 25):
        if (instances > 1):
            instances = math.ceil(instances / 2)
            j = j+10
    if j > len(averageUtil):
        break
    if int(averageUtil[j]) > 60:
        if ((instances*2) <= (2 * 10 ^ 8)):
            instances = instances * 2
            j = j+10
    if j > len(averageUtil):
        break

print(instances)
