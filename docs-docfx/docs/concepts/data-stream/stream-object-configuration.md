# Stream Object Configuration

Stream Objects are the building blocks of a Data Stream. Each Stream Object is an instance of an Agent that performs a specific function in the data flow. This page explains how to configure Stream Objects in a Data Stream.

## Overview

When you add a Stream Object to a Data Stream, you need to configure it to perform the specific function you want. The configuration options depend on the type of Agent the Stream Object is based on.

## Configuration Process

To configure a Stream Object:

1. Double-click on the Stream Object in the Data Stream Designer, or select the Stream Object and click the "Configure" button in the toolbar.
2. The configuration panel for the Stream Object will open, showing the available configuration options.
3. Configure the Stream Object according to your requirements.
4. Click "Apply" to save the configuration.

## Common Configuration Options

While each Agent type has its own specific configuration options, there are some common options that apply to most Stream Objects:

### Name

The name of the Stream Object. This is displayed on the Stream Object in the Data Stream Designer.

### Description

A description of the Stream Object. This is useful for documenting the purpose of the Stream Object.

### Input Mappings

Input Mappings define how data from the previous Stream Object is mapped to the inputs of the current Stream Object. This is particularly important when the output schema of the previous Stream Object doesn't match the input schema expected by the current Stream Object.

### Error Handling

Error Handling options define what happens when an error occurs in the Stream Object. Options typically include:

- **Continue**: Continue processing data even if an error occurs.
- **Stop**: Stop processing data if an error occurs.
- **Retry**: Retry the operation if an error occurs.

## Agent-Specific Configuration

Each Agent type has its own specific configuration options. For example:

### Listener Agents

Listener Agents ingest data from external sources. Configuration options typically include:

- **Connection details**: How to connect to the data source.
- **Data format**: The format of the data being ingested.
- **Polling interval**: How often to check for new data (for polling-based Listeners).

### Transformation Agents

Transformation Agents transform data as it flows through the Data Stream. Configuration options typically include:

- **Transformation logic**: How to transform the data.
- **Output schema**: The schema of the transformed data.

### Action Agents

Action Agents perform actions based on the data. Configuration options typically include:

- **Action details**: What action to perform.
- **Trigger conditions**: When to perform the action.

## Best Practices

When configuring Stream Objects, consider the following best practices:

- **Use meaningful names**: Give your Stream Objects meaningful names that describe their purpose.
- **Document your configuration**: Use the description field to document the purpose and configuration of the Stream Object.
- **Test your configuration**: Use the Live View feature to test your configuration with sample data.
- **Keep it simple**: Break complex transformations into multiple simple transformations for better maintainability.

## Related Concepts

- [Data Stream](index.md)
- [Verifying Stream Integrity](verifying-stream-integrity.md)
- [Running Data Streams](running-data-streams.md)
- [Timeline](timeline.md)
