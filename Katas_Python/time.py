def format_duration(seconds):
    if seconds == 0: return "now"
    strSeconds = str(seconds)
    resul = []
#     r = 0
    i = len(strSeconds)
    for _ in range(i):
        if int(strSeconds) - (60 * 60) >= 0:
            strSeconds = str(int(strSeconds) - (60 * 60))
            resul.append(1)
        elif int(strSeconds) - 60 >= 0:
            strSeconds = str(int(strSeconds) - 60)
            resul.append(1)
        elif int(strSeconds) > 0:
            resul.append(int(strSeconds))
            break
            
#         if len(strSeconds) == 4:
#             r = int(strSeconds) // 3600
#         elif len(strSeconds) == 3:
    print(resul)
    
print(format_duration(3662))