#include <WiFi.h>
#include <ArduinoJson.h>
#include <PubSubClient.h>

#define MQTT_DEBUG true

// Substitua os valores abaixo com as suas informações de rede e MQTT
const char* ssid = "RedmiNote8T";
const char* password = "yuridosreis";
const char* mqtt_server = "tcp://0.tcp.sa.ngrok.io";
const char* topic = "status";

WiFiClient wifiClient;
WiFiClient espClient;
PubSubClient client(espClient);

//Declaracao do pino conectado ao sensor
const int PINO_SENSOR = A0;
const int PINO_LED = 27;

//Declaracao da variavel que armazena as leituras do sensor
int leitura_sensor = 0;

//Declaracao da variavel que armazena a recomendação do sistema
int precisaRegar = 0;

//Declaracao da variavel que armazena o código da cultura que será utilizara como parâmetro
int codCultura;
int minimo = 0;
int maximo = 0;

//Declaracao das variaveis que armazenam os valores de calibracao para medição da UMIDADE
const int VALOR_MAXIMO = 4500; //Valor com solo seco
const int VALOR_MINIMO = 1000; //Valor com solo umido

void setup() {
  //Define os pinos coneipconfigictados ao sensor como entradas do sistema
  pinMode(PINO_SENSOR, INPUT);
  pinMode(27, OUTPUT); 
  
  Serial.begin(9600);
  WiFi.begin(ssid, password);

  Serial.print("Conectando à rede Wi-Fi...");
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(".");
  }
  Serial.println("Conectado!");
  
  //Agora, conectando ao SERVIDOR MOSQUITTO
  client.setServer(mqtt_server, 11272);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }

  //Fazendo requisição para descobrir o CÓDIGO DA CULTURA cadastrada como parâmetro
  if (wifiClient.connect("deep-ghosts-swim-201-3-27-224.loca.lt", 80)) {
    Serial.println("Conectado ao servidor");
    wifiClient.print("GET /params/cod HTTP/1.1\r\n");
    wifiClient.print("Host: ");
    wifiClient.print("deep-ghosts-swim-201-3-27-224.loca.lt");
    wifiClient.print("\r\n");
    wifiClient.print("Connection: close\r\n\r\n");
    
    // Espera a resposta
    while (!wifiClient.available());
    
    // Lê o cabeçalho da resposta
    String response = wifiClient.readStringUntil('\r');
    Serial.println(response);
    
    // Extrai o código de status
    int httpCode = response.substring(9,12).toInt();
    Serial.println(httpCode);

    // Lê o corpo da resposta (se houver)
    String payload = wifiClient.readString();

    int ultimaQuebraDeLinha = payload.lastIndexOf('\n');
    String codCulturaString = payload.substring(ultimaQuebraDeLinha + 1);
    codCultura = codCulturaString.toInt();
   
    Serial.println(codCultura);
  } else {
    Serial.println("Falha na conexão ao servidor");
    wifiClient.stop();
  }


  //Realiza a leitura do sensor, a mapeia entre 0 e 100 %
  leitura_sensor = analogRead(PINO_SENSOR);
  leitura_sensor = map(leitura_sensor, VALOR_MINIMO, VALOR_MAXIMO, 0, 100);

  //Como 100 é seco e 0 é totalmente úmido, colocamos 100-leitura_sensor para que 100 seja totalmente úmido e 0 seja seco, para que faça mais sentido o entendimento.
  int umidadePorcentagem = 100 - leitura_sensor;

  Serial.print("Nível da umidade: ");
  Serial.println(umidadePorcentagem);
  Serial.print("Código da cultura: ");  
  Serial.println(codCultura);
  
  
  switch(codCultura){
    //Alface
    case(1):
      minimo = 65;
      maximo = 90;
      break;
    //Tomate  
    case(2):
      minimo = 75;
      maximo = 95;
      break;
    //Cebola
    case(3):  
      minimo = 45;
      maximo = 70;
    break;
    //Pequi
    case(4): 
      minimo = 5;
      maximo = 25; 
    break;
    //Melancia
    case(5):  
      minimo = 65;
      maximo = 90;
      break;
    default:
          digitalWrite(PINO_LED, LOW);
          precisaRegar = 0;
    break;  
  }

  //LIGA O LED CASO SEJA PRECISO REGAR
  if(umidadePorcentagem<minimo || umidadePorcentagem>maximo){
    digitalWrite(PINO_LED, HIGH);
    if(umidadePorcentagem<minimo){
      precisaRegar = 1;
    }
    if(umidadePorcentagem>maximo){
      precisaRegar = 2;
    }
  }else{
    digitalWrite(PINO_LED, LOW);
    precisaRegar = 0;
  }
  
  char umidade[6];
  sprintf(umidade, "%d", umidadePorcentagem);
  
  // Cria um objeto JSON
  DynamicJsonDocument doc(1024);
  doc["precisaRegar"] = precisaRegar;
  doc["umidade"] = umidadePorcentagem;

  // Serializa o objeto JSON em uma string
  String json;
  serializeJson(doc, json);

  // Publica a string JSON no tópico MQTT
  client.publish(topic, json.c_str());
  delay(1000);
}

void reconnect() {
  while (!client.connected()) {
    Serial.println("Conectando ao MQTT...");
    String clientId = "ESP32Client-";
    clientId += String(random(0xffff), HEX);

    if (client.connect(clientId.c_str())) {
      Serial.println("Conectado ao MQTT!");
    } else {
      Serial.print("Falha na conexão ao MQTT, rc=");
      Serial.print(client.state());
      Serial.println(" tentando novamente em 5 segundos...");
      delay(5000);
    }
  }
} 
