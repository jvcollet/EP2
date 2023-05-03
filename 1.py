def define_posicoes(linha, coluna, orientacao, tamanho):
    lista_posicoes= []
    if orientacao=="vertical":
        for posicao in range(tamanho):
            lista_posicoes.append([linha+posicao, coluna])
    elif orientacao == 'horizontal':
        for posicao in range(tamanho):
            lista_posicoes.append([linha, coluna+posicao])
    return lista_posicoes


def preenche_frota(frota, nome, linha, coluna, orientacao, tamanho):
    cordenadas= define_posicoes(linha, coluna, orientacao, tamanho)
    if nome not in frota:
        frota[nome]= [cordenadas]
    else:
        frota[nome].append(cordenadas)
    return frota

def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna]= 'X'
    else:
        tabuleiro[linha][coluna]= '-'
    return tabuleiro

def posiciona_frota(navios):
    grid= [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    for navio_tipo in navios:
        for navio in navios[navio_tipo]:
            for cordenada in navio:
                grid[cordenada[0]][cordenada[1]]=1
    return grid
            

def afundados(frota, tabuleiro):
    resultado=0
    for modelo in frota:
        for navio in frota[modelo]:
            naufrago=True
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]]!='X':
                    naufrago=False
            if naufrago==True:
                resultado+=1
    return resultado

def posicao_valida(tabuleiro,linha, coluna, orientacao, tamanho):
    posicao= define_posicoes(linha, coluna, orientacao, tamanho)
    for posicoes in tabuleiro.values():
        for navio in posicoes:
            for i in posicao:
                if i in navio:
                    return False
                
    for i in posicao:
        if i[0]<0 or i[0]>9 or i[0]<0 or i[1]>9:
            return False
    return True

print(posicao_valida({'porta-aviões': [[[0, 0], [0, 1], [0, 2], [0, 3]]], 'navio-tanque': [[[4, 9], [5, 9], [6, 9]], [[6, 3], [7, 3], [8, 3]]], 'contratorpedeiro': [[[4, 3], [4, 4]]]}, 2, 9, 'horizontal', 2))



