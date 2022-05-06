def cria_matriz(value):
    return [[0] * value for _ in range(value)]

def spiralize (value):
    arr = cria_matriz(value)
    
    def anda_na_linha(linha=0, col=0, rev = False):
        posicao = [0,0]
        if rev == False:
            leng = len(arr[linha][col:]) - 1
            for c in range(leng):
                if arr[linha][c+col+1] != 1 :
                    arr[linha][c+col] = 1
                    posicao[0] = linha
                    posicao[1] = c + col
                    if c+col+1 == leng: arr[linha][c+col+1] = 1 ; posicao[1] = c+ col + 1
                else:
                    break
        else:
            for col in range(linha-1, -1, -1):
                if arr[linha][col-1] != 1:
                    arr[linha][col] = 1
                    posicao[0] = linha
                    posicao[1] = col
                    if col-1 == 0: arr[linha][col-1] = 1; posicao[1] = col -1
                else:
                    break 
        return posicao

    def anda_na_coluna(col=0, linha=0, rev = False):
        posicao = [0,0]
        if rev == False:
            leng = len(arr[linha:])-1
            for c in range(leng):
                if arr[c+linha+1][col] != 1:
                    arr[c+linha][col] = 1
                    if c + 1 == leng: arr[c+linha+1][col] = 1
                    posicao[0] = c + linha + 1
                    posicao[1] = col
                else:
                    break
        else:
            for c in range(linha, -1, -1):
                if arr[c-1][col] != 1:
                    arr[c][col] = 1
                    posicao[0] = col
                    posicao[1] = c
                else:
                    break 
        return posicao
    # criar a espiral
    y = [0,0] # posiçao onde a proxima funçao deve começar no array
    x = [0,0]
    rev = False # quando o rev for igual a True ele fara o movimento contrario
    for _ in range(value//2 + 1 if value % 2 != 0 else value // 2):
        y = anda_na_linha(x[1], x[0], rev)
        x = anda_na_coluna(y[1],y[0], rev)
        rev = not rev # inverte de False para True
    return arr

print(spiralize(12)) 

def spiralizee(value):
    x , y = [0, 0]
    arr = [[0 for _ in range(value)] for _ in range(value)]
    moves = [1, 0, -1, 0]
    for t in range(value):
        for _ in range(value - 2 * max([0,(t-1)//2])):
            arr[y][x] = 1
            x, y = (x + moves[t%4], y + moves[(t+3)%4])
        x, y = (x - moves[t%4], y - moves[(t+3)%4])
    return arr

print(spiralizee(8))