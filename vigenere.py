import matplotlib.pyplot as plt


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

print('Digite a mensagem')
mensagem = input()
print('Digite a chave')
chave = input()

def remove_char_especial(texto):
    texto = texto.lower()
    #texto = texto.replace(' ','')
    texto = texto.replace(',','')
    texto = texto.replace('.','')
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

    return texto

mensagem = remove_char_especial(mensagem)
chave = remove_char_especial(chave)

def vigenere(mensagem, chave):
    criptograma = ''
    i = 0
    for char in mensagem:
        if(char == ' '):
            criptograma = criptograma + ' '
            continue
        ascii_msg   = ord(char)-97
        ascii_chave = ord(chave[i])-97
        criptograma = criptograma + matriz[ascii_msg][ascii_chave]
        i = (i+1)%len(chave)
    return criptograma

def decrypt_vigenere(criptograma, chave):
    mensagem_original = ''
    i = 0
    for char in criptograma:
        if(char == ' '):
            mensagem_original = mensagem_original + ' '
            continue
        ascii_cript = ord(char)-97
        ascii_chave = ord(chave[i])-97
        for linha in matriz:
            if(linha[ascii_chave] == char):
                mensagem_original = mensagem_original + linha[0]
        i = (i+1)%len(chave)
    return mensagem_original

criptograma = vigenere(mensagem, chave)
mensagem_original = decrypt_vigenere(criptograma, chave)

print('criptograma = ' + criptograma)
print('mensagem = ' + mensagem_original)


frequencias_portugues = [14.63, 1.04, 3.88, 4.99, 12.57, 1.02, 1.3, 1.28, 6.18, 0.4, 0.02, 2.78, 4.74,
                         5.05, 10.73, 2.52, 1.2, 6.53, 7.81, 4.34, 4.63, 1.67, 0.01, 0.21, 0.01, 0.47]

#plt.bar(linhaA, frequencias_portugues)
#plt.title('Grafico de frequencias')
#plt.xlabel('Letras')
#plt.ylabel('Frequencia')
#plt.show()