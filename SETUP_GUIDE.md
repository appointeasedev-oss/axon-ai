# AXON AI - Complete Setup Guide

## Overview

AXON is a self-improving AI system that runs entirely on GitHub. It features a real-time dashboard hosted on GitHub Pages, autonomous training cycles, and self-modifying code capabilities.

## Prerequisites

- GitHub account with the `appointeasedev-oss` organization access
- OpenAI API key (for the self-improvement engine)
- Basic understanding of GitHub Actions and Git

## Step 1: Repository Setup

The main AXON repository is at: `https://github.com/appointeasedev-oss/axon-ai`

### Initial Configuration

1. Clone the repository:
   ```bash
   git clone https://github.com/appointeasedev-oss/axon-ai.git
   cd axon-ai
   ```

2. Verify the structure:
   ```
   axon-ai/
   ├── src/
   │   ├── model.py          # Core transformer model
   │   ├── train.py          # Training script
   │   ├── improve.py        # Self-improvement engine
   ├── .github/workflows/
   │   └── deploy-and-improve.yml  # Main automation workflow
   ├── metrics.json          # Performance metrics (auto-generated)
   └── README.md
   ```

## Step 2: GitHub Secrets Configuration

The system requires secrets to be configured in your GitHub repository.

### Required Secrets

1. **OPENAI_API_KEY** (Required for self-improvement)
   - Go to: `https://github.com/appointeasedev-oss/axon-ai/settings/secrets/actions`
   - Click "New repository secret"
   - Name: `OPENAI_API_KEY`
   - Value: Your OpenAI API key from https://platform.openai.com/api-keys
   - Click "Add secret"

2. **GITHUB_TOKEN** (Automatically provided by GitHub Actions)
   - This is automatically available in all workflows
   - Used for committing changes and pushing to the repository

### Optional Secrets

- `HUGGINGFACE_TOKEN`: For uploading models to Hugging Face Hub
- `WANDB_API_KEY`: For experiment tracking with Weights & Biases

## Step 3: Dashboard Deployment

The Axon Dashboard is a separate React application that displays real-time metrics and allows interaction with the AI.

### Dashboard Repository

The dashboard is located at: `/home/ubuntu/axon-dashboard`

### Deploy Dashboard to GitHub Pages

1. Build the dashboard:
   ```bash
   cd axon-dashboard
   npm install
   npm run build
   ```

2. The workflow automatically deploys to GitHub Pages when you push changes.

3. Access the dashboard at: `https://appointeasedev-oss.github.io/axon-dashboard`

## Step 4: Enable Autonomous Operation

### Activate the Main Workflow

1. Go to: `https://github.com/appointeasedev-oss/axon-ai/actions`
2. Select the "Deploy Dashboard & Autonomous Improvement" workflow
3. Click "Enable workflow"
4. The workflow will automatically run:
   - **Every hour** (scheduled)
   - **On push** to the main branch
   - **Manually** via "Run workflow" button

### What Happens in Each Cycle

1. **Dashboard Deployment** (5-10 minutes)
   - Builds the React dashboard
   - Deploys to GitHub Pages
   - Updates metrics display

2. **Training** (10-30 minutes, depending on data size)
   - Runs `src/train.py`
   - Generates `metrics.json` with performance data
   - Saves model checkpoints

3. **Self-Improvement** (5-15 minutes)
   - Analyzes source code and metrics
   - Uses OpenAI API to propose improvements
   - Applies changes to the codebase
   - Commits and pushes changes automatically

## Step 5: Monitoring Progress

### Via GitHub Actions

1. Go to: `https://github.com/appointeasedev-oss/axon-ai/actions`
2. View workflow runs in real-time
3. Click on any run to see detailed logs
4. Check the "Train and Improve" job for self-improvement details

### Via Dashboard

1. Access: `https://appointeasedev-oss.github.io/axon-dashboard`
2. View real-time metrics:
   - Training Loss
   - Model Accuracy
   - Number of Parameters
   - Improvement Count
3. Check System Status panel for GPU/Memory usage
4. Review Recent Improvements list
5. Chat with AXON to ask about its progress

### Via Repository

1. Check recent commits at: `https://github.com/appointeasedev-oss/axon-ai/commits/main`
2. Look for commits with message "AXON: Autonomous improvement cycle"
3. Review `metrics.json` for latest performance data

## Step 6: Customization

### Modify Training Parameters

Edit `src/train.py`:
```python
config = AxonConfig(
    vocab_size=50257,      # Vocabulary size
    n_embd=128,            # Embedding dimension
    n_head=4,              # Number of attention heads
    n_layer=4,             # Number of transformer layers
    block_size=128,        # Context window size
    dropout=0.1            # Dropout rate
)
```

### Adjust Improvement Frequency

Edit `.github/workflows/deploy-and-improve.yml`:
```yaml
on:
  schedule:
    - cron: '0 * * * *'  # Change this cron expression
```

Common cron patterns:
- `0 */6 * * *` - Every 6 hours
- `0 0 * * *` - Daily at midnight
- `*/30 * * * *` - Every 30 minutes

### Customize Dashboard

The dashboard is built with React and Tailwind CSS. Modify:
- `client/src/pages/Dashboard.tsx` - Main dashboard layout
- `client/src/components/NeuralNetwork.tsx` - Neural network visualization
- `client/src/components/MetricCard.tsx` - Metric display cards
- `client/src/components/ChatInterface.tsx` - Chat interface

## Step 7: Troubleshooting

### Workflow Fails with API Error

**Problem**: "OpenAI API key not found"
- **Solution**: Verify `OPENAI_API_KEY` is set in repository secrets
- Go to Settings → Secrets and variables → Actions
- Ensure the key is correctly copied (no extra spaces)

### Dashboard Not Updating

**Problem**: Dashboard shows old metrics
- **Solution**: 
  - Check if workflow is enabled: Actions → Enable workflow
  - Manually trigger: Actions → Run workflow
  - Check workflow logs for errors

### Git Push Fails in Workflow

**Problem**: "Permission denied" when pushing changes
- **Solution**: 
  - Verify `GITHUB_TOKEN` has write permissions
  - Check branch protection rules don't block automated commits
  - Ensure the workflow has `token: ${{ secrets.GITHUB_TOKEN }}`

### High API Costs

**Problem**: OpenAI API usage is expensive
- **Solution**:
  - Reduce workflow frequency in cron schedule
  - Use `gpt-4-mini` instead of full GPT-4 (already configured)
  - Implement rate limiting in `src/improve.py`

## Step 8: Advanced Features

### Custom Training Data

Replace the dummy training loop in `src/train.py` with your own data:
```python
def train():
    # Load your dataset
    dataset = load_your_dataset()
    
    # Train the model
    for epoch in range(num_epochs):
        for batch in dataset:
            # Training logic
            pass
```

### Model Versioning

The system automatically saves model checkpoints. Access them at:
- `models/axon_latest.pt` - Latest model weights
- `models/axon_backup_*.pt` - Previous versions

### Integrate with Hugging Face

Add to `src/improve.py` to upload models:
```python
from huggingface_hub import upload_folder
upload_folder(
    repo_id="appointeasedev-oss/axon",
    folder_path="models/",
    token=os.getenv("HUGGINGFACE_TOKEN")
)
```

## Performance Expectations

### First Cycle (Initial Setup)
- Dashboard deployment: ~5 minutes
- Training: ~15 minutes
- Self-improvement: ~10 minutes
- **Total**: ~30 minutes

### Subsequent Cycles
- Dashboard deployment: ~5 minutes
- Training: ~20 minutes (with more data)
- Self-improvement: ~15 minutes (more complex analysis)
- **Total**: ~40 minutes per cycle

### GitHub Actions Limits
- Free tier: 2,000 minutes/month
- With hourly cycles: ~730 hours/month (exceeds free tier)
- **Recommendation**: Use 6-hour or daily cycles for free accounts

## Next Steps

1. **Enable the workflow** by pushing the configuration files
2. **Set the OPENAI_API_KEY** secret in GitHub
3. **Manually trigger** the first workflow run
4. **Monitor** the dashboard at the GitHub Pages URL
5. **Customize** training data and parameters as needed

## Support & Resources

- **AXON Repository**: https://github.com/appointeasedev-oss/axon-ai
- **Dashboard Repository**: https://github.com/appointeasedev-oss/axon-dashboard
- **OpenAI Documentation**: https://platform.openai.com/docs
- **GitHub Actions Documentation**: https://docs.github.com/en/actions

---

**AXON is a living experiment in recursive AI improvement. Start small, iterate fast, and watch it evolve!**
