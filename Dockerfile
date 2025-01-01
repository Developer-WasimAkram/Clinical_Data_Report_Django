FROM python:3.12.4
WORKDIR /clinicalsApp
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

CMD [ "python","manage.py","runserver","0.0.0.0:8000" ]




#    Commad for building conatiner  :  docker build -f Dockerfile -t clinicals_app .