FROM python:3.9
RUN apt install python3 -y
RUN pip install mysql-connector-python
RUN pip install anvil-uplink
RUN pip install requests

WORKDIR ./

COPY app.py ./
