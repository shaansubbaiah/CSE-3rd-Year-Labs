// Shaan Subbaiah B C - 1BM18CS096
// TEMP SENSOR

void setup(){
  Serial.begin(9600);
}

void loop()
{
  int analog = analogRead(A0);
  // 31->-40     368->125
  
  float c = map(analog,31,368,-40,125);
  float f = (float)((9/5)*c)+32;
  Serial.println((String)"Analog: "+analog
                +", Temp: "+c+"C = "+f+"F");
  
  delay(1000);
}
