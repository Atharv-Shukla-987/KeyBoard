# mech_board
## Introduction
It is 60% wireless custum mechanical keyboard with a 0.96 Oled display with a slider[linear potential meter] for music control and some DJ vibes, yes a slider not a rotary encoder because for some reason i just don't like rotary encoders. 
## Components Used
### kerboard
 1.I have used raspberry pi pico w over others because beacause of high number of gpio pins and is easily programable and also is bluetooth and wifi for good contectivity 

 2. i have used TP4050 [charging module] for charging battery

 3. Used mcp1700 [voltage regulator] for converting 3.7v from battery to 5v requried from raspberry pi pico w
 
 4.Used 1N4148 Diode so that ghosting do not occurs 

 5.Used oled display 128x64 i2c for checking battery and making keyboard more intresting

 6. Used SK6812 MINI for lightening and vibe

 7. A female Usb type C for charging 

 8. A 3.7V 2000mah lipo battery for increased battery life 
### reciever  
1.esp32 mini s3 for conecting with keyboard 

2. USb type A 
