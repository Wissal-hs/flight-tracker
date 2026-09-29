# Flights Service

Microservice de gestion des vols (FastAPI + PostgreSQL + Docker).

## Étapes à suivre

### 1. Tester en local avec Docker
```bash
docker compose up --build
```
Ouvre ensuite : http://localhost:8000/docs
→ Tu verras l'interface Swagger générée automatiquement, tu peux tester tous les endpoints dessus.

### 2. Endpoints disponibles
- `GET /flights` — liste des vols (avec `?search=` pour rechercher)
- `GET /flights/{id}` — un vol précis
- `POST /flights` — créer un vol
- `PUT /flights/{id}` — modifier un vol
- `DELETE /flights/{id}` — supprimer un vol

### 3. Arrêter les conteneurs
```bash
docker compose down
```

### 4. Publier sur ton GitHub
Depuis le dossier `flights-service` :
```bash
git init
git add .
git commit -m "Initial commit - flights service"
git branch -M main
git remote add origin https://github.com/TON_USERNAME/gestion-vols-pfa.git
git push -u origin main
```
(remplace `TON_USERNAME` par ton nom d'utilisateur GitHub, et crée d'abord un repo vide nommé `gestion-vols-pfa` sur github.com)
