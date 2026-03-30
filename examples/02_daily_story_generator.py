"""
Example 2: Daily Story Generator

Automatically generate and publish stories to Twitter every morning at 9 AM.
Perfect for building a consistent content schedule.
"""

import asyncio
from helix_creative_spirals import createContentWorkflow


async def main():
    """Set up daily story generation"""
    
    # Create a scheduled workflow for daily story generation
    workflow = createContentWorkflow({
        "name": "Daily Story Generator",
        "trigger": "schedule",
        "schedule": "0 9 * * *",  # 9 AM every day
        "steps": [
            {
                "type": "generate",
                "engine": "narrative",
                "prompt": "A cyberpunk heist story set in a megacity",
                "preset": "balanced"  # Balanced for quality
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
            },
            {
                "type": "archive",
                "platform": "notion"
            }
        ]
    })
    
    print("📅 Daily Story Generator")
    print("=" * 50)
    print(f"Workflow: {workflow.config.name}")
    print(f"Schedule: {workflow.config.schedule} (9 AM daily)")
    print(f"Platforms: Twitter")
    print(f"Archive: Notion")
    print("\n✅ Workflow configured and ready to start")
    print("\nTo start the scheduler, call: await workflow.start()")
    print("To stop the scheduler, call: await workflow.stop()")
    
    # Example: Start the workflow
    # await workflow.start()
    # 
    # # Keep the scheduler running
    # try:
    #     while True:
    #         await asyncio.sleep(1)
    # except KeyboardInterrupt:
    #     print("\n🛑 Stopping scheduler...")
    #     await workflow.stop()


if __name__ == "__main__":
    asyncio.run(main())
