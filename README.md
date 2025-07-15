# openai-with-aws-test6

This repository provisions an S3 bucket, Lambda function and API Gateway using Terraform. Infrastructure is deployed via GitHub Actions using OIDC.

## Infrastructure
- **S3 Bucket**: `ontoscale-create-with-openai-codex`
- **Lambda**: writes a file to the bucket when triggered
- **API Gateway**: exposes an endpoint at `/create-file` that triggers the Lambda

Terraform backend is stored in `ontoscale-terraform-backend` (S3) in `us-east-1`.

## Workflows
- `Deploy Infrastructure` runs on merge to `main` and applies Terraform configuration.
- `Destroy Infrastructure` can be triggered manually from the Actions tab.

Set the secret `AWS_ROLE` in GitHub to the role ARN used for deployment.
