from mypackage import sum_array
<<<<<<< HEAD
<<<<<<< HEAD
from mypackage  import fibonacci
from mypackage  import factorial
from mypackage  import reverse
from mypackage  import bubble_sort
from mypackage import merge_sort
from mypackage import quick_sort
=======
=======
>>>>>>> 74fb01142927d07baa0e7120253c18750282907d
from mypackaget import fibonacci
from mypackage import factorial
from mypackage import reverse
from mypackage import bubble_sort
from mypackage import merge_sort
from mypackage imprt quick_sort
<<<<<<< HEAD
>>>>>>> a6c777e3be19a27ad73b999b97dc03fe57f7b25a
=======
>>>>>>> 74fb01142927d07baa0e7120253c18750282907d

def test_sum_array(array):

    '''Return sum of all items in array'''
    return(sum(array))
    assert sum_array([8,7,6,5,4,3,2,1]) == 36


def test_fibonacci(n):
    '''Return nth term in fibonacci sequence'''
    return fibonacci(n-1)+fibonacci(n-2)
    assert fibonacci(10) == 55

def test_factorial(n):

    '''Return n!'''
    return n * factorial(n-1)
    assert factorial(7) == 5040

def test_reverse(word):

    '''Return word in reverse'''
    return reversed_word
    assert reverse('Magwaza')== [azawgaM]

def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''

    return items
    assert bubble_sort(["H", "G", "A", "N", "B", "D"]) == ['A', 'B', 'D', 'G', 'H', 'N']

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
        return itemsarr
        assert merge_sort([90,40,10,20,50,76,11,1]) == [1, 10, 11, 20, 40, 50, 76, 90]

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
        return itemsarr
        assert quick_sort([4,20,3,17,7,32,14,10,20])==[4, 3, 20, 20, 17, 7, 14, 10, 32]
