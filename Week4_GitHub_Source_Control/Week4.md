# Week 4: GitHub and Source Control

## Course Outline

- Lecture: Overview Git, GitHub, why?
- Projects:
  **ADD THESE**

## Why Source Control?

- Track and manage changes to code
- Track and manage changes to code
  - Only people with access to repo can change the code
- Source of truth

## Protect the Code

- Easy to lose code that is only stored locally
- Rollbacks (go back to previous version if needed)
- Code reviews (make sure production code is done properly)
  - Source control allows for code review
- Pull requests (code can be reviewed than merged to the main branch, build on the code that is already there)

## Version Control

- Used interchangeably with source control but very different
- Manages a version of the code (different versions can live within source control)
- Allows for comparisons and diffs (can see what was added in new versions compared to version 1)
  - Helps understand why something was changed

## Source Control Best Practices

- Don't commit passwords/secrets!
- Write good commit messages
- Branching best practices
- Commit often
- Test before committing

## Git Branching

- Should be able to tell what's happening in production just by looking at the main branch
- Develop branch is what is about to go into production (like a staging area)
  - Features and changes that have been tested are on the develop branch and waiting for review from the team before being merged to master
- Feature branches are used for changes in progress than merged to develop branch
  - Nothing can be merged directly to master other than develop branch once it has been fully reviewed
  - Can be many feature branches for work in progress (new feature, bug fixes, etc.)
  - Develop branch is like a shield for the master branch

## Centralized Version Control

- One server
  - One branch has ALL versions of the code, everyone interacts directly with that
  - If there are no backups all code can be lost if the server crashes
- Everyone uses the code from one server
  - No chance to collaborate while working
- Need internet to work
- Single point of failure

## Distributed Version Control

- Most popular today (past 5-7 years)
- Create multiple branches, pull requests, and collaborate
- Don't need network connectivity
  - Everyone has a copy of the whole codebase on their own machine, they can work locally and not affect the whole codebase if there is a problem locally like a computer crash (this is a problem for centralized version control)
- Much faster, no need to communicate with main server while working, can work locally then commit (be sure to commit often)
