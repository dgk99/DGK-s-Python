# contains(lst, target)

def contains(lst, target):
    for i in lst:
        if i == target:
            return True
    else:
        return False

print(contains([1, 2, 3, 4], 3))
print(contains([1, 2, 3, 4], 8))