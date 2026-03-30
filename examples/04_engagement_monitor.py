"""
Example 4: Engagement Monitor

Generate content and track engagement metrics across platforms.
Reports are automatically archived in Notion for analysis.
"""

import asyncio
from helix_creative_spirals.templates import EngagementMonitorTemplate


async def main():
    """Monitor engagement across platforms"""
    
    print("📊 Engagement Monitor")
    print("=" * 50)
    print("Generating content and tracking engagement metrics...\n")
    
    # Create an engagement monitor template
    template = EngagementMonitorTemplate(
        prompt="A trending AI insight about creativity",
        tracking_platforms=["twitter", "linkedin"],
        report_to="notion",
        schedule="0 12 * * *"  # Noon daily
    )
    
    # Create the workflow
    workflow = template.create()
    
    print(f"Workflow: {workflow.config.name}")
    print(f"Schedule: {workflow.config.schedule} (Noon daily)")
    print(f"Tracking: Twitter, LinkedIn")
    print(f"Reporting to: Notion")
    print("\n✅ Engagement monitor configured")
    
    # Example: Execute once
    print("\nExecuting workflow once...\n")
    result = await workflow.execute()
    
    if result["success"]:
        print("✅ Content published and monitoring started!\n")
        
        for step in result["steps"]:
            if step["type"] == "analytics":
                analytics = step["result"]["analytics"]
                print("📈 Analytics Configuration:")
                print(f"  Tracking: {', '.join(analytics['tracked'])}")
                print(f"  Report to: {analytics['reportTo']}")
                print(f"  Metrics: {', '.join(analytics['metrics'].keys())}")
    else:
        print(f"❌ Error: {result['error']}")
    
    print("\nTo start continuous monitoring, call: await workflow.start()")


if __name__ == "__main__":
    asyncio.run(main())
