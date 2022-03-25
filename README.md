[![Test](https://github.com/devans10/pitt-cicd-demo/actions/workflows/test.yml/badge.svg)](https://github.com/devans10/pitt-cicd-demo/actions/workflows/test.yml)
[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=devans10_pitt-cicd-demo&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=devans10_pitt-cicd-demo) [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=devans10_pitt-cicd-demo&metric=coverage)](https://sonarcloud.io/summary/new_code?id=devans10_pitt-cicd-demo) [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=devans10_pitt-cicd-demo&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=devans10_pitt-cicd-demo)

# pitt-cicd-demo

## Prerequisites

+ k6
+ checkov
+ terraform
+ python
+ docker

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