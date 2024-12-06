#SORTING
'''
#1. Bubble Sort
x=[]
n=int(input('enter length = '))
for i in range(n):
    v=int(input('enter element = '))
    x.append(v)
for j in range(n-1):
    for k in range(n-1):
        if(x[k]>x[k+1]):
            x[k],x[k+1]=x[k+1],x[k]
print('sorted list=',x)

#2. Selection Sort
x=[]
n=int(input('enter length = '))
for i in range(n):
    v=int(input('enter element = '))
    x.append(v)
for j in range(n-1):
        for k in range(j+1,n):
          if(x[k]<x[j]):
            x[k],x[j]=x[j],x[k]
print('sorted list=',x)
'''
#3. Insertion Sort
x=[]
n=int(input('enter length = '))
for i in range(n):
    v=int(input('enter element = '))
    x.append(v)
for i in range(n):
    for j in range(n-1):
        if(x[i]<x[j]):
            x[i],x[j]=x[j],x[i]
print('sorted list=',x)
'''
#4. Merge Sort                                                                              Based on divide and conquer - recursive algorithm
#                                                                                           T(n)=  
x=[]
n=int(input('enter length = '))
for d in range(n):
    v=int(input('enter element = '))
    x.append(v)
def merge_sort(arr):
    if (len(arr) > 1):
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while (i < len(left_half) and j < len(right_half)):
            if (left_half[i] < right_half[j]):
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while (i < len(left_half)):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while (j < len(right_half)):
            arr[k] = right_half[j]
            j += 1
            k += 1
merge_sort(x)
print("Sorted list = ",x)

#5. Quick Sort                                                             Based on divide and conquer - recursive algorithm
#                                                                          T(n)=      
x=[]                                                                       
n=int(input('enter length = '))
for d in range(n):
    v=int(input('enter element = '))
    x.append(v)
u=n-1
def partition(x,l,u):
    p=x[u]
    for i in range(u+1):
        if(x[i]>p):
            x.append(x[i])
            x[i]='dummy'
    t=0
    for j in range(len(x)):
        if(x[j]=='dummy'):
             t=t+1
    for k in range(t):
        x.remove('dummy')
    return(x)
    for q in range(len(x)):
        if(x[q]==p):
            y=q
            break
    o=u+l//2
    first_half=[:y]
    second_half=[y+1:]
    partition(first_half,l,len(first_half)-1)
    partition(second_half,l,len(second_half)-1)
    merge()
'''
    







