# Hello Auth App

A simple Flask backend with API key authentication, containerized and deployed on AWS EC2.

## What it does

This app has two endpoints:
- `/health` - anyone can access it
- `/secure` - needs an API key to access

Built this as part of an assignment to learn backend basics, Docker, and AWS deployment.

## Stack

- Python + Flask
- Docker
- AWS EC2 (Ubuntu)

## Endpoints

**Public endpoint**
```
GET /health
```
Returns:
```json
{
  "status": "success",
  "message": "App is healthy"
}
```

**Protected endpoint**
```
GET /secure
```
Requires header: `x-api-key: my-secret-key`

Without key:
```json
{
  "status": "error",
  "message": "Unauthorized"
}
```

With valid key:
```json
{
  "status": "success",
  "message": "You are authenticated"
}
```

## Running locally

Install dependencies and run:
```bash
pip install -r requirements.txt
python app.py
```

## Docker setup

Build and run:
```bash
docker build -t hello-auth-app .
docker run -p 5000:5000 hello-auth-app
```

## AWS Deployment

Deployed on EC2 instance running Ubuntu 22.04. 

Steps I followed:
1. Launched EC2 instance
2. Installed Docker
3. Uploaded code files
4. Built image on server
5. Started container on port 80

Command used:
```bash
docker run -d -p 80:5000 --name hello-auth-container hello-auth-app
```

## Live URL

The app is running at: `http://13.60.220.100/health`

## Authentication

Using API key authentication with custom header `x-api-key`. Went with this approach since it's straightforward to implement and understand for a first backend project.
