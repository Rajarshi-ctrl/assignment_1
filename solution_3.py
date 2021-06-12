list1 = []
val = 0


def create_dict(list1):
    global val
    for i in list1:
        if type(i) == dict:
            a = list(i.values())
            for j in range(len(a)):
                val = val + a[j]
        elif type(i) == list:
            create_dict(i)
    return val


list1 = [{'x': 1}, {'x': 2}, {'x': 3}, [{'x': 4}, {'x': 5}, {'x': 6}, [{'x': 7}, [{'x': 8}]]], {'x': 9}]

print(create_dict(list1))
