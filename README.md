
# OSTE-Meta-Scanner
![Project Logo](OSTEscaner/images/meta.png)
This project aims to simplify the field of Dynamic Application Security Testing. The OSTE meta scanner is a comprehensive web vulnerability scanner that combines multiple DAST scanners, including Nikto Scanner, OWASP ZAP, Nuclei, SkipFish, and Wapiti.


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [ScreenShots](#ScreenShots)

## Introduction
This software offers a user-friendly graphical interface which presents a comprehensive report for each scan, making the scanning process effortless and straightforward.

The main focus of this scanner is on web injection vulnerabilities such as SQL injection, XSS injection, OS command injection, XML injection, and many more. Additionally, it provides a list of vulnerabilities supported by each scanner, apart from injection vulnerabilities.

We offer two types of reports. The first is a consolidated report in JSON format, which includes important reports from each scanner. It contains details such as the vulnerability, the corresponding URL, the parameter used, the Curl command, the attack vector, a description of the vulnerability, and more.

The second report is an HTML file format that specifically highlights successful injection attacks. Our results and decisions are based on a novel learning algorithm proposed during the ("A Meta-Scan based approach for the detection of injection vulnerabilities in Web applications.", -University May 8, 1945 -Guelma -, Computer Science Department, Presented by: SEYYID TAQY EDINE OUDJANI, Supervised by: DR. ABDELHAKIM HANNOUSSE. 2023). 

## Features

List of Main Vulnerabilities supported:
1. Injection
  - SQL injection
  - Cross site scripting
  - OS command injection
  - XML injection
  - XSLT injection
  - XML External entites
  - code  injection
  - host header injection
  - html injection
  - Template injection (server-side)
  - CRLF injection
  - OGNL injection 
2. Other vulnerabilities (refer to the repository of each scanner for a complete list.)
  - Skipfish Vulnerabilities support List.
  - Wapiti Vulnerabilities support List.
  - OWASP ZAP Active Attack list.
  - Nikto Vulnerabilities support List (Specified: Tunning 9 & 4).
  - Nuclei CVE-Template.
## Installation

The installation process requires a specific set of requirements. While this project is primarily supported on Kali Linux, it can also be compatible with other operating systems:

1. OWASP zaproxy:
  - kaliLinux: [ sudo apt install zaproxy ]  
  - Other OSs: [ https://github.com/zaproxy/zaproxy ]
  
2. Wapiti:
  - kaliLinux: [ sudo apt install wapiti ]  
  - Other OSs: [ https://wapiti-scanner.github.io/ ]  
  
3. Skipfish:
  - kaliLinux: [ sudo apt install skipfish ]  
  - Other OSs: [ https://gitlab.com/kalilinux/packages/skipfish ]  
    
4. Nikto :
  - kaliLinux: [ sudo apt install nikto ]  
  - Other OSs: [ https://github.com/sullo/nikto ]  

5. Nuclei:
  - kaliLinux: [ sudo apt install nuclei ]  
  - Other OSs: [ https://github.com/projectdiscovery/nuclei ]  

6. Python 3 * Libraries:
  - customtkinter 
  - zapv2
  - jinja2
  - webbrowser
  - PIL
  - matplotlib
  - BeautifulSoup
  - pprint

7. optional requirments for more features:
  - XAMP server   
  - NPM  

(Note: Please note that I will be creating a bash script to automate the installation steps for Linux users as soon as possible.)
  
## Usage

After cloning the repository to your local machine, you can initiate the application by executing the command python3 Metascan.py. 

Then, you can navigate through the interface of the application.

## Contributing

We welcome contributions to enhance and improve this project. To contribute, please follow these guidelines:

   1. Fork the repository and create a new branch for your contribution.
   2. Ensure that your code adheres to the project's coding standards.
   3. Make your changes, addressing the specific issue or adding the proposed enhancement.
   4. Test your changes thoroughly.
   5. Commit your changes and provide a clear and descriptive commit message.
   6. Push your changes to your forked repository.
   7. Submit a pull request, detailing the changes you've made and providing any relevant information or context.

Please note that all contributions will be reviewed by the project maintainers. We appreciate your effort and will do our best to provide timely feedback.

If you have any questions or need further clarification, feel free to reach out to us through the issue tracker or by contacting the project maintainers directly.

## License

This project is under  GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007.

This project is intended for educational purposes and aims to simplify the overall assessment of cybersecurity. However, we want to emphasize that we are not liable for any malicious use of this application. It is crucial that users of this software exercise responsibility and ethical behavior. We strongly recommend notifying the targets or individuals involved before utilizing this software.

## ScreenShots 
![Main Interface ](ScreenShots/Screenshot_2023-05-31_15-09-04.png)

## Contact

-  How to reach me email: oudjani.sayed.taki.eddine@gmail.com , sayedesg@gmail.com ;
   linkdin:(https://www.linkedin.com/in/oudjani-seyyid-taqy-eddine-b964a5228)

