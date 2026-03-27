## 1. Fonctions necessaires
- [ ] connect bdd
    - [ ] var d'environnement 
        - [ ] host
        - [ ] port
        - [ ] bdd
        - [ ] user
        - [ ] password
- [ ] insérer des données
- [ ] logs pour page admin (via token)
    - [ ] var d'env 
        - [ ] admin 
        - [ ] password
    - [ ] gestion de token java jsplus quoi faut que je regarde le blase
- [ ] recup des données dans la base
    - [ ] selon table
    - [ ] selon critère

## 2. Endpoint
(les urls d'interraction entre le frontend et le backend)
- [ ] /api/admin/insert_data : POST // insérer données
- [ ] /api/get_data : GET // recup données
    - [ ] table
    - [ ] col : valeur (dict ?)
- [ ] /api/admin/login : POST // connection

## 3. Fichier
- [ ] endpoints/admin_insert_data.py
- [ ] endpoints/get_date.py
- [ ] endpoints/admin_logins.py
- [ ] logins.py
- [ ] logger_setup.py
- [ ] db.py
- [ ] _types.py
- [ ] main.py // app start
