# Domain 1 - Development with AWS Services (32% of scored content)

## Task 1: Develop code for applications hosted on AWS.
Knowledge of:
### Architectural patterns (for example, event-driven, microservices, monolithic, choreography, orchestration, fanout)
* **Monolithic** There's one application or server to do all the tasks. The code can still be organized and partitioned logically. Can, many times, get better performance since communication is just function calling. It is harder to make code changes, and much harder to scale, since you have to scale the whole application.  
* **Microservices** Architectures partition the domain into many smaller, independent services, connected over the network. Code changes can be done independently for each microservice. Scaling can be done independently.

This is basically SOA with smaller services. How small should each service be? 
* **Event-driven** architectures react to events
* **fanout** of a service is how many other services it calls (and fan-in is how many other services call it)

### Idempotency
When an operation or API call can be performed repeatedly, with the same result as executing it once, we call that operation idempotent. In distributed systems, this helps since we don't need to ensure the operation is only done once, we could re-send or re-try.

### Differences between stateful and stateless concepts
### Differences between tightly coupled and loosely coupled components
### Fault-tolerant design patterns (for example, retries with exponential backoff and jitter, dead-letter queues)
### Differences between synchronous and asynchronous patterns

Skills in:
### Creating fault-tolerant and resilient applications in a programming language (for example, Java, C#, Python, JavaScript, TypeScript, Go)
### Creating, extending, and maintaining APIs (for example, response/request transformations, enforcing validation rules, overriding status codes)
### Writing and running unit tests in development environments (for example, using AWS Serverless Application Model [AWS SAM])
### Writing code to use messaging services
### Writing code that interacts with AWS services by using APIs and AWS SDKs
### Handling data streaming by using AWS services

## Task 2: Develop code for AWS Lambda.
Knowledge of:
### Event source mapping
### Stateless applications
### Unit testing
### Event-driven architecture
### Scalability
### The access of private resources in VPCs from Lambda code

Skills in:
### Configuring Lambda functions by defining environment variables and parameters (for example, memory, concurrency, timeout, runtime, handler, layers, extensions, triggers, destinations)
### Handling the event lifecycle and errors by using code (for example, Lambda Destinations, dead-letter queues)
### Writing and running test code by using AWS services and tools
### Integrating Lambda functions with AWS services
### Tuning Lambda functions for optimal performance

## Task 3: Use data stores in application development.
Knowledge of:
### Relational and non-relational databases
### Create, read, update, and delete (CRUD) operations
### High-cardinality partition keys for balanced partition access
### Cloud storage options (for example, file, object, databases)
### Database consistency models (for example, strongly consistent, eventually consistent)
### Differences between query and scan operations
### Amazon DynamoDB keys and indexing
### Caching strategies (for example, write-through, read-through, lazy loading, TTL)
### Amazon Simple Storage Service (Amazon S3) tiers and lifecycle management
### Differences between ephemeral and persistent data storage patterns

Skills in:
### Serializing and deserializing data to provide persistence to a data store
### Using, managing, and maintaining data stores
### Managing data lifecycles
### Using data caching services

## Services

* AWS Lambda
* Amazon DynamoDB

## Whitepapers

* [Overview of AWS Services](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/introduction.html?did=wp_card&trk=wp_card)
* [Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html?did=wp_card&trk=wp_card)
* Decision guides
    * [Choosing an AWS Database service](https://docs.aws.amazon.com/decision-guides/latest/databases-on-aws-how-to-choose/databases-on-aws-how-to-choose.html)
