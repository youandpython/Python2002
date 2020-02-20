
def list_true(list_object):
    if len(list_object) == len(set(list_object)):
        return False
    else:
        return True


ls = [1, 2, 3, 4, 5, 6, 7, 5]
print(list_true(ls))
