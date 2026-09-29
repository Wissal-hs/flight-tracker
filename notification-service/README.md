# Notification Service

Microservice de gestion des notifications (FastAPI + PostgreSQL + Docker).

## Étapes à suivre

### 1. Tester en local avec Docker
```bash
docker compose up --build
```
Ouvre ensuite : http://localhost:8003/docs

### 2. Endpoints disponibles
- `GET /notifications` — liste de toutes les notifications
- `GET /notifications/flight/{flight_number}` — notifications d'un vol précis
- `POST /notifications` — créer une notification

### 3. Exemple de test
**Créer une notification** (`POST /notifications`) :
```json
{
  "flight_number": "AT205",
  "message": "Vol retardé de 30 minutes",
  "type": "retard"
}
```

### 4. Arrêter les conteneurs
```bash
docker compose down
```

### 5. Publier sur ton GitHub
Place ce dossier `notification-service` à côté des 3 autres, à l'intérieur de `flights-service` (ton dossier racine du repo).

```bash
cd C:\Users\HP\Videos\pfa\flights-service
git add .
git commit -m "Add notification service"
git push
```
