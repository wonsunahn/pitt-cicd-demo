terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 3.59.0"
    }
  }

  backend "s3" {
    bucket     = "s3-dlc-svc-backend-use120210825020544795700000003"
    key        = "devans/terraform.tfstate"
    region     = "us-east-1"
    encrypt    = true
    kms_key_id = "812c468a-9478-4fff-8338-6c8f3ca2cab9"
  }
}

provider "aws" {
  region = "us-east-1"
  assume_role {
    role_arn = var.assume_role_arn
  }
}