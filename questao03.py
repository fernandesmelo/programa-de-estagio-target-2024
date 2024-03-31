# 3) Descubra a lógica e complete o próximo elemento:

# a) 1, 3, 5, 7, ___
# b) 2, 4, 8, 16, 32, 64, ____
# c) 0, 1, 4, 9, 16, 25, 36, ____
# d) 4, 16, 36, 64, ____
# e) 1, 1, 2, 3, 5, 8, ____
# f) 2,10, 12, 16, 17, 18, 19, ____

def proximo_elemento_a():
    ultimo_numero = 7
    proximo_numero = ultimo_numero + 2
    return proximo_numero

def proximo_elemento_b():
    ultimo_numero = 64
    proximo_numero = ultimo_numero * 2
    return proximo_numero

def proximo_elemento_c():
    ultimo_numero = 36
    proximo_numero = (int(ultimo_numero ** 0.5) + 1) ** 2
    return proximo_numero

def proximo_elemento_d():
    ultimo_numero = 64
    proximo_numero = (int(ultimo_numero ** 0.5) + 1) ** 2
    return proximo_numero

def proximo_elemento_e():
    penultimo_numero = 5
    ultimo_numero = 8
    proximo_numero = penultimo_numero + ultimo_numero
    return proximo_numero

print("Próximos elementos das sequências:")
print("a) ", proximo_elemento_a())
print("b) ", proximo_elemento_b())
print("c) ", proximo_elemento_c())
print("d) ", proximo_elemento_d())
print("e) ", proximo_elemento_e())
print("f) Indeterminado (necessita mais informações)")


#OBS: A sequ~encia F parece não seguir uma lógica clara por isso marquei como indeterminada.