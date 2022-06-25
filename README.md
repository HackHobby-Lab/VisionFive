# VisionFive
Download this file and 
Open Terminal in folder where you have downoaded this file.
Run this script by giving root previliges 'sudo'.
If not then the following error will appear.

![Screenshot_2022-06-22_04-42-27](https://user-images.githubusercontent.com/70629275/174900624-0ed47b6a-03a5-4f97-bf84-fa84cb3b3af5.png)

Once you use sudo and run the script the following messages displaying 'done' after each second will appear.

![Screenshot_2022-06-22_04-44-56](https://user-images.githubusercontent.com/70629275/174900789-cee59b6d-9bd0-455d-bd12-6775e57b2319.png)

Connect Led's Positive side to VisionFive Pin number 40 and Negative to the Pin Number 39.
If you are going to use Blue led like mine then there is no need to attach extra resistor but if you are using any other led the please use appropriate resistor.
Normal values like 220ohm 330 ohm can be used. But it can very according to your led.




https://user-images.githubusercontent.com/70629275/174902821-ca7bc81c-ccdd-4776-91f8-2ed8bce07e0d.mp4

# My recommendation is to start from here with these libraries

## Installing_New_Libraries

First, install Gpiod library using the following command:

`$ sudo pip install gpiod`

Or you can try:

`$ sudo dnf install gpiod`

Then you need to install libgpiod library. Here this thing takes us on two ways path. We have to take both of them :)

Firstly after gpiod is installed, we need to install the python3-libgpiod library. This was designed for python to access and manage gpios. So let's install it by using the following command.

`$ sudo dnf install python3-libgpiod`

After it is installed now we need to do the following commands "gpioinfo" , "gpiodetect" to get info about our gpio but for that, we need to install another library. So install it by:

`$ sudo dnf install libgpiod-utils`

Now after this we can check it by the following command:

`$ sudo gpiodetect`

This command should show you the output with different gpiochips available on the board. More about that was already discussed.

Note: _In my case, I have to install everything in this sequence otherwise it was giving me an error. I don't know why the hell but it was. So I had to uninstall all the libraries first and then install them in this sequence, or at least the solution that I figured out._

## And now you can blink the led and do everything with gpios


## For More Information & contact

https://www.instagram.com/hackhobby_lab/

https://www.instructables.com/Interfacing-Push-Button-With-VisionFive/

https://rvspace.org/

https://forum.rvspace.org/

https://youtu.be/W10YKBu7tG8

https://www.hackster.io/hamzah2/interfacing-push-button-with-visionfive-6b8c65
