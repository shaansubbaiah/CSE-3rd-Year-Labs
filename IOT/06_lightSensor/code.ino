// Shaan Subbaiah B C - 1BM18CS096
// LDR

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
}

void loop()
{
  int analog = analogRead(A0);
  
  if(analog < 520)
    digitalWrite(13, HIGH);
  else
    digitalWrite(13, LOW);
  
  Serial.println((String)"Sensed light = "+analog);
  
  delay(1000);
} 
