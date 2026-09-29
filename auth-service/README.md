# Auth Service

Microservice d'authentification (FastAPI + PostgreSQL + Docker + JWT).

## Étapes à suivre

### 1. Tester en local avec Docker
```bash
docker compose up --build
```
Ouvre ensuite : http://localhost:8002/docs

### 2. Endpoints disponibles
- `POST /register` — créer un utilisateur (email + mot de passe + rôle)
- `POST /login` — se connecter, renvoie un token JWT
- `GET /users` — liste des utilisateurs

### 3. Exemple de test
**Inscription** (`POST /register`) :
```json
{
  "email": "admin@onda.ma",
  "password": "motdepasse123",
  "role": "admin"
}
```

**Connexion** (`POST /login`) avec le même email/mot de passe → tu reçois un `access_token`.

### 4. Arrêter les conteneurs
```bash
docker compose down
```

### 5. Publier sur ton GitHub
Place ce dossier `auth-service` à côté de `booking-service`, à l'intérieur de `flights-service` (ton dossier racine du repo).

```bash
cd C:\Users\HP\Videos\pfa\flights-service
git add .
git commit -m "Add auth service"
git push
```
