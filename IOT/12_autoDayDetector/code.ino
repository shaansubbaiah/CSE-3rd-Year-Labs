// Shaan Subbaiah - 1BM18CS096
// Vibration on daylight

void setup()
{
  pinMode(6, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  int lightVal = analogRead(A0);
  
  Serial.println(lightVal);
  if(lightVal >= 200)
  	analogWrite(6, 255);
  else
    analogWrite(6, 0);
  
  delay(300);
}
