"""
Example 3: Multi-Platform Distribution

Generate content once and automatically distribute to multiple platforms
(Twitter, LinkedIn, Discord) with platform-specific formatting.
"""

import asyncio
from helix_creative_spirals import createContentWorkflow


async def main():
    """Distribute content to multiple platforms"""
    
    # Create a multi-platform workflow
    workflow = createContentWorkflow({
        "name": "Multi-Platform Campaign",
        "trigger": "manual",
        "steps": [
            {
                "type": "generate",
                "engine": "narrative",
                "prompt": "A thought-provoking question about the future of AI",
                "preset": "balanced"
            },
            {
                "type": "format",
                "target": "multi",
                "platforms": ["twitter", "linkedin", "discord"]
            },
            {
                "type": "publish",
                "platforms": ["twitter", "linkedin", "discord"]
            },
            {
                "type": "archive",
                "platform": "notion"
            }
        ]
    })
    
    print("🌐 Multi-Platform Distribution")
    print("=" * 50)
    print("Generating content and distributing to multiple platforms...\n")
    
    # Execute the workflow
    result = await workflow.execute()
    
    if result["success"]:
        print("✅ Content generated and distributed!\n")
        
        # Show what was published where
        for step in result["steps"]:
            if step["type"] == "publish":
                published = step["result"]["published"]
                print("📱 Published to:")
                for platform, data in published.items():
                    if data["success"]:
                        print(f"  ✓ {platform.upper()}: {data['url']}")
                    else:
                        print(f"  ✗ {platform.upper()}: {data['error']}")
            
            elif step["type"] == "archive":
                archived = step["result"]["archived"]
                print(f"\n📚 Archived to:")
                print(f"  ✓ {archived['platform'].upper()}: {archived['url']}")
    else:
        print(f"❌ Error: {result['error']}")


if __name__ == "__main__":
    asyncio.run(main())
