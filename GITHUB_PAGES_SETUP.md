# GitHub Pages Setup for Axon Dashboard

## Quick Start (5 Minutes)

### Step 1: Enable GitHub Pages in axon-dashboard Repository

1. Go to: `https://github.com/appointeasedev-oss/axon-dashboard`
2. Click **Settings** (top right)
3. Scroll down to **Pages** section (left sidebar)
4. Under "Build and deployment":
   - Source: Select **GitHub Actions**
   - This enables automatic deployment from Actions workflows

### Step 2: The Dashboard Will Auto-Deploy

Once GitHub Actions is enabled as the source:
- Every push to `main` branch triggers automatic build and deployment
- Dashboard becomes available at: `https://appointeasedev-oss.github.io/axon-dashboard`
- Updates happen automatically within 2-5 minutes

---

## Continuous Autonomous Improvement Setup

### Step 1: Create the Main Workflow File

Create this file in the axon-ai repository at: `.github/workflows/continuous-improve.yml`

**Via GitHub Web UI:**
1. Go to: `https://github.com/appointeasedev-oss/axon-ai`
2. Click **Add file** → **Create new file**
3. Name: `.github/workflows/continuous-improve.yml`
4. Paste the content below:

```yaml
name: Continuous Autonomous Improvement

on:
  schedule:
    - cron: '0 * * * *'  # Every hour
  workflow_dispatch:     # Manual trigger
  push:
    branches:
      - main

jobs:
  improve:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v4
        with:
          fetch-depth: 0
          token: ${{ secrets.GITHUB_TOKEN }}

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install torch openai requests

      - name: Run Training
        run: python src/train.py
        continue-on-error: true

      - name: Run Self-Improvement
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: python src/improve.py
        continue-on-error: true

      - name: Configure Git
        run: |
          git config user.name "AXON-AI"
          git config user.email "axon@self-improve.ai"

      - name: Commit improvements
        run: |
          if [[ -n $(git status -s) ]]; then
            git add -A
            git commit -m "🤖 AXON: Autonomous improvement cycle #$(date +%s)"
            git push origin main
          else
            echo "No changes to commit"
          fi
        continue-on-error: true

      - name: Update metrics
        run: |
          if [ -f metrics.json ]; then
            echo "=== Current Metrics ==="
            cat metrics.json
          fi
```

5. Click **Commit changes** → **Commit directly to main branch**

### Step 2: Create the Dashboard Deployment Workflow

Create this file in the axon-dashboard repository at: `.github/workflows/deploy.yml`

**Via GitHub Web UI:**
1. Go to: `https://github.com/appointeasedev-oss/axon-dashboard`
2. Click **Add file** → **Create new file**
3. Name: `.github/workflows/deploy.yml`
4. Paste the content below:

```yaml
name: Build and Deploy Dashboard

on:
  push:
    branches:
      - main
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pages: write
      id-token: write

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '18'

      - name: Install dependencies
        run: npm install || pnpm install || yarn install

      - name: Build
        run: npm run build || pnpm build || yarn build

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v2
        with:
          path: 'dist'

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v2
```

5. Click **Commit changes** → **Commit directly to main branch**

### Step 3: Set Required GitHub Secrets

#### For axon-ai Repository:

1. Go to: `https://github.com/appointeasedev-oss/axon-ai/settings/secrets/actions`
2. Click **New repository secret**
3. Add these secrets:

| Name | Value | Where to Get |
|------|-------|-------------|
| `OPENAI_API_KEY` | Your OpenAI API key | https://platform.openai.com/api-keys |
| `GITHUB_TOKEN` | (Auto-provided) | Automatically available |

#### For axon-dashboard Repository:

1. Go to: `https://github.com/appointeasedev-oss/axon-dashboard/settings/secrets/actions`
2. Click **New repository secret**
3. Add:

| Name | Value |
|------|-------|
| `GITHUB_TOKEN` | (Auto-provided) |

---

## Verify Everything is Working

### Check Workflow Status

1. **AXON-AI Repository:**
   - Go to: `https://github.com/appointeasedev-oss/axon-ai/actions`
   - You should see "Continuous Autonomous Improvement" workflow
   - Click on it to see runs

2. **AXON-Dashboard Repository:**
   - Go to: `https://github.com/appointeasedev-oss/axon-dashboard/actions`
   - You should see "Build and Deploy Dashboard" workflow
   - Click on it to see deployment runs

### Access the Dashboard

- **URL:** `https://appointeasedev-oss.github.io/axon-dashboard`
- **Status:** Should be live and updating every hour

### Monitor Improvements

1. Go to: `https://github.com/appointeasedev-oss/axon-ai/commits/main`
2. Look for commits with message "🤖 AXON: Autonomous improvement cycle"
3. Each commit represents a completed improvement cycle

---

## How Continuous Improvement Works

### The Cycle (Repeats Every Hour)

```
1. TRIGGER (0:00)
   ↓
2. CHECKOUT CODE (0:01)
   ↓
3. RUN TRAINING (0:02-0:15)
   - Train model on data
   - Generate metrics.json
   ↓
4. RUN SELF-IMPROVEMENT (0:16-0:25)
   - Read source code
   - Analyze metrics
   - Use OpenAI to propose improvements
   - Apply changes to files
   ↓
5. COMMIT & PUSH (0:26-0:27)
   - Commit all changes
   - Push to main branch
   ↓
6. DASHBOARD AUTO-DEPLOYS (0:28-0:33)
   - Build new dashboard
   - Deploy to GitHub Pages
   ↓
7. CYCLE COMPLETE (0:34)
   - Wait 26 minutes for next cycle
```

### What Gets Improved

Each cycle, AXON can modify:
- **Model Architecture** - Add/remove layers, adjust attention heads
- **Training Parameters** - Learning rate, batch size, dropout
- **Code Optimization** - Refactor for speed, improve efficiency
- **Training Data** - Filter/curate better datasets
- **Hyperparameters** - Adjust based on performance metrics

---

## Troubleshooting

### Workflow Doesn't Run

**Problem:** "Continuous Autonomous Improvement" workflow doesn't appear

**Solution:**
1. Verify the file exists: `https://github.com/appointeasedev-oss/axon-ai/blob/main/.github/workflows/continuous-improve.yml`
2. Go to Actions tab and click "Enable workflows"
3. Manually trigger: Click "Run workflow" button

### OpenAI API Error

**Problem:** Workflow fails with "OpenAI API key not found"

**Solution:**
1. Go to: `https://github.com/appointeasedev-oss/axon-ai/settings/secrets/actions`
2. Verify `OPENAI_API_KEY` exists
3. Ensure no extra spaces in the key value
4. Test the key at: https://platform.openai.com/account/api-keys

### Dashboard Not Updating

**Problem:** Dashboard shows old metrics or doesn't deploy

**Solution:**
1. Check: `https://github.com/appointeasedev-oss/axon-dashboard/actions`
2. Verify "Build and Deploy Dashboard" workflow ran
3. Check deployment logs for errors
4. Try manual trigger: Click "Run workflow"

### Git Push Fails

**Problem:** "Permission denied" when pushing changes

**Solution:**
1. Go to: `https://github.com/appointeasedev-oss/axon-ai/settings/actions`
2. Under "Workflow permissions", select "Read and write permissions"
3. Click "Save"

### High API Costs

**Problem:** OpenAI API usage is expensive

**Solution:**
- Change cron schedule to less frequent:
  - `0 0 * * *` - Daily instead of hourly
  - `0 0 * * 0` - Weekly
  - `0 0 1 * *` - Monthly

---

## Advanced Configuration

### Change Improvement Frequency

Edit `.github/workflows/continuous-improve.yml`:

```yaml
on:
  schedule:
    - cron: '0 */6 * * *'  # Every 6 hours
```

Common patterns:
- `0 * * * *` - Every hour
- `0 */6 * * *` - Every 6 hours
- `0 0 * * *` - Daily at midnight
- `0 0 * * 0` - Weekly on Sunday
- `0 0 1 * *` - Monthly on 1st

### Custom Improvement Logic

Edit `src/improve.py` to customize what gets improved:

```python
# Add custom improvement strategies
def analyze_and_improve():
    # Your custom logic here
    pass
```

### Link Dashboard to Metrics

The dashboard automatically fetches metrics from the repository. To enable live updates:

1. Dashboard reads from: `https://raw.githubusercontent.com/appointeasedev-oss/axon-ai/main/metrics.json`
2. Updates every 30 seconds
3. Displays in real-time on the dashboard

---

## Success Checklist

- [ ] `.github/workflows/continuous-improve.yml` created in axon-ai
- [ ] `.github/workflows/deploy.yml` created in axon-dashboard
- [ ] `OPENAI_API_KEY` secret added to axon-ai
- [ ] GitHub Pages enabled in axon-dashboard settings
- [ ] First workflow run completed successfully
- [ ] Dashboard accessible at `https://appointeasedev-oss.github.io/axon-dashboard`
- [ ] Improvement commits appearing in axon-ai repository
- [ ] Metrics updating in real-time on dashboard

---

## Next Steps

1. **Create both workflow files** using the instructions above
2. **Set the OpenAI API key** secret
3. **Enable GitHub Pages** for the dashboard
4. **Wait for first cycle** (up to 1 hour)
5. **Monitor the dashboard** and repository commits
6. **Customize** improvement logic as needed

**AXON is now running continuously and improving itself every hour!**
