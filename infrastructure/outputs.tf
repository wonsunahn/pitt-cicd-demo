output "ecr_repository_url" {
    value = aws_ecr_repository.repo.repository_url
}

output "api_endpoint" {
  value = aws_apigatewayv2_api.lambda.api_endpoint
}
