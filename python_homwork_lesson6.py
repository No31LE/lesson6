a = int(input('people?'))
l = list()
s = 0
ma = 0
mi = 100
l2 = list()
l3 = list()

for i in range(1,a+1):
    
    y = input('student name?')
    l.append(y)
    
    x = int(input('student score?'))
    l.append(x)

    s = s + l[i*2-1]
    if x>ma:
        l2.clear()
        ma = x
        l2.append(y)
        l2.append(ma)
    elif x<mi:
        l3.clear()
        mi = x
        l3.append(y)
        l3.append(mi)










print('average:',s/a)
print ('highest:','student:',l2[0],'|score:',l2[1])
print ('lowest:','student:',l3[0],'|score:',l3[1])