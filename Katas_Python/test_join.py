a = [1,2,5,4,3,2,1]
a = f"{a}"
result = [(int(b), a.count(b)) for b in list(set(a)) if b not in [",", " ", "[", "]"]]

print(result)