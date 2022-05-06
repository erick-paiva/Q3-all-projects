# def mix(s1):
#     for i in range(len(s1)):


def mix(s1, s2):
    # resultadoS1 = []
    # resultadoS2 = []
    finale = []
    for i in range(len(s1)):
        if not s1[i] == s1[i].upper() and s1[i] != " ":
            if s1[i-1] != s1[i] and s1.count(s1[i]) > 1 and not f"1:{s1[i] * s1.count(s1[i])}" in finale:
                # resultadoS1.append(f"{s1.count(s1[i]) * s1[i]}")
                
                if(s1.count(s1[i]) > s2.count(s1[i])):
                    finale.append(f"1:{s1[i] * s1.count(s1[i])}")
                    print(s1.count(s1[i]), s2.count(s1[i]))
                elif(s1.count(s1[i]) < s2.count(s1[i])) and s2.count(s1[i]) > 1:
                    finale.append(f"2:{s1[i] * s2.count(s1[i])}")
                else:
                    finale.append(f"=:{s1[i] * s1.count(s1[i])}")
    # resultadoS1.sort()

    for i in range(len(s2)):
        if not s2[i] == s2[i].upper() and s2[i] != " ":
            if s2[i-1] != s2[i] and s2.count(s2[i]) > 1 and not f"2:{s2[i] * s2.count(s2[i])}" in finale:
                # resultadoS2.append(f"{s2.count(s2[i]) * s2[i]}")
                
                # print( finale.count(s2[i]), finale, s2[i])
                if(s2.count(s2[i]) > s1.count(s2[i])):
                    finale.append(f"2:{s2[i] * s2.count(s2[i])}")
                elif(s2.count(s2[i]) < s1.count(s2[i])):
                    finale.append(f"1:{s1[i] * s1.count(s1[i])}")
                else:
                    if(finale.count(s2[i]) == 0):
                        finale.append(f"=:{s2[i] * s2.count(s2[i])}")
    # resultadoS2.sort()
    finale = sorted(set(finale))
 
    finale.sort()
    print(finale,"ee")

    resultado = "/".join(finale)
    print(resultado)


mix("Are they here", "yes, they are here")
'2:eeeee/2:yy/=:hh/=:rr'


