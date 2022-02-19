variable "assume_role_arn" {
  type    = string
  default = "arn:aws:iam::668998518041:role/iam-role-dlc-devans-terraform"
}

variable "container_registry_url" {
  type = string
}

variable "image_tag" {
  type = string
}

variable "environment" {
  type = string
}