# TP Docker & Flask :

## Comprendre la différence entre images et containers

Un conteneur Docker est une instance exécutable d’une image. 

## A quoi sert un ```Dockerfile```

Les Dockerfiles sont des fichiers qui permettent de construire une image Docker adaptée à nos besoins, étape par étape. Il permet de faire un fichier de configuration d'une image personnalisé.

## CheatSheet 

* **docker ```build```**: Permet de construire une image depuis un Dockerfile et un "context".

* **docker ```run```**: Permet de crée une couche de conteneur inscriptible sur l'image specifiée, puis la démarre.

* **docker ```exec```**: Permet de lancer une commande dans un conteneur en cours d'éxécution.

* **Port dans un container** : Lorsque que je vais lancer un serveur web comme nginx par exemple, il va rendre les pages web sur le port 80, mais seulement à l’intérieur du conteneur. Je n’y aurais pas accès car c’est totalement isolé, le conteneur a son propre réseau. Afin de pouvoir accéder aux pages web, je vais utiliser l’option -p qui va me permettre de spécifier le port de ma machine et lui dire vers quel port du conteneur je veux faire la liaison. De cette façon, je vais pouvoir accéder aux pages web via mon navigateur.

## Commandes éxécutés 

### Lancement du container getting-started

``` bash
docker run -d -p 80:80 docker/getting-started
```

Télécharge et lance le container tutorial de Docker

### Lancement du container *Hello World* 

``` bash
docker run hello-world
```

Télécharge et lance le container Hello World.

### Lancement du container ubuntu bash

``` bash
docker run -it ubuntu bash
```

Télécharge et lance le container de l'image ubuntu en bash. Après le lancement de la commande, une interface de commande ubuntu se lance.

### Liste des containers docker installés

``` bash
docker ps -a
```

La commande ```docker ps -a``` affiche la liste des containers dans docker.

Ici on a :
* docker/getting-started
* hello-world
* ubuntu


### Liste des containers docker en cours d'éxécutions

``` bash
docker ps 
```
La commande ```docker ps``` affiche la liste des containers éxécutés.

Ici on a : 
* docker/getting-started
* ubuntu

### Lance un container applicatif en python avec docker

``` bash
docker run -it --name python bitnami/python
```

Télécharge et lance un container python présent sur le hub docker.

Après téléchargement et installation, une interface de commande python s'éxécute.

### Création du Dockerfile

``` dockerfile
# Use the official image as a parent image.
FROM ubuntu:20.04
#FROM python:3.8

# Set the working directory.
WORKDIR /usr/src/app

# Install on ubuntu python3.7, python3-pip, and Vim
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3.7 \
    python3-pip \
    vim \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements.txt in filesystem working directory
COPY requirements.txt .

# Install with pip3 all python lib from requirements
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt

# copy all files from current directory to filesystem working directory.
COPY . .

# Add metadata to the image to describe which port the container is listening on at runtime.
EXPOSE 80

# Run the specified command within the container.
# Here is launch of app.py with python 3
CMD ["python3","app.py"]
```

### Création d'une image à partir du Dockerfile

On se place dans le dossier applicatif avec le DockerFile présent à l'intérieur.

``` bash
docker build --tag docker-python-flask .
```

Ici le nom de l'image sera ```docker-python-flask``` 

### Vérification de la création de l'image

``` bash
docker image ls 
```

Cette commande permet de voir via le terminale toutes les images docker installés.

Ici on a :
* docker-python-flask
* docker/getting-started
* hello-world
* ubuntu
* bitnami/python

### Éxécution de l'image build


``` bash
docker run -d -p 5000:5000 docker-python-flask
```

Lance le container à partir de l'image docker-python-flask avec le port 5000.