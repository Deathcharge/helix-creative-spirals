"""
Example 1: Quick Tweet Generation

Generate a tweet on-demand and publish to Twitter.
Perfect for quick content creation without scheduling.
"""

import asyncio
from helix_creative_spirals import createContentWorkflow


async def main():
    """Generate and publish a quick tweet"""
    
    # Create a simple workflow for quick tweet generation
    workflow = createContentWorkflow({
        "name": "Quick Tweet",
        "trigger": "manual",
        "steps": [
            {
                "type": "generate",
                "engine": "narrative",
                "prompt": "A funny observation about AI and creativity",
                "preset": "fast"  # Use fast preset for quick generation
            },
            {
                "type": "format",
                "target": "twitter",
                "maxLength": 280,
                "includeHashtags": True
            },
            {
                "type": "publish",
                "platform": "twitter"
            }
        ]
    })
    
    # Execute the workflow
    print("🚀 Generating quick tweet...")
    result = await workflow.execute()
    
    # Print results
    if result["success"]:
        print("\n✅ Tweet generated and published!")
        print(f"\nGenerated content:")
        for step in result["steps"]:
            if step["type"] == "generate":
                content = step["result"]["generatedContent"]
                print(f"Title: {content['title']}")
                print(f"Content: {content['content'][:200]}...")
            elif step["type"] == "publish":
                published = step["result"]["published"]
                for platform, data in published.items():
                    if data["success"]:
                        print(f"\n📱 Published to {platform}")
                        print(f"URL: {data['url']}")
    else:
        print(f"\n❌ Error: {result['error']}")


if __name__ == "__main__":
    asyncio.run(main())
