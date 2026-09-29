# Infrastructure AWS avec Terraform

Ce dossier contient le code Terraform qui crée automatiquement sur AWS :
- Un réseau (VPC) avec sous-réseaux publics uniquement (pas de NAT Gateway, pour rester gratuit)
- Un cluster Kubernetes managé (EKS) avec 1 nœud worker
- 4 dépôts ECR (un par microservice) pour stocker tes images Docker

## Étape 1 : Initialiser et créer l'infrastructure

Dans PowerShell, va dans CE dossier (celui qui contient main.tf, vpc.tf, eks.tf...) :
```
cd chemin\vers\ce\dossier
```
```
terraform init
```
```
terraform plan
```
```
terraform apply
```
Tape `yes` quand demandé. **Ça prend 10-15 minutes** (création du cluster EKS).

## Étape 2 : Connecter kubectl au cluster AWS

```
aws eks update-kubeconfig --region eu-west-3 --name gestion-vols-cluster
```
```
kubectl get nodes
```

## Étape 3 : Pousser tes images Docker sur ECR

Récupère les adresses ECR :
```
terraform output ecr_repository_urls
```

Pour chaque service (exemple avec flights-service) :
```
aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin <ID_COMPTE>.dkr.ecr.eu-west-3.amazonaws.com

docker tag flights-service:local <ID_COMPTE>.dkr.ecr.eu-west-3.amazonaws.com/flights-service:latest

docker push <ID_COMPTE>.dkr.ecr.eu-west-3.amazonaws.com/flights-service:latest
```
Répète pour `booking-service`, `auth-service`, `notification-service`.

## Étape 4 : Déployer sur EKS

Dans tes fichiers `k8s/*/*.yaml`, remplace chaque `image: xxx-service:local` par
l'adresse ECR correspondante, puis :
```
kubectl apply -f 00-namespace.yaml
kubectl apply -f flights-service/flights-service.yaml
kubectl apply -f booking-service/booking-service.yaml
kubectl apply -f auth-service/auth-service.yaml
kubectl apply -f notification-service/notification-service.yaml
kubectl get pods -n gestion-vols
```

## Étape 5 : Tester

```
kubectl get nodes -o wide
```
Récupère l'IP publique du node, puis dans le navigateur :
`http://<IP_DU_NODE>:30800/docs`

## Étape 6 : TRÈS IMPORTANT — Supprimer l'infrastructure après tes tests/captures

```
kubectl delete namespace gestion-vols
```
```
terraform destroy
```
Tape `yes`. Vérifie ensuite dans la console AWS que le cluster EKS a bien disparu.

## Suivi des coûts

Configure une alerte de budget (gratuit) :
1. Console AWS → cherche **"Budgets"**
2. **Create budget** → Budget mensuel → Montant : 5$ ou 10$
3. Ajoute ton email pour être alertée si ça approche ce montant
