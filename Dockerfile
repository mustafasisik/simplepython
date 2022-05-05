FROM python:"3.8"

WORKDIR /mytest

COPY requirements.txt .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app ./app
CMD ["python", "./app/main.py"]