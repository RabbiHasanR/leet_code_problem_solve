# complete binary tree te ses level ar ager level porjonto full binary tree thakbe and ses level a left side puron kore tar por
# right side puron korbe

# heep hosse complete binary tree jekhane node ar value tar left and right child ar value theke big or same hole
# ata max heep and jodi small hoy tahole min heep hobe. amar heep k list a rakhte pari
# list ar n index a jodi kono node thake tahole tar left child node thakbe (2*n) index a
# and right node thakbe ((2*n)+1) index a. kono node ar parent ar index jante hole oi node ar index k 2 diye
# divide korlei hobe parent node index = (n//2)

def create_heep():
    heep = [None] * 10
    heep[1] = 19
    heep[2] = 7
    heep[3] = 17
    heep[4] = 3
    heep[5] = 5
    heep[8] = 1
    heep[9] = 2
    heep[6] = 12
    heep[7] = 10

def left(i):
    return i * 2
def right(i):
    return (i*2)+1
def parent(i):
    return i//2

def is_max_heep(h):
    n = len(h) - 1

    for i in range(n, 1, -1):
        p = parent(i)
        if h[p] < h[i]:
            return False
    return True

if __name__ == "__main__":
    H = [None,19,7,17,3,5,12,10,1,2]
    print(H, is_max_heep(H))
    H = [None,19,7,17,3,5,12,10,1,4]
    print(H, is_max_heep(H))
    H = [None,1,2,3]
    print(H, is_max_heep(H))
    H = [None,2,1,3]
    print(H, is_max_heep(H))
    H = [None,3,1,2]
    print(H, is_max_heep(H))
