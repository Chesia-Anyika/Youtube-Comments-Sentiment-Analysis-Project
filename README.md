# DSA3030-Project
YouTube serves as a vast repository of user-generated content, spanning various genres such as entertainment, education, and advertising. This project aims to create a sentiment analysis system tailored for YouTube comments. 


# I. Problem Domain

YouTube serves as a vast repository of user-generated content, spanning various genres such as entertainment, education, and advertising. This project aims to create a sentiment analysis system tailored for YouTube comments. By analyzing comments, this platform will help businesses gauge audience sentiment towards their content, products, or brand, thus empowering businesses to engage with their audience effectively and make informed decisions about content creation and marketing strategies.

# II. Project Plan

## A. Requirements Gathering

**Social Media Platform Selection**

We focused solely on Youtube due to its vast user base, vast repository of user generated content, real-time nature, and availability of comprehensive APIs for data access.

**Feature Definition**

We defined the key feature for sentiment analysis in our data as the verbatim comments users left on our chosen video. With that, we used natural language processing to determine comment sentiments as either positive, negative, or compound. 

## B. Data Ingestion and Preparation

**Data Scraping**

We utilised the Youtube API to collect real time comments from a specific video. The chosen video is titled ‘*Can Israelis and Palestinians See Eye to Eye? || Creators for Change | Middle Ground*’, from the *Jubilee* youtube channel. 

[Link to Video](https://www.youtube.com/watch?v=_Jj8vne0ca0)

The video was chosen due to the following reasons: 

- The video is pertinent to current social events, thus engagement on the video is high, having 13 million views and 100,000 comments to date. Thus, we are likely to get comments from a wide variety of youtube users.
- The video covers a highly divisive topic, thus comments are likely to showcase a wide variety of sentiments to train our model on.

The data scraping will be performed on Google Colab, and the data saved to a json file. 

**Streaming Data using integrated kafka-pyspark pipeline.** 

An Integrated Kafka-PySpark pipeline refers to the combination of Apache Kafka and PySpark, typically used for real-time data processing and analysis. Here's a breakdown:

1. **Apache Kafka**: Kafka is a distributed streaming platform that is commonly used for building real-time data pipelines and streaming applications. It is designed to handle high-throughput, fault-tolerant, and scalable data streams. Kafka allows producers to publish data to topics and consumers to subscribe to these topics and process the data in real-time.
2. **PySpark**: PySpark is the Python API for Apache Spark, which is a powerful open-source framework for distributed data processing and analysis. PySpark allows you to write Spark applications using Python, enabling scalable and high-performance data processing, machine learning, and analytics.

A Kafka-PySpark integration typically involves the following steps:

- **Data ingestion**: Apache Kafka serves as the data source, where producers publish data to Kafka topics. This data can be logs, events, sensor readings, or any other streaming data.
- **Data processing**: PySpark is used to consume the data from Kafka topics, perform various transformations, analyses, and computations on the data streams. PySpark provides rich libraries and APIs for data manipulation, including SQL queries, machine learning, and graph processing.
- **Real-time analytics**: By integrating Kafka with PySpark, organizations can perform real-time analytics on streaming data. This includes tasks such as aggregations, filtering, enrichment, pattern detection, and anomaly detection, enabling businesses to gain insights and make data-driven decisions in real-time.
- **Scalability and fault-tolerance**: Both Kafka and Spark are designed for scalability and fault-tolerance, making them well-suited for handling large volumes of data and ensuring continuous processing even in the event of failures or network partitions

There are several benefits of implementing Spark-Kafka integration. You can ensure minimum data loss through Spark Streaming while saving all the received Kafka data synchronously for an easy recovery. Users can read messages from a single topic or multiple Kafka topics.

Along with this level of flexibility you can also access high scalability, throughput and fault-tolerance and a range of other benefits by using Spark and Kafka in tandem. This integration can be understood with a data pipeline that functions in the methodology shown below:

This pipeline would allow us to stream the comments data scraped of the Youtube api for batch processing.

**Creation of Docker containers**

Docker is a containerization platform that allows developers to package applications application and its dependencies into a standardized unit called a container. Containers are great for *Continuous Integration and Continuous Delivery (CI/CD)* workflows, which involve frequently integrating code changes, early error detection and automating the deployment of code changes to production.

For the Kafka-PySpark pipeline:

- Using a Docker container ensures a consistent environment for running the Kafka and PySpark application across development, testing, and production.
- The Containers enable scalability, as multiple instances of Kafka and PySpark containers can be spun up easily to handle varying workloads.

Overall, the Docker containers will streamline the development, testing, and deployment of the Kafka-PySpark pipeline within a CI/CD workflow, providing consistency, reliability, and scalability.

**Data Preprocessing**

We will preprocess the collected data to remove noise, filter out duplicate comments and format it for analysis. 

## C. Application Development

**Sentiment Analysis**

We implemented sentiment analysis in Google Colab using *Natural Language Toolkit (NLTK).* This is a leading platform for building Python programs to work with human language data. NLTK provides easy-to-use interfaces to over 50 corpora and lexical resources, such as WordNet, along with a suite of text processing libraries for tasks like tokenization, stemming, tagging, parsing, and semantic reasoning.

For the model, we used the *Valence Aware Dictionary and sEntiment Reasoner (VADER)* model which is a part of the NLTK library and is specifically designed for sentiment analysis of text. It's a lexicon and rule-based sentiment analysis tool that is particularly well-suited for analyzing sentiment in social media texts, online reviews, and other short, informal texts. we chose this model due to its high performance on informal texts that may contain emoticons, slang or other non-standard language features. 

**Visualisation**

We integrated visualisation elements of our analysis using Matplotlib, to create visualisations of our sentiment analysis results. 

## D. Technologies and Tools Used

- Youtube API for data access.
- Docker Desktop for containerisation.
- Apache Kafka, Pyspark and Jupyter Notebook for data streaming.
- NLTK and VADER for sentiment analysis.
- Matplotlib for visualisation.
- Python programming language for implementation.
