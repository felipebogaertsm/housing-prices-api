FROM python:3.10

WORKDIR /usr/app

COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt

COPY ./ ./

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app:app"]