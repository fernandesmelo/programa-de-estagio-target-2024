# 4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

# Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?

def verificar_interruptores():
    lampadas = [0, 0, 0]

    lampadas[0] = 1

    lampadas[1] = 1
    lampadas[0] = 0

    print("Estado das lâmpadas:")
    for i in range(len(lampadas)):
        if lampadas[i] == 1:
            print(f"Lâmpada {i+1} está acesa.")
        else:
            print(f"Lâmpada {i+1} está apagada.")

verificar_interruptores()
