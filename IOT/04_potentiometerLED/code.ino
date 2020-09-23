void setup()
{ 
  Serial.begin(9600);
  pinMode(9, OUTPUT);
}

void loop(){
  int analog = analogRead(A0);
  int brightness = map(analog,0,1023,0,255);
  
  analogWrite(9,brightness);
  
  Serial.println((String)"Analog: "+analog
                 +" Brightness: "+brightness);
  
  delay(500);
}
