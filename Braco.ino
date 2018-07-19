#include <Servo.h>
Servo ser,ser1,ser2;
int incoming[2];

void setup(){
    pinMode(10,OUTPUT);
     pinMode(11,OUTPUT);
      pinMode(9,OUTPUT);
   ser.attach(11);//manda energia para a porta 11
    ser1.attach(10);
    ser2.attach(9);
   
  Serial.begin(9600);

  
}

void loop(){
  while(Serial.available() >= 3){
    
    
    
    for (int i = 0; i < 3; i++){
       
      incoming[i] = Serial.read();
    }
   
  ser.write(incoming[0]);
  ser1.write(incoming[1]);
  ser2.write(incoming[2]);
  
   //analogWrite(10,incoming[1]);
  // analogWrite(11,incoming[0]);
   
  
}
}
