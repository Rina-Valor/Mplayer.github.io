import ddf.minim.*;
import ddf.minim.analysis.*;
import ddf.minim.effects.*;
import ddf.minim.signals.*;
import ddf.minim.spi.*;
import ddf.minim.ugens.*;
Minim minim;
AudioPlayer song0, song1, song2, song3, song4, song5, song6, song7;
AudioPlayer soundEffect0, soundEffect1;
//
int time = 7000;
//
Boolean activateWindow=false;
//
void setup() {
  size(300, 300);
  loadMusic();
  //
  //Illsutrate Garbage Collection of Local Variable
  //println("Music Pathway is", musicPathway); //local variable doesn't exit outside of void loadMusic() {}
  //
  
} //End setup
//
void draw() {
  if ( activateWindow == true ) background(0);
}
void keyPressed() {
  soundEffect0.play();
  soundEffect0.rewind();
  delay(4000);
  //
  keyPressedShortCuts();
  quitButtons();
  //
}
//
void mousePressed() {
  if ( activateWindow==false ) activateWindow = true;
}
