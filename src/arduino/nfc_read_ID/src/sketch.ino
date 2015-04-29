// programme de lecture d'ID NFC

#include <SPI.h>
#include <PN532_SPI.h>
#include <PN532.h>
#include <NfcAdapter.h>

// utilisation de NDEF 
PN532_SPI pn532spi(SPI, 10);
NfcAdapter nfc = NfcAdapter(pn532spi);

void setup() {

	Serial.begin(9600);

	nfc.begin();
}

void loop() {

	if (nfc.tagPresent()) {

		NfcTag tag = nfc.read();
		//tag.print();
		Serial.print("{\"ID\":\"");
		Serial.print(tag.getUidString());
		Serial.print("\"}");
		Serial.println();
		delay(400);
	}
}
