# Semi-Automated Plant Watering System Controlled via WhatsApp

This repository contains the demo code for a semi-automated plant watering system. The system leverages the widespread use of the mobile messaging application, WhatsApp, to provide users with a simple yet effective means of controlling the watering schedule of their plants remotely.

## Main Components

The main components of this system include:

- NodeMCU (esp8266) flashed with [Micropython](https://micropython.org/) as the main processing unit.
- moisture sensor
- DHT22 or DHT11 temperature and humidity sensor to monitor the environmental conditions.
- Water pump to water the plants.
- Relay module to control the water pump.
- Breadboard for easy connection of components.
- Jumper wires for connecting the components.

## Requirements

The following libraries are required to run this system:

1. `json`: This library is used for parsing JSON data.
2. `umqtt.simple`: This is a simple MQTT client for MicroPython. MQTT is a machine-to-machine (M2M)/"Internet of Things" connectivity protocol.

## Getting Started

To get started with this project, you need to flash your NodeMCU with Micropython. Follow the instructions on the [Micropython](https://docs.micropython.org/en/latest/esp8266/tutorial/intro.html) website to do this.

Once you have Micropython running on your NodeMCU, you can clone this repository and install the required libraries 'MIP' (package installer for micropython) is recomended.

create account in both [twillio](https://www.twilio.com/en-us) and [ThingESP server](https://thingesp.siddhesh.me/).

watch youtube videos for a step by step tutorial (might based on arduino but you'll get the idea) 

## Usage

After setting up, you can control the watering schedule of your plants remotely via WhatsApp. Enjoy the convenience of taking care of your plants from anywhere in the world!
