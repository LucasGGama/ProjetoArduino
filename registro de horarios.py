import serial
import time
import tkinter as tk
from tkinter import scrolledtext
import pandas as pd  # Para exportar para Excel

# Inicializa a comunicação serial (substitua 'COM3' pela porta serial que o Arduino está usando)
arduino = serial.Serial('COM3', 9600)

# Lista para armazenar os registros
registros = []

# Função para registrar o horário em que o botão foi apertado
def registrar_horario():
    if arduino.in_waiting > 0:
        # Lê a linha enviada pelo Arduino
        linha = arduino.readline().decode('utf-8').strip()

        # Registra o horário atual do sistema
        horario_computador = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        # Exibe a informação na área de texto
        texto_scroll.insert(tk.END, f"Recebido do Arduino: {linha} - Horário do computador: {horario_computador}\n")
        texto_scroll.see(tk.END)  # Rola automaticamente para a última linha

        # Armazena o registro na lista
        registros.append({"Registro Arduino": linha, "Horário do Computador": horario_computador})

        # Opcional: salvar o horário em um arquivo de texto
        with open("horarios_registrados.txt", "a") as arquivo:
            arquivo.write(f"{linha} - Horário do computador: {horario_computador}\n")

    # Chama a função novamente após 100 milissegundos, mantendo o loop não bloqueante
    root.after(100, registrar_horario)

# Função para iniciar o loop de verificação da porta serial
def iniciar_arduino():
    registrar_horario()  # Inicia a leitura sem bloquear o Tkinter

# Função para exportar os registros para um arquivo Excel
def exportar_para_excel():
    if registros:
        df = pd.DataFrame(registros)  # Cria um DataFrame a partir da lista de registros
        df.to_excel("horarios_arduino.xlsx", index=False)  # Exporta para um arquivo Excel
        texto_scroll.insert(tk.END, "Registros exportados para 'horarios_arduino.xlsx'.\n")
        texto_scroll.see(tk.END)
    else:
        texto_scroll.insert(tk.END, "Nenhum registro para exportar.\n")
        texto_scroll.see(tk.END)

# Função para encerrar o programa e exportar os registros para Excel
def encerrar():
    exportar_para_excel()  # Exporta os registros antes de fechar
    root.destroy()  # Fecha a janela do Tkinter

# Criar a janela do Tkinter
root = tk.Tk()
root.title("Registro de Horários do Arduino")

# Aumenta o tamanho da janela
root.geometry("600x400")  # Define a largura (600px) e altura (400px)

# Área de texto com scroll para exibir as mensagens
texto_scroll = scrolledtext.ScrolledText(root, width=70, height=20)
texto_scroll.pack(fill=tk.BOTH, expand=True, pady=10)  # Ajusta o preenchimento e expansão da área de texto

# Frame para organizar os botões lado a lado
frame_botoes = tk.Frame(root)
frame_botoes.pack(pady=5)

# Botão para iniciar a leitura do Arduino
botao_iniciar = tk.Button(frame_botoes, text="Iniciar Registro", command=iniciar_arduino)
botao_iniciar.pack(side=tk.LEFT, padx=10)  # Botão à esquerda com espaço entre eles

# Botão para exportar os registros para Excel
botao_exportar = tk.Button(frame_botoes, text="Exportar para Excel", command=exportar_para_excel)
botao_exportar.pack(side=tk.LEFT, padx=10)  # Botão à esquerda ao lado do outro botão

# Botão para encerrar o programa e gerar Excel
botao_encerrar = tk.Button(frame_botoes, text="Encerrar", command=encerrar)
botao_encerrar.pack(side=tk.LEFT, padx=10)  # Botão à esquerda ao lado do outro botão

# Executa o loop principal do Tkinter
root.mainloop()
