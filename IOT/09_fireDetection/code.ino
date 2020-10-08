// Shaan Subbaiah B C - 1BM18CS096
// FIRE Sensor
void setup()
{
  Serial.begin(9600);
  pinMode(2, OUTPUT);
}

void loop()
{
 int temp_alg = analogRead(A0);
 float c = map(temp_alg,31,368,-40,125);
 
 if(c > 70){
   	Serial.println("Buzzing!");
	digitalWrite(2, HIGH);
    delay(2000);
    digitalWrite(2, LOW);
 }else{
  	Serial.println("Idle");
  }
}