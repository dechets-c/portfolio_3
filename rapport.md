# Rapport de projet - Portfolio BUT 3

## Contexte général

Ce projet consiste à concevoir un portfolio personnel pour un étudiant de BUT, avec une logique de présentation claire, sobre et facile à maintenir. L’objectif n’est pas seulement d’obtenir un site visuellement correct, mais aussi de construire une base technique propre permettant d’ajouter, modifier et organiser les contenus au fil du temps. Le projet s’inscrit donc dans une logique de communication, de valorisation des compétences et de prise en main d’outils de développement web modernes.

Le portfolio s’appuie sur une architecture séparée entre un backend FastAPI et un frontend React. Cette séparation permet de distinguer la gestion des données, la logique applicative et l’interface utilisateur. Elle rend aussi le projet plus évolutif, notamment si l’on souhaite plus tard enrichir le site avec une authentification, un espace d’administration ou des contenus dynamiques.

## Rapport des activités réalisées

Plusieurs activités ont été menées afin de faire avancer le projet de manière cohérente. Dans un premier temps, il a fallu analyser les besoins fonctionnels d’un portfolio étudiant : présentation du profil, mise en avant des projets, description des compétences, formation, centres d’intérêt et moyens de contact. Cette phase de réflexion a servi à définir les informations réellement utiles pour un visiteur, tout en évitant de surcharger l’interface.

Ensuite, la structure du projet a été mise en place. Le backend a été organisé autour de FastAPI, de SQLAlchemy et d’Alembic afin de gérer les modèles de données, les migrations et les routes API. Le frontend a été développé avec React, en s’appuyant sur une organisation par composants pour séparer les différentes sections du portfolio. Cette approche facilite la maintenance, la lecture du code et les évolutions futures.

Une autre activité importante a consisté à concevoir la base de données. Le choix a été fait de représenter les entités principales du portfolio sous forme de tables distinctes : utilisateurs, profils, projets, compétences, formations, outils, loisirs et langages. Ce découpage permet de structurer les contenus proprement et de préparer une éventuelle administration du site.

Enfin, plusieurs ajustements ont été apportés pour rendre le projet plus exploitable : gestion des données, préparation des schémas, réflexion sur l’authentification et organisation des fichiers. L’ensemble de ces tâches montre une progression du projet depuis une simple maquette vers une application web plus complète et plus professionnelle.

## Analyse et critique de l’existant

Les eportfolios réalisés en BUT2 présentent généralement une bonne base de départ, car ils permettent déjà de découvrir les compétences de l’étudiant, ses projets et son parcours. Ils remplissent donc leur rôle principal : donner une image synthétique et personnelle du profil. Dans certains cas, ces réalisations sont même très réussies sur le plan visuel, avec une identité graphique marquée et une navigation simple.

Cependant, plusieurs limites reviennent souvent dans les versions existantes. D’abord, le contenu est parfois trop statique : les informations sont directement écrites dans le code, ce qui complique les mises à jour et rend l’évolution du site peu pratique. Ensuite, l’organisation des données n’est pas toujours pensée pour durer. Les pages peuvent fonctionner correctement, mais sans structure métier claire en arrière-plan, ce qui limite les possibilités d’ajout de fonctionnalités.

On remarque aussi que certains portfolios BUT2 privilégient l’apparence au détriment de la lisibilité ou de la hiérarchisation de l’information. Le visiteur peut alors avoir du mal à identifier rapidement les éléments importants : compétences, expériences, projets, contact. Un bon portfolio ne doit pas seulement être esthétique ; il doit surtout être efficace, fluide et utile pour un recruteur ou un enseignant.

Le projet actuel cherche justement à corriger ces limites. L’idée est de proposer un socle plus structuré, avec une vraie séparation entre l’affichage, la logique applicative et les données. Cela permet d’obtenir un résultat plus propre, plus robuste et plus simple à faire évoluer.

## La base SQL

La base SQL joue un rôle central dans le projet, car elle sert à organiser les informations du portfolio de manière cohérente. Le schéma principal contient plusieurs tables correspondant aux entités du site. On y retrouve notamment une table `users` pour les comptes, une table `profiles` pour les informations personnelles, une table `projects` pour les réalisations, ainsi que des tables dédiées aux compétences, formations, outils, loisirs et langages.

Ce choix de structure permet de séparer les données selon leur nature. Par exemple, les projets ne sont pas mélangés avec les formations, et les compétences sont indépendantes des informations de profil. Cette modélisation rend la base plus lisible et limite les doublons. Elle facilite aussi l’interrogation des données depuis le backend, puisqu’il devient possible de récupérer uniquement les blocs nécessaires à l’affichage.

Le fichier SQL montre une structure simple mais adaptée à un portfolio étudiant. Les identifiants sont gérés automatiquement, des index sont présents sur plusieurs tables pour améliorer l’accès aux données, et la table utilisateurs inclut les champs essentiels pour une future authentification. La base constitue donc un fond solide pour une évolution vers un système d’administration ou de mise à jour du contenu.

Dans une logique de projet, cette base SQL n’est pas seulement un support technique : elle traduit aussi une manière de penser le site. Au lieu de stocker les informations de façon dispersée, tout est regroupé dans un modèle relationnel propre. Cela donne au portfolio une meilleure stabilité et le rend plus crédible dans une perspective de présentation professionnelle.

## Bilan

Ce projet de portfolio BUT 3 vise à dépasser le simple site vitrine. Il cherche à construire un outil structuré, maintenable et évolutif, capable de présenter un parcours étudiant de façon claire et sérieuse. Le travail réalisé autour du backend, du frontend et de la base SQL montre une volonté d’aller vers une solution plus propre que les portfolios de génération précédente, souvent limités par une architecture trop figée.

Au final, le projet met en avant trois idées fortes : une présentation lisible du profil, une organisation technique solide, et une base de données pensée pour durer. C’est cette combinaison qui permet de transformer un simple portfolio en véritable application de valorisation personnelle.