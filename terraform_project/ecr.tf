# ECR = "Docker Hub privé" d'AWS. Il faut y pousser tes images Docker
# pour que le cluster EKS puisse les utiliser (une image "locale" sur ton PC
# n'est pas visible depuis AWS).

locals {
  services = ["flights-service", "booking-service", "auth-service", "notification-service"]
}

resource "aws_ecr_repository" "services" {
  for_each = toset(local.services)

  name         = each.value
  force_delete = true # permet de supprimer le repo même s'il contient des images (pratique en test)
}

output "ecr_repository_urls" {
  description = "Adresses des dépôts ECR, à utiliser pour pousser tes images Docker"
  value       = { for k, repo in aws_ecr_repository.services : k => repo.repository_url }
}
