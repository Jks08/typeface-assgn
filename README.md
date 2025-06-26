# Random Joke Generator - DevOps Project

## Project Overview

This project demonstrates a complete DevOps pipeline for a simple web application that serves random jokes. It consists of a Flask backend API and a React frontend, deployed to Kubernetes using Azure DevOps pipelines.

## Architecture

- **Backend**: Python Flask API serving random jokes
- **Frontend**: React application that displays jokes
- **Infrastructure**: Azure Kubernetes Service (AKS)
- **CI/CD**: Azure DevOps Pipelines
- **Source Control**: Azure Repos

## Local Development Setup

### Prerequisites

- Python 3.9+
- Node.js 14+
- Git
- Azure CLI
- kubectl
- Docker

### Backend Setup

1. Clone the repository:

```bash
git clone <your-azure-repo-url>
cd joke-generator
```

2. Install Python dependencies:

`pip install flask flask-cors`

3. Run the backend server:

`python app.py`

The server will start on http://localhost:5000

### Frontend Setup

Navigate to the frontend directory:

`cd frontend`

Install dependencies:

`npm install`

Start the development server:

`npm start`

The frontend will be available at http://localhost:3000
