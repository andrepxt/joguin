# Exibe uma mensagem de boas-vindas
print("Olá, seja bem-vindx ao 'Perguntinhas' \n")

# Pergunta o nome do jogador
nome = input("Qual o seu nome?\n")

# Exibe uma mensagem de boas-vindas com o nome do jogador
print("Muito prazer,", nome,"!" "\n")

# Explica as regras do jogo
print("Vou escolher um número de 1 a 100 e você deve adivinhar qual foi, ok?\n")
print("Você terá 5 (cinco) chances para acertar esse número e a cada palpite vou te avisando se você acertou seguido de uma dica no caso do palpite estar errado.\n")

# Pergunta se o jogador deseja começar
seleção1 = (input("Deseja começar?\n")) 

# Condição para verificar se a resposta foi "sim" ou "Sim" para começar o jogo
if seleção1.lower() == "sim":  # Usando .lower() para tornar a comparação insensível ao caso
    import random  # Importa o módulo random para gerar números aleatórios

    num1 = random.randint(1, 100)  # Gera um número aleatório entre 1 e 100

    tentativas = 5  # Estipula 5 tentativas para o jogador
    while tentativas > 0:  # Enquanto o jogador tiver tentativas restantes
        print(f"\nVocê tem {tentativas} tentativas restantes.")  # Informa o número de tentativas restantes
        print(f"Palpite {6 - tentativas}:")  # Exibe o número da tentativa atual (começando de 1)
        palpite1 = input()  # O jogador dá o palpite

        # Verifica se o palpite do jogador está correto
        if int(palpite1) == num1:
            print("Parabéns, seu palpite está correto!\n")
            break  # Sai do loop se o jogador acertar o número

        # Se o palpite estiver errado, verifica se o número é maior ou menor
        elif int(palpite1) > num1:
            print("Huuum, você tem que escolher um número menor... Tente de novo.\n")
        elif int(palpite1) < num1:
            print("Huuum, você tem que escolher um número maior... Tente de novo.\n")

        tentativas -= 1  # Decrementa o número de tentativas restantes

    # Se o jogador não acertou após as 5 tentativas, exibe uma mensagem final
    if tentativas == 0:
        print(f"O número era {num1}. Que pena, você não acertou! Tente novamente da próxima vez.")

# Caso o jogador não deseje começar, o programa termina
else:
    print("Que pena, talvez na próxima vez!")
    
# Espera o jogador pressionar Enter para sair
input("Pressione Enter para sair")
