
import time

def timer():
    sec = int(input("\nDigite a quantidade de segundos: "))
    print("\nContagem iniciando...  ")
    temp = sec
    while temp != 0:
        if temp != sec:
            print("\b"*len(str(temp)), end="")
        time.sleep(1)
        temp -= 1
        print(temp, end='')
    print("\nContagem encerrada! \n")

print("Contador de segundos\n")
while 1:
    choice = input("Deseja iniciar uma contagem agora? (sim/nao): ")
    if "sim" in choice.lower():
        timer()
    elif "nao" in choice.lower():
        print("Saindo...")
        break
    else:
        print("Comando inválido tente novamente...")