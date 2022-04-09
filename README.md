[![Test](https://github.com/devans10/pitt-cicd-demo/actions/workflows/test.yml/badge.svg)](https://github.com/devans10/pitt-cicd-demo/actions/workflows/test.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=devans10_pitt-cicd-demo&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=devans10_pitt-cicd-demo) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=devans10_pitt-cicd-demo&metric=coverage)](https://sonarcloud.io/summary/new_code?id=devans10_pitt-cicd-demo) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=devans10_pitt-cicd-demo&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=devans10_pitt-cicd-demo)

# pitt-cicd-demo

## Prerequisites

+ awscli - [Install Instructions](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ terraform - [Install Instructions](https://learn.hashicorp.com/tutorials/terraform/install-cli)


## Prepare Development Environment

Clone repository
```
git clone https://github.com/devans10/pitt-cicd-demo.git
cd pitt-cicd-demo
```

Install python dependancies
```
make install
```

## Build 
Build container image
```
docker build pitt-cicd-demo .
docker scan pitt-cicd-demo
```

## Local Test environment
```
docker-compose up
```

## Running tests
Unit Tests
```
make test

```

# CI/CD Setup

## GitHub

1. Sign up for GitHub Account.  We will use this account for all the other services required.

![GitHub Signup](/assets/github-signup.png)

2. Fork the repository
    While signed into GitHub, navigate to [https://github.com/pittdemo/pitt-cicd-demo](https://github.com/pittdemo/pitt-cicd-demo)

3. In the Upper right hand corner, click the Fork button

![Fork Button](/assets/fork-button.png)


## SonarCloud

1. SonarCloud is free for open-source projects. Go to [sonarcloud.io](https://sonarcloud.io)

2. Click the "GitHub" button.
![SonarCloud Signup](/assets/sonarcloud-signup.png)

3. Authorize SonarCloud in GitHub
![SonarCloud GitHub Authorize](/assets/sonar-github-authorize.png)

4. Import your GitHub Organization to SonarCloud
![Import GitHub Organization](/assets/sonar-github-import.png)

5. Select the Forked Repository to install SonarCloud.
![Install SonarCloud](/assets/sonar-install.png)

6. Create a SonarCloud Organization and select the Free plan.
![SonarCloud Organization](/assets/sonar-org.png)

7. Select the repository, and click "Setup"
![SonarCloud Setup](/assets/sonar-setup.png)

8. On the "Choose your Analysis Method", select "With GitHub Actions"
![SonarCloud Analyze Method](/assets/sonar-github-actions.png)

9. Follow the on screen instructions to create the `SONAR_TOKEN` secret in your repository.
    + In your GitHub repository, go to "Settings" -> "Secrets" and click "New repository secret"
![GitHub Secret](/assets/sonar-github-secret.png)
    + For the Name enter `SONAR_TOKEN` and the Value displayed on the SonarCloud page. Click "Add Secret"
![Sonar Token](/assets/sonar-token.png)

10. You do not need to update `.github/workflows/build.yml`. This is already part of the forked repository. Click "Other" and "Continue"

11. Update the `sonar-project.properties` file.
    + In your repository, select the `sonar-project.properties` file. Click the "Edit" icon.
![GitHub Edit](/assets/github-edit.png)
    + Replace the `sonar.projectKey` and `sonar.organization` with the values in the SonarCloud prompt.
![Sonar Project Properties](/assets/sonar-project-props.png)
    + Commit your changes

Your GitHub Actions Workflow will NOT run yet. Leave the SonarCloud page open and move on to the next section.

## Snyk
1. Navigate to [snyk.io](https://snyk.io), and click the "Sign up" button.

2. Click "GitHub" under "Get started for free"
![Snyk Signup](/assets/snyk-signup.png)

3. Authorize Snyk for GitHub.
![Snyk Authorize](/assets/snyk-authorize.png)

4. Select GitHub.
![Snyk Code](/assets/snyk-code.png)

5. Select the Default permissions and click Continue.
![Snyk Permissions](/assets/snyk-permissions.png)

6. Authorize Snyk in GitHub
![Snyk Authorize](/assets/snyk-github-authorize2.png)

7. Select the forked repository, and click "Import and scan".
![Snyk Import](/assets/snyk-import.png)

8. In the top right corner, click on your user icon and select "Account Settings"
![Synk Account Settings](/assets/snyk-account-settings.png)

9. Under "Auth Token", click to show the token key.  Copy this value.
![Snyk Auth Token](/assets/snyk-auth-token.png)

10. Create a Secret in your GitHub Repository for `SNYK_TOKEN`
    + In your GitHub repository, go to "Settings" -> "Secrets" and click "New repository secret"
![GitHub Secret](/assets/sonar-github-secret.png)
    + For the Name enter `SNYK_TOKEN` and the Value displayed on the Snyk page. Click "Add Secret"
![Snyk Token](/assets/snyk-secret)



## Terraform Cloud

1. Navigate to [Terraform Cloud](https://cloud.hashicorp.com/products/terraform)

2. Click "Try cloud for free" in the top-right corner.

3. Fill out the "Create an account" form.
![Terraform Create Account](/assets/terraform-cloud-signup.png)

4. On the "Choose your setup workflow", select "Start from scratch"
![Terraform Setup](/assets/terraform-setup.png)

5. Create a Terraform Organization
![Terraform Org](/assets/terraform-org.png)

6. On the "Create a new Workspace", select "CLI-driven workflow"
![Terraform Workspace Setup](/assets/terraform-workspace-setup.png)

7. Name your workspace `pitt-cicd-demo-shared`
![Terraform Workspace Name](/assets/terraform-name-workspace.png)

8. On the right-hand side. Add a tag to your workspace called `pitt-cicd-demo`
![Workspace Tag](/assets/terraform-workspace-tag.png)

9. Go to the Settings -> General section, Set the "Execution Mode" to local. Save the settings
![Workspace Setting](/assets/terraform-workspace-settings.png)

9. At the top of the page, go to "Workspaces" and click "+ Workspace"
![Workspace Add](/assets/terraform-add-workspace.png)

11. Add a 2nd Workspace
    + Workflow: `CLI-driven workflow`
    + Name: `pitt-cicd-demo-prod`
    + Tag: `pitt-cicd-demo`
    + Execution Mode: `local`

12. Add a 3rd Workspace:
    + Workflow: `CLI-driven workflow`
    + Name: `pitt-cicd-demo-test`
    + Tag: `pitt-cicd-demo`
    + Execution Mode: `local`

13. In the top right corner, click your user icon and select "User Settings"
![Terraform User Settings](/assets/terraform-user-settings.png)

14. Select Tokens and "Create an API token"
![Terraform Token](/assets/terraform-token.png)

13. Name the Token and copy the value.
![Terraform API Token](/assets/terraform-api-token.png)

14. Create another secret in your GitHub repository called `TF_API_TOKEN`
![GitHub Secret](/assets/terraform-github-secret.png)

15. In the GitHub repository, go to the "infrastructure" directory.
![infrastructure](/assets/github-infrastructure.png)

16. Edit the `versions.tf`, set the `cloud { organization = "" }` to the Organization set in Step 5. Commit your changes.

17. Navigate to the `infrastructure/shared` directory, Edit the same block in that `versions.tf`. Commit your changes.


## GitHub Environments

1. In your GitHub repository, go to Settings -> Environments, click "New Environment"
![GitHub Environment Setup](/assets/github-env-setup.png)

2. Add an environment called `prod`, click "Configure Environment"
![Prod Environment](/assets/github-env-prod.png)

3. Add an Environment secret called `TF_WORKSPACE`
    + Click "Add Secret"
![Add Secret](/assets/terraform-config-env.png)
    + Name `TF_WORKSPACE` value `pitt-cicd-demo-prod`
![Secret](/assets/github-env-secret.png)

4. Repeat the above steps for the `test` Environment
    + Name: `test`
    + Secret Name: `TF_WORKSPACE`
    + Secret Value: `pitt-cicd-demo-test`


## AWS
1. Create an [AWS Account.](https://aws.amazon.com/)
    + Click "Create an AWS Account" in upper right corner
    + Complete the signup information
        + WARNING!! There is a Free Tier, but this does require a credit card be entered. AWS does not warn about going out of free tier parameters, this could cost you money.
    + Select "Basic support - Free"
![aws Signup](/assets/aws-signup.png)

2. In the Search bar, type "IAM", and select IAM from the Services results.
![IAM Search](/assets/aws-iam.png)

3. Click on "Users" and "Add users"
![Add Users](/assets/aws-add-user.png)

4. Name the user `terraform` and select "Access key - Programmatic access", click "Next: Permissions"
![Terraform User](/assets/aws-terraform-user.png)

5. For Permissions, select "Attach existing policies directly", check "AdministratorAccess", click Next.
![User Permissions](/assets/aws-user-perms.png)

6. Click Next twice, and Create User.

7. Copy the `Access key ID` and the `Secret access key`
![User Keys](/assets/aws-user-keys.png)

8. In your GitHub repository, create 2 repository secrets `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` with the respective values.

9. You should now have the below secrets configured.
![GitHub Secrets](/assets/github-secrets.png)

## Enable Actions

Since the repository is forked, actions are disabled by default.  To enable them, go to "Actions" and click the "I understand my workflows, go ahead and enable them"

![GitHub Actions](/assets/github-actions.png)

## Deploy Shared Infrastructure

1. Clone your forked repository

```
git clone https://github.com/pittdemo/pitt-cicd-demo.git
cd pitt-cicd-demo/infrastructure/shared
```

2. Login to Terraform
```
terraform login
```
+ Copy the API Token generated and paste it in at the prompt.

3. Run `terraform init`, select the `pitt-cicd-demo-shared` workspace when prompted.
```
PS C:\Users\devans\code\pitt-cicd-demo\infrastructure\shared> terraform init

Initializing Terraform Cloud...

The currently selected workspace (default) does not exist.
  This is expected behavior when the selected workspace did not have an
  existing non-empty state. Please enter a number to select a workspace:

  1. pitt-cicd-demo-prod
  2. pitt-cicd-demo-shared
  3. pitt-cicd-demo-test

  Enter a value: 2


Initializing provider plugins...
- Finding hashicorp/aws versions matching ">= 3.59.0"...
- Installing hashicorp/aws v4.9.0...
- Installed hashicorp/aws v4.9.0 (signed by HashiCorp)

Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.

Terraform Cloud has been successfully initialized!

You may now begin working with Terraform Cloud. Try running "terraform plan" to
see any changes that are required for your infrastructure.

If you ever set or change modules or Terraform Settings, run "terraform init"
again to reinitialize your working directory.
```

4. Run `terraform plan`

```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # aws_ecr_lifecycle_policy.policy will be created
  + resource "aws_ecr_lifecycle_policy" "policy" {
      + id          = (known after apply)
      + policy      = jsonencode(
            {
              + rules = [
                  + {
                      + action       = {
                          + type = "expire"
                        }
                      + description  = "Keep last 2 images"
                      + rulePriority = 1
                      + selection    = {
                          + countNumber   = 2
                          + countType     = "imageCountMoreThan"
                          + tagPrefixList = [
                              + "v",
                            ]
                          + tagStatus     = "tagged"
                        }
                    },
                ]
            }
        )
      + registry_id = (known after apply)
      + repository  = "pitt-cicd-demo"
    }

  # aws_ecr_repository.repo will be created
  + resource "aws_ecr_repository" "repo" {
      + arn                  = (known after apply)
      + id                   = (known after apply)
      + image_tag_mutability = "IMMUTABLE"
      + name                 = "pitt-cicd-demo"
      + registry_id          = (known after apply)
      + repository_url       = (known after apply)
      + tags_all             = (known after apply)

      + encryption_configuration {
          + encryption_type = "KMS"
          + kms_key         = (known after apply)
        }

      + image_scanning_configuration {
          + scan_on_push = true
        }
    }

  # aws_kms_key.ecr will be created
  + resource "aws_kms_key" "ecr" {
      + arn                                = (known after apply)
      + bypass_policy_lockout_safety_check = false
      + customer_master_key_spec           = "SYMMETRIC_DEFAULT"
      + deletion_window_in_days            = 10
      + description                        = "ECR KMS key"
      + enable_key_rotation                = true
      + id                                 = (known after apply)
      + is_enabled                         = true
      + key_id                             = (known after apply)
      + key_usage                          = "ENCRYPT_DECRYPT"
      + multi_region                       = (known after apply)
      + policy                             = (known after apply)
      + tags_all                           = (known after apply)
    }

Plan: 3 to add, 0 to change, 0 to destroy.

Changes to Outputs:
  + ecr_repository_url = (known after apply)

```
5. Run `terraform apply`, enter `yes` when prompted to confirm the apply.


```
Do you want to perform these actions in workspace "pitt-cicd-demo-shared"?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

aws_kms_key.ecr: Creating...
aws_kms_key.ecr: Creation complete after 4s [id=4c2ec58b-8948-4fa5-8af9-13c15fce7af8]
aws_ecr_repository.repo: Creating...
aws_ecr_repository.repo: Creation complete after 0s [id=pitt-cicd-demo]
aws_ecr_lifecycle_policy.policy: Creating...
aws_ecr_lifecycle_policy.policy: Creation complete after 0s [id=pitt-cicd-demo]

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

Outputs:

ecr_repository_url = "433366580096.dkr.ecr.us-east-1.amazonaws.com/pitt-cicd-demo"
```
