# Creating Schematics  

It was the first step and the most important because I need to think what I want to make. I decided to make a 60% keyboard with linear slider for volume and a oled display for showing battery percentage , current mode(wifi/usd) , and current rgb setting  yes you are right it is a wireless keyboard with battery. I can use it in both way wired and wireless . I have used rasberrypi pico w , before it I was using ardiuno nano esp32 but it has not enough gpio pins so I decided to switch. As it runs on battery , for charging the battery I need a type c female port but it has 5v as output so I add MCP1700 voltage regulator and a charging module. I also add diodes to prevent ghosting and added leds for good looks. I have also done the decoupling . But i dont know how the battery percentage is calulated so I asked on slack and do some research about it finding about voltage divider so i used it. It was a long process as I am new to electronics . doing many mistakes and learning new things . But the it was not finished soon I realise my pc does not have in built blutooth so now i need to design a reciever. It was easy compared to previous work , I just use a esp32 mini s3 n4 chip for blutooth and a type A male port with a same MCP1700 voltage regulator.

<img width="870" height="577" alt="image" src="https://github.com/user-attachments/assets/6ad03dde-b578-4850-ab7d-2740e4487cb6" />
<img width="470" height="559" alt="image" src="https://github.com/user-attachments/assets/7c055212-9ce7-40e8-8495-3f06c8cafb73" />
<img width="451" height="484" alt="image" src="https://github.com/user-attachments/assets/4e4d5485-aea1-407c-a11e-edd683199dca" />

  **Total time spent: 5 hours**

# Finding footprint 

I didn't thought it would took me soo long just to find right footprint. The most difficult footprint to find was of my linear slider because almost everyone uses rotary encoders . But I really want to use it . I was able to find only one footprint for it , I am still not satisfied by it but I can't do anything . I tried everywhere. I request to all of you who are reading this , if you find any such footprint please inform me.Other than i have used many wrong footprint which were later changed by me. it was the step where I size my switchs.

<img width="699" height="546" alt="image" src="https://github.com/user-attachments/assets/fb079e85-2a03-4cd0-8532-0d24ea669ebb" />

**Total time spent: 2 hours**

# PCB desiging 

Now , it was the time to create actual pcb . My aim was to make it as compact as possible, so it wont take too much space on my desk and is easy to carry. I placed rasberry pi pico on the right side beneath the pcb so I can fully utilize the area by placing linear slider on top. I did he same with oled display and charging port. I placed the display on top of pcb and charging port beneath the pcb . It was difficult to trace on the right side as there is the brain of my keyboard , pico w . As you can see in the image . There was some part in this area on  which I cannot trace , it is because there was no trace area . If I trace there than it can act as faraday cage blocking the communication signal of pico w . This make it extremely difficult as trace on right bottom cant go directly to right top , they must have to make a long route.

<img width="1073" height="447" alt="Screenshot 2026-05-21 210723" src="https://github.com/user-attachments/assets/1c6f896a-ab87-4d74-a190-719c267536df" />

**Total time spent: 7 hours**

# Making the case 

I made the whole case in two part , top case and bottom case. Bottom case is the main body of the case. Its base is of 5mm and the wall are of 1cm ( first I made it of 5 mm too but while placing the screw , I thought it is good to use 1cm). It has 1cm deep hollow space for components beneath the pcb such as pico w , charging port and the battery . It also has hole for charging port and pico w port in walls. The top case is just a plate on non-switch region with wall of case . Its height is 5mm and the height of plate is 3mm . creating the top case was difficult than the bottom one , it is because ,sometimes the actual size of components is different from the footprint which conffused me. So I leave some margin . After it I offset the edges. Also I placed screw hole so I can assemble it . 

<img width="772" height="428" alt="Case_bottom" src="https://github.com/user-attachments/assets/3f903350-c530-4b4e-b765-9174f4e845a2" />
<img width="884" height="469" alt="Case_top" src="https://github.com/user-attachments/assets/c84ea540-1259-4227-8597-94c5c3b5a3f5" />
<img width="561" height="324" alt="Assembly" src="https://github.com/user-attachments/assets/d5f0b142-7360-4614-878a-52811efb2ddb" />

**Total time spent: 4 hours**

# Changing the PCB layout 

I do that because I have used wrong footprint for led so when I changed it to correct one it show so many errors . It  was because correct has holes and is reverse mount . So almost every led trace came on hole or edge.cut .Not only that , my switch layout was custom so I was unable to find right keycap set and I am not great at all in CAD so I cant design them and buying every keycap separately makes it expensive. Thus  I decided to change switch size , changing the layout to a standard one so I had to retrace almost everything. It was same as making it again.

<img width="1056" height="551" alt="keyboard_pcb_layout" src="https://github.com/user-attachments/assets/50ce8e06-83d1-4bc2-9f6f-a106c717db6e" />

**Total time spent: 6 hours**

# Making the Bom and organising github repository 

making bom was one of easiest yet tiring part of this project , which was mainly due to my part selection , as i tried to reduce the overall cost of the project but whenever i found a cheaper option then its shipping charges were more than its actual value . and the most time consuming part was finding slider in budget as it the slider is not used much making it harder to find in exect size ....    

<img width="1366" height="374" alt="bom" src="https://github.com/user-attachments/assets/45fbd3b5-f124-44e1-ac3a-d79e4870055d" />

**Total time spent: 5.5 hours**

