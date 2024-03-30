# Data Engineering on AWS with Apache Kafka
## Overview

This project AWS project features Kafka producer and consumer applications on EC2, monitored with CloudWatch, streaming data to specific Kafka topics, with data then transferred to a staging folder in an S3 bucket, undergoing periodic Glue ETL to merge into a data lake folder, followed by Glue crawler creation of database and tables for querying via Athena.

## Key Components

### Kafka Producer & Consumer Applications

- **Producer**: EC2 instances host a Python-based Kafka producer application responsible for generating and publishing data streams to specified Kafka topics.
- **Consumer**: Another set of EC2 instances run a Python-based Kafka consumer application, subscribing to Kafka topics, consuming the data, and transferring it to downstream components.

The following image shows the producer application generating messages using the data from the dataset:
<img width="1280" alt="Screenshot (65)" src="https://github.com/githar5h/AWS-Kafka-Data-Engineering/assets/96515805/a2a6f8fa-04eb-4191-bca1-dfdd8322a61a">


### CloudWatch Monitoring

- **Monitoring**: CloudWatch is utilized for real-time monitoring and management of EC2-based Kafka producer and consumer applications. Metrics such as CPU utilization, memory usage, and network throughput are tracked to ensure optimal performance.

### S3 Staging and Data Storage

- **Staging Area**: Data consumed by the Kafka consumer application is temporarily stored in an S3 staging folder. This staging area acts as a buffer for incoming data before further processing.
- **Data Storage**: Once staged, the data is stored persistently in an S3 bucket. This allows for durable storage and easy accessibility for downstream processing.

### Glue ETL Processing

- **ETL Jobs**: Glue ETL jobs are scheduled periodically to process the staged data from the S3 bucket. These jobs perform data transformations, cleansing, and aggregation as necessary.
- **Data Lake Formation**: Processed data is organized and aggregated into a structured datalake format within the same S3 bucket. This structured datalake serves as a centralized repository for all processed data.

The following image shows the Glue ETL job:
<img width="525" alt="Screenshot (70)" src="https://github.com/githar5h/AWS-Kafka-Data-Engineering/assets/96515805/62616e2e-5bfd-4ba2-bca2-d4652e40f12e">

### Automated Schema Detection with Glue Crawlers

- **Schema Detection**: Glue crawlers are employed to automatically detect the schema of the processed data within the datalake. These crawlers scan the data, infer the schema, and create corresponding databases and tables for query optimization.
- **Dynamic Cataloging**: As new data is added to the datalake, Glue crawlers dynamically update the catalog, ensuring that the database and table definitions remain up-to-date.

### Querying and Analysis with Athena

- **Querying**: Once the schema is cataloged, users can leverage Amazon Athena to query and analyze the data stored in the datalake. Athena provides a serverless, interactive query service that allows users to analyze large datasets with standard SQL queries.
- **Ad-hoc Analysis**: With Athena, users can perform ad-hoc analysis, generate reports, and gain insights from the data without the need for complex infrastructure setup.

### Tech Stack
- Kafka: Streaming data ingestion
- Python: Language used for Kafka producer and consumer applications
- S3: Data storage and staging
- Glue: ETL processing and schema detection
- Athena: Querying and analysis
- CloudWatch: Monitoring and management of EC2 instances

## Getting Started

To deploy and run the data pipeline in your AWS environment, follow these steps:

1. **Set Up Kafka Producer & Consumer**: Deploy Kafka producer and consumer applications on EC2 instances. Configure Kafka topics and communication.
2. **Set Up S3 Bucket**: Create an S3 bucket for staging and storing data. Configure access permissions and policies as necessary.
3. **Configure Glue ETL Jobs**: Define Glue ETL jobs to process staged data from the S3 bucket. Specify data transformations, mappings, and output destinations.
4. **Automate with Glue Crawlers**: Set up Glue crawlers to automatically detect and catalog the schema of processed data within the datalake.
5. **Query Data with Athena**: Use Amazon Athena to query and analyze the data stored in the datalake. Write SQL queries to extract insights and generate reports.
