This lab is done collaboratively with Liqin He (lh553) and Xinning Fang (xf49)

# Little Interactions Everywhere

## Prep

1. Pull the new changes from the class interactive-lab-hub. (You should be familiar with this already!)
2. Install [MQTT Explorer](http://mqtt-explorer.com/) on your laptop.
3. Readings before class:
   * [MQTT](#MQTT)
   * [The Presence Table](https://dl.acm.org/doi/10.1145/1935701.1935800) and [video](https://vimeo.com/15932020)


## Overview

The point of this lab is to introduce you to distributed interaction. We have included some Natural Language Processing (NLP) and Generation (NLG) but those are not really the emphasis. Feel free to dig into the examples and play around the code which you can integrate into your projects if wanted. However, we want to emphasize that the grading will focus on your ability to develop interesting uses for messaging across distributed devices. Here are the four sections of the lab activity:

A) [MQTT](#part-a)

B) [Send and Receive on your Pi](#part-b)

C) [Streaming a Sensor](#part-c)

D) [The One True ColorNet](#part-d)

E) [Make It Your Own](#part-)

## Part 1.

### Part A
### MQTT

MQTT is a lightweight messaging portal invented in 1999 for low bandwidth networks. It was later adopted as a defacto standard for a variety of [Internet of Things (IoT)](https://en.wikipedia.org/wiki/Internet_of_things) devices. 

#### The Bits

* **Broker** - The central server node that receives all messages and sends them out to the interested clients. Our broker is hosted on the far lab server (Thanks David!) at `farlab.infosci.cornell.edu/8883`. Imagine that the Broker is the messaging center!
* **Client** - A device that subscribes or publishes information to/on the network.
* **Topic** - The location data gets published to. These are *hierarchical with subtopics*. For example, If you were making a network of IoT smart bulbs this might look like `home/livingroom/sidelamp/light_status` and `home/livingroom/sidelamp/voltage`. With this setup, the info/updates of the sidelamp's `light_status` and `voltage` will be store in the subtopics. Because we use this broker for a variety of projects you have access to read, write and create subtopics of `IDD`. This means `IDD/ilan/is/a/goof` is a valid topic you can send data messages to.
*  **Subscribe** - This is a way of telling the client to pay attention to messages the broker sends out on the topic. You can subscribe to a specific topic or subtopics. You can also unsubscribe. Following the previouse example of home IoT smart bulbs, subscribing to `home/livingroom/sidelamp/#` would give you message updates to both the light_status and the voltage.
* **Publish** - This is a way of sending messages to a topic. Again, with the previouse example, you can set up your IoT smart bulbs to publish info/updates to the topic or subtopic. Also, note that you can publish to topics you do not subscribe to. 


**Important note:** With the broker we set up for the class, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`. Also, setting up a broker is not much work, but for the purposes of this class, you should all use the broker we have set up for you!


#### Useful Tooling

Debugging and visualizing what's happening on your MQTT broker can be helpful. We like [MQTT Explorer](http://mqtt-explorer.com/). You can connect by putting in the settings from the image below.


![input settings](imgs/mqtt_explorer.png?raw=true)


Once connected, you should be able to see all the messages under the IDD topic. , go to the **Publish** tab and try publish something! From the interface you can send and plot messages as well. Remember, you are limited to subtopics of `IDD`. That is, to publish or subcribe, the topics will start with `IDD/`.

![publish settings](imgs/mqtt_explorer_2.png?raw=true)


### Part B
### Send and Receive on your Pi

[sender.py](./sender.py) and and [reader.py](./reader.py) show you the basics of using the mqtt in python. Let's spend a few minutes running these and seeing how messages are transferred and shown up. Before working on your Pi, keep the connection of `farlab.infosci.cornell.edu/8883` with MQTT Explorer running on your laptop.

**Running Examples on Pi**

* Install the packages from `requirements.txt` under a virtual environment, we will continue to use the `circuitpython` environment we setup earlier this semester:
  ```
  pi@ixe00:~ $ source circuitpython/bin/activate
  (circuitpython) pi@ixe00:~ $ cd Interactive-Lab-Hub/Lab\ 6
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ pip install -r requirements.txt
  ```
* Run `sender.py`, fill in a topic name (should start with `IDD/`), then start sending messages. You should be able to see them on MQTT Explorer.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python sender.py
  pi@ReiIDDPi:~/Interactive-Lab-Hub/Lab 6 $ python sender.py
  >> topic: IDD/ReiTesting
  now writing to topic IDD/ReiTesting
  type new-topic to swich topics
  >> message: testtesttest
  ...
  ```
* Run `reader.py`, and you should see any messages being published to `IDD/` subtopics.
  ```
  (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python reader.py
  ...
  ```

**\*\*\*Consider how you might use this messaging system on interactive devices, and draw/write down 5 ideas here.\*\*\***
<img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/remote_control.jpeg" height="450" />

A remote control that helps the user control smart furnitures at his/her home. Button and sensor inputs are sent over the web and transformed into servo movement by a second device.

----------------

<img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/dog_surveillance.jpeg" height="400" />

A dog surveillance system that uses computer vision to identify dogs' behaviors, and send the behavior class to the user who has a second device.

----------------

<img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/wac-a-mole.jpeg" height="400" />

Whac-a-mole game that one user controls the moles while the other smashes them with a hammer. 

----------------

<img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/shooting_game.jpeg" height="400" />

A shooting game where two players each control a aircraft and shoot each other. Location and shooting status will be sent over the web.

----------------

![IMG_0584](https://user-images.githubusercontent.com/39501842/142068728-0043a3ae-07ba-4018-b153-f8fd5ad0be9e.jpg)

A real time voting system that gathers answers from all devices and present the total result. 


### Part C
### Streaming a Sensor

We have included an updated example from [lab 4](https://github.com/FAR-Lab/Interactive-Lab-Hub/tree/Fall2021/Lab%204) that streams the [capacitor sensor](https://learn.adafruit.com/adafruit-mpr121-gator) inputs over MQTT. We will also be running this example under `circuitpython` virtual environment.

Plug in the capacitive sensor board with the Qwiic connector. Use the alligator clips to connect a Twizzler (or any other things you used back in Lab 4) and run the example script:

<p float="left">
<img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
<img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
<img src="https://cdn-learn.adafruit.com/guides/cropped_images/000/003/226/medium640/MPR121_top_angle.jpg?1609282424" height="150"/>
<img src="https://media.discordapp.net/attachments/679721816318803975/823299613812719666/PXL_20210321_205742253.jpg" height="150">
</p>

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python distributed_twizzlers_sender.py
 ...
 ```

**\*\*\*Include a picture of your setup here: what did you see on MQTT Explorer?\*\*\***
<p>
<img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/part-c-twizzler.png" height="300" />
</p>

<img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/MQTT twizzler.PNG" height="500" />

We changed the name of the topic to "nek/twizzler", and when we ran the program, the subtopic was created with a message being sent to the topic indicating which sensor was touched. When we touched another sensor, the message would be overwritten by the latest sensor touched.

**\*\*\*Pick another part in your kit and try to implement the data streaming with it.\*\*\***
<img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/part-c-button.png" height="500" />


We used the button and implemented the data streaming. Everytime when the butotn is pressed, a "button pressed" message will be sent to the subtopic, which is "nek/button".

### Part D
### The One True ColorNet

It is with great fortitude and resilience that we shall worship at the altar of the *OneColor*. Through unity of the collective RGB, we too can find unity in our heart, minds and souls. With the help of machines, we can overthrow the bourgeoisie, get on the same wavelength (this was also a color pun) and establish [Fully Automated Luxury Communism](https://en.wikipedia.org/wiki/Fully_Automated_Luxury_Communism).

The first step on the path to *collective* enlightenment, plug the [APDS-9960 Proximity, Light, RGB, and Gesture Sensor](https://www.adafruit.com/product/3595) into the [MiniPiTFT Display](https://www.adafruit.com/product/4393). You are almost there!

<p float="left">
  <img src="https://cdn-learn.adafruit.com/assets/assets/000/082/842/large1024/adafruit_products_4393_iso_ORIG_2019_10.jpg" height="150" />
  <img src="https://cdn-shop.adafruit.com/970x728/4210-02.jpg" height="150">
  <img src="https://cdn-shop.adafruit.com/970x728/3595-03.jpg" height="150">
</p>


The second step to achieving our great enlightenment is to run `color.py`. We have talked about this sensor back in Lab 2 and Lab 4, this script is similar to what you have done before! Remember to ativate the `circuitpython` virtual environment you have been using during this semester before running the script:

 ```
 (circuitpython) pi@ixe00:~ Interactive-Lab-Hub/Lab 6 $ python color.py
 ...
 ```

By running the script, wou will find the two squares on the display. Half is showing an approximation of the output from the color sensor. The other half is up to the collective. Press the top button to share your color with the class. Your color is now our color, our color is now your color. We are one.

(A message from the previous TA, Ilan: I was not super careful with handling the loop so you may need to press more than once if the timing isn't quite right. Also, I haven't load-tested it so things might just immediately break when everyone pushes the button at once.)

You may ask "but what if I missed class?" Am I not admitted into the collective enlightenment of the *OneColor*?

Of course not! You can go to [https://one-true-colornet.glitch.me/](https://one-true-colornet.glitch.me/) and become one with the ColorNet on the inter-webs. Glitch is a great tool for prototyping sites, interfaces and web-apps that's worth taking some time to get familiar with if you have a chance. Its not super pertinent for the class but good to know either way. 

**\*\*\*Can you set up the script that can read the color anyone else publish and display it on your screen?\*\*\***

The code for this part is in [color_reader.py](https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/color_reader.py). 
As shown in the screenshot on the left below, the color on the right was sent to MQTT, and as shown in the image on the right, the rgb code was read and displayed:

<p float="left">
  <img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/part-d-sender.png" height="250" />
  <img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/part-d-reader.png" height="250">
</p>

<img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/MQTT Color.PNG" height="500" />

### Part E
### Make it your own

Find at least one class (more are okay) partner, and design a distributed application together based on the exercise we asked you to do in this lab.

**\*\*\*1. Explain your design\*\*\*** 

**Whac-a-mole game**

Whac-a-mole is a one player retro arcade game in which the arcade machine decides the position and timing for the mole to surface, while the player needs to hit the surfaced mole with the hammer. Our version is an improvement on the traditional whac-a-mole game, and introducing the second player who replaces the arcade machine and controls the moles. The two players can play competitively with two devices at different locations. 

**\*\*\*2. Diagram the architecture of the system.\*\*\*** Be clear to document where input, output and computation occur, and label all parts and connections. For example, where is the banana, who is the banana player, where does the sound get played, and who is listening to the banana music?

<img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/DeviceDiagram.jpg" height="500" />

Two identical devices are needed for the game. Each device has a touch sensor that gathers inputs from the player. Upon start, users can first select their roles, whether to be the mole or the hammer. During the game, the device adjusts the game stats based on the inputs and renders the game board with pygame through VNC. A string that consists of five integers is sent and received from MQTT, which represents the information about the status of the game. Each digit can be 0-3 which represents a hole, a mole, a hammer hitting a hole, and a hammer hitting a mole respectively. 

A whac-a-mole class is created to turn the numbers into a game screen, display it, and control the inputs to update the game. It is stored in [whac_a_mole.py](whac_a_mole.py). The main algorithm that handles input and communication over MQTT is at [whac_a_mole_host.py](whac_a_mole_host.py). 

Pygame and image library are needed for the game. Run the code below to install them:

    sudo pip3 install pygame
    sudo apt-get install -y libsdl2-image-2.0-0

**\*\*\*3. Build a working prototype of the system.\*\*\*** Do think about the user interface: if someone encountered these bananas somewhere in the wild, would they know how to interact with them? Should they know what to expect?

<img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/DeviceSetup.jpg"/>

<img src="https://github.com/AdamYuzhenZhang/Interactive-Lab-Hub/blob/Fall2021/Lab%206/imgs/WhacAMoleDesign.png"/>

We built two prototypes with two laptops and two raspberry pis. We created a laser-cutted box for the pi so that the user can hold the pi like holding a game controller, and press the cutouts with fingers. The five holes on the box maps to the five mole holes in the game so it is easy for the users to understand the game quickly. 

We also drew the interface with Figma and designed this retro arcade looking layout. And we designed the moles and the hammer to visualize the interactions. 

**\*\*\*4. Document the working prototype in use.\*\*\*** It may be helpful to record a Zoom session where you should the input in one location clearly causing response in another location.

[![whac-a-mole video](https://img.youtube.com/vi/cXkujgNt9Ig/0.jpg)](https://www.youtube.com/watch?v=cXkujgNt9Ig)

<!--**\*\*\*5. BONUS (Wendy didn't approve this so you should probably ignore it)\*\*\*** get the whole class to run your code and make your distributed system BIGGER.-->

