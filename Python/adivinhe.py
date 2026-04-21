import random

print("ADIVINHE O NÚMERO")
erros = 0
escolha = random.randint(1, 10)

while True:
    n = int(input("Manda o número de 1 a 10: "))
    if n != escolha:
        if n > 10:
            print("ATENÇÃO! Só pode número de 1 a 10")
        print("Errou, tente de novo!")
        erros +=1
    else:
        print("Certinho!")
        break

#print("----------------------")#
    
if erros == 0:
    print("Brabo! Pelé das adivinhações!🥵. Errou nenhuma vez")
elif erros == 1:
    print("Quem nunca erra, né? Errou só uma vez")
elif erros == 5:
    print(f"Demorou ein...Quase perdi as contas... Errou {erros} vezes")
elif erros > 5:
    print(f"Perdi as contas, mas sua sorte foi que o robô contou que tu errou {erros} vezes")

print("------------------------")