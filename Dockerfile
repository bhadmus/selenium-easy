FROM python:latest
MAINTAINER Ademola Bhadmus
# create a work directory
WORKDIR /root
# copy local files into docker work directory
COPY . .
# install from requirements.txt
RUN pip install -r requirements.txt

# Install dependencies
RUN apt-get update && \
    apt-get install -y unzip xvfb libxi6 libgconf-2-4 && \
    apt-get install sudo

# Install webdriver
RUN sudo wget -N http://chromedriver.storage.googleapis.com/`curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE`/chromedriver_linux64.zip -P ~/ && \
    unzip ~/chromedriver_linux64.zip -d ~/ && \
    rm ~/chromedriver_linux64.zip && \
    sudo mv -f ~/chromedriver /usr/local/bin/chromedriver && \
    sudo chown root:root /usr/local/bin/chromedriver && \
    sudo chmod 0755 /usr/local/bin/chromedriver

# Install Chrome Browser
RUN sudo curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
    sudo echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    sudo apt-get -y update && \
    sudo apt-get -y install google-chrome-stable

# Execute the script
ENTRYPOINT ["behave"]