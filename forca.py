import random
import jogos

def jogar():
    imprime_abertura()

    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    # print(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        chute = solicita_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            print("Chances restantes: {}".format(6-erros))
            desenha_forca(erros)
            erros += 1

        enforcou = erros == 7
        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdeu(palavra_secreta)
    jogos.escolha_jogo()

def imprime_abertura():
    print("***************************")
    print("Bem vindo ao jogo da Forca!")
    print("***************************\n")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip().upper()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero]
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def solicita_chute():
    chute = input("Qual letra? ").upper().strip()
    return chute

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 0):
        print(" |      ( )   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def imprime_mensagem_perdeu(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def marca_chute_correto(chute, letras, palavra):
    index = 0
    for letra in palavra:
        if chute == letra:
            letras[index] = letra
            # print("Encontrei a letra {} na posição {}".format(letra,index))
        index += 1

if (__name__ == "__main__"):
    jogar()
    #inicia jogo