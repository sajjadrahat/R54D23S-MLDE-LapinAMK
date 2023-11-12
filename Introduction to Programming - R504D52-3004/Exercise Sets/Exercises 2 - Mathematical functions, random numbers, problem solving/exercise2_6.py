import math
# 2+2x2+2 −2 − 2 = 2 cherries
# we will find 1 cherry value
cherry = int((2+2*2+2-2-2)/2)
#now we will find 1 apple value
apple = int((math.sqrt(3+10-4))/3 + ((math.pow(5,3)-5)/20) + 3)
# Find orange values
orange = apple-9
# 2 cherries - 3 bananas = 10
banana = int((2*cherry -10)/3)
#3 bananas +pear = 8
pear = (8-3*banana)
#print final value
print(apple-2*banana+2*orange*(pear+cherry))


