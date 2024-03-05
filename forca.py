 palavra_secreta="oii"
    letras_corretas = ["_","_","_"]
    tentativas= 2;
    while tentativas > 0 and "_" in letras_corretas:
        palpite = input ("digite uma letra").lower()
        
        if palpite in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if palpite == letra: 
                    letras_corretas[index] = letra
                index += 1
        else: 
            tentativas -=1 
            print(f"Restam apenas {tentativas} tentativas.")
            
        print(" ".join(letras_corretas)) 
        
    if "_" not in letras_corretas:
        print("parabens, voce ganhou!")
    else:
            print(f"que pena voce perdeu, a palavra secreta era {palavra_secreta}")
if__name__ == "__main__":
        jogar()
