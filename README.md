
***
[Watch below for the English version](#LITReview_project-en) 
***

# Projet LITReview (fr)

***

Ce projet est entièrement codé en python 3.

Il est réalisé dans le cadre d'une formation sur le site [OpenClassrooms](https://openclassrooms.com/fr/).
Ce projet est une interface web qui permet de poster des critiques de livre et des demandes de critiques. Un utilisateur peut suivre un autre utilisateur afin de voir ses critiques et ses demandes de critiques dans son flux.

## Table des matières
1. [Informations génerales](#informations-generales)
2. [Installation/usage](#installation-usage)

***

## Informations Generales

Ce projet utilise le framework [django](https://docs.djangoproject.com/fr/3.2/) pour la création du backend. Pour la création de l'interface frontend, le projet utilise [bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/). Pour le système de notation en étoiles, le projet utilise les étoiles proposées par [line awesome](https://icons8.com/line-awesome). Le projet utilise un rendu coté serveur pour afficher des pages dynamiquement aux utilisateurs du site.

Dans django, le projet utilise deux applications (en dehors des applications django pré-installées) :

*	review: l'application qui est l'application principale et qui gère tout le système de critique et d'abonnement entre utilisateurs.

*	account: l'application qui gère le système de connexion et de création de compte utilisateur (le projet utilise le [système d'authentification](https://docs.djangoproject.com/fr/3.2/topics/auth/) inclus dans django).

L'ensemble des packages et dépendances à installer pour pouvoir lancer le projet sont notés dans le fichier 'requirements.txt' présent à la racine du projet.

Une base de données contenant déjà des utilisateurs des tickets et des reviews en exemple est présente dans le repository. 

Le site est accèssible aux utilisateurs connéctés uniquement.

Un compte de démonstration disposant d'abonnements de critiques et de tickets est accessible :

**nom de compte**: DEMO 
**mot de passe**: MLKJHGFDSQ

Il est aussi possible de créer un compte en remplissant le formulaire d'inscription.

Lors de votre première connection, vos onglets flux et posts sont vides. Il est possible de créer un commentaire une critique ou de suivre d'autres utilisateurs pour afficher du contenu dans ces onglets.

Pour suivre un autre utilisateur il faut taper son nom d'utilisateur dans le champ prévu à cet effet dans l'onglet abonnement. Dans ce MVP la fonction d'auto-complétion n'est pas disponible.

La synthaxe du code respecte les directives de la PEP 8 (vérification avec flake-8). Un rapport flake8 est disponible dans le repertoire flake-report à la racine du projet.

Pour information, actuellement, le parametre DEBUG présent dans le fichier src/LITReviw/settings.py a pour valeur "True". En cas de mise en production il sera nécessaire de le passer à "False".

## Installation Usage

Tout d'abord il faut cloner le projet depuis github grâce à la commande suivante :

```
$ git clone https://github.com/npaillasson/LITReview_project.git
```

Il est ensuite recommandé de créer un environement virtuel avec venv afin d'installer tous les packages et dépendances nécéssaires au fonctionnement du projet :

```
$ python3 -m venv env
```

Utilisez ensuite la commande suivante pour activer l'environnement :
```
$ source env/bin/activate
```

Vous pouvez ensuite installer les packages nécéssaire grace à pip et au fichier requirements.txt :
```
$ pip install requirements.txt
```

Pour lancer le serveur exécuter la commande suivante :
```
$ python3 src/manage.py runserver
```

Vous pouvez ensuite aller sur le [site](http://127.0.0.1:8000/) (http://127.0.0.1:8000/)

Pour désactiver l'environnement virtuel, utilisez la commande suivante :
```
$ deactivate
```

Pour créer un rapport de conformité à la pep 8 vous pouvez utiliser la commande suivante à la racine du projet :

```
$ flake8 --format=html --htmldir=flake-report --max-line-length=119 --exclude='src/*/migrations/*.py' src/
```
***
# LITReview_project (en)
***
This project is entirely coded in python 3.

It is realized within the framework of a training on the site [OpenClassrooms](https://openclassrooms.com/fr/).
This project is a web interface to post book reviews and review requests. A user can follow another user to see these reviews and review requests in their feed.


## Table of contents
1. [General information](#general-information)
2. [Installation/usage](#installation)

***

## General Information

This project uses the [django](https://docs.djangoproject.com/en/3.2/) framework to create the backend. For the frontend creation, the project uses [bootstrap](https://getbootstrap.com/docs/5.1/getting-started/introduction/). For the star rating system, the project uses the stars proposed by [line awesome](https://icons8.com/line-awesome). The project uses server side rendering to display pages dynamically to the users of the site.

This project uses two applications (besides the pre-installed django applications) :

* review: the application that is the main application and manages the whole review and subscription system.

* account: the application that manages the login, logout and user account creation system (the project uses the [authentication system](https://docs.djangoproject.com/en/3.2/topics/auth/) included in django).

All the packages and dependencies needed for the project are noted in the 'requirements.txt' file at the root of the project.

A database already containing users, tickets and reviews in example is present in the repository. 

The site is accessible to connected users only.

A demo account with review and ticket subscription is available :

**account name**: DEMO 
**password**: MLKJHGFDSQ

It is also possible to create an account by filling out the registration form.

When you first connect, your feeds and posts tabs are empty. It is possible to create a comment, a review or to follow other users to post content in these tabs.

To follow another user, you must type his or her user name in the field provided in the subscription tab. In this MVP, the auto-complete function is not available.

The synthaxe of the code is compliant with the pep 8 (check with flake-8). A flake8 report is available in the flake-report directory at the root of the project.

For the moment, the DEBUG parameter in the src/LITReviw/settings.py file has the value "True". If the project goes into production, it will be necessary to change it to "False".

## Installation

To clone the project locally use the following command :

```
$ git clone https://github.com/npaillasson/LITReview_project.git
```

it is recommended to create a virtual environment with venv :

```
$ python3 -m venv env
```

To activate the virtual environment use :
```
$ source env/bin/activate
```

To install the necessary packages use pip and the file requierements.txt :
```
$ pip install requirements.txt
```

To launch the server use :
```
$ python3 src/manage.py runserver
```

Now you can access the [website](http://127.0.0.1:8000/) (http://127.0.0.1:8000/)

To deactivate the virtual environement use :
```
$ deactivate
```

You can create a flake-8 repport with the next command at the project root :

```
$ flake8 --format=html --htmldir=flake-report --max-line-length=119 --exclude='src/*/migrations/*.py' src/
```

****