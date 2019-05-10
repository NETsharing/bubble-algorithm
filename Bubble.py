z = input('Enter the massive: ').split(' ')
a = list(map(int,z))
n = len(a)
x= []
# for m in reversed(range(n)):
#     for i in range(m) :
#         if a[i]>a[i+1]:
#             x = a[i+1]
#             a[i+1] = a[i]
#             a[i] = x
# print (a)
j =n-1
while j>0:
    i=0
    while i<j:
        if a[i]>a[i+1]:
            x = a[i+1]
            a[i+1]= a[i]
            a[i]=x

        i+=1
    j-=1
print(a)