# FastAPI CI/CD Project

This project demonstrates a FastAPI application deployed using GitHub Actions, Kubernetes, and ArgoCD. The application includes endpoints to display API details and container information.

## Features

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs.
- **CI/CD**: Automated deployment pipeline using GitHub Actions.
- **Kubernetes**: Container orchestration for managing deployments.
- **ArgoCD**: GitOps-based continuous delivery tool for Kubernetes.
- **Health Check Endpoint**: Displays application and container details.

---

## Endpoints

### Root Endpoint
- **URL**: `/`
- **Method**: `GET`
- **Response**:
  ```json
  {
      "message": "Hello from FastAPI CICD Project!"
  }
  ```

---

## Project Structure

```
fastapi-cicd/
├── app/
│   ├── __init__.py
│   ├── main.py
├── .env
├── Dockerfile
├── requirements.txt
├── kubernetes/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── configmap.yaml
├── .github/
│   ├── workflows/
│       ├── ci-cd.yaml
├── README.md
```
