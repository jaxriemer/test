# Final Project: Interactive Van Gogh

### Group members: Angela Chen(ac2689), Kaiyuan Deng(kd487), Xinning Fang(xf49), Ken He(lh553), Yuzhen Zhang(yz869)

## Overview
Our project is an art-based device that was conceived to be displayed in an art exhibition. This device, the interactive Van Gogh, should be able to interact with users by eyelid, eyeball, and eyebrow movements. Sound would also be played when users make different preset hand gestures. In addition, the position where the user stands would be reflected by a canvas that shows the position of the shadow.

![input settings](Pics/Drawing.jpg?raw=true)
![input settings](Pics/Drawing2.jpg?raw=true)


## Design
As a whole, we used three pi devices and two of those were connected to cameras. One camera was in charge of getting the 
position of the user, whether he was on the left side, at the middle, and on the right in terms of the canvas. Another 
was used to distinguish the hand gesture the user made in order for the interactive Van Gogh to speak to the user. 
Different hand gestures would trigger different conversations and facial expressions of the interactive Van Gogh. 
Below is a flow chart that explains the parts we used in this project, the scripts running on them, and their relation to each other.

![input settings](Pics/Drawing8.jpg?raw=true)


Servo played a critical role in our project. We used a substantial amount of servos in order for the parts to move. Below 
are the original design of how servos were placed on both the canvas and the interactive Van Gogh to help different parts move. 

In the original design of the Canvas, we introduced a sliding mechanism to pull and push multiple "pixels" along a row with one servo, in order to reduce the number of servos in the design. While in the design of the Portrait, we extracted moving components that could be used to express emotions on the face, and designed mechanisms to control them with servos.

![input settings](Pics/Drawing3.jpg?raw=true)
![input settings](Pics/Drawing4.jpg?raw=true)
![input settings](Pics/OriginalDesign.JPG?raw=true)
![input settings](Pics/Drawing6.jpg?raw=true)
![input settings](Pics/Drawing7.jpg?raw=true)

## Implementation
For the implementation, we split the project into two parts, one is for the canvas that reflected the shadows of users, and another one for the interactive Van Gogh. We trained two models using Teachable, one for the position of the user in terms of the canvas and one for the hand gesture the user was making. When the camera detected the position of the user and predicted which position the user was at, the prediction was sent to the corresponding channel via MQTT. The pi in charge of the canvas then read the position from the channel and rotated the servos that slid different shadow components forward and backward. At the meantime, the pi that was used to control the interactive Van Gogh would read the position of the user and moved the eyeballs to make him look at the user. 

![input settings](Pics/Interaction_Portrait.png?raw=true) 
![input settings](Pics/Interaction_Canvas.png?raw=true)


Similarly, the camera that detected the user’s hand gesture would predict which gesture the user made given the trained model and sent the prediction to MQTT. The pi that controlled the interactive Van Gogh then got the prediction and would play the corresponding audio responding to the hand gesture the user made with different facial expressions.

![input settings](Pics/GestureRecognition.png?raw=true)


We spent some time looking for the angles each servo needed to rotate given different conditions, including:
- Open and close of eyelids of the interactive Van Gogh
- Positions of the eyeballs of the interactive Van Gogh
- Positions of the eyebrows of the interactive Van Gogh responding to different hand gestures by users
- Forward and backward movements of shadow components 

One of the biggest challenges we met during the project was the smoothness of the device printed by the 3D printer. In our original design, we reduced the servo amount by creating the sliding mechanism. However, it is extremely hard to make this mechanism reliable and precise. To fix the problem while saving time, we decided to group multiple pixels together and create smaller sliding mechanism for each group. The reduction in scale and complexity made it possible to install and test it within the limited time range. 

In our revised design of the Canvas, as shown in the diagram below, each servo was in charge of four shadow components (blue rectangles in the image). When each servo started to rotate, all four connected shadow components would move together. There were two groups of shadow components for each side(left, middle and right) that would move forward and backward to draw a shadow on the Canvas that indicates the standing position of the user. 

![input settings](Pics/Drawing5.jpg?raw=true)

Below are photos of the mechanisms on the Canvas and the Portrait.

![input settings](Pics/Mechanism_Canvas.png?raw=true) 
![input settings](Pics/Mechanism_Portrait.png?raw=true)

## Video
[![Interactive Van Gogh video](Pics/VideoPic.png?raw=true)](https://youtu.be/EN9Ri0R0MEw)


## Work Distribution
- Model Design: Yuzhen Zhang
- Model Production and Installation: Angela Chen, Kaiyuan Deng, Xinning Fang, Ken He, Yuzhen Zhang
- Painting of the canvas and Van Gogh: Angela Chen, Xinning Fang, Yuzhen Zhang
- Coding and testing: Kaiyuan Deng, Xinning Fang, Ken He
- Video Shooting: Angela Chen, Xinning Fang, Ken He, Yuzhen Zhang
- Video Making: Angela Chen, Yuzhen Zhang


