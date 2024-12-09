#!/bin/bash

echo "Updating and upgrading the system..."
sudo apt update && sudo apt upgrade -y

echo "Installing dependencies..."
sudo apt install git python3-venv python3-pip -y

echo "Cloning Cowrie repository..."
git clone https://github.com/cowrie/cowrie.git
cd cowrie || exit

echo "Setting up Python virtual environment..."
python3 -m venv cowrie-env
source cowrie-env/bin/activate

echo "Installing Cowrie dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Copying configuration template..."
cp etc/cowrie.cfg.dist etc/cowrie.cfg

echo "Setup complete! Customize your configuration in 'etc/cowrie.cfg' before starting Cowrie."
