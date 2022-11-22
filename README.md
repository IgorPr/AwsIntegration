# Aws lambda integration example
## Install github cli
brew install gh

### Authenticate with GitHub:
gh auth login

#### Add AWS credentials as GitHub secrets. By using GitHub secrets, your credentials are encrypted and cannot be seen publicly. Use the gh secret set command to upload your AWS credentials one by one (you'll be prompted to paste the values for each one):

#### !!! pay attention to the region where the lambda is added !!!

#### AWS_ACCESS_KEY_ID:
gh secret set AWS_ACCESS_KEY_ID

#### AWS_SECRET_ACCESS_KEY:
gh secret set AWS_SECRET_ACCESS_KEY

#### AWS_REGION:
gh secret set AWS_REGION

#### To  make sure your credentials have been uploaded correctly, you can list the available GitHub secrets:
gh secret list


aws configure --profile localstack

# (serverless deploy)
serverless deploy --stage local