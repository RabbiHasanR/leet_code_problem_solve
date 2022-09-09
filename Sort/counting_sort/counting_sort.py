# counting sort

# in counting sort input must be positive number
# and must be know highest number value
# now make highest number value + 1 size array

def counting_sort(L):
    sorted_list = []
    count = [0] * 11
    for x in L:
        count[x] = count[x] + 1

    for index, value in enumerate(count):
        if value > 0:
            sorted_list.extend([index] * value)

    return sorted_list
    
L = [3,4,1,6,2,4,9,7,8,4,2,1]
print(counting_sort(L))