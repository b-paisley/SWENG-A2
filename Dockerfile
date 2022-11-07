FROM python:3.8-slim-buster

WORKDIR /app

EXPOSE 5000

COPY . .

RUN python3 -m pip install Flask

CMD [ "python3", "-m", "flask", "run", "--host=0.0.0.0"]



