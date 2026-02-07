# AXON: A Self-Improving AI System

## Introduction

AXON is an experimental, autonomous, and self-improving AI system designed to operate entirely within a GitHub environment. Its primary objective is to demonstrate the feasibility of an AI that can analyze, understand, and modify its own source code to enhance its performance and capabilities over time. This project serves as a living experiment in recursive AI improvement, where the system continuously evolves through automated cycles of training, evaluation, and code modification.

## Architecture Overview

AXON's architecture is composed of several key Python modules, each responsible for a specific aspect of its operation:

### 1. Core Model (`src/model.py`)

This module defines the neural network architecture of AXON. It is a custom transformer model built from scratch using PyTorch, without relying on any pre-trained weights. The design includes standard components such as multi-head attention mechanisms, feed-forward networks, and layer normalization, allowing for a flexible and scalable foundation for the AI's learning capabilities.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import math

# ... (rest of the model.py content)
```

### 2. Training Logic (`src/train.py`)

The `train.py` script handles the model's training process. It initializes the `AxonModel`, sets up an optimizer, and simulates a training loop. Crucially, after each training run, it captures key performance metrics (e.g., loss, number of parameters) and saves them to a `metrics.json` file. This file serves as the empirical feedback mechanism for the self-improvement engine.

```python
import torch
import torch.optim as optim
from model import AxonModel, AxonConfig
import json
import os

# ... (rest of the train.py content)
```

### 3. Self-Improvement Engine (`src/improve.py`)

This is the brain of AXON's self-modification capability. The `improve.py` script performs the following steps:

1.  **Context Gathering**: It reads its own source code files (from the `src/` directory) and loads the latest performance metrics from `metrics.json`.
2.  **Analysis and Proposal**: It uses an external Large Language Model (LLM) (specifically, `gpt-4.1-mini` via OpenAI's API) to analyze the gathered context. The LLM is prompted to identify bottlenecks, propose specific code changes, and output these changes in a structured JSON format.
3.  **Code Modification**: The proposed changes are then applied directly to the relevant source code files within the repository.
4.  **Version Control**: After applying changes, the script automatically stages, commits, and pushes these modifications to the GitHub repository. This ensures that every self-improvement step is version-controlled and triggers subsequent automated workflows.

```python
import os
import json
import torch
import subprocess
from openai import OpenAI

# ... (rest of the improve.py content)
```

## GitHub Actions Workflow (`.github/workflows/autonomous.yml`)

The continuous self-improvement cycle of AXON is orchestrated by a GitHub Actions workflow. This workflow is designed to run periodically (e.g., every hour) or can be manually triggered. It automates the entire process:

1.  **Checkout Code**: Fetches the latest version of the repository.
2.  **Setup Python**: Configures the Python environment.
3.  **Install Dependencies**: Installs necessary Python packages (e.g., `torch`, `openai`).
4.  **Run Training**: Executes `src/train.py` to train the model and generate updated `metrics.json`.
5.  **Run Self-Improvement**: Executes `src/improve.py`, which analyzes the code and metrics, generates improvements, and commits them back to the repository.

This closed-loop system allows AXON to autonomously iterate on its design and performance.

```yaml
name: Axon Autonomous Cycle

on:
  schedule:
    - cron: '0 * * * *' # Run every hour
  workflow_dispatch: # Allow manual trigger

jobs:
  improve:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v3
        with:
          fetch-depth: 0
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install torch openai

      - name: Run Training
        run: python src/train.py

      - name: Run Self-Improvement
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python src/improve.py
```

## Setup Instructions

To activate AXON's self-improvement capabilities, follow these steps:

1.  **Repository Access**: Ensure you have access to the `appointeasedev-oss/axon-ai` GitHub repository.
2.  **Create Workflow File**: Due to GitHub App permissions, the `autonomous.yml` workflow file could not be pushed directly. Please create this file manually in your repository at `.github/workflows/autonomous.yml` and paste the YAML content provided above.
3.  **GitHub Secrets**: Add an `OPENAI_API_KEY` to your repository secrets. This key is essential for the `improve.py` script to access the external LLM for code analysis and generation. The `GITHUB_TOKEN` is automatically provided by GitHub Actions with sufficient permissions for committing changes.

Once these steps are completed, the workflow will begin running according to its schedule, initiating AXON's autonomous improvement cycles.

## Future Enhancements and Phases

The current implementation lays the groundwork for AXON's evolution. Future phases, as discussed, include:

*   **Phase 1 (Small)**: The current ~1M parameter transformer with basic training.
*   **Phase 2 (Self-Aware)**: Enhancing the self-evaluator to more accurately measure performance and tune hyperparameters.
*   **Phase 3 (Self-Modifying)**: Expanding the improvement engine's capabilities to modify architectural components (e.g., adding/removing layers, changing attention heads) and autonomously curating training data.
*   **Phase 4 (Scaling)**: Implementing an auto-scaler that allows AXON to grow its own architecture and parameter count based on performance bottlenecks and available compute resources.

This iterative approach aims to build a truly self-improving AI that can adapt and grow its intelligence over time, entirely managed within a GitHub-native, open-source framework.
