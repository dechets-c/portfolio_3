Automatisation: extraire CV et seed via le front

Fichiers ajoutés:
- `extract_cv.py` : heuristiques simples pour extraire nom, email, téléphone, linkedin depuis un PDF.
- `seed_via_front.py` : script Playwright (navigateur réel) qui crée/connexion admin via l'API, ouvre le front et soumet le formulaire `profile`.
- `requirements-playwright.txt` : dépendances pour ces scripts.

Usage (préparer, ne pas exécuter sans vérification):

1. Installer dépendances Python et Playwright browsers:

```bash
python -m pip install -r tools/requirements-playwright.txt
playwright install
```

2. Extraire le CV (ex : `cv_quentin_delrive_data_engineer.pdf` placé à la racine):

```bash
python tools/extract_cv.py cv_quentin_delrive_data_engineer.pdf > cv.json
```

3. Servir le build frontend (ou lancer le serveur dev). Par exemple servir le dossier `src/frontend/build` sur `http://localhost:3000` :

```bash
pushd src/frontend/build
python -m http.server 3000
popd
```

4. Lancer le seeder (option `--register` crée d'abord l'utilisateur admin via l'API `/auth/register`):

```bash
python tools/seed_via_front.py cv.json --admin-email you@example.com --admin-password S3cret! --register
```

Sécurité et limites:
- Le script crée un utilisateur admin via l'API si demandé; il n'effectue aucune requête SQL directe.
- L'extraction PDF est heuristique — vérifie `cv.json` avant de lancer.
- Je n'exécuterai rien sans ton approbation explicite.
