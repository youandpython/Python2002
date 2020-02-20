
def list_true(list_object):
    count = {}
    for li in list_object:
        count[li] = count.get(li, 0) + 1

    for val in count.values():
        if val > 1:
            return True
    else:
        return False


ls = [1, 2, 3, 4, 5, 6, 7, 3]
print(list_true(ls))
