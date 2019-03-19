def sum_array(array):

    '''Return sum of all items in array'''
    return(sum(array))

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n ==0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4))
def factorial(n):

    '''Return n!'''
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def reverse(word):

    '''Return word in reverse'''
    wordlength = len(word)
    reversed_word = ""
    for i in range(wordlength-1,-1,-1):
        reversed_word += word[i]
    return reversed_word
