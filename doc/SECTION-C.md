# Workshop
## Section C: 
### Step C.1: Create a Pull Request
* Clone your forked repository to your workstation
* Create and checkout a new branch:
```
$ cd <repo>
$ git checkout -b feature/test-cases
```
* Make a trivial change, for example, in README.md, and then create a Pull Request to merge to master
  **N.B: MAKE SURE** the Pull Request is created to merge your feature branch to master branch of **your fork**, not the master branch of the original repo
  
* In the pull request screen in GitHub, notice a build get kicked off in Jenkins

### Step C.2: Setup Branch Protection
* In your fork in GitHub, go to Settings > Branches
* Under 'Branch Protection Rules', click 'Add Rule':
  * Apply rule to: 'master'
  * Check 'Require status checks to pass before merging'
    * Check `continuous-integration/jenkins/pr-merge`
  * Click 'Create'
