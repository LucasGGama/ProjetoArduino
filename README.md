Projeto de Registro de Horários com Arduino e Python
Este projeto foi desenvolvido com o objetivo de registrar o horário em que um botão conectado ao Arduino é pressionado, e integrar esse registro com uma interface gráfica no Python usando a biblioteca Tkinter. O sistema permite visualizar os registros em tempo real e exportar os dados para um arquivo Excel para facilitar o gerenciamento e análise.

Componentes Utilizados
Arduino Uno: Utilizado para capturar os dados do botão e enviar via comunicação serial.
Botão Push-Button: Conectado ao Arduino para simular uma ação de "senha" que é registrada a cada vez que é pressionado.
Display LCD: Utilizado para exibir o número da "senha" no Arduino.
Python com Tkinter: Interface gráfica para exibir os registros capturados e exportar para Excel.

#ALGUNS ERROS.

Segue o erro que eu dei após instalar o manda e pedir para exportar os dados para excel, precisava de mais uma biblioteca para salvar os arquivos em excel precisava da biblioteca "openpyxl"

Exception in Tkinter callback 
Traceback (most recent call last):
  File "C:\Users\Exitu\AppData\Local\Programs\Python\Python312\Lib\tkinter\_init.py", line 1948, in __call_
    return self.func(*args)
           ^^^^^^^^^^^^^^^^
  File "C:/Users/Exitu/AppData/Local/Programs/Python/Python312/registro de horarios.py", line 44, in exportar_para_excel
    df.to_excel("horarios_arduino.xlsx", index=False)  # Exporta para um arquivo Excel
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Exitu\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\util\_decorators.py", line 333, in wrapper
    return func(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\Exitu\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\core\generic.py", line 2417, in to_excel
    formatter.write(
  ERRO :
File "C:\Users\Exitu\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\io\formats\excel.py", line 943, in write
    writer = ExcelWriter(
             ^^^^^^^^^^^^
  File "C:\Users\Exitu\AppData\Local\Programs\Python\Python312\Lib\site-packages\pandas\io\excel\openpyxl.py", line 57, in __init_
    from openpyxl.workbook import Workbook
ModuleNotFoundError:

[08:40, 05/11/2024] Lucas Gama: Para organizar os botões "Iniciar Registro" e "Exportar para Excel" lado a lado, você pode usar o layout pack() com a opção side=tk.LEFT ou usar o layout grid() ou place(). Vou ajustar o código para usar o pack() com os botões lado a lado.
[08:40, 05/11/2024] Lucas Gama: O que foi alterado:
Frame para os botões: Criei um Frame chamado frame_botoes para conter os dois botões.
Layout lado a lado: Os botões Iniciar Registro e Exportar para Excel agora estão organizados lado a lado usando o layout pack() com a opção side=tk.LEFT e algum padx para espaçamento horizontal entre eles.
[08:40, 05/11/2024] Lucas Gama: pip install pandas
FOI NECESSÁRIO PRA FAZER A EXPORTAÇÃO PARA EXCEL
[08:40, 05/11/2024] Lucas Gama: texto_scroll.pack(fill=tk.BOTH, expand=True): 
Troquei porque ficava 600x400 e se eu aumentasse a janela ficava mal posicionado 
A opção fill=tk.BOTH faz com que a área de texto preencha tanto horizontal quanto verticalmente o espaço disponível. A opção expand=True permite que o widget se expanda conforme a janela aumenta ou diminui de tamanho.
[08:40, 05/11/2024] Lucas Gama: foi necessário acrescentar o código para que a interface gerada pelo tkinter não travasse, explicação
root.after(100, registrar_horario): Isso garante que a função registrar_horario() seja chamada a cada 100 milissegundos sem travar a interface gráfica. O Tkinter pode continuar atualizando a interface enquanto a função é chamada periodicamente.
[08:40, 05/11/2024] Lucas Gama: Criei duas def para exportar para o excel
