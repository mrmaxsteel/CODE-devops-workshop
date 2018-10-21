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
  * Check 'Require pull request reviews before merging'
  * Check 'Require status checks to pass before merging'
    * Check `continuous-integration/jenkins/pr-merge`
  * Click 'Create'

### Step C.3: Implement Calculator Multiplication logic using TDD and CI
* In your GitHub fork, create a new branch called `feature/multiplication`
* Complete task 1 of the Unit Test section in the readme located at 'app/README.md' in your feature branch, push to GitHub, and open a Pull Request to master.
  **N.B: MAKE SURE** the Pull Request is created to merge your feature branch to master branch of **your fork**, not the master branch of the original repo
* Complete tasks 2-4 using the Continuous Integration builds to validate your tests
* Once you are happy with your work, assign a friend to review the Pull Request. Once the PR is approved go ahead and merge it to master
* Notice the CI build redeploy your application. Try testing the mul logic by appending `/calc/92*100` to the url.

### Step C.4: Implement Division logic using TDD and local Dockerised builds
* Create a new branch called `feature/division`
* Complete tasks 5-6 through dockerised builds on your local workstation and using TDD. Remember to commit often.
* Once you are happy with your work, push to GitHub and create a PR to master. Again ask a friend to review and then merge.
* Test the division logic through the UI on the production application.

### Step C.5: Implment the Integration Tests
* Complete the Integration Test section of the readme located at 'app/README.md' using what you have learnt in this kata.

