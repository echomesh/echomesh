#include <Arduino.h>
#include <SPI.h>

#define PIN_SCK   18
#define PIN_MISO  19
#define PIN_MOSI  23
#define PIN_SS    5          // LoRa NSS / CS
#define PIN_DIO0  26
#define PIN_VMON  34         // 3V3 rail to ADC

uint8_t regRead(uint8_t addr) {
  digitalWrite(PIN_SS, LOW);
  uint8_t v = SPI.transfer(addr & 0x7F);
  v        = SPI.transfer(0x00);
  digitalWrite(PIN_SS, HIGH);
  return v;
}

void setup() {
  Serial.begin(115200);
  while (!Serial);

  pinMode(PIN_SS, OUTPUT);  digitalWrite(PIN_SS, HIGH);
  SPI.begin(PIN_SCK, PIN_MISO, PIN_MOSI, PIN_SS);

  Serial.println(F("tick | REG42  SS SCK MOSI MISO DIO0  VCC"));
  Serial.println(F("-----+------------------------------------"));
}

void loop() {
  static unsigned long t = 0;

  uint8_t ver = regRead(0x42);      // read LoRa REG_VERSION
  int ss   = digitalRead(PIN_SS);
  int sck  = digitalRead(PIN_SCK);
  int mosi = digitalRead(PIN_MOSI);
  int miso = digitalRead(PIN_MISO);
  int dio0 = digitalRead(PIN_DIO0);
  float vcc = analogRead(PIN_VMON) * 3.3 / 4095.0;

  Serial.printf("%04lu | 0x%02X   %d  %d   %d    %d     %d   %.2f V\r\n",
                ++t, ver, ss, sck, mosi, miso, dio0, vcc);

  delay(1000);   // sample every second
}