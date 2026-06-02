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

<img width="254" height="335" alt="image" src="https://github.com/user-attachments/assets/29fe04f6-e866-44f0-bedb-313aad6702c9" />


## PCB layout

<img width="502" height="538" alt="reciever_pcb" src="https://github.com/user-attachments/assets/cb2673c5-9dc8-4bfb-81f8-1e4ac6c04e3c" />


## 3d

### Front

<img width="282" height="365" alt="image" src="https://github.com/user-attachments/assets/49324e36-aa2d-404a-b36f-76e6eb41ed10" />

### Back

<img width="227" height="358" alt="image" src="https://github.com/user-attachments/assets/d88e9e16-014f-44c4-a02e-54e11611ad61" />


# KEYBOARD

## schematic

<img width="1142" height="580" alt="keyboard_schematics" src="https://github.com/user-attachments/assets/84e76ac3-8324-48ac-90fc-c4fcdd8018f6" />


## PCB layout

<img width="1056" height="551" alt="keyboard_pcb_layout" src="https://github.com/user-attachments/assets/717664c6-0da8-41e4-91b6-49cf0cc06a51" />



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

## Case

### Top case

<img width="884" height="469" alt="Case_top" src="https://github.com/user-attachments/assets/e6e3cc10-ac79-43db-866e-d49388c9cb42" />

### Bottom case

<img width="772" height="428" alt="Case_bottom" src="https://github.com/user-attachments/assets/adab5107-6f58-4f37-95a0-44b557ea4fab" />

### Assembled case

<img width="561" height="324" alt="Assembly" src="https://github.com/user-attachments/assets/b26abd1e-5f79-477a-8d12-5c8d4bca76ba" />

# BOM 

https://docs.google.com/spreadsheets/d/1NN-7fyjT-_NMtKUpMZtBps8UBcZRbg7seoi4lXChdCc/edit?usp=sharing
<img width="1366" height="374" alt="image" src="https://github.com/user-attachments/assets/4b9ccf21-1c37-4efc-a63e-01272a3e3774" />
