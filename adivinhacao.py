import random

#Declaração de uma função jogar_adivinhação
def jogar_adivinhação():
    
    #Solicita o jogador que escolha o ível de dificuldade
    nivel = int(input("Escolha o nível de dificuldade (1- Fácil, 2- Médio, 3- Difícil):"))
    max_numero: 30 if nivel == 1 else 50 if nivel == 2 else 100
    numero_secreto= random.randint(1,max_numero)
    tentativas= 30 if nivel == 1 else 15 if nivel == 2 else 5
    Pontos = 1000
    
    print (f"Jogo de advinhação -Nível{nivel}")
    print (f"Tente adivinhar o número que estou pensando, entre 1 e {max_numero}.")
    
    for tentativa in range (1, tentativas + 1):
          print(f"Tentativa {tentativa} de {tentativas}")
          palpite = int(input("Digite seu palpite:"))
    if palpite < 1 or palpite > max_numero:
        print(f"Digite um número entre 1 e {max_numero})
        
        acertou = palpite == numero_secreto
        maior = palpite > numero_secreto
        menor = palpite < numero_secreto
            
        if acertou 
            print(f"Vc acertou e fez {pontos} pontos!!)
            break 
        else:
            pontos_perdidos = abs(numero_secreto - palpite)
            pontos-= pontos_perdidos
            if maior:
                print(f"Seu palpite foi maior que o número secreto.)
            elif menor: 
                print(f"Seu palpite foi menor que o número secreto.)
        if not acertou:
        print(f"Suas tentativas acabaram o número secreto era {numero_secreto}")
        print ("Obrigado por jogar- Bjs")
        
 if __name__  == "__main__":
     jogar_advinhacao()

