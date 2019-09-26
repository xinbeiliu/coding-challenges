#write a function to decode a string

#decode("0h1ae2bcy") -> 'hey'

#pseudo code
#create a new list
#loop over, if item is an int, append the item at
#(index + int) to the new list
#return new list

def decode(s):

    result = []

    for i, item in enumerate(s):
        if i is int:
            temp = s[i + item]
            result.append(temp)

    return result

print(decode('0h1ae2bcy'))