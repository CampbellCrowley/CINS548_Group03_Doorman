# Doorman
CINS 548 - Group 3

The goal of this project is to couple facial recognition with an additional TOTP entry for unlocking a computer.  

A RaspberryPi will be used to validate and process the login flow.

Using a webcam connected to the RPi, we will first wait until a known face is
recognized to identify the user and account to eventually unlock. Once a user
has been identified, we will then prompt for a TOTP code to be entered from an
authenticator app like Authy or Google Authenticator to additionally verify the
user's intent to unlock their device. If a code fails to be entered within
30 seconds of the user being recognized, the computer will return to a fully
locked state and the login flow must begin again.

The login code although entered through the device attempting to be unlocked,
will be sent to the RPi and verified by the RPi. All processing and verification
takes place on the RPi. The device to unlock has a companion app that only
accepts 2 commands from the RPi: to lock or unlock the device.

## Installation

`./RaspberryPi/`: Contains everything related to the RPi for this project.  
`./Windows/`: Contains Windows side of this project (The unlockable device).

Each is a separate project that can be installed by running `make init` in the respective directory, or `pip install -r requirements.txt`.

Running each can be done with `make run`, or `python3 doorman.py`.

## Authors
This project was created for CINS-548 a CSU Chico Fall 2020.
- Campbell Crowley
  - Project structure and organization,
  - Webserver and networking,
  - TOTP generation and verification,
  - RPi <--> Windows communication API,
  - Code cleanup and unification,
  - Comments and Documentation.
- Kyle Crowley
  - Face recognition.
- Zelin Hu
  - Windows locking/unlocking.
