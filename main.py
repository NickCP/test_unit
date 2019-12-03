def sorting_v(lists):
    was_swap = True
    while was_swap:
        was_swap = False
        for i in range(len(lists)-1):
            if lists[i] > lists[i+1]:
                lists[i], lists[i+1] = lists[i+1], lists[i]
                was_swap = True
    return lists

def sorting(lists):
    if len(lists) <= 1:
        return lists
    base_elem = lists[0]
    less_then = [elem for elem in lists if elem < base_elem]
    more_then = [elem for elem in lists if elem > base_elem]
    return  sorting(less_then) + [base_elem] + sorting(more_then)
