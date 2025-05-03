# Data Stream

A Data Stream is a visual representation of a flow of data. It is created through the Data Stream Designer and consists of Stream Objects that ingest, transform, analyze, and act on data.

## Overview

Data Streams are the backbone of real-time data processing in XMPro. They allow you to:

- Ingest data from various sources
- Transform and enrich data
- Analyze data for patterns and anomalies
- Take actions based on the data

Data Streams are designed to be:

- Visual and intuitive
- Real-time
- Scalable
- Flexible

## Components of a Data Stream

A Data Stream consists of the following components:

### Stream Objects

Stream Objects are the building blocks of a Data Stream. They are instances of Agents that perform specific functions in the data flow. Stream Objects are connected together to form a pipeline of data processing.

### Connections

Connections define how data flows between Stream Objects. They are represented as arrows in the Data Stream Designer.

### Data

Data flows through the Stream Objects and is transformed, analyzed, and acted upon as it moves through the Data Stream.

## Types of Data Streams

There are two types of Data Streams:

### Streaming

Streaming Data Streams run continuously, processing data as it arrives. They are used for real-time monitoring and alerting.

### Recurrent

Recurrent Data Streams run on a schedule, processing data in batches. They are used for periodic reporting and analysis.

## Related Concepts

- [Stream Object Configuration](stream-object-configuration.md)
- [Verifying Stream Integrity](verifying-stream-integrity.md)
- [Running Data Streams](running-data-streams.md)
- [Timeline](timeline.md)
