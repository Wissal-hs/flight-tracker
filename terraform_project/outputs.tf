output "cluster_name" {
  description = "Nom du cluster EKS créé"
  value       = module.eks.cluster_name
}

output "cluster_endpoint" {
  description = "Adresse de l'API du cluster Kubernetes"
  value       = module.eks.cluster_endpoint
}

output "configure_kubectl" {
  description = "Commande à exécuter pour connecter kubectl à ce cluster AWS"
  value       = "aws eks update-kubeconfig --region ${var.aws_region} --name ${module.eks.cluster_name}"
}
