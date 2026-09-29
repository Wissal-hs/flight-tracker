# Cluster Kubernetes managé par AWS (EKS).
# Les workers (machines qui font tourner les pods) sont placés dans les sous-réseaux
# PUBLICS définis dans vpc.tf, pour éviter d'avoir besoin d'un NAT Gateway payant.

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.0"
  enable_cluster_creator_admin_permissions = true
  
  cluster_name    = "${var.project_name}-cluster"
  cluster_version = var.cluster_version

  vpc_id     = module.vpc.vpc_id
  subnet_ids = module.vpc.public_subnets

  # Nécessaire car les workers sont en sous-réseau public (pas de NAT)
  cluster_endpoint_public_access = true

  eks_managed_node_groups = {
    default = {
      instance_types = [var.node_instance_type]
      min_size       = 1
      max_size       = 1
      desired_size   = 1

      subnet_ids = module.vpc.public_subnets
    }
  }
}
