#include <SPI.h>
#include <LoRa.h>

String inputString = "";
String Ping = "";
void setup() {
  Serial.begin(9600);
  while (!Serial);

  Serial.println("LoRa Sender");

  if (!LoRa.begin(868E6)) {
    Serial.println("Starting LoRa failed!");
    while (1);
  }
}

void loop() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    //Serial.println(inputString);
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      break;
    }
    
  }
  LoRa.beginPacket();
   if (inputString == ""){
    Ping = "Ping";
    Serial.print("Ty no alefa ra tsisy inputstring: ");
    Serial.println(Ping);
    LoRa.print(Ping);
  }
   else{
      Serial.print("packet: ");
      Serial.println(inputString);
  //    send packet
      LoRa.print( inputString);
  }
  LoRa.endPacket();
  inputString = "";
  delay(5000);
}
