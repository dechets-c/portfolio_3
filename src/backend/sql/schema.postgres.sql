-- Portfolio S3 database schema for PostgreSQL.

CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR NOT NULL UNIQUE,
    hashed_password VARCHAR NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS ix_users_id ON users (id);
CREATE INDEX IF NOT EXISTS ix_users_email ON users (email);

CREATE TABLE IF NOT EXISTS profiles (
    id SERIAL PRIMARY KEY,
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
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    description VARCHAR,
    date_debut DATE,
    date_fin DATE,
    role VARCHAR,
    url VARCHAR
);

CREATE INDEX IF NOT EXISTS ix_projects_id ON projects (id);

CREATE TABLE IF NOT EXISTS competences (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    categorie_comp VARCHAR,
    date_debut_comp DATE
);

CREATE INDEX IF NOT EXISTS ix_competences_id ON competences (id);

CREATE TABLE IF NOT EXISTS formations (
    id SERIAL PRIMARY KEY,
    nom_formation VARCHAR,
    nom_ecole VARCHAR,
    niveau VARCHAR,
    secteur VARCHAR,
    date_debut DATE,
    date_fin DATE
);

CREATE INDEX IF NOT EXISTS ix_formations_id ON formations (id);

CREATE TABLE IF NOT EXISTS outils (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    categorie VARCHAR,
    niveau INTEGER,
    url_logo VARCHAR
);

CREATE INDEX IF NOT EXISTS ix_outils_id ON outils (id);

CREATE TABLE IF NOT EXISTS loisirs (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    description VARCHAR
);

CREATE INDEX IF NOT EXISTS ix_loisirs_id ON loisirs (id);

CREATE TABLE IF NOT EXISTS langages (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    niveau VARCHAR
);

CREATE INDEX IF NOT EXISTS ix_langages_id ON langages (id);