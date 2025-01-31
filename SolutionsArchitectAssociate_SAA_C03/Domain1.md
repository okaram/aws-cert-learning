# Domain 1: Design Secure Architectures
## Task Statement 1.1: Design secure access to AWS resources.

***
Knowledge of
*** 

### Access controls and management across multiple accounts
* IAM
* federated accounts
* Organizations, policies etc

### AWS federated access and identity services (for example, AWS Identity and Access Management [IAM], AWS IAM Identity Center [AWS Single Sign-On])

### AWS global infrastructure (for example, Availability Zones, AWS Regions)
* A Region is a geographical area that contains multiple Availability zones (AZs). Regions are designed to be independent and isolated from each other.
    * An Availability zone is a set of data centers, isolated from other AZs in the region
        * A Data Center is a bunch of computers, with high-speed network connections to other data centers in the AZ
    * A Local Zone is like a smaller AZ, which allows you to put compute closer to your users
    * [More info](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#available-local-zones)

### AWS security best practices (for example, the principle of least privilege)
### The AWS shared responsibility model

AWS is responsible for security OF the cloud (vms, network, data centers etc), you're responsible for security IN the cloud (managing access to your resources in the AWS cloud).

***
Skills in
***

### Applying AWS security best practices to IAM users and root users (for example, multi-factor authentication [MFA])
### Designing a flexible authorization model that includes IAM users, groups, roles, and policies
###  Designing a role-based access control strategy (for example, AWS Security Token Service [AWS STS], role switching, cross-account access)
### Designing a security strategy for multiple AWS accounts (for example, AWS Control Tower, service control policies [SCPs])
### Determining the appropriate use of resource policies for AWS services
### Determining when to federate a directory service with IAM roles
