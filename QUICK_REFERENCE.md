# AXON Quick Reference Guide

## ⚡ 3-Step Setup (5 Minutes)

### Step 1: Enable GitHub Pages
```
Go to: https://github.com/appointeasedev-oss/axon-dashboard/settings/pages
Select: GitHub Actions as source
Save
```
✅ Dashboard will be at: `https://appointeasedev-oss.github.io/axon-dashboard`

### Step 2: Add API Key Secret
```
Go to: https://github.com/appointeasedev-oss/axon-ai/settings/secrets/actions
New secret → OPENAI_API_KEY → [Your key from https://platform.openai.com/api-keys]
```

### Step 3: Create Workflow Files
Create these 2 files via GitHub Web UI:

**File 1:** `.github/workflows/continuous-improve.yml` in axon-ai repo
```yaml
name: Continuous Autonomous Improvement
on:
  schedule:
    - cron: '0 * * * *'
  workflow_dispatch:
  push:
    branches: [main]

jobs:
  improve:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          token: ${{ secrets.GITHUB_TOKEN }}
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - run: pip install torch openai requests
      - run: python src/train.py
        continue-on-error: true
      - run: python src/improve.py
        env:
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        continue-on-error: true
      - run: |
          git config user.name "AXON-AI"
          git config user.email "axon@self-improve.ai"
          if [[ -n $(git status -s) ]]; then
            git add -A
            git commit -m "🤖 AXON: Improvement cycle"
            git push origin main
          fi
        continue-on-error: true
```

**File 2:** `.github/workflows/deploy.yml` in axon-dashboard repo
```yaml
name: Build and Deploy Dashboard
on:
  push:
    branches: [main]
  workflow_dispatch:

jobs:
  build-and-deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: read
      pages: write
      id-token: write
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
      - run: npm install || pnpm install || yarn install
      - run: npm run build || pnpm build || yarn build
      - uses: actions/upload-pages-artifact@v2
        with:
          path: 'dist'
      - uses: actions/deploy-pages@v2
```

---

## 📊 Access Points

| What | Where |
|------|-------|
| **Dashboard** | `https://appointeasedev-oss.github.io/axon-dashboard` |
| **Improvements** | `https://github.com/appointeasedev-oss/axon-ai/commits/main` |
| **Workflow Status** | `https://github.com/appointeasedev-oss/axon-ai/actions` |
| **API Key Setup** | `https://github.com/appointeasedev-oss/axon-ai/settings/secrets/actions` |
| **GitHub Pages Settings** | `https://github.com/appointeasedev-oss/axon-dashboard/settings/pages` |

---

## 🔄 The Improvement Cycle (Runs Every Hour)

```
00:00 - Trigger workflow
00:01 - Checkout code
00:02 - Run training (15 min)
00:17 - Run self-improvement (10 min)
00:27 - Commit & push
00:30 - Dashboard deploys (5 min)
00:35 - Cycle complete, wait 25 min
```

---

## 🎯 What Gets Improved

- Model layers and attention heads
- Training parameters (learning rate, batch size)
- Code optimization and efficiency
- Hyperparameters based on metrics

---

## 💡 Customization

### Change Frequency
Edit cron in `.github/workflows/continuous-improve.yml`:
- `0 * * * *` = Every hour (default)
- `0 0 * * *` = Daily
- `0 0 * * 0` = Weekly

### Bigger Model
Edit `src/model.py`:
```python
config = AxonConfig(
    n_embd=256,    # was 128
    n_head=8,      # was 4
    n_layer=8,     # was 4
)
```

---

## ✅ Verify It's Working

1. **Dashboard loads?** → `https://appointeasedev-oss.github.io/axon-dashboard`
2. **Workflow running?** → Check Actions tab
3. **Commits appearing?** → Look for 🤖 AXON commits
4. **Metrics updating?** → Check dashboard metrics cards

---

## 🚨 Common Issues

| Issue | Solution |
|-------|----------|
| Workflow not running | Enable in Actions tab, then run manually |
| API key error | Verify `OPENAI_API_KEY` in secrets (no extra spaces) |
| Dashboard not updating | Hard refresh (Ctrl+Shift+R), check Actions logs |
| Git push fails | Go to Settings → Actions → Enable "Read and write permissions" |

---

## 📞 Quick Links

- OpenAI API Keys: https://platform.openai.com/api-keys
- GitHub Actions Docs: https://docs.github.com/en/actions
- AXON Repository: https://github.com/appointeasedev-oss/axon-ai
- Dashboard Repository: https://github.com/appointeasedev-oss/axon-dashboard

---

## 🎉 You're Done!

AXON is now running continuously and improving itself every hour!

Monitor it at: `https://appointeasedev-oss.github.io/axon-dashboard`
