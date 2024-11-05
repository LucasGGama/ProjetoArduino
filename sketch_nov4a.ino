#include <LiquidCrystal.h>  // Biblioteca para displays LCD sem I2C 

// Definindo os pinos do LCD: RS, E, D4, D5, D6, D7
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 

// Definindo os pinos
const int botaoPin = 7;  // Pino digital ao qual o botão está conectado
int fila = 1;            // Variável para armazenar o número da fila
int estadoBotao;         // Variável para armazenar o estado atual do botão
int ultimoEstadoBotao = LOW;  // Armazena o último estado do botão
unsigned long ultimaMudanca = 0; // Armazena o último tempo de mudança
const unsigned long debounceDelay = 200; // Tempo para evitar "bounce" (ruído) ao apertar o botão

void setup() {
  Serial.begin(9600);  // Inicializa a comunicação serial
  pinMode(botaoPin, INPUT_PULLUP);  // Define o pino do botão com o resistor de pull-up interno
  lcd.begin(16, 2);          // Inicializa o display LCD no modo 16 colunas e 2 linhas
  lcd.setCursor(0, 0);       // Define o cursor na primeira linha e primeira coluna
  lcd.print("Sua senha : ");  // Exibe "Numero da Fila" no LCD
  lcd.print(fila);           // Exibe o número inicial da fila (1)
}

void loop() {
  // Lê o estado atual do botão (invertido porque o pull-up faz o estado HIGH ser o padrão)
  estadoBotao = digitalRead(botaoPin);

  // Verifica se o botão foi pressionado (transição de HIGH para LOW)
  if (estadoBotao == LOW && ultimoEstadoBotao == HIGH && (millis() - ultimaMudanca > debounceDelay)) {
    ultimaMudanca = millis();  // Atualiza o tempo da última mudança
    fila++;                    // Incrementa o número da fila

    // Se a fila for maior que 99, volta para 1
    if (fila > 99) {
      fila = 1;
    }

    // Atualiza o display LCD
    lcd.clear();               // Limpa o display
    lcd.setCursor(0, 0);       // Define o cursor na primeira linha
    lcd.print("Sua senha : ");  // Exibe "Numero da Fila"
    lcd.print(fila);           // Exibe o número atual da fila

    // Envia o horário e número da fila para o Python via serial
    Serial.print("Fila: ");
    Serial.print(fila);
    Serial.print(" - Horário: ");
    Serial.println(millis());  // Envia o valor de millis() para indicar o tempo de execução
  }

  // Armazena o estado do botão para a próxima leitura
  ultimoEstadoBotao = estadoBotao;
}
