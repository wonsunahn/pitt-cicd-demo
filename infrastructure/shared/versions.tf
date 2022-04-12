terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.59.0"
    }
  }

  cloud {
    organization = "cicd-demo-wonsunahn"

    workspaces {
      tags = ["pitt-cicd-demo"]
    }
  }
}

provider "aws" {
  region = "us-east-1"
}
