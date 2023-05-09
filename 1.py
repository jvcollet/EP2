def define_posicoes( linha, coluna, orientacao, tamanho):
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


#Posicionando frota

frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}

dicionario_embarcacoes = {'porta-aviões': [1, 4], 'navio-tanque': [2, 3], 'contratorpedeiro': [3, 2], 'submarino': [4, 1]}

for navio, tamanho in dicionario_embarcacoes.items():
    
    for i in range(0, tamanho[0]):
        print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho[1]}')

        linha = int(input('Linha: '))
        coluna = int(input('Coluna: '))

        if navio != 'submarino':
            orientacao = int(input('[1] Vertical [2] Horizontal > '))

            if orientacao == 1:
                orientacao = 'vertical'
            if orientacao == 2:
                orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho[1]) == False:
                while posicao_valida(frota, linha, coluna, orientacao, tamanho[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if navio != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'
                
                frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho[1])
            
            else:
                frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho[1])

        else:
            orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho[1]) == False:
                while posicao_valida(frota, linha, coluna, orientacao, tamanho[1]) == False:

                    print('Esta posição não está válida!')
                    print(f'Insira as informações referentes ao navio {navio} que possui tamanho {tamanho[1]}')

                    linha = int(input('Linha: '))
                    coluna = int(input('Coluna: '))

                    if navio != 'submarino':
                        orientacao = int(input('[1] Vertical [2] Horizontal > '))

                        if orientacao == 1:
                            orientacao = 'vertical'
                        if orientacao == 2:
                            orientacao = 'horizontal'

                frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho[1])
                
            else:
                frota = preenche_frota(frota, navio, linha, coluna, orientacao, tamanho[1])

print(frota)

