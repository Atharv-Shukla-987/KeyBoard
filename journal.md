# TIME : 5hr

It was the first step and the most important because I need to think what I want to make. I decided to make a 60% keyboard with linear slider for volume and a oled display for showing battery percentage , yes you are right it is a wireless keyboard with battery. I can use it in both way wired and wireless . I have used rasberrypi pico w , before it I was using ardiuno nano esp32 but it has not enough gpio pins so I decided to switch. As it runs on battery , for charging the battery I need a type c female port but it has 5v as output so I add MCP1700 voltage regulator and a charging module. I also add diodes to prevent ghosting and added leds for good looks. I have also done the decoupling . But i dont know how the battery percentage is calulated so I asked on slack and do some research about it finding about voltage divider so i used it. It was a long process as I am new to electronics . doing many mistakes and learning new things . But the it was not finished soon I realise my pc does not have in built blutooth so now i need to design a reciever. It was easy compared to previous work , I just use a esp32 mini s3 n4 chip for blutooth and a type A male port with a same MCP1700 voltage regulator.

<img width="870" height="577" alt="image" src="https://github.com/user-attachments/assets/6ad03dde-b578-4850-ab7d-2740e4487cb6" />
<img width="470" height="559" alt="image" src="https://github.com/user-attachments/assets/7c055212-9ce7-40e8-8495-3f06c8cafb73" />
<img width="451" height="484" alt="image" src="https://github.com/user-attachments/assets/4e4d5485-aea1-407c-a11e-edd683199dca" />


# TIME : 2hr

I didn't thought it would took me soo long just to find right footprint. The most difficult footprint to find was of my linear slider because almost everyone uses rotary encoders . But I really want to use it . I was able to find only one footprint for it , I am still not satisfied by it but I can't do anything . I tried everywhere. I request to all of you who are reading this , if you find any such footprint please inform me.Other than i have used many wrong footprint which were later changed by me. it was the step where I size my switchs.

<img width="699" height="546" alt="image" src="https://github.com/user-attachments/assets/fb079e85-2a03-4cd0-8532-0d24ea669ebb" />
