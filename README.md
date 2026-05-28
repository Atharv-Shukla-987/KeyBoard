# mech_board
## Introduction
It is compact wireless custum mechanical keyboard based on rasberry pi pico w with a 0.96 Oled display for displaying battery percentage and with a slider[linear potential meter] for music control and some DJ vibes, yes a slider not a rotary encoder because for some reason i just don't like rotary encoders. It has battery of 2000 mah . It can act as wired and wireless keyboard , both . I have a slider switch for changing the mode . It got two holes on its case wall one for charging port and other for pico port . I have also used RGBs for some asthetics. My pc does not have in built blutooth so , I have also made a reciever dougle.
## Components Used
### kerboard
 1.I have used raspberry pi pico w over others because beacause of high number of gpio pins and is easily programable and also is bluetooth and wifi for good contectivity
 2. A TP4050 [charging module] for charging battery
 
 3. A mcp1700 [voltage regulator] for converting 3.7v from battery to 5v requried from raspberry pi pico w
 
 4.A 1N4148 Diode so that ghosting do not occurs 

 5. A oled display 128x64 i2c for checking battery and making keyboard more intresting

 6. A SK6812 MINI for lightening and vibe

 7. A female Usb type C for charging 

 8. A 3.7V 2000mah lipo battery for increased battery life

 9. keycaps from meckeys

 10. custum pcb
 
 11. 3d printed case
 
 12. cherry x switches
 
 13. Capacitors and registors 

### reciever 

1.esp32 mini s3 for conecting with keyboard 

2. USb type A

3. MCP1700 voltage regulator


# RECIEVER

## schematics

<img width="385" height="510" alt="reciever_schematics" src="https://github.com/user-attachments/assets/21d13f42-d7d7-404f-afff-d35f3a051fff" />

## PCB layout

<img width="506" height="541" alt="image" src="https://github.com/user-attachments/assets/848fa37b-da84-429c-8860-2a590bcb1b1b" />

## 3d

### Front

<img width="282" height="365" alt="image" src="https://github.com/user-attachments/assets/49324e36-aa2d-404a-b36f-76e6eb41ed10" />

### Back

<img width="227" height="358" alt="image" src="https://github.com/user-attachments/assets/d88e9e16-014f-44c4-a02e-54e11611ad61" />


# KEYBOARD

## schematic
<img width="1142" height="580" alt="Screenshot 2026-05-27 211034" src="https://github.com/user-attachments/assets/5da0b96a-b9de-40d6-abfa-094d84a97ed3" />

## PCB layout

<img width="1056" height="551" alt="Screenshot 2026-05-28 190013" src="https://github.com/user-attachments/assets/2e07c5e9-535a-4161-87c1-d54fc9614b9a" />

## 3D 
### front

<img width="822" height="293" alt="Screenshot 2026-05-28 190126" src="https://github.com/user-attachments/assets/8e4fd60a-9dfa-4532-af41-0882207ea927" />
### back Model

<img width="922" height="325" alt="Screenshot 2026-05-28 190143" src="https://github.com/user-attachments/assets/cb98541c-94aa-45bd-9c01-62cb48e53bba" />

## footprints

<img width="701" height="60" alt="image" src="https://github.com/user-attachments/assets/1e4222cf-f1d0-4f15-9c97-514e568e7518" />
<img width="693" height="15" alt="image" src="https://github.com/user-attachments/assets/472a8b6e-5521-4433-8d48-0364bf82e216" />
<img width="694" height="89" alt="image" src="https://github.com/user-attachments/assets/6b40438a-95aa-42ad-a15d-e1bed4682d01" />
<img width="698" height="58" alt="image" src="https://github.com/user-attachments/assets/5b715b23-f193-4054-ba78-b8f92f46a1ad" />
<img width="703" height="40" alt="image" src="https://github.com/user-attachments/assets/36ee1c26-f36a-4477-b8f7-8e7ae8413bea" />



# BOM 

https://docs.google.com/spreadsheets/d/1NN-7fyjT-_NMtKUpMZtBps8UBcZRbg7seoi4lXChdCc/edit?usp=sharing
<img width="1364" height="380" alt="image" src="https://github.com/user-attachments/assets/ecbca997-9428-45c8-a26e-da2b1bcfcc91" />
