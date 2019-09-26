#using binary search to pick a number from 1 to 100
#it should not take more than 7 guesses 
# >>>binary_search(25) -> 2
# >>>binary_search(31) <= 7
# >>>True

#pseudo code
#num_guesses = 0
#lower = 1, higher = 100, mid= (lower+higher)/2
#loop, will stop until lower === higher, increment num_guesses

def binary_search(val):

    num_guesses = 0
    lower = 1
    higher = 100
    guess = None

    while guess != val:

        num_guesses += 1
        guess = (lower + higher) // 2

        if val < guess:
            higher = guess

        elif val > guess:
            lower = guess

    return num_guesses

print(binary_search(75))


