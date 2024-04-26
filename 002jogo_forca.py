import random

todas_palavras_secretas = ["Gustavo", "Roniel", "Silva"]
random.shuffle(todas_palavras_secretas)

palavra_do_jogo = todas_palavras_secretas[0].lower()
letras_acertadas = ""
numero_tentativas = 0

while True:
    letra_digitada = input("Digite uma letra ")
    numero_tentativas += 1

    if len(letra_digitada) > 1:
        print("Digite apenas uma letra")
        continue

    if letra_digitada in palavra_do_jogo:
        letras_acertadas += letra_digitada

    palavra_formada = ""
    for letra_secreta in palavra_do_jogo:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += "*"
    print("Palavra formada: ", palavra_formada)

    if palavra_formada == palavra_do_jogo:
        print("PARABÉNS, VOCÊ GANHOU!")
        print("A palavra secreta era ", palavra_do_jogo.upper())
        print(f"Você levou {numero_tentativas} tentativas para acertar")
        break
