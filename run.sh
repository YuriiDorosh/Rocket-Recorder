#!/bin/bash


# Move to the project folder
cd Rocket-Recorder

if [ $? -ne 0 ]; then
  echo "Error: Failed to enter to project folder."
  exit 1
fi

# Make virtual environment
python3 -m venv env

if [ $? -ne 0 ]; then
  echo "Error: Failed to create virtual environment."
  exit 1
fi

# Activation of the virtual environment
source env/bin/activate

if [ $? -ne 0 ]; then
  echo "Error: Failed to activate the virtual environment."
  exit 1
fi

# Installing dependencies from requirements.txt
pip install -r requirements.txt

if [ $? -ne 0 ]; then
  echo "Error: Unable to set dependency."
  exit 1
fi


# Start the project
cd ..
python3 Rocket-Recorder

# Exit the script
exit 0
