// Un simple code qui teste la liaison série

void setup()
{
	Serial.begin(9600);
	Serial.println("Hello Cube !");
        pinMode(13,OUTPUT);
}


void loop()
{
	Serial.println("ping");
        digitalWrite(13,HIGH);
	delay(1000);
	Serial.println("pong");
        digitalWrite(13,LOW);
	delay(1000);
}
