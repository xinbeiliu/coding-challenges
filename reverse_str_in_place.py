# Reverse a String meaning swap items
# lst = [1, 2, 3, 4, 5]
# lst = [5, 4, 3, 2, 1]

def reverse(list_of_chars):

    left_index = 0
    right_index = len(list_of_chars) - 1

    while left_index < right_index:
        # Swap characters
        list_of_chars[left_index], list_of_chars[right_index] = \
            list_of_chars[right_index], list_of_chars[left_index]

        # Move towards middle
        left_index  += 1
        right_index -= 1

print(reverse(['cat', 'dog', 'seal', 'rabbit', 'whale']))