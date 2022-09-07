# insertion sort explain

# L = [5,3,7,2,6]


# algorithm for acending order insertion sort
# input: assume L is a n numbers of list where n is a list length

# step 1: list a jodi akti item thake tahole seti already sort kora ase. tai list ar next item theke suru kore end porjonto every item ar jonno next 2 step follow korte hobe
# step 2: one specific item ar jonno tar age list a jesob item ase segulo jodi tar theke boro hoy tahole tader k
# ak ghore dane sorai.tahole specific item ar jonno specific jaygay khuje pabo
# step 3: specific item ti tar kankhito jaygay bosai
# step 4: list L acending order a sajano ase



def insertion_sort_asc(L):
    n = len(L)
    for i in range(1, n):
        item = L[i]
        j = i - 1

        while j >=0 and L[j] > item:
            L[j+1] = L[j]
            j = j - 1
        
            L[j + 1] = item
    return L

L = [5,3,7,2,6]
print(insertion_sort_asc(L))