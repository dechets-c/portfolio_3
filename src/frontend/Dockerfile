# --- Étape 1 : Build de l'application ---
FROM node:18-alpine AS builder
WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .
RUN npm run build

# --- Étape 2 : On garde juste les fichiers ---
FROM alpine:latest
WORKDIR /usr/share/caddy

# On copie le build du React ici
COPY --from=builder /app/build .

# Une commande infinie pour que le conteneur reste en vie 
# et que Caddy puisse piocher dans ses fichiers
CMD ["sleep", "infinity"]