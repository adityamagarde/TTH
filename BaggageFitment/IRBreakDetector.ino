#define IRsensor 9    //Active IR Sensor
#define opto 2        //Optocoupler

//Variables
int  detectorState;  /* Holds the last state of the switch */
int trigger = 4;

void setup()
{
  detectorState = 0;                 
  pinMode (IRsensor, INPUT);
  pinMode (opto, OUTPUT);
   
  Serial.begin(9600);

  Serial.println("Beginning to detect");
  delay(5000);
  Serial.println ("Ready ");
  
}

void  loop ()
{
  detector_state = digitalRead (IRsensor);
  if(HIGH == detector_state) 
  {
    digitalWrite(opto, LOW );
  } 
  else 
  {
    for (int x = 0; x < 4; x++) {
    digitalWrite (opto, HIGH );
    delay (200);
    digitalWrite (opto, LOW);
    delay (1000);
    Serial.println("Motion Detected");
    }
  }
  delay (100);
}