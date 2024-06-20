FROM python:3.12-bookworm 

WORKDIR /mgc_test
COPY . /mgc_test

 # Create virtual environment
RUN apt update && apt install -y python3-venv
RUN python3 -m venv .venv
RUN . .venv/bin/activate

# Install required packages on virtual environment
RUN pip install -r requirements.txt

# Install Chrome and Firefox
RUN apt-get update && apt-get install firefox-esr -y
RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
