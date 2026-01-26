# FastAPI Containerized CI/CD Pipeline 🚀

![Build Status](https://github.com/ofekh12/fastapi-ghcr-deploy/actions/workflows/deploy.yml/badge.svg)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-blue)](https://ofekh12.github.io/fastapi-ghcr-deploy/)

## Overview
This project demonstrates a full modern DevOps lifecycle for a FastAPI application. It includes automated testing, containerization, and a continuous integration/deployment (CI/CD) pipeline.

## 🔗 Live Resources
* **Project Documentation:** [View Docs here](https://ofekh12.github.io/fastapi-ghcr-deploy/)
* **Docker Image:** [Available on GHCR](https://github.com/ofekh12/fastapi-ghcr-deploy/pkgs/container/fastapi-app)

## 🛠 Tech Stack
* **Framework:** FastAPI (Python 3.10)
* **Testing:** Pytest with TestClient
* **Containerization:** Multi-stage Docker build
* **CI/CD:** GitHub Actions
* **Registry:** GitHub Container Registry (GHCR)
* **Documentation:** Jekyll & GitHub Pages

## 🚀 Pipeline Workflow
The CI/CD pipeline (`deploy.yml`) is triggered on every push to the `main` branch:
1. **Lint & Test:** Runs `pytest` inside a dedicated Docker tester stage.
2. **Build:** Creates a slim production-ready Docker image.
3. **Push:** Authenticates and pushes the image to GitHub Container Registry.
4. **Deploy Docs:** Automatically updates the Jekyll documentation site.

## 💻 How to Run Locally

### Using Docker (Recommended)
```bash
docker pull ghcr.io/ofekh12/fastapi-app:latest
docker run -d -p 8000:80 ghcr.io/ofekh12/fastapi-app:latest
Manual Installation
Clone the repo: git clone https://github.com/ofekh12/fastapi-ghcr-deploy.git

Install dependencies: pip install -r requirements.txt

Run the app: uvicorn app.main:app --reload

Created by Ofek Harari- DevOps Student Project