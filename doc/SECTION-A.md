# Workshop
## Section A: Stand up a Dockerized Jenkins Master in AWS
### Step A.1: Launch your pre-configured Docker Host
* Log onto the AWS Console, go to Services > EC2
* Select 'Launch Instance'
* Under 'My AMIs', search for AMI id "ami-45c7593d" and select it
* Choose t2.micro instance type, then 'Configure Instance Details'.
* Accept the defaults for 'Configure Instance Details' and 'Add Storage'
* Then, add a tag with Key="Name" and Value="devops-\<your-initials\>"
* Check 'Select an existing security group', and choose "devops-workshop" (sg-feab4080) from the list, notice the 3 ports we have open
* Click 'Review and Launch', and then 'Launch' 
* Choose keypair called "devops-workshop" and then 'Launch Instances', taking note of the Public DNS Name of the instance

### Step A.2: Connect to the Docker Host using SSH
* Download the SSH key called devops-workshop.pem
* From a Git Bash, SSH to instance with:
```
$ ssh ubuntu@<PUBLIC_DNS_NAME> -i /path/to/devops-workshop.pem
```

### Step A.3: Run a Jenkins CI container
* From an SSH terminal on the AWS Docker Host, run:
```
$ docker container run \
   --mount type=volume,source=jenkins-data,destination="/var/jenkins_home",volume-driver=local \
   -v /var/run/docker.sock:/var/run/docker.sock \
   -p 8080:8080 \
   --name jenkins -d \
   maxsteel/jenkins-code:latest
```
* Test that Jenkins has started by visiting http://<PUBLIC_DNS_NAME>:8080/