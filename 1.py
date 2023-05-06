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

i= 0                            #Condição Inicial para entrar no while
frota = {
    "porta-aviões":[],
    "navio-tanque":[],
    "contratorpedeiro":[],
    "submarino": [],
}                               #Dicionario vazio

while i< 10:                    #Quantidade de navios
    if i == 0 :
        nome= 'porta-aviões'
        tamanho= 4
    elif i >=1 and i <=2:
        nome= 'navio-tanque'
        tamanho= 3
    elif i >= 3 and i <= 6:
        nome = 'contratorpedeiro'
        tamanho = 2
    elif i > 6: 
        nome = 'submarino'
        tamanho = 1
    print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
    condicao= True
    while condicao:
        linha= input("Linha: ")
        coluna= input("Coluna: ")
        orientacao_numero= input('[1] Vertical [2] Horizontal >')
        orientacao=''
        if orientacao_numero== '1':
            orientacao='vertical'
        elif orientacao_numero== '2':
            orientacao = 'horizontal'
        if define_posicoes(linha, coluna, orientacao, tamanho)== True:
            preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
            i+=1
            condicao= False
        else:
            print('Esta posição não está válida!')
print(frota)

