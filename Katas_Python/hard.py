def modes(data):
    print(data)
    newarr = []
    maior = data[0]
    for i in set(data):
        print(i)
        if data.count(i) > 1 and data.count(i) > data.count(maior):
            maior = i
            newarr = [i]
        elif data.count(i) > 1 and data.count(i) == data.count(maior):
            newarr.append(i)
    
    
    if sorted(newarr) == sorted(set(data)):
        return []
   
    print(newarr)
#     resul = [m[1] for m in newarr if ]
    return sorted(newarr)

print(modes("tomato"))
# g
# jipijapa

print([*range(10)])