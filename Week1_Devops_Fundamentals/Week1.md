# Week 1: DevOps Fundamental Skills

## Course Outline

**Lecture**: Overview of predictions and core DevOps skills
**Projects**:

- Getting started with GitHub
- Setting up first Azure environment
- Setting up first AWS environment
- Setting up projects in GitHub
- Setting up first GitHub Action

## Cloud Computing

- Using Microsoft of Amazon resources
  - Hundreds of data centers around the world for you to interact with (like an application)
- Renting (using services you don't own, you don't need to have your own server)
- Scalability at ease
- Quick deployments
  - Don't need to worry about all the server setup, can deploy hundreds of virtual machines at once

## Collaboration

- Communication
- Working together
  - If one person is off even a bit or not working with the team everything can fall apart in DevOps, you aren't working alone
- Working with management
  - Management and engineering need to be on the same page
- Working with other teams

  - Any other tech teams are all working together

- DevOps engineers need to be aware of the goals and be able to say no to management and know what's best for the team, management and engineers, and the business
  - Make sure goals are communicated and everyone is on the same page

## Major DevOps Tooling

- Coding and development practices
  - Don't need to know everything!
  - Tools are constantly changing
- Orchestration (Kubernetes)
- Containerization (Docker, containerd, CRI-O)
- Monitoring
- Cloud
  - Serverless means you are not the one managing the server! There is still a server
  - AWS and Azure are focus, but there is also Google Cloud
- CI/CD
- Infrastructure-as-code

## Security Skills

- Static code analysis: linters can test from security perspective
- Unit tests: Confirms code is doing what it's supposed to be doing
- Performance tests: Benchmark testing (speed of running or deploying)
- Vulnerability tests: Passwords or security issues
  - These tests are in the CI/CD pipeline so before deploying tests should always be run

## Command-Line (CLI)

- Command-line wizardry
  - Important to be able to do things quickly without opening a browser or using UI
- Most popular for cloud:
  - Azure CLI
  - AWS CLI
- CLI tool is a middle-man to API (use this to interact with section of UI instead of loading and logging into the service)
- Using the CLI

## Version/Source Control

- Place to store code
- Version control == manage versions
  - Think GitHub, we have multiple versions of the code stored virtually
- Collaboration
  - Everyone needs to be able to work on the code and see what is going on
- Less bugs
  - More eyes on the code the less chance of bugs in production
- Everyone is aware (code is public)

### Centralized Version Control

- One server
- Everyone uses the code from one server
- Very hard to collaborate (results in a lot of conflicts because everyone has local copies)
- Still very common in banks and large code bases like Windows

### Distributed Version Control

- Create multiple branches, pull requests and collaborate
  - Removes the problem of having one person accessing the code at one time, everyone can pull their own updated version (a local repo)
- Most popular today

## CI/CD

- Continuous Integration/Continuous Deployment or Delivery
  - Continuous Delivery: Allows you to automatically deploy code daily, weekly, hourly, etc.
    - Click a button or set a schedule to deploy
  - Continuous Deployment: Auto-deploy
    - Runs each time the code is committed
- Build, test, and create artifact out of code to be used in deployment
- Deploy code with button click or as code is committed to a repo

## Books

- Read these in order:
  - The Phoenix Project
  - The DevOps Handbook
  - Accelerate
