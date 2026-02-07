# AXON: Autonomous Self-Improving AI System

**AXON is a revolutionary self-improving AI that runs entirely on GitHub, continuously enhancing its own code and capabilities with zero manual intervention.**

## 🚀 Quick Start (10 Minutes)

### 1. Enable GitHub Pages for Dashboard

```bash
# Go to: https://github.com/appointeasedev-oss/axon-dashboard/settings/pages
# Under "Build and deployment":
# - Source: Select "GitHub Actions"
# - Save
```

**Dashboard will be available at:** `https://appointeasedev-oss.github.io/axon-dashboard`

### 2. Add OpenAI API Key Secret

```bash
# Go to: https://github.com/appointeasedev-oss/axon-ai/settings/secrets/actions
# Click "New repository secret"
# Name: OPENAI_API_KEY
# Value: [Your OpenAI API key from https://platform.openai.com/api-keys]
# Click "Add secret"
```

### 3. Create Continuous Improvement Workflow

Create file: `.github/workflows/continuous-improve.yml`

**Via GitHub Web UI:**
1. Go to: `https://github.com/appointeasedev-oss/axon-ai`
2. Click **Add file** → **Create new file**
3. Name: `.github/workflows/continuous-improve.yml`
4. Copy content from `GITHUB_PAGES_SETUP.md` (Continuous Autonomous Improvement section)
5. Click **Commit changes**

### 4. Create Dashboard Deployment Workflow

Create file: `.github/workflows/deploy.yml` in axon-dashboard repository

**Via GitHub Web UI:**
1. Go to: `https://github.com/appointeasedev-oss/axon-dashboard`
2. Click **Add file** → **Create new file**
3. Name: `.github/workflows/deploy.yml`
4. Copy content from `GITHUB_PAGES_SETUP.md` (Dashboard Deployment Workflow section)
5. Click **Commit changes**

### 5. Done! 🎉

AXON is now running continuously. Check:
- **Dashboard:** `https://appointeasedev-oss.github.io/axon-dashboard`
- **Improvements:** `https://github.com/appointeasedev-oss/axon-ai/commits/main`
- **Workflow Status:** `https://github.com/appointeasedev-oss/axon-ai/actions`

---

## 📊 System Architecture

### Core Components

| Component | Purpose | Location |
|-----------|---------|----------|
| **Model** | Custom transformer built from scratch | `src/model.py` |
| **Training** | Trains the model and generates metrics | `src/train.py` |
| **Self-Improvement** | Analyzes code and proposes improvements | `src/improve.py` |
| **Dashboard** | Real-time monitoring interface | `axon-dashboard/` |
| **Workflows** | GitHub Actions automation | `.github/workflows/` |

### The Improvement Cycle

```
Every Hour:
├─ 1. Checkout latest code
├─ 2. Run training (generates metrics.json)
├─ 3. Self-improvement engine analyzes:
│  ├─ Current source code
│  ├─ Performance metrics
│  └─ Proposes improvements via OpenAI
├─ 4. Apply changes to source files
├─ 5. Commit and push to main
└─ 6. Dashboard auto-deploys with new metrics
```

---

## 🎯 What AXON Can Improve

Each autonomous cycle, AXON can modify:

- **Model Architecture** - Add/remove layers, adjust attention heads, change embedding dimensions
- **Training Parameters** - Learning rate, batch size, dropout, weight decay
- **Code Optimization** - Refactor for speed, improve memory efficiency, better error handling
- **Training Data** - Filter low-quality samples, augment data, balance classes
- **Hyperparameters** - Adjust based on real performance metrics

---

## 📈 Monitoring Progress

### Real-Time Dashboard

Access at: `https://appointeasedev-oss.github.io/axon-dashboard`

**Features:**
- 🧠 Animated neural network visualization
- 📊 Real-time metric cards (loss, accuracy, parameters)
- 💻 System status (GPU, memory, training speed)
- 📝 Recent improvements list
- 💬 Chat interface to interact with AXON

### GitHub Commits

Each improvement creates a commit: `https://github.com/appointeasedev-oss/axon-ai/commits/main`

Look for commits with message: `🤖 AXON: [Improvement Name]`

### Workflow Logs

View detailed execution logs: `https://github.com/appointeasedev-oss/axon-ai/actions`

---

## 🔧 Configuration

### Change Improvement Frequency

Edit `.github/workflows/continuous-improve.yml`:

```yaml
on:
  schedule:
    - cron: '0 * * * *'  # Change this line
```

**Common patterns:**
- `0 * * * *` - Every hour (default)
- `0 */6 * * *` - Every 6 hours
- `0 0 * * *` - Daily at midnight
- `0 0 * * 0` - Weekly on Sunday

### Adjust Model Size

Edit `src/model.py`:

```python
config = AxonConfig(
    vocab_size=50257,      # Vocabulary size
    n_embd=256,            # Larger = more capacity (was 128)
    n_head=8,              # More heads = better attention (was 4)
    n_layer=8,             # More layers = deeper model (was 4)
    block_size=256,        # Longer context (was 128)
    dropout=0.1
)
```

### Customize Improvement Logic

Edit `src/improve.py` to change what gets improved:

```python
def analyze_and_propose_improvements(source_code, metrics):
    # Customize the prompt to focus on specific improvements
    prompt = f"""Your custom improvement strategy here..."""
```

---

## 💰 Cost Management

### GitHub Actions Free Tier

- **2,000 minutes/month** for private repositories
- **Unlimited** for public repositories
- Hourly cycles = ~730 hours/month (exceeds free tier)

### Recommendations

**For Free Tier:**
- Use 6-hour or daily cycles
- Cron: `0 0 * * *` (daily at midnight)

**For Frequent Updates:**
- Upgrade to GitHub Pro ($4/month)
- Or use self-hosted runners

### OpenAI API Costs

- **gpt-4-mini**: ~$0.15 per improvement cycle
- **Daily cycles**: ~$4.50/month
- **Hourly cycles**: ~$108/month

**To reduce costs:**
- Use daily instead of hourly cycles
- Implement local improvement logic (no API calls)
- Use cheaper models (gpt-3.5-turbo)

---

## 🚨 Troubleshooting

### Workflow Not Running

**Problem:** Workflow doesn't appear in Actions tab

**Solution:**
1. Verify file exists: `.github/workflows/continuous-improve.yml`
2. Go to Actions tab → Click "Enable workflows"
3. Manually trigger: Click "Run workflow" button

### OpenAI API Error

**Problem:** "OpenAI API key not found"

**Solution:**
1. Go to: `https://github.com/appointeasedev-oss/axon-ai/settings/secrets/actions`
2. Verify `OPENAI_API_KEY` exists and is correct
3. Test key at: https://platform.openai.com/account/api-keys

### Dashboard Not Updating

**Problem:** Dashboard shows stale metrics

**Solution:**
1. Check: `https://github.com/appointeasedev-oss/axon-dashboard/actions`
2. Verify "Build and Deploy Dashboard" workflow ran
3. Check for deployment errors in logs
4. Hard refresh dashboard (Ctrl+Shift+R)

### Git Push Fails

**Problem:** "Permission denied" when pushing

**Solution:**
1. Go to: `https://github.com/appointeasedev-oss/axon-ai/settings/actions`
2. Under "Workflow permissions", select "Read and write permissions"
3. Click "Save"

---

## 📚 Documentation

- **[SETUP_GUIDE.md](SETUP_GUIDE.md)** - Detailed setup instructions
- **[GITHUB_PAGES_SETUP.md](GITHUB_PAGES_SETUP.md)** - GitHub Pages & workflows configuration
- **[AXON_AI_Report.md](AXON_AI_Report.md)** - Architecture and design documentation

---

## 🎓 How It Works (Technical)

### Self-Improvement Engine Flow

```python
1. Gather Context
   ├─ Read all source code files
   └─ Load metrics.json (performance data)

2. Analyze
   ├─ Send code + metrics to OpenAI
   └─ Get improvement suggestions

3. Apply
   ├─ Modify source files
   └─ Update configuration

4. Commit
   ├─ Stage changes
   ├─ Create commit message
   ├─ Push to main
   └─ Trigger dashboard deployment

5. Monitor
   ├─ Dashboard updates with new metrics
   ├─ Logs show improvement details
   └─ Cycle repeats
```

### Model Architecture

- **Type:** Transformer (from scratch, no pretrained weights)
- **Size:** ~1M parameters (configurable)
- **Attention:** Multi-head self-attention
- **Layers:** 4 transformer blocks (configurable)
- **Training:** PyTorch with AdamW optimizer

---

## 🌟 Features

✅ **Fully Autonomous** - Runs without human intervention
✅ **Self-Modifying** - Changes its own source code
✅ **GitHub Native** - Everything on GitHub Actions
✅ **Free Forever** - Open source, no paid services required
✅ **Real-Time Dashboard** - Monitor progress live
✅ **Version Controlled** - Every change tracked in git
✅ **Scalable** - Grow from 1M to billions of parameters
✅ **Transparent** - All improvements are visible and auditable

---

## 🔮 Future Enhancements

- [ ] Multi-GPU distributed training
- [ ] Automatic dataset curation
- [ ] Neural architecture search (NAS)
- [ ] Model pruning and quantization
- [ ] Federated learning support
- [ ] Web UI for parameter tuning
- [ ] Integration with Hugging Face Hub
- [ ] Experiment tracking with Weights & Biases

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review workflow logs: `https://github.com/appointeasedev-oss/axon-ai/actions`
3. Check dashboard: `https://appointeasedev-oss.github.io/axon-dashboard`

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙏 Acknowledgments

Built with:
- PyTorch for deep learning
- OpenAI API for intelligent improvements
- GitHub Actions for automation
- React for the dashboard

---

**AXON: The AI that improves itself. Every hour. Forever.**

🚀 Start now: Follow the Quick Start section above!
