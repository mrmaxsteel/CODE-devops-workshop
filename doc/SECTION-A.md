# Workshop
## Section A: Stand up a Dockerized Jenkins Master in AWS
### Step A.1: Launch a CentOS server
* Log onto the AWS Console, go to Services > EC2
* Select 'Launch Instance'
* Under 'AWS Marketplace', search for 'centos' and select CentOS 7 (x86_64) - with Updates HVM
* Choose t2.micro instance type (it should say "free tier eligible"), then 'Configure Instance Details'.
* Accept the defaults for 'Configure Instance Details' and then 'Add Storage'
* Accept the defaults for 'Add Storage' and then 'Add Tags'
* Then, add a tag with Key="Name" and Value="devops-\<your-initials\>" and then 'Configure Security Groups'
* Ensure a rule exists for SSH over port 22, then select 'Add Rule' to add the following:
   * Custom TCP Rule - TCP - 8080 - Custom 0.0.0.0/0, ::/0 - Description: Web UI for Jenkins
   * Custom TCP Rule - TCP - 5000 - Custom 0.0.0.0/0, ::/0 - Description: Web UI for Python App
* Click 'Review and Launch', and then 'Launch' 
* Select 'Create a new key pair', name it devops-code and then 'Download Key Pair' and copy to ~/.ssh/ec2_keys
* Select 'Launch Instances', then click on the instance ID. From the Description pane, take not of the Public DNS name

### Step A.2: Connect to the Docker Host using SSH
* Download the SSH key called devops-workshop.pem
* From a Git Bash (Windows) or terminal (Mac), SSH to instance with:
```
$ ssh centos@<PUBLIC_DNS_NAME> -i /path/to/devops-code.pem
```
(you may need to change permissions of your .pem key using `chmod 600 devops-code.pem`)

### Step A.3: Install Docker-CE
* Follow https://docs.docker.com/install/linux/docker-ce/centos/#install-using-the-repository to install Docker CE, skipping the Optional step to enable edge and test repos.
* Run the following commands to allow the centos user to run docker commands without sudo and jenkins to connect to the docker socket:
```
$ sudo usermod -aG docker centos
$ sudo useradd jenkins
$ sudo usermod -aG docker jenkins
$ sudo chmod 777 /var/run/docker.sock
```

### Step A.4: Run a Jenkins CI container
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
