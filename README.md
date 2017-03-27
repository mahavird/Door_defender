# Door_defender

Ever wondered who was standing on the front porch, ringing the doorbell? Maybe it was the neighbor or the mailman. Maybe it was someone unfamiliar. Door  Defender— the affordable, smart doorbell and camera — is perfect for those moments.
There’s a new system that allows you to screen your visitors just like you screen your calls, keep your home safely monitored while you’re out, and even receive updates when your family members return home safely. Its name is Door Defender.
It is the smartest, most cost effective solution to monitoring your doorstep and the rest of your home. It’s a totally wireless monitoring solution that can be installed anywhere. 
Door Defender even allows guests to leave a voice message. Vibration Sensors can be spread throughout the windows of your house, so that intruders will be caught and you will be notified if one is opened.
Door Defender is the universal home-security system that connects to your smart phone to make protecting your home or office easier than ever. Imagine having the convenience of a butler, organization of a secretary, and protection of a security guard rolled into one, easy-to-install monitoring system. That’s what Door Defender offers. 
It consists of one Door Defender that acts as a camera, doorbell, and alarm system. It can be used individually, inside or outside, or with Vibration and Motion sensors. Each Door Defender device sends alerts to your smart phone within seconds of recognition, whether that be photos, or voice messages.

Why do you need Door Defender ?
> Who is at my door? Do I need to answer him?
> Did my kids get home safely from school?
> Is a stranger approaching back of my house or tampering with windows?
> Did delivery man drop off my package?
> Did the mail come yet?
> Is my child safe while home alone?
> Did someone actually let the dog out?

Key Components Used In Device:
1.Beagle bone Black
2.USB Camera(720p)
3.Vibration Sensors
4.PIR sensor
5.Power Bank
6.CC3200

This is how Door Defender works:
Door Defender uses Beagle-Bone Black as the server that receives signals from the sensors/modules attached to CC3200(clients) via wifi . BBB then sends the intrusion message to the home owner on his mobile ( Watsapp ). 

Door Defender attaches to any surface and offers around-the-clock surveillance as well as alerts and chimes when suspicious activity occurs. It’s a totally wireless monitoring solution that can be used inside and outside.
Door Defender has been divided into two modules  :

1.BeagleBone Black(Front Door):
When a visitor approaches the Door Defender unit, the PIR sensor detects that motion and switches on the device which snaps a picture of the scene and sends this snapshot straight to the home owner's smart phone.
It also switches on the microphone attached to it ,so that if the visitor  wants to leave a message he/she can record it and it would sent be home owner's smart phone. 


2.CC3200 (Windows)
The vibration sensors are placed on the windows of the house , Hence if in any case someone is intruding through window, the vibration sensor would get activated,which would send a signal to main Beagle-Bone via WiFi integrated on the CC3200.
After receiving a signal from CC3200 module,the Beagle-Bone would send an alert message home owner's smart phone.

![alt tag](https://github.com/mahavird/Door_defender/blob/master/Block_diagram.png)

Power Efficient:  
The motion sensor allows the camera to turn itself on and off at appropriate times. When the motion sensor detects movement, it will activate the camera’s functions immediately, and also alert your phone.

Future enhancement :
Door Defender can be further improved by adding additional feature wherein the owner has an option to reply/message to the person at the door.



