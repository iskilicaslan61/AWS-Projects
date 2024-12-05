#! /bin/bash
dnf update -y
dnf install python3 -y
dnf install python3-pip -y
pip3 install flask
dnf install git -y
FOLDER="https://raw.githubusercontent.com/iskilicaslan61/AWS-Projects/refs/heads/main/Day4_roman-numerals-converter/templates"
cd /home/ec2-user
wget -P templates ${FOLDER}/index.html
wget -P templates ${FOLDER}/result.html
wget https://raw.githubusercontent.com/iskilicaslan61/AWS-Projects/refs/heads/main/Day4_roman-numerals-converter/roman-numerals-converter-app.py
python3 roman-numerals-converter-app.py