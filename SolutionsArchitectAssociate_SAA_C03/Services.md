# Services

The following services are in-scope.

## [Analytics](https://aws.amazon.com/big-data/datalakes-and-analytics/)

* **[Amazon Athena](https://aws.amazon.com/athena/)** - Serverless, interactive analytics service built on open-source frameworks, supporting open-table and file formats. SQL on S3 :)
    * Skillbuilder - [Intro to Amazon Athena](https://explore.skillbuilder.aws/learn/course/external/view/elearning/152/introduction-to-amazon-athena)
    * [Cheatsheet (TD)](https://tutorialsdojo.com/amazon-athena/)

* **[AWS Data Exchange](https://aws.amazon.com/data-exchange/)** - Find, subscribe to, and use third party data in the AWS Cloud.

* **[AWS Data Pipeline](https://aws.amazon.com/what-is/data-pipeline/)** DEPRECATED - Data pipeline service. Use Glue/Step functions, or managed workflows for Airflow

* **[Amazon EMR](https://aws.amazon.com/emr/)** - Easily run and scale Apache Spark, Hive, Presto, and other big data workloads. 
    * Skill Builder - [Getting Started with Amazon EMR](https://explore.skillbuilder.aws/learn/course/external/view/elearning/8827/getting-started-with-amazon-emr)
    * [Cheatsheet (TD)](https://tutorialsdojo.com/amazon-EMR/)

* **[AWS Glue](https://aws.amazon.com/glue/)** - Discover, prepare, and integrate all your data at any scale.
    * Skillbuilder - [Getting Started with AWS Glue](https://explore.skillbuilder.aws/learn/course/external/view/elearning/8171/getting-started-with-aws-glue)
    * [Cheatsheet (TD)](https://tutorialsdojo.com/aws-glue/)

* **[Amazon Kinesis](https://aws.amazon.com/kinesis/)** - Collect, process, and analyze real-time video and data streams.
    * [Cheatsheet (TD)](https://tutorialsdojo.com/amazon-kinesis/)
    * **Amazon Kinesis Data Analytics** -
    * **Amazon Kinesis Data Firehose** -
    * **Amazon Kinesis Data Streams** -

* AWS Lake Formation
* Amazon Managed Streaming for Apache Kafka (Amazon MSK)
* Amazon OpenSearch Service
* Amazon QuickSight
* Amazon Redshift

## Application Integration

* [Amazon AppFlow](https://aws.amazon.com/appflow/)
    * [Cheatsheet (TD)](https://tutorialsdojo.com/amazon-appflow/)

* [AWS AppSync](https://aws.amazon.com/appsync/) - GraphQL API service for connecting events, data and applications. API Gateway for GraphQL?

* Amazon EventBridge
* Amazon MQ
* Amazon Simple Notification Service (Amazon SNS)
* Amazon Simple Queue Service (Amazon SQS)
* AWS Step Functions

## AWS Cost Management:
* AWS Budgets
* AWS Cost and Usage Report
* AWS Cost Explorer
* Savings Plans

## Compute:
* [AWS Batch](https://aws.amazon.com/batch/) - Batch processing (lambda but for batches :)
* [Amazon EC2](https://aws.amazon.com/ec2/) - Virtual machines in the cloud, plus magic.
* [Amazon EC2 Auto Scaling](https://aws.amazon.com/autoscaling/) - Automatically add or remove EC2 instances.
* AWS Elastic Beanstalk
* AWS Outposts
* AWS Serverless Application Repository
* VMware Cloud on AWS
* AWS Wavelength

## Containers:
* Amazon ECS Anywhere
* Amazon EKS Anywhere
* Amazon EKS Distro
* Amazon Elastic Container Registry (Amazon ECR)
* Amazon Elastic Container Service (Amazon ECS)
* Amazon Elastic Kubernetes Service (Amazon EKS)

## Database:
* Amazon Aurora
* Amazon Aurora Serverless
* Amazon DocumentDB (with MongoDB compatibility)
* Amazon DynamoDB
* Amazon ElastiCache
* Amazon Keyspaces (for Apache Cassandra)
* Amazon Neptune
* Amazon Quantum Ledger Database (Amazon QLDB)
* Amazon RDS
* Amazon Redshift

## Developer Tools
* AWS X-Ray

## Front-End Web and Mobile:
* AWS Amplify
* Amazon API Gateway
* AWS Device Farm
* Amazon Pinpoint

## Machine Learning
* Amazon Comprehend
* Amazon Forecast
* Amazon Fraud Detector
* Amazon Kendra
* Amazon Lex
* Amazon Polly
* Amazon Rekognition
* Amazon SageMaker
* Amazon Textract
* Amazon Transcribe
* Amazon Translate

## Management and Governance:
* AWS Auto Scaling
* AWS CloudFormation
* AWS CloudTrail
* Amazon CloudWatch
* AWS Command Line Interface (AWS CLI)
* AWS Compute Optimizer
* AWS Config
* AWS Control Tower
* AWS Health Dashboard
* AWS License Manager
* Amazon Managed Grafana
* Amazon Managed Service for Prometheus
* AWS Management Console
* AWS Organizations
* AWS Proton
* AWS Service Catalog
* AWS Systems Manager
* AWS Trusted Advisor
* AWS Well-Architected Tool

## Media Services
* Amazon Elastic Transcoder
* Amazon Kinesis Video Streams

## Migration and Transfer
* AWS Application Discovery Service
* AWS Application Migration Service
* AWS Database Migration Service (AWS DMS)
* AWS DataSync
* AWS Migration Hub
* AWS Snow Family
* AWS Transfer Family

## Networking and Content Delivery
* AWS Client VPN
* Amazon CloudFront
* AWS Direct Connect
* Elastic Load Balancing (ELB)
* AWS Global Accelerator
* AWS PrivateLink
* Amazon Route 53
* AWS Site-to-Site VPN
* AWS Transit Gateway
* Amazon VPC
    * An *elastic network interface*, **EIN** is a logical networking component in a VPC that represents a virtual network card. 


## Security, Identity, and Compliance:
* AWS Artifact
* AWS Audit Manager
* AWS Certificate Manager (ACM)
* AWS CloudHSM
* Amazon Cognito
* Amazon Detective
* AWS Directory Service
* AWS Firewall Manager
* Amazon GuardDuty
* AWS IAM Identity Center (AWS Single Sign-On)
* AWS Identity and Access Management (IAM)
* Amazon Inspector
* AWS Key Management Service (AWS KMS)
* Amazon Macie
* AWS Network Firewall
* AWS Resource Access Manager (AWS RAM)
* AWS Secrets Manager
* AWS Security Hub
* AWS Shield
* AWS WAF

## Serverless
* AWS AppSync
* AWS Fargate
* AWS Lambda

## Storage:
* AWS Backup
* [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/) - Elastic Block storage. NAS-like block storage for EC2 instances
* [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/) - Elastic NFS file system
* [Amazon FSx](https://aws.amazon.com/fsx/) - Umbrella for several specialized file systems
* [Amazon S3](https://aws.amazon.com/s3/)
    * [Cheatsheet (TD)](https://tutorialsdojo.com/amazon-s3/)
    * [Storage classes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/storage-class-intro.html)
        * Frequent access
            * S3 Standard - fast, 3 copies, multi-az
            * S3 Express one zone - single-digit milisecond access, ONE AZ.
            * Reduced redundancy storage - less redundancy, NOT RECOMMENDED
        * Infrequent - Cheaper storage, almost as fast, charges for retrieval, minimum 128k
            * S3 Standard IA
            * S3 One-Zone IA
        * Rarely access/Archive - Low storage cost, slow retrieval, minimum size(128k(/duration(90 days), 
            * S3 Glacier Instant Retrieval - milliseconds
            * S3 Glacier Flexible Retrieval - Up to 12 hours
            * S3 Glacier Deep Archive - Up to 48 hours
        * Automatic
            * S3 Inteligent-Tiering
                * Moves between
                    * Frequent access (standard)
                    * Infrequent access
                    * Archive instant access
                    * Archive (optional)
                    * Deep Archive (optional) 


* Amazon S3 Glacier
* AWS Storage Gateway