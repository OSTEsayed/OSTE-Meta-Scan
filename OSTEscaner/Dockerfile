# Docker image for oste met scanner base on kali linux 
# the current metascan need an xserver running

FROM kalilinux/kali-rolling

RUN apt update -y 
RUN apt install python3-pip python3-tk -y 
RUN apt install zaproxy  wapiti skipfish  nikto nuclei -y

COPY ./ ./scanner/
WORKDIR "/scanner"

RUN pip install -r ./requirements.txt

CMD ["python3", "Metascan.py"]
