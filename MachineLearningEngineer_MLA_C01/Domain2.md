# Domain 2: Design Resilient Architectures

* Scale **in** - detach and terminate instances.
* Scale **out** - create and attach instances.
* [Autoscaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html) 

* [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#bp-users-federation-idp)

## Task Statement 2.1: Design scalable and loosely coupled architectures.

***
Knowledge of
***

### API creation and management (for example, Amazon API Gateway, REST API)
### AWS managed services with appropriate use cases (for example, AWS Transfer Family, Amazon Simple Queue Service [Amazon SQS], Secrets Manager)
### Caching strategies
* [Caching](https://aws.amazon.com/caching/) and [Best Practices](https://aws.amazon.com/caching/best-practices/)

### Design principles for microservices (for example, stateless workloads compared with stateful workloads)
### Event-driven architectures
* [What is an Event-Driven architecture](https://aws.amazon.com/event-driven-architecture/)

### Horizontal scaling and vertical scaling
* **Horizontal** scaling involves adding more processing nodes; *more machines*.
* **Vertical** scaling involves adding memory or processing power, basically a *bigger machine*.

### How to appropriately use edge accelerators (for example, content delivery network [CDN])
### How to migrate applications into containers
### Load balancing concepts (for example, Application Load Balancer)
### Multi-tier architectures
### Queuing and messaging concepts (for example, publish/subscribe)
### Serverless technologies and patterns (for example, AWS Fargate, AWS Lambda)
### Storage types with associated characteristics (for example, object, file, block)
### The orchestration of containers (for example, Amazon Elastic Container Service [Amazon ECS], Amazon Elastic Kubernetes Service [Amazon EKS])
### When to use read replicas
### Workflow orchestration (for example, AWS Step Functions)

***
Skills in
***
### Designing event-driven, microservice, and/or multi-tier architectures based on requirements
### Determining scaling strategies for components used in an architecture design
### Determining the AWS services required to achieve loose coupling based on requirements
### Determining when to use containers
### Determining when to use serverless technologies and patterns
### Recommending appropriate compute, storage, networking, and database technologies based on requirements
### Using purpose-built AWS services for workloads

## Task Statement 2.2: Design highly available and/or fault-tolerant architectures.
***
Knowledge of:
***

### AWS global infrastructure (for example, Availability Zones, AWS Regions, Amazon Route 53)
### AWS managed services with appropriate use cases (for example, Amazon Comprehend, Amazon Polly)
### Basic networking concepts (for example, route tables)

### Disaster recovery (DR) strategies (for example, backup and restore, pilot light, warm standby, active-active failover, recovery point objective [RPO], recovery time objective [RTO])
*  [Disaster Recovery whitepaper](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/introduction.html)

* **Resiliency** is the ability of a workload to recover from infrastructure, service, or application disruptions, dynamically acquire computing resources to meet demand, and mitigate disruptions, such as misconfigurations or transient network issues.
* **Disaster recovery (DR)** concerns how your workload responds when a disaster strikes
* **availability** objectives measure mean values over a period of time. MTBF = Mean time between failures, MTTR Mean time to recover
* **RPO**, Recovery Point Objective - How much data could you lose; maximum time between 'backups'
* **RTO**, Recovery Time Objective - How long does it take for the 'backup' to take over

* Disaster recovery strategies:
    * Active/Passive
        * Backup and Restore
            * Create backups, restore from backups, recreate infrastructure
            * RPO/RTO of hours
            * very cheap
        * Pilot light
            * Keep minimal infrastructure ready, scale when needed
            * RPO/RTO 10s of minutes
            * \$
        * Warm Standby
            * Smaller than regular, but always running
            * RPO/RTO of minutes
            * \$\$
        Multi-Site active/active
            * Keep several sites active all the time
            * Almost zero downtime/data loss (RTO/RPO)
            * \$\$\$
![diagram](images/disaster-recovery-strategies.png)

### Distributed design patterns
### Failover strategies
### Immutable infrastructure
### Load balancing concepts (for example, Application Load Balancer)
### Proxy concepts (for example, Amazon RDS Proxy)
### Service quotas and throttling (for example, how to configure the service quotas for a workload in a standby environment)
### Storage options and characteristics (for example, durability, replication)
### Workload visibility (for example, AWS X-Ray)

***
Skills in
*** 

### Determining automation strategies to ensure infrastructure integrity
### Determining the AWS services required to provide a highly available and/or fault-tolerant architecture across AWS Regions or Availability Zones
### Identifying metrics based on business requirements to deliver a highly available solution
### Implementing designs to mitigate single points of failure
### Implementing strategies to ensure the durability and availability of data (for example, backups)
### Selecting an appropriate DR strategy to meet business requirements
### Using AWS services that improve the reliability of legacy applications and applications not built for the cloud (for example, when application changes are not possible)
### Using purpose-built AWS services for workloads
