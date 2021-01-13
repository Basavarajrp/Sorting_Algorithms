def bubble_sort(lis_):
    n = len(lis_)
    for i in range(n):

        sorted = True
        for j in range(n-i-1):
            if lis_[j]>lis_[j+1]:
                lis_[j],lis_[j+1]=lis_[j+1],lis_[j]

                sorted = False

        if sorted:
            break


    return lis_



sort = bubble_sort([1,9,2,3,6,4,3])
print(sort)    
