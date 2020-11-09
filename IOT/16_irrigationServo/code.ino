#include <Servo.h>

Servo myServo;
int isOpened = 0;

void setup()
{
  myServo.attach(2);
  Serial.begin(9600);
}

void loop()
{
  int moistureVal = analogRead(A0);
  Serial.println(moistureVal);
  
  if(moistureVal >= 512){
    if(isOpened == 0)
    	myServo.write(90);
    isOpened = 1;
  }
  else{
  	if(isOpened == 1)
      myServo.write(0);
    isOpened = 0;
  }
  
  delay(1000);
}