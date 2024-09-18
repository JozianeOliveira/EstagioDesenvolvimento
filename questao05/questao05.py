# Definindo o estado dos interruptores e lâmpadas
interruptores = {
    "Interruptor 1": "Desligado",
    "Interruptor 2": "Desligado",
    "Interruptor 3": "Desligado"
}

lampadas = {
    "Lâmpada 1": "Desligada",
    "Lâmpada 2": "Desligada",
    "Lâmpada 3": "Desligada"
}

def ligar_interruptor(interruptor):
    interruptores[interruptor] = "Ligado"

def desligar_interruptor(interruptor):
    interruptores[interruptor] = "Desligado"

def acender_lampada(lampada):
    lampadas[lampada] = "Ligada"

def apagar_lampada(lampada):
    lampadas[lampada] = "Desligada"

# Simulação do processo
# Passo 1: Ligar o Interruptor 1 e esperar
ligar_interruptor("Interruptor 1")
# Simulando o tempo de espera (aqui representado como um atraso)
import time
time.sleep(5)  # Espera simulada de 5 segundos
desligar_interruptor("Interruptor 1")
# Passo 2: Ligar o Interruptor 2
ligar_interruptor("Interruptor 2")

# Simulação dos resultados após a visita às salas das lâmpadas
lampadas_resultados = {
    "Lâmpada 1": "Quente e Desligada",  # Conectada ao Interruptor 1
    "Lâmpada 2": "Ligada e Quente",     # Conectada ao Interruptor 2
    "Lâmpada 3": "Desligada e Fria"     # Conectada ao Interruptor 3
}

print("Estado dos Interruptores:", interruptores)
print("Estado das Lâmpadas:", lampadas_resultados)

# Explicação dos resultados
print("\nExplicação dos Resultados:")
for lampada, estado in lampadas_resultados.items():
    if estado == "Ligada e Quente":
        print(f"A {lampada} está ligada e quente. Esta lâmpada está conectada ao Interruptor 2, que está atualmente ligado.")
    elif estado == "Quente e Desligada":
        print(f"A {lampada} está quente e desligada. Esta lâmpada está conectada ao Interruptor 1, que foi ligado anteriormente e depois desligado.")
    elif estado == "Desligada e Fria":
        print(f"A {lampada} está desligada e fria. Esta lâmpada está conectada ao Interruptor 3, que nunca foi ligado.")
