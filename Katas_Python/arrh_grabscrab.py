# def loose_change(cents):
#     quarters = cents // 25 or 0
#     cents = cents % 25

#     dimes = cents // 10 or 0
#     cents = cents % 10

#     nickels = cents // 5 or 0
#     cents = cents % 5

#     pennies = cents // 1 or 0
#     cents = cents % 1

#     return {'Nickels': nickels, 'Pennies': pennies, 'Dimes': dimes, 'Quarters': quarters}

# loose_change(56)

# {'Nickels': 1, 'Pennies': 1, 'Dimes': 0, 'Quarters': 2}

# 'Quarters' = 2
# sobra = 6
# Nickels = 1
# sobra = 1
# #
# def index(array, n):
#     # print(array[n], n, array)
#     if n <= len(array)-1:
#         return array[n] ** n
#     return -1

# a = "abc"
# print(list(a).sort())

# print(index([15, 4, 15, 0], 4))
def hidden(num):
    objj = {6: "a",
            1: "b",
            7: "d",
            4: "e",
            3: "i",
            2: "l",
            9: "m",
            8: "n",
            0: "o",
            5: "t"}
    # num = str(num)
    new_str = ""
    for l in num:
        new_str += objj[int(l)]
    # Code here
    return new_str

print(hidden("49632"))

def arr(n=0): 
    return [*range(n)]

print(arr(5))
print(*range(100))

def aa():
    a = ((True + True) ** (True + True) + True)* len("aaaaaaaaaa") * len("aa")
    print(a)
    return [*range(a)]
print(aa())
