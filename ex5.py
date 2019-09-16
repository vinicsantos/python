def defineChances():
    chances = int(input("Entre com a quantidade de chances para a forca: "))
    return chances

def definePalavra():
    palavra = input("Entre com a palavra desejada para a forca: ")
    return palavra

def insereUnderlines(palavra):
    palavrinha = ""
    for i in range(0, len(palavra)):
        palavrinha = palavrinha + ("_ ")
    return palavrinha

def insereLetra(letra, posicaoLetra, palavra, palavrinha):
    for j in range(0, len(palavra)):
        for i in range(0, len(posicaoLetra)):
            if(posicaoLetra[i] == j):
                palavrinha = palavrinha + letra + " "
                print(palavrinha)
    return palavrinha

def iniciaJogo(palavra, chances, palavrinha):
    letrasInseridas = ""
    while(chances > 0):
        posicaoLetra = []
        palavrinha = palavrinha
        if(letrasInseridas == ""):
            print(palavrinha)
            print("")
            print("Chances restantes: %i" %chances)
            letra = input("Escolha uma letra: ")
            if (len(letra) > 1):
                    print("Apenas uma letra por vez.")
            else:
                if(palavra.lower() == palavrinha.replace(" ", "").lower()):
                    print("Parabens!!!!!!!!!!!!!!! Voce ganhou!")
                else:
                    if(letra.lower() in palavra.lower()):
                        for i in range(0, len(palavra)):
                            if(letra == palavra[i]):
                                posicaoLetra.append(i)
                                palavrinha = insereLetra(letra, posicaoLetra, palavra,palavrinha)
                    letrasInseridas = letra
                    chances = chances - 1
        else:
            print(palavrinha)
            print("")
            print("Letras jogadas: %s" %letrasInseridas)
            print("Chances restantes: %i" %chances)
            letra = input("Escolha uma letra: ")
            if(letra.lower() in letrasInseridas.lower()):
                print("Esta letra ja foi inserida!")
            else:
                if(palavra.lower() == palavrinha.replace(" ", "").lower()):
                    print("Parabens!!!!!!!!!!!!!!! Voce ganhou!")
                else:
                    if (len(letra) > 1):
                        print("Apenas uma letra por vez.")
                    else:
                        if(letra.lower() in palavra.lower()):
                            for i in range(0, len(palavra)):
                                if(letra == palavra[i]):
                                    posicaoLetra.append(i)
                                    palavrinha = insereLetra(letra, posicaoLetra, palavra, palavrinha)
                        letrasInseridas = letrasInseridas + ", " + letra
                        chances = chances - 1
        

palavra = definePalavra()
chances = defineChances()
palavrinha = insereUnderlines(palavra)
iniciaJogo(palavra, chances, palavrinha)