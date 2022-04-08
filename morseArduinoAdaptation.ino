// These are the basic setup variables, you can change them to match whatever your desired setup is.
// Includes support for output via serial console, LED, and piezo speaker

const int led = 13; // The output LED pin
const int piezo = 8; // The output piezo speaker pin
const bool unitsInWPM = false; // Set to true if you want to specify units in words per minute
int unit = 132; // Length of a 'unit' of time, in milliseconds or WPM. 0.132 seconds is apparently the FCC standard 'unit' rate.
const char message[] = "hello professor holley this is my morse code app"; //Message should be all lower case and with no punctuation

// Set the frequency of the dit and dah tones (in Hz) - if you'd like to be able to use auto-decoder software, these should be the same. Otherwise, varying pitches can help with tone identification
const int ditTone = 440; 
const int dahTone = 530;


void dit() {
  Serial.print("dit");
  digitalWrite(led,HIGH);
  tone(piezo,ditTone,unit);
  delay(unit);
  digitalWrite(led,LOW);
  delay(unit);
}

void dah(){
  Serial.print("dah");
  digitalWrite(led,HIGH);
  tone(piezo,dahTone,unit*3);
  delay(unit*3);
  digitalWrite(led,LOW);
  delay(unit);
}

// Dit and dah functions include 1 unit delay, so delays between characters and words are shortened by 1 unit
void cSpace(){
  Serial.print(" ");
  delay(unit*2);
}

void wSpace(){
  Serial.print("\n");
  delay(unit * 6);
}

// Loops through the message by character, outputting the appropriate combination of dits and dahs
void writeMsg() {
  for(int i = 0;i<strlen(message);i++) {
    char c = message[i];
    if(c == ' ') {
      wSpace();
      continue;
    } else {
      switch(c) { //Not as pretty but what can you do, C doesn't have dicts or hashtables and I don't want to waste memory with a struct.
        case ' ':wSpace();break;
        case 'a':dit();dah();break;
        case 'b':dah();dit();dit();dit();break;
        case 'c':dah();dit();dah();dit();break;
        case 'd':dah();dit();dit();break;
        case 'e':dit();break;
        case 'f':dit();dit();dah();dit();break;
        case 'g':dah();dah();dit();break;
        case 'h':dit();dit();dit();dit();break;
        case 'i':dit();dit();break;
        case 'j':dit();dah();dah();dah();break;
        case 'k':dah();dit();dah();break;
        case 'l':dit();dah();dit();dit();break;
        case 'm':dah();dah();break;
        case 'n':dah();dit();break;
        case 'o':dah();dah();dah();break;
        case 'p':dit();dah();dah();dit();break;
        case 'q':dah();dah();dit();dah();break;
        case 'r':dit();dah();dit();break;
        case 's':dit();dit();dit();break;
        case 't':dah();break;
        case 'u':dit();dit();dah();break;
        case 'v':dit();dit();dit();dah();break;
        case 'w':dit();dit();dah();break;
        case 'x':dah();dit();dit();dah();break;
        case 'y':dah();dit();dah();dah();break;
        case 'z':dah();dah();dit();dit();break;
        default:
          Serial.print("invalid character"); // This only shows up if you ignore the instructions above and feed it something other than a lower case letter or space
          break;
      }
      cSpace();
    }
  }
}

void setup() {
  pinMode(led, OUTPUT);
  if(unitsInWPM) {
    unit = ((60/unit)/5) * 1000; // Per FCC standard, assumes an average of 5 letters per word
  }
}

void loop() {
  writeMsg();
  delay(3000); // End of message delay
}
