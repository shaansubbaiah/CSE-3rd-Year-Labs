// Shaan Subbaiah B C - 1BM18CS096
// LDR+PIR

void setup()
{
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(2, INPUT);
}

void loop()
{
  int isDark, isMoving;
  
  int analog = analogRead(A0);
  if(analog < 520)
    isDark = 1;
  else
    isDark = 0;
  
  isMoving = digitalRead(2);
  
  if(isMoving && isDark){
    Serial.println((String)"Someone is in the dark.");
    digitalWrite(13, HIGH);
  }
  else{
    Serial.println("...");
    digitalWrite(13, LOW);
  }  
  
  delay(1000);
} 
