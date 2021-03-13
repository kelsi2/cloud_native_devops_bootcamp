# Theory of CI/CD

- Projects:
  - Deploy .Net Web App with GitHub Actions
  - Building a Continuous Integration pipeline
  - Deploying Terraform via GitHub Actions
  - Setting up Continuous Monitoring in Azure DevOps
  - Artifacts and Packages in CI/CD
  - Builds with AWS CodeBuild

## What is CI/CD

- Committing and rolling out changes as fast and securely as possible
- Allow companies to stay competitive by rolling out changes quickly

## Difference between CI, CD, and CD

- Continuous Integration - Automating the process of merging code back into master
- Continuous Delivery - Extending CI by deploying new merged code into the environment for testing, qa, and production
- Continuous Deployment - Extending continuous delivery by removing human intervention from the CI/CD process

## Which Tool to Use?

- Azure DevOps
- GitHub Actions
- AWS Code Deploy
  - We are focusing on these 3 but they're all very much the same, don't need to know them all
- Jenkins
- CircleCI
- TravisCI

## CI/CD Not Just for Applications

- Infrastructure
- Database Administration
- 3rd Party Artifacts
  - Packages
  - Executables
  - Installable Software

## Tips and Tricks

- Use Pipeline Templates for common code
- For CI speed is key
  - Caching strategy to reuse data from previous build
  - Run jobs in parallel where it makes sense
- Secure pipelines
  - Secrets
  - Permissions

## How to Get Started with CI/CD

- Be creative, think outside the box and marketing materials
- Use on-premise agents if hybrid-cloud
- Store scripts in version control
  - Write scripts > Run scripts > Evaluate test results > Report test results
- Start slow
  - Most companies don't have end to end CI/CD, it takes time
