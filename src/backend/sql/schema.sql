-- Portfolio S3 database schema generated from the SQLAlchemy models.

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR NOT NULL UNIQUE,
    hashed_password VARCHAR NOT NULL,
    is_active BOOLEAN DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_users_id ON users (id);
CREATE INDEX IF NOT EXISTS ix_users_email ON users (email);

CREATE TABLE IF NOT EXISTS profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prenom VARCHAR,
    nom VARCHAR,
    email VARCHAR,
    telephone VARCHAR,
    adresse VARCHAR,
    dn DATE,
    linkedin VARCHAR,
    github VARCHAR,
    photo VARCHAR,
    bio TEXT
);

CREATE INDEX IF NOT EXISTS ix_profiles_id ON profiles (id);

CREATE TABLE IF NOT EXISTS projects (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    description VARCHAR,
    date_debut DATE,
    date_fin DATE,
    role VARCHAR,
    url VARCHAR
);

CREATE INDEX IF NOT EXISTS ix_projects_id ON projects (id);

CREATE TABLE IF NOT EXISTS competences (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    categorie_comp VARCHAR,
    date_debut_comp DATE
);

CREATE INDEX IF NOT EXISTS ix_competences_id ON competences (id);

CREATE TABLE IF NOT EXISTS formations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom_formation VARCHAR,
    nom_ecole VARCHAR,
    niveau VARCHAR,
    secteur VARCHAR,
    date_debut DATE,
    date_fin DATE
);

CREATE INDEX IF NOT EXISTS ix_formations_id ON formations (id);

CREATE TABLE IF NOT EXISTS outils (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    categorie VARCHAR,
    niveau INTEGER,
    url_logo VARCHAR
);

CREATE INDEX IF NOT EXISTS ix_outils_id ON outils (id);

CREATE TABLE IF NOT EXISTS loisirs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    description VARCHAR
);

CREATE INDEX IF NOT EXISTS ix_loisirs_id ON loisirs (id);

CREATE TABLE IF NOT EXISTS langages (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR,
    niveau VARCHAR
);

CREATE INDEX IF NOT EXISTS ix_langages_id ON langages (id);