# Booking Service

Microservice de gestion des réservations (FastAPI + PostgreSQL + Docker).

## Étapes à suivre

### 1. Tester en local avec Docker
```bash
docker compose up --build
```
Ouvre ensuite : http://localhost:8001/docs

### 2. Endpoints disponibles
- `GET /bookings` — liste des réservations
- `GET /bookings/{id}` — une réservation précise
- `POST /bookings` — créer une réservation
- `DELETE /bookings/{id}` — annuler une réservation (change son statut à "annulee")

### 3. Arrêter les conteneurs
```bash
docker compose down
```

### 4. Publier sur ton GitHub
Ce microservice va dans le même repo que flights-service (`flight-tracker`), dans un sous-dossier `booking-service`.

Depuis le dossier racine de ton projet (celui qui contient à la fois `flights-service` et `booking-service`) :
```bash
git add .
git commit -m "Add booking service"
git push
```

Si tu n'as pas encore un dossier racine commun, place `booking-service` à côté de `flights-service` dans `C:\Users\HP\Videos\pfa\` avant de faire le commit.
