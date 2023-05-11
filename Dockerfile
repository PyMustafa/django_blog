FROM python:3.11

ENV PYTHONUNBUFFERED=1
WORKDIR /code

COPY requirments.txt .

RUN pip install -r requirments.txt
                

COPY . .
EXPOSE 8000

CMD ["python","manage.py","runserver"]