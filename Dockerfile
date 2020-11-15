FROM centos/python-36-centos7

USER root
RUN python -m pip install --upgrade pip

# install node js
RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash -
RUN yum install nodejs -y
RUN node --version

WORKDIR yotube-list-downloader

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY package.json .
COPY package-lock.json .
RUN npm install
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm
RUN yum install ./google-chrome-stable_current_*.rpm -y
COPY . .

CMD [ "python", "youtube-video-converter.py" ]