#!/usr/bin/env bash
set -e

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BACKEND="$ROOT/src/backend"
FRONTEND="$ROOT/src/frontend"

if [ ! -f "$BACKEND/.env" ]; then
  echo "[!] Fichier $BACKEND/.env manquant."
  cp "$BACKEND/.env.example" "$BACKEND/.env"
  echo "Un .env vide a ete cree a partir de .env.example."
  echo "Renseigne db_name, db_user, db_password, db_host et secret_key, puis relance ce script."
  exit 1
fi

echo "Lancement du backend FastAPI sur http://127.0.0.1:8000 ..."
(cd "$BACKEND" && uv run uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload) &

if [ ! -d "$FRONTEND/node_modules" ]; then
  echo "Installation des dependances frontend (premiere fois)..."
  (cd "$FRONTEND" && npm install)
fi

echo "Lancement du frontend React sur http://localhost:3000 ..."
(cd "$FRONTEND" && npm start) &

echo ""
echo "Portfolio public : http://localhost:3000"
echo "Interface admin  : http://localhost:3000/#b7a9f3c2"
wait
