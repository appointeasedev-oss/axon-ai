# AXON: Self-Improving AI

AXON is an experimental, autonomous, self-improving AI system designed to run entirely on GitHub infrastructure. It has full access to its own source code and uses an internal improvement engine to analyze its performance and modify its architecture.

## Core Features

- **Custom Transformer Architecture**: Built from scratch using PyTorch.
- **Autonomous Self-Improvement**: Uses LLM-based reasoning to analyze code and metrics.
- **GitHub-Native**: Training and improvement cycles are managed via GitHub Actions.
- **Self-Scaling**: Capable of modifying its own hyperparameters and layer configurations.

## Repository Structure

- `src/model.py`: The core neural network architecture.
- `src/train.py`: Training logic and metric collection.
- `src/improve.py`: The self-improvement engine that modifies the source code.
- `.github/workflows/autonomous.yml`: The automation pipeline.

## How It Works

1. **Training**: The `train.py` script runs, training the model on available data and outputting `metrics.json`.
2. **Analysis**: The `improve.py` script reads the source code and metrics.
3. **Modification**: It proposes and applies changes to the source code to optimize performance.
4. **Evolution**: Changes are committed back to the repository, triggering the next cycle.

## Setup

To enable the self-improvement cycle, ensure the following secrets are set in your GitHub repository:
- `OPENAI_API_KEY`: Required for the improvement engine's reasoning.
- `GITHUB_TOKEN`: (Provided by default in Actions) Used for committing changes.

---
*AXON is a living experiment in recursive AI improvement.*
