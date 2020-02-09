def warikireru(a,n):
    I=[]
    i=0
    while i <= len(a):
        if a[i] % n == 0:
            I.append(a[i])
            i = i +1
        else:
            i = i +1

a = [98,24,42,88,100,23,32,96]
n = 2

warikireru( [98,24,42,88,100,23,32,96],2)