#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

void setup() {
  pinMode(8, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  
  lcd.begin(16, 2);
  lcd.print("RGB demo :)");
}

void loop() {
  lcd.setCursor(0, 1);
 
  lcd.print("Red  ");
  digitalWrite(10, HIGH);
  digitalWrite(9, LOW);
  digitalWrite(8, LOW);
  
  delay(500);
  lcd.setCursor(0, 1);
  
  lcd.print("Blue ");
  digitalWrite(10, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(8, LOW);
  
  delay(500);
  lcd.setCursor(0, 1);
  
  lcd.print("Green");
  digitalWrite(10, LOW);
  digitalWrite(9, LOW);
  digitalWrite(8, HIGH);
  
  delay(500);
}
 
