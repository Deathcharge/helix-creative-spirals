# Helix Creative Spirals

**AI-powered social media automation with creative content generation**

Combines [Helix Narrative Engine](https://github.com/Deathcharge/helix-narrative-engine) with [Helix Spirals](https://github.com/Deathcharge/helix-spirals) to automate creative content generation and distribution across social media platforms.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

---

## Features

- **Automated Content Generation**: Generate stories, articles, and creative content on-demand
- **Multi-Platform Distribution**: Publish to Twitter, LinkedIn, Discord, Slack, and more
- **Scheduled Workflows**: Run content generation and distribution on a schedule
- **Social Media Integration**: 130+ pre-built connectors via Helix Spirals
- **Quality Control**: Built-in quality assessment and ethical compliance
- **Analytics**: Track engagement and performance metrics

---

## Quick Start

### Installation

```bash
git clone https://github.com/Deathcharge/helix-creative-spirals.git
cd helix-creative-spirals
pip install -e .
```

### Basic Usage

```python
from helix_creative_spirals import createContentWorkflow

# Create a workflow that generates and publishes content
workflow = createContentWorkflow({
    "name": "Daily Story Generator",
    "trigger": "schedule",
    "schedule": "0 9 * * *",  # 9 AM daily
    "steps": [
        {
            "type": "generate",
            "engine": "narrative",
            "prompt": "A cyberpunk heist story",
            "preset": "balanced"
        },
        {
            "type": "format",
            "target": "twitter",
            "maxLength": 280
        },
        {
            "type": "publish",
            "platform": "twitter"
        },
        {
            "type": "archive",
            "platform": "notion"
        }
    ]
})

await workflow.execute()
```

---

## Workflow Templates

### 1. Twitter Story Generator
Generates short stories optimized for Twitter threads.

### 2. LinkedIn Content Scheduler
Generates professional insights and publishes to LinkedIn.

### 3. Multi-Platform Distributor
Generates once, distributes to multiple platforms with format adaptation.

### 4. Engagement Monitor
Generates content and tracks engagement metrics.

---

## Architecture

### Workflow Pipeline

1. **Generation** - Helix Narrative Engine creates content
2. **Formatting** - Adapt content for target platform
3. **Publishing** - Distribute via Helix Spirals connectors
4. **Archiving** - Store in Notion/database for reference
5. **Analytics** - Track engagement and performance

---

## Environment Variables

```bash
# Narrative Engine
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GEMINI_API_KEY="AIza..."

# Spirals Integrations
export TWITTER_API_KEY="..."
export LINKEDIN_ACCESS_TOKEN="..."
export DISCORD_WEBHOOK_URL="..."
export NOTION_API_KEY="..."
```

---

## Related Projects

- [Helix Narrative Engine](https://github.com/Deathcharge/helix-narrative-engine) - Creative content generation
- [Helix Spirals](https://github.com/Deathcharge/helix-spirals) - Workflow automation
- [Helix Orchestration](https://github.com/Deathcharge/helix-orchestration) - Multi-agent coordination
- [Helix Ethics](https://github.com/Deathcharge/helix-ethics) - Ethical AI governance

---

**License:** Apache 2.0

**Built with ❤️ by the Helix Team**
