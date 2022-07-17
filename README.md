# B-Safe. - Project 3 

## DESCRIPTION

Create a CI/CD Pipeline to convert the legacy development process to a DevOps
process.

### Background of the problem statement:

A leading US healthcare company, __Aetna__, with a large IT structure had a
12-week release cycle and their business was impacted due to the legacy
process. To gain true business value through faster feature releases, better
service quality, and cost optimization, they wanted to adopt agility in their
build and release process. The objective is to implement iterative
deployments, continuous innovation, and automated testing through the
assistance of the strategy.

### Implementation requirements:

1. Install and configure the Jenkins architecture on AWS instance
1. Use the required plugins to run the build creation on a containerized
    platform
1. Create and run the Docker image which will have the application artifacts
1. Execute the automated tests on the created build
1. Create your private repository and push the Docker image into the
    repository
1. Expose the application on the respective ports so that the user can access
    the deployed application
1. Remove container stack after completing the job

### The following tools must be used:

1. EC2
1. Jenkins
1. Docker
1. Git

### The following things to be kept in check:

1. You need to document the steps and write the algorithms in them.
1. The submission of your Github repository link is mandatory. In order to
    track your tasks, you need to share the link of the repository.
1. Document the step-by-step process starting from creating test cases, the
    executing it, and recording the results.
1. You need to submit the final specification document, which includes:
    - Project and tester details
    - Concepts used in the project
    - Links to the GitHub repository to verify the project completion
    - Your conclusion on enhancing the application and defining the USPs
        (Unique Selling Points)

## Solution

### Setup Github

- [Create course-3-project-5 repo](https://github.com/davidmargolis/course-3-project-5) in Github
- [Generate personal access token](https://github.com/settings/tokens/new) for integrating jenkins

### Setup Jenkins in AWS Practice Lab

1. Open and start [practice labs](https://caltech.lms.simplilearn.com/courses/4041/-PG-DO---CI%2FCD-Pipeline-with-Jenkins/practice-labs)
1. Open [aws](https://us-east-1.console.aws.amazon.com/console/home?region=us-east-1#)
1. Create AWS Architecture
    1. [Create key pair](https://us-east-1.console.aws.amazon.com/ec2/v2/home?region=us-east-1#CreateKeyPair:):
        - name - `jenkins_on_ec2`
        - Private key file format - `pem`
    1. [Create security group](https://us-east-1.console.aws.amazon.com/ec2/v2/home?region=us-east-1#CreateSecurityGroup:):
        - Security group name - `WebServerSG`
        - Description - `Jenkins`
        - Add Inbound Rules:
            - Rule 1:
                - Type - `SSH`
                - Source - `My IP`
            - Rule 2:
                - Type - `HTTP`
                - Source - `Anywhere-IPv4`
            - Rule 3:
                - Type - `Custom TCP`
                - Port range - `8080`
                - Source - `Anywhere-IPv4`
            - Rule 4:
                - Type - `Custom TCP`
                - Port range - `5000`
                - Source - `Anywhere-IPv4`
        - Click `Save rules`
    1. [Create ec2 instance](https://us-east-1.console.aws.amazon.com/ec2/v2/home?region=us-east-1#LaunchInstances:):
        - Instance type pair name - `jenkins_on_ec2`
        - Key pair name - `jenkins_on_ec2`
        - Select <input type=radio checked> `existing security group`
        - Common security groups Info - `WebServerSG`
1. Install Jenkins in EC2 instance
    1. Shell into ec2:
        ```
        mv /mnt/c/Users/david/Downloads/jenkins_on_ec2.pem ~/.ssh \
        && chmod 400 ~/.ssh/jenkins_on_ec2.pem \
        && ssh -i ~/.ssh/jenkins_on_ec2.pem ec2-user@ec2-54-165-149-225.compute-1.amazonaws.com
        ```
    1. Install docker, git, java 11, and jenkins on EC2
        ```
        sudo yum update –y \
            && sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo \
            && sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io.key \
            && sudo amazon-linux-extras install docker java-openjdk11 -y \
            && sudo yum install git jenkins maven -y \
            && sudo systemctl enable jenkins \
            && sudo systemctl start jenkins \
            && sudo systemctl status jenkins
        ```
    1. Get jenkins password:
        ```
        cat /var/lib/jenkins/secrets/initialAdminPassword
        ```
1. Configure Jenkins
    1. Log into Jenkins <http://ec2-54-165-149-225.compute-1.amazonaws.com:8080/> using password revealed from the last step
    1. Choose `Install standard plugins`
    1. Add [Docker plugin](https://plugins.jenkins.io/docker-plugin/) and [Docker Pipeline plugin](https://plugins.jenkins.io/docker-workflow/)
    1. Add GitHub Server
        1. [Configure System](http://ec2-54-165-149-225.compute-1.amazonaws.com:8080/configure)
        1. Click `Add GitHub Server` -> `GitHub Server`
        1. Click `Save`
    1. Expand access
        1. [Configure Global Security](http://ec2-54-165-149-225.compute-1.amazonaws.com:8080/configureSecurity/)
        1. Choose `Authorization` - `Anyone can do anything`
        1. Click `Save`
    1. [Create new job](http://ec2-54-165-149-225.compute-1.amazonaws.com:8080/view/all/newJob)
        1. `Enter an item name` - `course-5-project-3`
        1. Select `Pipeline`
        1. Click `OK`
        1. Check <input type="checkbox" checked> `Discard old builds`
        1. Check <input type="checkbox" checked> `GitHub project`
        1. `Project url` - <https://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@github.com/davidmargolis/course-5-project-3.git>
        1. Check <input type="checkbox" checked> `GitHub hook trigger for GITScm polling`
            1. `Definition` - `Pipeline script from SCM`
            1. `SCM` - `Git`
            1. `Repository URL` - <https://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@github.com/davidmargolis/course-5-project-3.git>
        1. Click `Save`
    1. [Add webhook](https://github.com/davidmargolis/course-5-project-3/settings/hooks/new) in GitHub:
        1. `Payload URL` - <http://ec2-54-165-149-225.compute-1.amazonaws.com:8080/github-webhook/>
        1. `Content type` - `application/type`

### Run Jenkins Pipeline

1. Push a change to git repo to trigger pipeline
1. See pipeline is run automatically <http://ec2-54-165-149-225.compute-1.amazonaws.com:8080/job/course-5-project-3/>
1. See tomcat server is deployed <http://ec2-54-165-149-225.compute-1.amazonaws.com:8081/course-5-project-3/>
