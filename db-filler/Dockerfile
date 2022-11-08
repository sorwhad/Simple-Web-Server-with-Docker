FROM python:3.9
WORKDIR /db-filler
COPY filler.py ./db-filler
RUN pip install mysql-connector-python 
CMD ["python", "filler.py"]


