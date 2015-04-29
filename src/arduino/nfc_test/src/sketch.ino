// programme de test NFC par simple lecture de l'UID

#include <SPI.h>
#include <PN532_SPI.h>
#include <PN532.h>
#include <NfcAdapter.h>

// utilisation de NDEF 
PN532_SPI pn532spi(SPI, 10);
NfcAdapter nfc = NfcAdapter(pn532spi);

void setup() {
	Serial.begin(9600);
	delay(3000);
	Serial.println("Test NFC !");
	// 
	nfc.begin();
	//
	Serial.println("Attente d'un tag NFC");
}

void loop() {

	if (nfc.tagPresent()) {

		Serial.println();
		Serial.println("BLIP ! ");

	}
 //	} else {

		Serial.print(".");

//	}
	delay(500);

}
