variable "aws_region" {
  description = "Région AWS où déployer l'infrastructure"
  type        = string
  default     = "eu-west-3" # Paris
}

variable "project_name" {
  description = "Nom du projet, utilisé comme préfixe pour les ressources"
  type        = string
  default     = "gestion-vols"
}

variable "cluster_version" {
  description = "Version de Kubernetes pour le cluster EKS"
  type        = string
  default     = "1.32"
}

variable "node_instance_type" {
  description = "Type d'instance EC2 pour les workers du cluster"
  type        = string
  default     = "c7i-flex.large"
}
