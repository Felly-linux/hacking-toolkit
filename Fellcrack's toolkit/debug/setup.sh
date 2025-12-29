sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt autoremove -y && sudo apt clean -y
clear
echo "Installing system..."
sudo apt install metasploit-framework -y
sudo apt install python3 -y && pip3 install -r requierements.txt --break-system-packages