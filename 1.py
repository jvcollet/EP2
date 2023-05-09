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

frota_jogador = {
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

            if posicao_valida(frota_jogador, linha, coluna, orientacao, tamanho[1]) == False:
                while posicao_valida(frota_jogador, linha, coluna, orientacao, tamanho[1]) == False:

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
                
                frota_jogador = preenche_frota(frota_jogador, navio, linha, coluna, orientacao, tamanho[1])
            
            else:
                frota_jogador = preenche_frota(frota_jogador, navio, linha, coluna, orientacao, tamanho[1])

        else:
            orientacao = 'horizontal'

            if posicao_valida(frota_jogador, linha, coluna, orientacao, tamanho[1]) == False:
                while posicao_valida(frota_jogador, linha, coluna, orientacao, tamanho[1]) == False:

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

                frota_jogador = preenche_frota(frota_jogador, navio, linha, coluna, orientacao, tamanho[1])
                
            else:
                frota_jogador = preenche_frota(frota_jogador, navio, linha, coluna, orientacao, tamanho[1])


#Jogadas do jogador

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador =  posiciona_frota(frota_jogador)

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

jogando = True
cordenadas = []
while jogando:
    perguntando = True
    tabuleiros = monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente)
    print(tabuleiros)
    while perguntando:
        linha_ataque = int(input("Linha do ataque:"))
        while linha_ataque < 0 or linha_ataque > 9: 
            print('Linha inválida!')
            linha_ataque = int(input("Linha do ataque:"))
        
        coluna_ataque = int(input("Coluna do ataque:"))
        while coluna_ataque < 0 or coluna_ataque > 9:
            print('Coluna inválida!')
            coluna_ataque = int(input("Coluna do ataque:"))
        if [linha_ataque, coluna_ataque] not in cordenadas:
            cordenadas.append([linha_ataque,coluna_ataque])
            break
        else:
            print(f'A posição linha_ataque {linha_ataque} e coluna_ataque {coluna_ataque} já foi informada anteriormente!')
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha_ataque, coluna_ataque)
    if afundados(frota_oponente, tabuleiro_oponente)== True :
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
        break


