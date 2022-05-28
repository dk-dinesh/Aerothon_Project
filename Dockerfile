FROM ubuntu:20.04
ENV DEBIAN_FRONTEND noninteractive
WORKDIR /myproject
COPY /requirements.txt .
RUN apt-get update -y && apt-get upgrade -y && apt-get install python3 -y && apt-get install python3-pip -y \
&& apt install curl -y && apt install npm -y && curl -sL https://deb.nodesource.com/setup_16.x -o /tmp/nodesource_setup.sh \
&& apt install nodejs -y && npm -g install create-react-app -y
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
