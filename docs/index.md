---
layout: default
title: FastAPI CI/CD Project
---

# FastAPI Professional Deployment Project 🚀

Welcome to the documentation for my automated API deployment project. This repository demonstrates a complete **Production-Ready** workflow, integrating modern DevOps practices.

## Key Features
* **High-Performance API:** Built with **FastAPI** including structured logging.
* **Automated Testing:** Integrated **Pytest** suite ensuring code reliability.
* **Containerization:** Optimized **Multi-stage Docker** builds.
* **CI/CD Pipeline:** Fully automated workflow using **GitHub Actions**.
* **Registry Integration:** Packages are automatically built and pushed to **GitHub Container Registry (GHCR)**.

## Project Architecture
The project follows a modern CI/CD flow:
1. **Code Push:** Triggered on every push to the `main` branch.
2. **Test Stage:** A Docker 'tester' layer runs the test suite.
3. **Build Stage:** Upon success, a slim production image is created.
4. **Deploy:** The image is pushed to GHCR for deployment.

## How to Run
To pull and run the latest version of this API, use:

```bash
docker pull ghcr.io/ofekh12/fastapi-app:latest
docker run -d -p 8001:80 ghcr.io/ofekh12/fastapi-app:latest

Developed by Ofek Harari as part of a DevOps Hands-on Lab.