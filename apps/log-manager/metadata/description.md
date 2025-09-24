# Log Manager

A comprehensive log management solution built on the OpenSearch stack, providing centralized log collection, storage, search, and visualization capabilities.

## Features

- **OpenSearch**: High-performance search and analytics engine for log data
- **OpenSearch Dashboards**: Rich visualization and exploration interface
- **Fluent Bit**: Lightweight log processor and forwarder
- **Multi-source Support**: Collects logs from Docker containers, system files, and network devices
- **Real-time Processing**: Stream processing and real-time log analysis
- **Scalable Architecture**: Designed to handle large volumes of log data

## Components

### OpenSearch
- Full-text search and analytics engine
- RESTful API for data operations
- Cluster-ready architecture
- Advanced query capabilities

### OpenSearch Dashboards
- Web-based visualization interface
- Custom dashboard creation
- Real-time log monitoring
- Advanced filtering and search

### Fluent Bit
- Lightweight log processor (< 1MB)
- High-performance log collection
- Multiple input/output plugins
- Built-in parsing and filtering

## Use Cases

- **System Monitoring**: Centralize logs from multiple servers and applications
- **Security Analysis**: Monitor security events and detect anomalies
- **Performance Debugging**: Track application performance and errors
- **Compliance**: Maintain audit trails and regulatory compliance
- **DevOps**: Streamline log management in containerized environments

## Network Ports

- **5601**: OpenSearch Dashboards web interface (main port)
- **9200**: OpenSearch HTTP API
- **9600**: OpenSearch performance analyzer
- **24224**: Fluent Bit log input (Docker logs)
- **5140**: Fluent Bit syslog input (UDP)
- **12201**: Fluent Bit GELF input (UDP)

## Configuration

The application comes with sensible defaults but can be customized through:
- Memory allocation for OpenSearch
- Security plugin settings
- Log parsing configuration
- Custom dashboards and visualizations

## Getting Started

1. Install and start the Log Manager
2. Access OpenSearch Dashboards at `http://your-server:5601`
3. Configure log sources to send data to the Fluent Bit ports
4. Create dashboards and visualizations for your log data

## Requirements

- Minimum 2GB RAM recommended for OpenSearch
- Sufficient disk space for log retention
- Network access to log sources