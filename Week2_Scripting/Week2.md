# Week 2: Scripting Like a Developer

## Course Outline

**Lecture**: Core developer theory for DevOps and how to code like a developer
**Projects**:

- Setting up a dev environment
- Reusable and clean Python code
- Reusable and clean PowerShell code
- Linting in PowerShell and Python
- Testing in PowerShell and Python
- Documenting code

## Developer Theory

- Immutable
  - You can't change it (Terraform)
    - Objects and arrays
- Mutable

  - Change the code and the environment stays the same (Ansible)
    - Strings and numbers

- Declarative
  - Tell me what to do, not how to do it (Terraform, CloudFormation, Go)
  - Describe the outcome
  - System is smart and will figure it out
- Imperative

  - Tell me how to do it (Java, C#, C++)
  - Explicit instructions
  - System is stupid, you are smart
    **Python is declarative AND imperative**

- Procedural programming
  - A set of steps
  - Imperative
- Object Oriented Programming (OOP)
  - Defining classes, objects of those classes, and methods
  - Imperative AND declarative
- Functional programming

  - Like a mathematical function
  - Declarative

- Idempotence

  - Make the same call without the result changing (going to google.com will always result in the same page showing up)
  - Making multiple, identical requests has the same effect as a single request
  - Performing an operation again gives the same result
  - GET, HEAD, PUT, and DELETE are idempotent
    - POST and PATCH are not
    * DELETE is iffy...if we have already deleted an item it is no longer there so in that regard it is not idempotent, however, no matter how many times we try to delete it after the first time the result will always be the same (204)

- Unit testing
  - Test a specific component or functionality
  * Does it do what it's supposed to do?

* Mock Tests
  - Extension of or approach to unit tests, allows you to make assertions (a confirmation [is it a string, does this value equal what it should])

- Regression testing
  - Does a new feature have an impact on existing features? Does it break something?

* Linting
  - Check syntax for spacing and formatting errors
