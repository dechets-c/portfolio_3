# Rapport d'activité — Projet Portfolio (BUT 3 S6)

**Période couverte :** 27 mars 2026 – 11 juin 2026
**Membres de l'équipe :** Quentin Delrive, Reda Belarbi
**Dépôt :** `dechets-c/portfolio_3`

## 1. Présentation du projet

Le projet consiste à développer un site portfolio personnel composé de :
- un **backend** en Python (FastAPI + SQLAlchemy + PostgreSQL), exposant une API REST sécurisée par authentification JWT, avec gestion CRUD des différentes sections du portfolio (projets, compétences, formations, outils, langues, loisirs, profil, expériences, certifications) ;
- un **frontend** (React) consommant cette API pour l'affichage public et pour une interface d'administration.

## 2. Répartition des activités

Le travail a été réparti à parts égales entre les deux membres de l'équipe :
- **Quentin Delrive** : initialisation du projet, modélisation des données et mise en place du CRUD de base (mars – avril 2026).
- **Reda Belarbi** : sécurisation de l'application, observabilité (logging), gestion des erreurs, migrations de base de données et tests (mai – juin 2026).

---

## 3. Activités de Quentin Delrive (27 mars – 21 avril 2026)

### Phase 1 — Initialisation du projet (27 mars 2026)
- Démarrage du dépôt et structure initiale du projet.
- Mise en place du fichier `.gitignore` et configuration des fichiers `.env` (variables sensibles exclues du suivi de version).
- Ajout des premiers fichiers Python du backend.

### Phase 2 — Architecture et connexion à la base de données (9 – 11 avril 2026)
- Réorganisation du dépôt : déplacement du backend et du frontend dans un dossier commun `src/`.
- Mise en place de la structure de fichiers du backend (routers, modèles, schémas).
- Configuration de la connexion à la base de données PostgreSQL.
- Mise en place du chargement des variables d'environnement (et fichier `.env.example`).
- Création de l'ORM SQLAlchemy et de l'entité **Projet**, avec endpoint d'insertion en base.
- Démarrage de l'application FastAPI (`main.py`).

### Phase 3 — Développement du CRUD applicatif (13 avril 2026)
Mise en place des modèles, schémas et routes backend pour les entités suivantes :
- Compétences
- Formations
- Outils
- Profil
- Loisirs
- Langues

### Phase 4 — Extensions du portfolio (21 avril 2026)
- Ajout de la fonctionnalité **Expériences** (modèle, schéma, endpoints).
- Ajout de la fonctionnalité **Certifications** (modèle, schéma, endpoints).

---

## 4. Activités de Reda Belarbi (15 mai – 11 juin 2026)

### Phase 1 — Sécurité et authentification (15 mai 2026)
- Mise en place d'un système d'**authentification JWT** (génération/validation de tokens, hachage des mots de passe).
- Protection de l'ensemble des routes d'administration par authentification.
- Ajout des dépendances nécessaires à l'authentification et aux tests (`pyproject.toml`, `uv.lock`).

### Phase 2 — CRUD avancé et endpoints publics (15 mai 2026)
- Ajout d'endpoints typés de mise à jour et de suppression pour toutes les entités CRUD, avec schémas Pydantic dédiés.
- Création d'endpoints publics en lecture seule, destinés à l'affichage du portfolio côté frontend.
- Écriture de tests d'intégration couvrant la sécurité et les opérations CRUD.

### Phase 3 — Observabilité et logging (15 mai 2026)
- Mise en place d'un middleware d'identification de requêtes (request ID) et de logging avancé.
- Ajout de logs sur les opérations d'authentification (router `auth`).
- Ajout de logs sur les opérations CRUD du back-office (router `admin`).
- Ajout de logs sur les requêtes en lecture seule (router `public`).

### Phase 4 — Robustesse et configuration (15 mai 2026)
- Mise en place d'**Alembic** pour la gestion des migrations de base de données.
- Création d'une hiérarchie d'exceptions personnalisées.
- Ajout de schémas de réponses paginées et de gestion d'erreurs standardisés.
- Mise en place d'une gestion centralisée des erreurs et amélioration de la configuration de l'application.

### Phase 5 — Réorganisation du dépôt (21 mai 2026)
- Conversion du frontend, jusque-là intégré en sous-module Git, en répertoire classique du dépôt.
- Fusion des branches et résolution des divergences entre les travaux des deux membres.

### Phase 6 — Travaux en cours (juin 2026, non finalisés)
- Génération de la migration initiale Alembic correspondant au schéma complet de la base de données.
- Extension des modèles et schémas **Certifications** et **Expériences** (champs de mise à jour).
- Nouveaux endpoints publics et d'administration pour ces entités (`routers/admin.py`, `routers/public.py`).
- Intégration côté frontend : appels API (`api.js`) et interface d'administration (`Admin.js`) pour gérer ces nouvelles données.
- Mise à jour des dépendances backend.

---

## 5. Bilan

| Volet | Responsable | Statut |
|---|---|---|
| Initialisation & architecture du projet | Quentin Delrive | ✅ Terminé |
| Modélisation des données & CRUD de base | Quentin Delrive | ✅ Terminé |
| Authentification JWT & sécurisation des routes | Reda Belarbi | ✅ Terminé |
| CRUD avancé, endpoints publics, tests | Reda Belarbi | ✅ Terminé |
| Logging & observabilité | Reda Belarbi | ✅ Terminé |
| Migrations de base de données (Alembic) | Reda Belarbi | ✅ Terminé / 🔄 finalisation en cours |
| Gestion centralisée des erreurs | Reda Belarbi | ✅ Terminé |
| Intégration frontend des nouvelles entités | Reda Belarbi | 🔄 En cours |

## 6. Prochaines étapes
- Finaliser et appliquer la migration Alembic initiale.
- Terminer l'intégration frontend (gestion des certifications et expériences dans l'interface admin).
- Mettre à jour la documentation technique du projet.
