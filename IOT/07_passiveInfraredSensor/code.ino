// Shaan Subbaiah B C - 1BM18CS096
// PIR SENSOR

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(2, INPUT);
}

void loop()
{
  int pirVal = digitalRead(2);
  if(pirVal == HIGH)
    digitalWrite(13, HIGH);
  else
    digitalWrite(13, LOW);
  
  Serial.println((String)"Is something moving: "+pirVal);
  
  delay(1000);
} 
