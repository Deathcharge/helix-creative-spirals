# Helix Creative Spirals - Example Workflows

Complete examples demonstrating how to use Helix Creative Spirals for various content generation and distribution scenarios.

---

## 📚 Examples Overview

### 1. Quick Tweet (`01_quick_tweet.py`)
**Purpose**: Generate and publish a tweet on-demand

**Use Case**: Quick content creation without scheduling

**Key Features**:
- Fast preset for quick generation
- Single platform publishing
- Immediate execution

**Run**:
```bash
python examples/01_quick_tweet.py
```

**Output**:
- Generated tweet
- Published URL
- Platform confirmation

---

### 2. Daily Story Generator (`02_daily_story_generator.py`)
**Purpose**: Automatically generate stories every morning

**Use Case**: Build consistent content schedule

**Key Features**:
- Scheduled execution (9 AM daily)
- Balanced preset for quality
- Notion archiving
- Long-running scheduler

**Run**:
```bash
python examples/02_daily_story_generator.py
```

**Output**:
- Workflow configuration
- Scheduler status
- Instructions for starting/stopping

---

### 3. Multi-Platform Distribution (`03_multi_platform_distribution.py`)
**Purpose**: Generate once, publish to multiple platforms

**Use Case**: Maximize reach with minimal effort

**Key Features**:
- Platform-specific formatting
- Twitter, LinkedIn, Discord support
- Notion archiving
- Single content generation

**Run**:
```bash
python examples/03_multi_platform_distribution.py
```

**Output**:
- Generated content
- Publication status per platform
- Archive confirmation

---

### 4. Engagement Monitor (`04_engagement_monitor.py`)
**Purpose**: Track engagement metrics across platforms

**Use Case**: Measure content performance

**Key Features**:
- Multi-platform tracking
- Analytics collection
- Notion reporting
- Scheduled monitoring

**Run**:
```bash
python examples/04_engagement_monitor.py
```

**Output**:
- Analytics configuration
- Tracking setup
- Reporting destination

---

### 5. Custom Agent Configuration (`05_custom_agents.py`)
**Purpose**: Fine-tune agent parameters for specific needs

**Use Case**: Optimize generation for your use case

**Key Features**:
- Custom agent selection
- Temperature tuning
- Provider selection
- Agent multiplicity

**Run**:
```bash
python examples/05_custom_agents.py
```

**Output**:
- Agent configuration details
- Generated content
- Quality metrics

---

## 🚀 Quick Start

### Installation

```bash
# Install helix-creative-spirals
pip install helix-creative-spirals

# Or install from source
git clone https://github.com/Deathcharge/helix-creative-spirals.git
cd helix-creative-spirals
pip install -e .
```

### Environment Setup

```bash
# Set required API keys
export OPENAI_API_KEY="sk-..."
export ANTHROPIC_API_KEY="sk-ant-..."
export GEMINI_API_KEY="AIza..."
export XAI_API_KEY="xai-..."
export SONAR_API_KEY="pplx-..."

# Social media platforms (optional)
export TWITTER_API_KEY="..."
export LINKEDIN_ACCESS_TOKEN="..."
export DISCORD_WEBHOOK_URL="..."
export NOTION_API_KEY="..."
```

### Run an Example

```bash
# Quick tweet
python examples/01_quick_tweet.py

# Daily story (setup only)
python examples/02_daily_story_generator.py

# Multi-platform
python examples/03_multi_platform_distribution.py

# Engagement monitor
python examples/04_engagement_monitor.py

# Custom agents
python examples/05_custom_agents.py
```

---

## 🎯 Choosing the Right Example

| Need | Example | Trigger |
|------|---------|---------|
| Quick content | Quick Tweet | Manual |
| Consistent schedule | Daily Story | Schedule |
| Maximum reach | Multi-Platform | Manual/Schedule |
| Track performance | Engagement Monitor | Schedule |
| Fine-tune generation | Custom Agents | Manual |

---

## 🔧 Customization

### Modify Prompts
```python
workflow = createContentWorkflow({
    "steps": [
        {
            "type": "generate",
            "prompt": "Your custom prompt here",
            "preset": "balanced"
        }
    ]
})
```

### Change Schedule
```python
workflow = createContentWorkflow({
    "trigger": "schedule",
    "schedule": "0 14 * * *",  # 2 PM daily
    ...
})
```

### Add Platforms
```python
workflow = createContentWorkflow({
    "steps": [
        {
            "type": "publish",
            "platforms": ["twitter", "linkedin", "discord", "slack"]
        }
    ]
})
```

### Adjust Agent Settings
```python
custom_agents = [
    {
        "agentId": "agni",
        "provider": "openai",
        "temperature": 0.95,  # More creative
        "multiplicity": 3  # Run 3 times
    }
]

result = await generateNarrative(prompt, GenerationOptions(customAgents=custom_agents))
```

---

## 📊 Understanding Output

### Generation Result
```python
{
    "success": True,
    "generationId": "gen_1234567890_abc123def",
    "title": "Story Title",
    "content": "Full story content...",
    "metadata": {
        "wordCount": 1850,
        "qualityScore": 0.87,
        "ethicalApproval": True,
        "agentContributions": {...}
    }
}
```

### Workflow Execution Result
```python
{
    "workflowId": "wf_1234567890_abc123def",
    "executionId": "exec_1234567890_abc123def",
    "success": True,
    "steps": [
        {
            "index": 0,
            "type": "generate",
            "success": True,
            "result": {...}
        },
        {
            "index": 1,
            "type": "publish",
            "success": True,
            "result": {
                "published": {
                    "twitter": {
                        "success": True,
                        "url": "https://twitter.com/..."
                    }
                }
            }
        }
    ]
}
```

---

## 🐛 Troubleshooting

### API Key Errors
```
ValueError: OPENAI_API_KEY environment variable not set
```
**Solution**: Set environment variables before running examples

### Generation Timeout
```
asyncio.TimeoutError
```
**Solution**: Use a faster preset or increase timeout

### Platform Publishing Failed
```
Error: Failed to publish to twitter
```
**Solution**: Check API credentials and rate limits

---

## 📚 Learn More

- [Helix Creative Spirals Documentation](https://github.com/Deathcharge/helix-creative-spirals)
- [Helix Narrative Engine Documentation](https://github.com/Deathcharge/helix-narrative-engine)
- [Helix Spirals Documentation](https://github.com/Deathcharge/helix-spirals)

---

## 🤝 Contributing

Found a bug or have an idea for a new example? Open an issue or submit a PR!

---

**Happy automating! 🚀**
