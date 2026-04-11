# 🚀 Flask to GKE CI/CD Pipeline via Google Cloud Build

## 📌 Project Overview
This repository demonstrates a complete, automated Cloud-Native CI/CD pipeline. A Python Flask application is containerized using Docker, automatically built and pushed to Google Container Registry (GCR) via Google Cloud Build, and declaratively deployed to a Google Kubernetes Engine (GKE) cluster. 

This project emphasizes Infrastructure as Code (IaC), zero-downtime deployment practices, and automated environment management using a GitOps-style branching strategy.

## 🛠️ Tech Stack & Architecture
* **Application:** Python 3.8, Flask
* **Containerization:** Docker
* **CI/CD:** Google Cloud Build, GitHub Webhooks
* **Container Registry:** Google Container Registry (GCR)
* **Orchestration:** Google Kubernetes Engine (GKE)
* **Infrastructure Management:** Kubernetes Manifests (YAML)

## 🏗️ CI/CD Workflow & Branching Strategy
The deployment lifecycle is fully automated and triggered by GitHub push events, ensuring environments are always in sync with the codebase.

### Branching Strategy
* **`main` Branch (Production):** Code pushed or merged into `main` automatically triggers a Cloud Build pipeline that deploys the application to the `gcp-devops-prod` namespace in GKE.
* **`development` Branch (Dev/Staging):** Code pushed to the `development` branch triggers a separate build pipeline tailored for testing new features in an isolated environment before promoting them to production.

### Pipeline Steps (`cloudbuild.yaml`)
1. **Build:** Cloud Build pulls the latest code and executes the `Dockerfile` to create a lightweight Python environment.
2. **Push:** The newly built container image is tagged and pushed to GCR (`gcr.io/$PROJECT_ID/gcpdevops`).
3. **Deploy:** The pipeline uses the `gke-deploy` builder to declaratively apply `gke.yaml`, updating the GKE deployment in the `us-central1-a` zone.

## 📂 Repository Structure

```text
├── Dockerfile          # Defines the lightweight Python 3.8 container
├── app.py              # Single-file Flask application with inline HTML rendering
├── cloudbuild.yaml     # CI/CD pipeline steps for GCP Cloud Build
├── gke.yaml            # Kubernetes Deployment and LoadBalancer Service manifests
├── readme.md           # Project documentation
└── requirements.txt    # Python dependencies
