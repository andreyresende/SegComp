linhaA = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
linhaB = ['b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a']
linhaC = ['c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b']
linhaD = ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c']
linhaE = ['e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d']
linhaF = ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e']
linhaG = ['g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f']
linhaH = ['h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g']
linhaI = ['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h']
linhaJ = ['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i']
linhaK = ['k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j']
linhaL = ['l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k']
linhaM = ['m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l']
linhaN = ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
linhaO = ['o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n']
linhaP = ['p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
linhaQ = ['q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p']
linhaR = ['r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q']
linhaS = ['s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']
linhaT = ['t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s']
linhaU = ['u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t']
linhaV = ['v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
linhaW = ['w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v']
linhaX = ['x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
linhaY = ['y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x']
linhaZ = ['z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']

matriz = [linhaA, linhaB, linhaC, linhaD, linhaE, linhaF, linhaG, linhaH, linhaI, linhaJ, linhaK, linhaL, linhaM, 
          linhaN, linhaO, linhaP, linhaQ, linhaR, linhaS, linhaT, linhaU, linhaV, linhaW, linhaX, linhaY, linhaZ]

frequencias_portugues = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.3, 1.28, 6.18, 0.4, 0.02, 2.78, 4.74,
                         5.05, 10.73, 2.52, 1.2, 6.53, 7.81, 4.34, 4.63, 1.67, 0.01, 0.21, 0.01, 0.47]

def remove_char_especial(texto):
    texto = texto.lower()
    texto = texto.replace(' ','')
    texto = texto.replace(',','')
    texto = texto.replace('.','')
    texto = texto.replace(':','')
    texto = texto.replace(';','')
    texto = texto.replace('?','')
    texto = texto.replace('+','')
    texto = texto.replace('/','')
    texto = texto.replace('\'','')
    texto = texto.replace('\"','')
    texto = texto.replace('á','a')
    texto = texto.replace('à','a')
    texto = texto.replace('â','a')
    texto = texto.replace('ã','a')
    texto = texto.replace('é','e')
    texto = texto.replace('ê','e')
    texto = texto.replace('í','i')
    texto = texto.replace('ó','o')
    texto = texto.replace('ô','o')
    texto = texto.replace('õ','o')
    texto = texto.replace('ú','u')
    texto = texto.replace('ç','c')
    texto = texto.replace('(','')
    texto = texto.replace(')','')
    texto = texto.replace('[','')
    texto = texto.replace(']','')
    texto = texto.replace('{','')
    texto = texto.replace('}','')
    texto = texto.replace('-','')
    texto = texto.replace('_','')
    texto = texto.replace('0','')
    texto = texto.replace('1','')
    texto = texto.replace('2','')
    texto = texto.replace('3','')
    texto = texto.replace('4','')
    texto = texto.replace('5','')
    texto = texto.replace('6','')
    texto = texto.replace('7','')
    texto = texto.replace('8','')
    texto = texto.replace('9','')

    return texto

def vigenere(mensagem, chave):
    criptograma = ''
    i = 0
    for caractere in mensagem:
        if(caractere == ' '):
            criptograma = criptograma + ' '
            continue
        ascii_msg   = ord(caractere)-ord('a')
        ascii_chave = ord(chave[i])-ord('a')
        criptograma = criptograma + matriz[ascii_chave][ascii_msg]
        i = (i+1)%len(chave)
    return criptograma

def decrypt_vigenere(criptograma, chave):
    mensagem_original = ''
    i = 0
    for caractere in criptograma:
        if(caractere == ' '):
            mensagem_original = mensagem_original + ' '
            continue
        ascii_chave = ord(chave[i])-ord('a')
        for linha in matriz:
            if(linha[ascii_chave] == caractere):
                mensagem_original = mensagem_original + linha[0]
        i = (i+1)%len(chave)
    return mensagem_original

def cria_subtextos(criptograma, k):#Dado um tamanho de chave k especifico, cria k subtextos para calcular o indice de coincidencia
    subtextos = [''] * k
    i = 0

    for letra in criptograma: #Coloca uma letra de cada vez no subespaco apropriado
        subtextos[i] = subtextos[i] + letra
        i += 1
        if (i == k):
            i = 0
    return subtextos

def calcula_indice_coincidencia(subtexto):#Calcula o indice de coincidencia de um unico subtexto
    tamanho  = len(subtexto)
    if tamanho <= 1:
        return 0 #Quando o texto eh pequeno o teste com chaves grandes gera subespacos pequenos e pode acontecer divisao por zero
    contador = [0] * 26 #Um contador para cada armazenar quantas vezes cada letra aparece
    numerador = 0

    for caractere in subtexto:#Conta quantas vezes cada letra apareceu
        i = ord(caractere) - ord('a')
        contador[i] += 1

    for quantidade in contador:#Aplica o somatorio que define a formula para calcular o indice de coincidencia
        produto = quantidade * (quantidade - 1)
        numerador += produto

    denominador = tamanho * (tamanho - 1)
    return numerador/denominador

def calcula_media_indices(criptograma, k):
    subtextos = cria_subtextos(criptograma, k)
    soma = 0
    for subtexto in subtextos:
        soma += calcula_indice_coincidencia(subtexto)
    return soma/k

def mostra_indices_coincidencia(criptograma):
    for i in range(1, 21): #Mostra os indices para todos os tamanhos de chave de 1 a 20
        print('Para chave de tamanho ' + str(i) +', indice de coincidencia = ' + str(round(calcula_media_indices(criptograma, i),3)))

def desloca_texto(texto, deslocamento):
    texto_deslocado = ''
    for letra in texto:
        cod_ascii_deslocado = (((ord(letra)-ord('a'))-deslocamento)%26)+ord('a')
        texto_deslocado += chr(cod_ascii_deslocado)
    return texto_deslocado            

print('Digite a mensagem')
mensagem = input()
print('Digite a chave')
chave = input()

mensagem = remove_char_especial(mensagem)
chave = remove_char_especial(chave)

criptograma = vigenere(mensagem, chave)
mensagem_original = decrypt_vigenere(criptograma, chave)

print('Criptograma = ' + criptograma)
print('Mensagem = ' + mensagem_original)

mostra_indices_coincidencia(criptograma)
print('Qual tamanho de chave mais se adequa?')
tamanho_chave = int(input())
