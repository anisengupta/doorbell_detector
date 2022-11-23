Project Guide
=============================================
The Doorbell Detector repository contains code that is able to monitor a
doorbell's sounds and report on whether the doorbell has been rung.

The motivation for this project came through the fact when we moved house in
February 2022, we had an outbuilding which I converted into my office during the
spring. I was initially working from home in the dining room which was the first
room in the house after you entered, so naturally you knew when the doorbell had rung.

After a while, I then moved to the outbuilding (after creating a custom desk and
the making sure I got WiFi) which made hearing the doorbell almost impossible.
The only solution I had was to make sure my wife was working from home and would
be able to text if there was somebody at the door. This however did not work when
she worked in the office so I had to find another solution.

Of course, you can get several solutions online that would be able to detect
doorbell sounds and send a notification to your phone but buying it outright was
no fun; I decided to make my own.

Below is a guide on how I was able to achieve this simple project using a
Raspberry Pi.

Setup
-----
The first thing I had to do was to make sure I had the relevant hardware. I knew
that the code itself would not be hard to write, but what might be harder was the
fact that I had to initialise it on some hardware that would be next to the
doorbell itself. This might prove difficult as I only had experience in writing
and testing software but I had never experimented with hardware before.

I therefore turned to the solution of using a Raspberry Pi, a super small computer
that is so simple to use that it is used by children as their first foray into
computers and programming.

Along with a Raspbery Pi, I also needed some sort of sound detector that would
be able to detect a doorbell ring but not be too sensitive and detect footsteps,
or people talking.

I therefore bought the following items for the project:
- Raspberry Pi (https://www.amazon.co.uk/gp/product/B01CD5VC92/ref=ppx_yo_dt_b_asin_title_o02_s01?ie=UTF8&psc=1).
- SD Memory Card - to make sure the Pi would have plenty of memory for Python and other modules needed to work (https://www.amazon.co.uk/gp/product/B073JWXGNT/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1).
- Sound Detection Microphone (https://www.amazon.co.uk/gp/product/B07ZHGDYF7/ref=ppx_yo_dt_b_asin_title_o03_s00?ie=UTF8&psc=1).
- Jumper Cables - to connect the microphone to the Pi (https://www.amazon.co.uk/gp/product/B074P726ZR/ref=ppx_yo_dt_b_asin_title_o03_s01?ie=UTF8&psc=1).


The Process Guide
-----------------
I will now outline below the series of steps I took to get this project finished 
end to end.

Step 1 - Sort out the hardware
******************************
The first step would be to make sure that the sound detector is properly connected
to the Pi.

To achieve this, we needed three female to female jumper cables (brown, black and white).
The sound sensor has four prongs but we only need three of them to correctly connect them
to the Pi:

.. image:: ../images/sound_sensor.png

The prongs we need on the sensor are the power (+), the ground (GND) and the digital out signal (D0):

.. image:: ../images/sound_sensor_magnified.png

When we then connect the sensor to the Pi, we should see both red lights come on (the two leds). To make
sure that our sensor has the correct sensitivity, we need to adjust it so the second led flashes when there
is a loud sound but not to every sound. We need a flat screwdriver to adjust the blue bit on the top
until we achieved our desired sensitivity (turn counterclockwise until the red light dissapears then experimented
accordingly):

.. image:: ../images/sound_sensor_adjust.png

We then need to power up our Pi and make sure that the sound sensor is working accordingly:

.. image:: ../images/raspberry_pi_power.png


Step 2 - Write the code
***********************