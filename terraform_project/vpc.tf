# Réseau virtuel (VPC) qui va héberger le cluster Kubernetes.
# On utilise uniquement des sous-réseaux PUBLICS et on désactive le NAT Gateway
# pour éviter des coûts supplémentaires (choix budgétaire assumé, expliqué dans le rapport).

module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "~> 5.0"

  name = "${var.project_name}-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["${var.aws_region}a", "${var.aws_region}b"]
  public_subnets  = ["10.0.1.0/24", "10.0.2.0/24"]
  private_subnets = [] # aucun sous-réseau privé => pas besoin de NAT Gateway

  enable_nat_gateway       = false
  map_public_ip_on_launch  = true

  # Tags requis par EKS pour savoir où placer les ressources (load balancers, etc.)
  public_subnet_tags = {
    "kubernetes.io/role/elb"                            = "1"
    "kubernetes.io/cluster/${var.project_name}-cluster" = "shared"
  }
}
