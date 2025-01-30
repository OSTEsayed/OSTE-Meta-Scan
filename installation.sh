#!/bin/bash

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to check if command was successful
check_status() {
if [ $? -eq 0 ]; then
echo -e "${GREEN}[✓] $1 successfully installed${NC}"
else
echo -e "${RED}[✗] Failed to install $1${NC}"
fi
}

# Function to check if running as root
check_root() {
if [ "$EUID" -ne 0 ]; then
echo -e "${RED}Please run as root (use sudo)${NC}"
exit 1
fi
}

# Main installation function
main_install() {
check_root

# Update package lists
echo "Updating package lists..."
apt update

# Install main scanners
echo "Installing main scanning tools..."
apt install -y zaproxy
check_status "ZAP"

apt install -y wapiti
check_status "Wapiti"

apt install -y skipfish
check_status "Skipfish"

apt install -y nikto
check_status "Nikto"

# Install Nuclei
echo "Installing Nuclei..."
apt install -y nuclei
check_status "Nuclei"

# Install Python3 and pip if not present
apt install -y python3 python3-pip
check_status "Python3 and pip"

# Install required Python packages
echo "Installing Python dependencies..."
pip3 install customtkinter python-owasp-zap-v2.4 jinja2 pillow matplotlib beautifulsoup4
check_status "Python packages"

# Optional: Install XAMPP
echo "Do you want to install XAMPP? (y/n)"
read -r install_xampp
if [ "$install_xampp" = "y" ]; then
echo "Installing XAMPP..."
wget https://www.apachefriends.org/xampp-files/8.0.28/xampp-linux-x64-8.0.28-0-installer.run
chmod +x xampp-linux-x64-8.0.28-0-installer.run
./xampp-linux-x64-8.0.28-0-installer.run
check_status "XAMPP"
fi

# Optional: Install NPM
echo "Do you want to install NPM? (y/n)"
read -r install_npm
if [ "$install_npm" = "y" ]; then
echo "Installing NPM..."
apt install -y npm
check_status "NPM"
fi
}

# Run the installation
echo "Starting OSTE-Meta-Scanner dependencies installation..."
main_install
echo -e "${GREEN}Installation complete!${NC}"
