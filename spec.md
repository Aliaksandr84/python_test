Project Spec: Data Quality Validator as a Self-Service Web Platform
Summary
Build a web platform where data analysts and engineers can upload CSV datasets and receive automated data quality reports. The platform provides an audit trail of uploads, a searchable list of past reports, and quality suggestions.


Purpose
Organizations struggle with “dirty” data in their pipelines. By allowing users to quickly validate data for common issues (missing values, duplicate rows, outlier detection, type mismatches), this project saves time, increases reliability, and forms a foundation for wider data governance.


Target Users
Data analysts

Data engineers

BI/pipeline owners

Core Features
1. User-friendly Web UI
Simple dashboard

CSV uploads

List of past uploads and reports

2. Automated Data Quality Checks
Schema/type validation

Missing/null detection

Duplicate row detection

Basic outlier/stats detection

3. Report Generation
HTML & downloadable summary

Clear issue summaries and suggestions

4. History & Audit Trail
Per-user list of uploads/reports (add authentication as optional stretch)

Technical Components
Frontend

Simple HTML/Jinja via Flask (or React/NextJS for future)

Upload form, reports tables, and dashboard

Backend

Flask or FastAPI

Endpoints: /upload, /reports, /report/<id>, /

Uses pandas for CSV validation logic

File and report metadata stored in SQLite or local file system (MVP)

Testing

Unit tests for quality checks (pytest)

Integration tests for upload/report endpoints

Deployment/Packaging

Dockerized app, ready for K8s deployment

Helm chart (optional stretch)

Example User Story
> - As an analyst, I upload a CSV file.
> - Instantly, I receive a clear report showing missing values, outliers, and duplicates.
> - I can view and download reports for all my past uploads in the same interface.


Example Data Quality Report Output
Filename: customers-jan.csv

Uploaded: 2026-02-09 14:05

Summary:

Missing values: 3 columns

Duplicates found: 27

Outlier detection: 2 columns (age, salary)

Column type mismatch: 1 (customer_id, expected int, found float)

Stretch Goals / Nice to Have
User authentication (JWT or OAuth)

Email notifications on report completion

API endpoints for integration into CI pipelines

Visualization of data distributions

Data catalog and profiling features

Out of Scope (for v1)
Real-time processing

Big data pipeline integration

Connections to databases/lakes (future potential)

Deliverables
Source code (GitHub repo)

README.md with system description and usage

Dockerfile, deployment manifests (K8s YAMLs)

Example tests and sample input files