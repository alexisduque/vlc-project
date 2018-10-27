---
title: "Alexis defended his thesis"
date: 2018-10-10T11:13:31+01:00
draft: false
tags: [
    "news"
]
categories: [
    "news"
]
---


After 3 year of intensive at **Rtone** and in the **AGORA** of the **CITI Lab**, Alexis has successfully defended his PhD thesis on *"Bidirectional Visible Light Communications for the Internet of Things"* on **Tuesday October 9th**.

You can find an abstract of the thesis and the jury in the following.

### The jury will be composed of:

* **Emmanuel CHAPUT**, Professeur des Universités, INP Toulouse, Rapporteur
* **Anne JULIEN-VERGONJANNE**, Professeur des Universités Univ. Limoges, Rapporteur
* **Josep PARADELLS ASPAS**, Professeur UPC, Rapporteur
* **Luc CHASSAGNE**, Professeur des Universités UVSQ, Examinateur
* **Valeria LOSCRI**, Chargé de Recherche INRIA Lille, Examinateur
* **Hervé RIVANO**, Professeur des Universités INSA Lyon, Directeur de thèse
* **Razvan STANICA**, Maître de Conférences INSA Lyon, co Directeur de thèse

### Abstract

With the exponential growth of the Internet of Things, people now expect every household appliance to be smart and connected. At the same time, smartphones have become ubiquitous in our daily life. Their continuous performance improvement and their compatibility with a broad range of radio protocols as WiFi, Bluetooth Low Energy (BLE) or NFC make them the most convenient way to interact with these smart objects. However, providing wireless connectivity with BLE or NFC means adding an extra chipset and an antenna, increasing the object size and price. Previous works already have demonstrated the possibility of receiving information through visible light using an unmodified smartphone thanks to its camera. Also, LED-to-LED communication for smart devices like toys has been shown previously. However, past efforts in LED to camera communication for IoT device communication have been limited.

In this work, we design LightIoT, a bidirectional visible-light communication (VLC) system between a low-cost, low-power colored LED that is part of an IoT device and an off-the-shelf smartphone. The IoT device is thus able to send and receive information through its LED, while the smartphone uses its camera to receive data and its flashlight to send information. We implement and experimentally evaluate a LED-to-camera VLC system, designed specifically for small LEDs. The proposed solution exploits the rolling shutter effect of unmodified smartphone cameras and an original decoding algorithm, achieving a throughput of nearly 2 kb/s.
Based on the insight gained from an extensive experimental study, we model, for the first time in the literature, the LED-to-camera communication channel. We propose a Markov-modulated Bernoulli process model, which allows us to easily study the performance of different message retransmission strategies. We further exploit this model to implement a simulator for LED-to- Camera communications performance evaluation.

In order to achieve bi-directional communications, we evaluate flashlight-to- LED communications using non-rooted smartphones and small LEDs. With these constraints, our implementation achieves a throughput of 30 bits/second. While limited, this is enough for a feed-back channel coming to support the required redundancy mechanisms. Some of these redundancy mechanisms are based on random linear coding, never tested previously in VLC.
Therefore, we design and implement, for the first time in the literature, a pseudo random linear coding scheme especially fitted for line-of-sight LED-to-camera conditions. Experimental evaluation highlights that this type of approach increases the goodput up to twice compared to classical retransmission strategies.

Finally, we compare the energy consumption of LightIoT with the one of a BLE module with similar activity. Our results show that using the LED for communication purposes reduces the energy consumption under a normal usage behavior.
