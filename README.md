LegalDocIQ
AI-Powered Legal Document Triage Platform
LegalDocIQ is a serverless AWS application that automatically processes legal documents, extracts text using OCR, analyzes content using AI, and generates structured legal intelligence.

The platform is designed to help law firms and legal departments reduce document review time, identify high-risk matters quickly, and automate legal document intake workflows.

Architecture
PDF Upload
      │
      ▼
S3 Upload Bucket
      │
      ▼
S3 ObjectCreated Event
      │
      ▼
Standard SQS Queue
      │
      ▼
AWS Lambda Processor
      │
      ▼
Amazon Textract OCR
      │
      ▼
Extracted Document Text
      │
      ▼
Claude AI Analysis
      │
      ▼
Structured Legal Data
      │
      ▼
DynamoDB Storage
      │
      ▼
Dashboard & Reporting
      │
      ▼
SNS Alerts (High Risk Documents)
Technologies Used
Cloud
AWS Lambda

Amazon S3

Amazon SQS

Amazon Textract

AWS Secrets Manager

Amazon DynamoDB

Amazon SNS

Amazon CloudWatch

Infrastructure as Code
Terraform

Programming
Python 3.12

Boto3

AI
Claude API (Anthropic)

Features
Document Ingestion
Upload PDF legal documents

Automatic event-driven processing

Scalable serverless architecture

OCR Extraction
Supports scanned PDF documents

Amazon Textract OCR integration

Extracts text from image-based documents

AI Analysis
Legal document classification

Risk assessment

Key party extraction

Critical date extraction

Executive summaries

Storage
Original documents stored in S3

Structured results stored in DynamoDB

Notifications
High-risk document alerts

SNS integration

Infrastructure Provisioned with Terraform
Networking
Custom VPC

Public Subnet

Private Subnet

Internet Gateway

Route Tables

Storage
S3 Upload Bucket

S3 Processed Bucket

Messaging
Standard SQS Queue

Compute
AWS Lambda Processor

Security
IAM Roles

IAM Policies

AWS Secrets Manager

Monitoring
CloudWatch Logs

Current Status
Completed
Terraform infrastructure deployed

S3 upload pipeline operational

SQS event processing operational

Lambda trigger operational

Textract OCR extraction operational

CloudWatch logging operational

Secrets Manager integration operational

In Progress
Claude AI integration

DynamoDB persistence

SNS alerting

Dashboard interface

Example Workflow
User uploads a PDF to Amazon S3.

S3 generates an ObjectCreated event.

Event is sent to Amazon SQS.

Lambda automatically processes the message.

Textract extracts document text.

Claude analyzes the content.

Structured results are generated.

Results are stored in DynamoDB.

High-risk documents trigger SNS alerts.

Skills Demonstrated
This project demonstrates:

AWS Serverless Architecture

Event-Driven Design

Infrastructure as Code (Terraform)

OCR Processing

AI Integration

Cloud Security

Secrets Management

Asynchronous Messaging

Python Automation

Monitoring & Observability

Author
Edmond Chamunorwa

Cloud Engineering | AWS | Terraform | Python | Networking | Kubernetes
