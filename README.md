# CODE DevOps Workshop: Clouds, Containers, CI/CD and You!
## Summary
This workshop will be a mixture of interactive learning and hands-on practical work, so come prepared to get your hands dirty! In this workshop we will:
* Use Amazon Web Services (AWS) to launch and use compute resources in the Cloud
* Run a Jenkins Continuous Integration (CI) server as a Docker container ([jenkins-code](https://github.com/mrmaxsteel/jenkins-code)) on an AWS instance
* Set up a CI/CD pipeline for a GitHub repository, so you can have automated Build, Test and Deploy, each time you commit
* Practise some TDD on a Python application, and see how it interacts with the CI system 

Prior to the workshop, please complete the [Pre-Work](#pre-work)

## Repository Contents
This repository contains the following:
```
CODE-devops-workshop
├── app
│   └── ... # Source code for Python Flask app 
├── doc
│   ├── SECTION-A.md ─┐
│   ├── SECTION-B.md  ├── # Contains workshop instructions
│   └── SECTION-C.md ─┘
├── Dockerfile # Source for the Docker container to be built
├── Jenkinsfile # CI/CD Pipeline as Code
└── README.md # This readme
```

## Pre-Work
### You will need
* A personal GitHub account
* A laptop with:
   * Git installed (www.git-scm.com/downloads)
   * A text editor of your choice (e.g. [VS Code](https://code.visualstudio.com/))
* An active AWS Educate account (see [Register your AWS Educate Account](#register-your-aws-educate-account))

### Recommended Reading
* Feel free to browse the code of the Python Flask application under the [app](app) directory. Check out the readme located at [app/README.md](app/README.md)
* You can read about Jenkins here: https://jenkins.io/
* You can read about Docker here: https://www.docker.com/what-docker

### Register your AWS Educate Account
*Amazon Web Services (AWS) is a public cloud provider, that we will use to launch preconfigured instances for this workshop*
* Visit https://www.awseducate.com/Registration and register your Student account.
* Log in to AWS Educate account by visiting https://www.awseducate.com, and entering your credentials

To log into the AWS console:
* Log into your AWS educate account, click 'AWS Account' from the menu bar, click "Go to your AWS Educate starter account"
* This will launch a new window. Hit 'Start Lab' and 'Open Console'
