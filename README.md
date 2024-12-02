﻿# RenshuuAPI

This repository ultimately aims to serve as a GUI displaying Renshuu user stats upon booting up a windows device. This includes showing the number of terms a user has to review on a given day, and how many terms the user completed reviewing. I also plan on implementing JLPT progress graphs that displays what percentage of each category (vocab, kanji, sentences, and grammar) have been studied for each level.

This project is currently a work in progress. Functionality to load upon boot-up is not yet implemented, the reload button on the GUI is still in development, and some minor features are not yet created.

## To Run

Clone this repository. Make sure Python is installed on your device. Create a renshuu account at https://www.renshuu.org/. Navigate to resources/tools/renshuuAPI. Copy and paste the read/write API key. Create a new file titled api_key.py in the current directory. Inside api_key.py, type api_key = "your copied api key". Save the file and run the command Python frame.py. Entering the API key through the settings tab of the GUI will be implemented in a future version.
