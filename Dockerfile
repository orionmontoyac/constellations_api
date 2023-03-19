FROM python

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --default-timeout=100 future

COPY . .
EXPOSE 5000

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]