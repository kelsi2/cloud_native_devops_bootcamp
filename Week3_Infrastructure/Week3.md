# Week 3: Infrastructure as Code

## Course Outline

**Lecture**: Theory of Infrastructure as Code
**Projects**:

- Deploy VM with ARM in Azure
- Build a Terraform Module to deploy EC2 in AWS
- Write a Test for the Terraform Module using Terratest
- Intro to Azure Bicep

## Infrastructure as Code

- Defining infrastructure with code and managing it like a software developer
- DevOps Culture: IaC supports effort to bridge gaps and improve collaboration

## New Way of Thinking

- Considerably less effort to deploy an environment
- Environment defined in code which means software development tools like linting and source control can be applied to infrastructure
- Benefits of IaC:
  - Reduce risk of change
  - Faster iteration
  - More reliable systems
  - Faster DR
  - Improved speed of troubleshooting
  - Governance and security

## Self Service Infrastructure

- Don't need to wait for servers to be set up, infrastructure can be created as a standalone
- Build First, Automate Later
  - Can easily fix issues and build tests as you go

## Core Practices of IaC

- Define everything as code
  - Reusability
  - Consistency
  - Transparency
- Validate and Test
- Small simple pieces that can change independently
  - This makes testing easier and we can manage and understand the pieces individually

## ARM/CloudFormation or Terraform?

- ARM = IaC for Azure
- AWS = IaC for AWS
- Terraform = IaC for EVERYTHING!
- Terraform concerns:
  - Will I get less functionality?
    - No, sometimes it's even more up to date than others and you can use ARM for example with Terraform
  - Will it cost me too much?
    - Free and open source, only pay for support
  - I only use one cloud right now
    - Even if you don't plan to use both it will often happen anyway so good to start with Terraform regardless

## Pulumi vs. Terraform

- Pulumi:
  - Use programming languages like Python and JS to manage infrastructure
  - Harder to transition to from System Engineering role because it's more like programming
  - Better high level abstraction
- Terraform
  - Uses own language called HashiCorp Configuration Language
  - Easier to understand and learn for most non-programmers
  - Functional limitations, relies on tools like Terragrunt for high level abstraction and functionality

## Types of Tests

- Static Analysis - Testing code without running it
- Unit Testing - Testing a single unit
- Integration Testing - Testing functionality between two or more units
- End-to-End Testing - Testing entire application infrastructure from the ground up
  - Get more expensive, cost more time, and have more failures from top to bottom

## Where do I start?

- Automate one thing at a time, start slow
  - IaC for new environment or application first
  - Automate most tedious processes first like server build
  * DevOps is all about making small changes then testing before moving on, not everything at once
- BEWARE: If you try to do everything at once you will most likely have to redo it

## Setting up ARM template

- Built in json (see template.json)
- Can just type arm! for default template
