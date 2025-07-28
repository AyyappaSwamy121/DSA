def insertion_sort():
    for i in range(1,len(a)):
        j = i-1
        temp =a[i]
        while j>=0 and a[j]>temp:
            a[j+1]=a[j]
            j-=1
        a[j+1]=temp
a = [4,33,43,77,9]
insertion_sort()
print("Array after sorted::",a)
