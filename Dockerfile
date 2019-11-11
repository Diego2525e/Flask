FROM python:3
ADD app.py /
RUN pip3 install flask && pip3 install flask_restplus
CMD [ "python3", "./app.py" ]
EXPOSE 5000
