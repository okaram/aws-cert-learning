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

* Skillbuilder [AWS IAM - Architecture and Terminology](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/479/aws-identity-and-access-management-architecture-and-terminology)
* Skillbuilder [Deep Dive with Security - IAM](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/104/deep-dive-with-security-aws-identity-and-access-management-iam)

### AWS global infrastructure (for example, Availability Zones, AWS Regions)
* A Region is a geographical area that contains multiple Availability zones (AZs). Regions are designed to be independent and isolated from each other.
    * An Availability zone is a set of data centers, isolated from other AZs in the region
        * A Data Center is a bunch of computers, with high-speed network connections to other data centers in the AZ
    * A Local Zone is like a smaller AZ, which allows you to put compute closer to your users
    * [More info](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#available-local-zones)

### AWS security best practices (for example, the principle of least privilege)
* [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
    * Require human users to use federation with an identity provider to access AWS using temporary credentials
    * Require workloads to use temporary credentials with IAM roles to access AWS
    * Require multi-factor authentication (MFA)
    * Update access keys when needed for use cases that require long-term credentials
    * Follow best practices to protect your root user credentials
    * Apply least-privilege permissions
    * Get started with AWS managed policies and move toward least-privilege permissions
    * Use IAM Access Analyzer to generate least-privilege policies based on access activity
    * Regularly review and remove unused users, roles, permissions, policies, and credentials
    * Use conditions in IAM policies to further restrict access
    * Verify public and cross-account access to resources with IAM Access Analyzer
    * Use IAM Access Analyzer to validate your IAM policies to ensure secure and functional permissions
    * Establish permissions guardrails across multiple accounts
    * Use permissions boundaries to delegate permissions management within an account

### The AWS shared responsibility model

AWS is responsible for security OF the cloud (vms, network, data centers etc), you're responsible for security IN the cloud (managing access to your resources in the AWS cloud).

***
Skills in
***

### Applying AWS security best practices to IAM users and root users (for example, multi-factor authentication [MFA])
* Don't use the root user to do real work
* Enable MFA for root user, for others too (unless you have other enterprise solutions).


### Designing a flexible authorization model that includes IAM users, groups, roles, and policies
* An **IAM user** represents a user identity, usually associated with a person.
###  Designing a role-based access control strategy (for example, AWS Security Token Service [AWS STS], role switching, cross-account access)
### Designing a security strategy for multiple AWS accounts (for example, AWS Control Tower, service control policies [SCPs])
### Determining the appropriate use of resource policies for AWS services
### Determining when to federate a directory service with IAM roles

## Task Statement 1.2: Design secure workloads and applications.

***
Knowledge of
***
### Application configuration and credentials security
### AWS service endpoints
* An **endpoint** is the URL of the entry point for an AWS web service.
* SDKs automatically use the default one, but you can specify a different one.
* Endpoints can be regional or global, and sometimes FIPS or dual stack.
* Private link enables you to create VPC endpoints, which would create different DNS names and private IP addresses for the services.
### Control ports, protocols, and network traffic on AWS

* Skillbuilder [AWS Networking basics](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/12439/aws-networking-basics)
* Skillbuilder [AWS Security best practices - Network Infrastructure](https://explore.skillbuilder.aws/learn/course/internal/view/elearning/11218/aws-security-best-practices-network-infrastructure)

### Secure application access Security services with appropriate use cases (for example, Amazon Cognito, Amazon GuardDuty, Amazon Macie)
### Threat vectors external to AWS (for example, DDoS, SQL injection)

***
Skills in
***

### Designing VPC architectures with security components (for example, security groups, route tables, network ACLs, NAT gateways)
### Determining network segmentation strategies (for example, using public subnets and private subnets)
### Integrating AWS services to secure applications (for example, AWS Shield, AWS WAF, IAM Identity Center, AWS Secrets Manager)
### Securing external network connections to and from the AWS Cloud (forexample, VPN, AWS Direct Connect)

## Task Statement 1.3: Determine appropriate data security controls.

***
Knowledge of
***
### Data access and governance
### Data recovery
### Data retention and classification
### Encryption and appropriate key management

***
Skills in
***
### Aligning AWS technologies to meet compliance requirements
### Encrypting data at rest (for example, AWS Key Management Service [AWS KMS])
### Encrypting data in transit (for example, AWS Certificate Manager [ACM] using TLS)
### Implementing access policies for encryption keys
### Implementing data backups and replications
### Implementing policies for data access, lifecycle, and protection
### Rotating encryption keys and renewing certificates