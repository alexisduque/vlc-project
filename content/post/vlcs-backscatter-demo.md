+++
type = "post"
description = ""
tags = [
    "news", "vlcs", "backscatter"
]
categories = [
    "news"
]
title = "VLC Demo: Battery-free Visible Light Sensing"
date = 2017-10-23T03:08:00+02:00
draft = false
+++

During the 4th VLCS workshop that took place on Monday, October 16th during the Mobicom week at Snowbird, Andreas Soleiman and Ambuj Varshney from Uppsala University (Sweden) introduced a new battery-free gesture sensing system.

Their prototype relies on visible light sensing and backscatter technology to achieve accurate hand motion sensing and wireless communication using RFID without any battery.
They take advantage off 2 solar cells, one for powering the small circuit and charging a 2uF capacitance, and the second, much smaller, as a light sensor.
To achieve "passive" wireless transmission, they backscatter FM radio wave using the TI CC1310 RF transceiver and retransmit the reflected radiowave generating a carrier signal at the 868 MHz frequency.

Their system has a power consumption as low as 2uW and can detect 5 different kinds of hand gestures, with a communication range of 70m indoor.

[1] A. Soleiman, A. Varshney, L. Mottola, and T. Voigt, “Demo: Battery-free Visible Light Sensing,” in Proceedings of the 4th ACM Workshop on Visible Light Communication Systems - VLCS’17, 2017, pp. 35–35.

![VLC Sensing Poster](/img/poster-vlcs-backscatter.png)

![VLC Sensing Demo](/img/demo-vlcs-backscatter.png)
