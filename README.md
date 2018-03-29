# CODE DevOps Workshop: Clouds, Containers, CI/CD and You!
This workshop will be a mixture of interactive learning and hands-on practical work, so come prepared to get your hands dirty! In this workshop we will:
*	Use Amazon Web Services (AWS) to launch and use compute resources in the Cloud
*	Run a Jenkins Continuous Integration (CI) server as a Docker container on an AWS instance
*	Set up a CI/CD pipeline for a GitHub repository, so you can have automated Build, Test and Deploy, each time you commit!

Hopefully, you will come away knowing more about public clouds and why they are being used more and more in industry. You will be introduced to containers, and learn a bit about why they are the hottest topic in tech at the moment. And you will have a better understanding of Continuous Integration/Continuous Deployment (CI/CD), and how it can really help accelerate time to market and improve software quality. 

Finally, and perhaps most practically, you will leave knowing everything you need to know to easily set up your own end-to-end DevOps pipeline, so you can hit the ground running on your next software project! 

## Pre-work
What you will need:
* A personal GitHub account
* A laptop with:
   * Git installed (www.git-scm.com/downloads)
   * A text editor of your choice (e.g. VS Code)
* An active AWS Educate account

### Register your AWS Educate Account
*Amazon Web Services (AWS) is a public cloud provider, that we will use to launch preconfigured instances for this workshop*
* Visit https://www.awseducate.com/Registration and register your Student account.
* Log in to AWS Educate account, click 'AWS Account' from the menu bar, click "Go to your AWS Educate starter account"
* This will launch a new window, with the AWS console

## Workshop
### Step 1: Launch your preconfigured Docker Host
* Log onto the AWS Console, go to Services > EC2
* Select "Launch Instance"
* Search for AMI id "ami-45c7593d", choose keypair called "devops-workshop" and security group called "devops-workshop"
* Launch the instance, take note of the public DNS of the instance

### Step 2: Connect to the instance using SSH
* Download the SSH key called devops-workshop.pem
* From a Git Bash, SSH to instance with:
```
ssh ubuntu@<PUBLIC_DNS> -i /path/to/devops-workshop.pem
```

### Step 3: Run a Jenkins CI container
* Run following:
```
docker container run \
   --mount type=volume,source=jenkins-data,destination="/var/jenkins_home",volume-driver=local \
   -v /var/run/docker.sock:/var/run/docker.sock \
   -p 8080:8080 \
   --name jenkins -d \
   maxsteel/jenkins-code:latest
```
### Step 4: Cofigure Security
### Step 5: Configure WebHooks
* Create a GitHub Personal Access Token: 
  * Go to https://github.com/settings/tokens and 'Generate New Token'
  * Call the token something like "Jenkins"
  * Select the following scopes: repo, admin:repo_hook, user
  * Click "Generate Token", copy the token and keep it safe
* On the Jenkins UI > Credentials
* Under Domains, click "(global)"
* Add Crendential:
  * Kind: Username with Password
  * Scope: Global
  * Username: <your GitHub username>
  * Password: <PAToken generated above>
  * ID: GITHUB_PATOKEN_USERPASS
  * Description: GITHUB_PATOKEN_USERPASS
* Add a second Crendential:
  * Kind: Secret Text
  * Scope: Global
  * Secret: <PAToken generated above>
  * ID: GITHUB_PATOKEN_SECRET
  * Description: GITHUB_PATOKEN_SECRET
* Go to Jenkins > Manage Jenkins > Configure System
* Scroll down to GitHub, under GitHub Servers, select GITHUB_PATOKEN_SECRET from the Credentials drop-down
* Check 'Manage Hooks'
* Test Connection
  
## Other Stuff
### Pseudocode
* Introduce App
* Show Dockerfile
* Show Jenkinsfile
    * Build
    * Test
    * Deploy (docker service update)
* Start AMI in AWS with Docker installed
* ssh to Instance and start jenkins service
* Log into Jenkins UI
* Add github repo
* Do initial build on master
* Make a code change on a new branch with TDD, submit a pull request, view build & test
* Merge PR, view build, test & deploy

### AMI config
* Install docker-ce
* usermod -aG docker ubuntu

### AWS IAM Profile permissions
* Create Key Pair
* Create Security Group
* Create AMI
* Create/launch/delete Instance
* Create/launch/delete ELB
