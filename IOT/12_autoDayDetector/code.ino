// Shaan Subbaiah - 1BM18CS096
// Gas Detection

void setup()
{
  pinMode(13, OUTPUT);
  pinMode(A0, INPUT);
  
  Serial.begin(9600);
}

void loop()
{
  float gasVal = analogRead(A0);
  
  if(gasVal > 200)
    digitalWrite(13, HIGH);
  else
    digitalWrite(13, LOW);
  
  Serial.println((String)"Gas value: "+gasVal);
  delay(1000);
}
