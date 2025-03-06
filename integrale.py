# from math import sqrt, pi #importo sqrt e pi greco dal modulo math
# b = 1/100
# area = 0.0

# for i in range (0, 100) :
#     area += b * sqrt(1 - (b*i) ** 2) #
# print(area/pi)

from math import sqrt, pi
def integra(parti):
    b = 1/parti
    area = 0.0
    for i in range (0, parti) :
        area += b * sqrt(1 - (b*i) ** 2) #
    return(area/pi)

print(integra(1000))
