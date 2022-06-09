# PIS-Picenator3000
# Opis projekta
Ponuđeno je nekoliko alkoholnih pića. Pritiskom na jedan od njih pokreće se lista pjesama sa najboljom ocjenom za odabrano piće. Postoji admin sučelje pomoću kojeg se može urediti ocjena te dodati nova pjesma putem url-a. Također,korisnik ima opciju davanja ocjene odabranom piću.


#How to start
Databaza ne dolazi sa podatcima. Podatci se nalaze u Pjesme_JSON folderu te se dodaju pomoću add data funkcije u MongoDb Compassu.

1.create docker bridged network

```docker network create veza```

2.run mongodb with docker

```docker pull mongodb```

```docker run --name mongodb -p 27017:27017 --net veza -d mongo ```

3.run flask with docker

```docker build . -f dockerfile.docker -t backend ```

```docker run --name backend_pis -p 5000:5000 --net veza -d backend ```

4.run

```docker build . -f docker.dockerfile -t frontend ```

```docker run --name frontend_pis -p 8080:8080 --net veza -d frontend  ```
