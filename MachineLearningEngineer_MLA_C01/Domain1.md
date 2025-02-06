# Domain 1:  Data Preparation for Machine Learning (ML) (28%

## Task Statement 1.1: Ingest and store data.

Knowledge of:
***

### Data formats and ingestion mechanisms (for example, validated and non-validated formats)

SageMaker supports many different formats for [Training](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-training.html) and [Inference](https://docs.aws.amazon.com/sagemaker/latest/dg/cdf-inference.html), including:

* [Apache Parquet](https://parquet.apache.org/) - an open source, column-oriented data file format designed for efficient data storage and retrieval.
* [JSON](https://www.json.org/) - Javascript Object Notation, a text-based format close to how Javascript would represent a dictionary or object.
* [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) - Comma-separated values. Text based, each line is a row, values are separated by commas; may wrap values in "" if they contain commas; may contain a header or not.
* [Apache ORC]()
* [Apache Avro]()
* [RecordIO]()

###  How to use the core AWS data sources (for example, Amazon S3, Amazon Elastic File System [Amazon EFS], Amazon FSx for NetApp ONTAP)

### How to use AWS streaming data sources to ingest data (for example, Amazon Kinesis, Apache Flink, Apache Kafka)

### AWS storage options, including use cases and tradeoffs

***
Skills in:
***

### Extracting data from storage (for example, Amazon S3, Amazon ElasticBlock Store [Amazon EBS], Amazon EFS, Amazon RDS, Amazon DynamoDB) by using relevant AWS service options (for example, Amazon S3 Transfer Acceleration, Amazon EBS Provisioned IOPS)
### Choosing appropriate data formats (for example, Parquet, JSON, CSV, ORC) based on data access patterns
### Ingesting data into Amazon SageMaker Data Wrangler and SageMaker Feature Store
### Merging data from multiple sources (for example, by using programming techniques, AWS Glue, Apache Spark)
### Troubleshooting and debugging data ingestion and storage issues that involve capacity and scalability
### Making initial storage decisions based on cost, performance, and data
structure

## Task Statement 1.2: Transform data and perform feature engineering.

Knowledge of:
***

### Data cleaning and transformation techniques (for example, detecting and treating outliers, imputing missing data, combining, deduplication)
### Feature engineering techniques (for example, data scaling and standardization, feature splitting, binning, log transformation, normalization)
### Encoding techniques (for example, one-hot encoding, binary encoding, label encoding, tokenization)
### Tools to explore, visualize, or transform data and features (for example, SageMaker Data Wrangler, AWS Glue, AWS Glue DataBrew)
### Services that transform streaming data (for example, AWS Lambda, Spark)
### Data annotation and labeling services that create high-quality labeled datasets

Skills in:
***

### Transforming data by using AWS tools (for example, AWS Glue, AWS Glue DataBrew, Spark running on Amazon EMR, SageMaker Data Wrangler)
### Creating and managing features by using AWS tools (for example, SageMaker Feature Store)
### Validating and labeling data by using AWS services (for example, SageMaker Ground Truth, Amazon Mechanical Turk)

## Task Statement 1.3: Ensure data integrity and prepare data for modeling.
***
Knowledge of:
***

* Pre-training bias metrics for numeric, text, and image data (for example,
class imbalance [CI], difference in proportions of labels [DPL])
* Strategies to address CI in numeric, text, and image datasets (for example,
synthetic data generation, resampling)
* Techniques to encrypt data
* Data classification, anonymization, and masking
* Implications of compliance requirements (for example, personally
identifiable information [PII], protected health information [PHI], data
residency) 

***
Skills in:
***

* Validating data quality (for example, by using AWS Glue DataBrew and AWS
Glue Data Quality)
* Identifying and mitigating sources of bias in data (for example, selection
bias, measurement bias) by using AWS tools (for example, SageMaker
Clarify)
* Preparing data to reduce prediction bias (for example, by using dataset
splitting, shuffling, and augmentation)
* Configuring data to load into the model training resource (for example,
Amazon EFS, Amazon FSx)
