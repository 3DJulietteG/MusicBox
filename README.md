# MusicBox
Custom node created to rig a Music box. Given a bounding box and different locators, it will out the positions of the locators in the bounding box.

Project presentation :

![image](https://github.com/3DJulietteG/MusicBox/assets/111455565/01521574-4079-4883-a2ab-dea42acfba83)

The purpose of the script is to determine which locators are in the collide area and to out their position to other locators (here contact locators).


How does it work:

Given a mesh bounding box min and max and different locators positions it will compare the value and select all the locators existing in the bounding box.
If there are multiple locators in the bounding box it will compare the translateY and take only the top one.
If there are no locators in the bounding box it will out the rest pose position.

After :

Using Bifrost :

  -Create a proxy using the rest pose position. 
  
  -Check if there is a collision between the proxy and the partition.
  
  -Get the rest pose position and the contact locators positions (given by the custom node)
  
  -Find the closest position on a given "path mesh" to the contact locators.
  
  -If there is a collision, loc Move = closest position on "path"
  
    If not loc Move = rest pose

