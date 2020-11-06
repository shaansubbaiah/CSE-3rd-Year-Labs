#include <Servo.h>
#include <IRremote.h>

// setup servo pin, initializae pos
int pos = 0;
Servo servo_9;

// setup ir reciever
int ir_in = 7;
IRrecv irrecv(ir_in);
decode_results results;

void setup()
{
  Serial.begin(9600);
  
  servo_9.attach(9);
  Serial.println("Enabled Servo");
  irrecv.enableIRIn();
  Serial.println("Enabled IRin");
}

void loop()
{
  if (irrecv.decode(&results)) {
    switch (results.value){
      case 0xFD609F:
		servo_9.write(360);
		Serial.println("Clockwise");
        break;
      case 0xFD20DF:
		servo_9.write(-360);
		Serial.println("Counter Clockwise");
        break; 
      default:
        Serial.print("Use only << or >>");
        break;        
    }    
    irrecv.resume(); 
  }
}
