def bubble_sort(items):

    '''Return array of items, sorted in ascending order'''
    for passnum in range(len(items)-1,0,-1):
        for i in range(passnum):
            if items[i] > items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items

def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    if len(items)<2:
        return items
    itemsarr = []
    mid = int(len(items)/2)
    x = merge_sort(items[:mid])
    y = merge_sort(items[mid:])
    i = 0
    j = 0
    while i < len(x) and j < len(y):
        if x[i] > y[j]:
            itemsarr.append(y[j])
            j += 1
        else:
            itemsarr.append(x[i])
            i +=1
    itemsarr += x[i:]
    itemsarr += y[j:]
    return itemsarr

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    if not items:
        return []

    pivots = [x for x in items if x == items[0]]
    lesser = quick_sort([x for x in items if x < items[0]])
    greater = quick_sort([x for x in items if x > items[0]])
    itemsarr = pivots + lesser + greater

    return itemsarr

def quick_sort(items):

    '''Return array of items, sorted in ascending order'''
    if not items:
        return []

    pivots = [x for x in items if x == items[0]]
    lesser = quick_sort([x for x in items if x < items[0]])
    greater = quick_sort([x for x in items if x > items[0]])
    itemsarr = pivots + lesser + greater

    return itemsarr
