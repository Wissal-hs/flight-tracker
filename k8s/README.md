# Déploiement Kubernetes (test local avec Docker Desktop)

Ce dossier contient les manifests Kubernetes pour les 4 microservices.
On teste ici en local (cluster Kubernetes intégré à Docker Desktop), avant de refaire
la même chose plus tard sur AWS (EKS) une fois Terraform en place.

## Étape 1 : Construire les images Docker localement

Kubernetes a besoin d'images Docker déjà construites (il ne lit pas directement
ton code source). Depuis PowerShell, va dans chaque dossier de service et construis
l'image avec un tag `:local` :

```bash
cd C:\Users\HP\Videos\pfa\flights-service\flights-service
docker build -t flights-service:local .

cd C:\Users\HP\Videos\pfa\flights-service\booking-service
docker build -t booking-service:local .

cd C:\Users\HP\Videos\pfa\flights-service\auth-service
docker build -t auth-service:local .

cd C:\Users\HP\Videos\pfa\flights-service\notification-service
docker build -t notification-service:local .
```

## Étape 2 : Créer le namespace

Un namespace regroupe toutes les ressources de ton projet, séparément du reste du cluster :

```bash
kubectl apply -f 00-namespace.yaml
```

## Étape 3 : Déployer chaque microservice

```bash
kubectl apply -f flights-service/flights-service.yaml
kubectl apply -f booking-service/booking-service.yaml
kubectl apply -f auth-service/auth-service.yaml
kubectl apply -f notification-service/notification-service.yaml
```

## Étape 4 : Vérifier que tout tourne

```bash
kubectl get pods -n gestion-vols
```

Tu dois voir 8 pods (4 services + 4 bases de données) avec le statut `Running`.

```bash
kubectl get services -n gestion-vols
```

## Étape 5 : Tester dans le navigateur

- flights-service : http://localhost:30800/docs
- booking-service : http://localhost:30801/docs
- auth-service : http://localhost:30802/docs
- notification-service : http://localhost:30803/docs

## Si une image n'est pas trouvée (ErrImageNeverPull / ImagePullBackOff)

Ça arrive si le cluster ne trouve pas l'image locale. Vérifie d'abord :
```bash
kubectl describe pod <nom_du_pod> -n gestion-vols
```

## Commandes utiles pour la suite

- Voir les logs d'un service :
  ```bash
  kubectl logs -n gestion-vols deployment/flights-service
  ```
- Supprimer tout (pour repartir de zéro) :
  ```bash
  kubectl delete namespace gestion-vols
  ```
