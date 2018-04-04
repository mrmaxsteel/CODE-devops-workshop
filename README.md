# CODE DevOps Workshop: Clouds, Containers, CI/CD and You!
This workshop will be a mixture of interactive learning and hands-on practical work, so come prepared to get your hands dirty! In this workshop we will:
*	Use Amazon Web Services (AWS) to launch and use compute resources in the Cloud
*	Run a Jenkins Continuous Integration (CI) server as a Docker container on an AWS instance
*	Set up a CI/CD pipeline for a GitHub repository, so you can have automated Build, Test and Deploy, each time you commit!

## This Repository
This repository contains the following:
```
CODE-devops-workshop
├── app
│   └── # Source code for Flask App (https://github.com/plain-vanilla-games/flask-test-kata)
├── doc
│   ├── SECTION-A.md 
│   ├── SECTION-B.md # Contains workshop instructions
│   └── SECTION-C.md 
├── Dockerfile # Source for the Docker container to be built
├── Jenkinsfile # CI/CD Pipeline as Code
└── README.md # This readme
```

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
* This will launch a new window, Hit 'Start Lab' and 'Open Console', to open the AWS console