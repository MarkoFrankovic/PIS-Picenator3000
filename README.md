# PIS-Picenator3000
# Opis projekta
Ponuđeno je nekoliko alkoholnih pića. Pritiskom na jedan od njih pokreće se lista pjesama sa najboljom ocjenom za odabrano piće. Postoji admin sučelje pomoću kojeg se može urediti ocjena te dodati nova pjesma putem url-a. Također,korisnik ima opciju davanja ocjene odabranom piću.


#How to start

1.create docker bridged network

```docker network create veza```

2.run mongodb with docker

```docker pull mongodb```
```docker run --name mongodb -p 27017:27017 --net veza -d mongo ```

3.run mongodb with docker

```docker build . -f dockerfile.docker -t backend ```
