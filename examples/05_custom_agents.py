"""
Example 5: Custom Agent Configuration

Customize which agents participate in content generation and their parameters.
This allows fine-tuning the generation process for specific needs.
"""

import asyncio
from helix_narrative_engine import generateNarrative, GenerationOptions


async def main():
    """Generate content with custom agent configuration"""
    
    print("🤖 Custom Agent Configuration")
    print("=" * 50)
    print("Generating content with custom agent setup...\n")
    
    # Define custom agents with specific configurations
    custom_agents = [
        {
            "agentId": "oracle",
            "provider": "openai",
            "temperature": 0.8,
            "multiplicity": 1
        },
        {
            "agentId": "lumina",
            "provider": "anthropic",
            "temperature": 0.75,
            "multiplicity": 1
        },
        {
            "agentId": "gemini",
            "provider": "google",
            "temperature": 0.7,
            "multiplicity": 1
        },
        {
            "agentId": "agni",
            "provider": "openai",
            "temperature": 0.95,  # Higher temperature for more creativity
            "multiplicity": 2  # Run twice for enhanced creativity
        },
        {
            "agentId": "researcher",
            "provider": "perplexity",
            "temperature": 0.3,
            "multiplicity": 1
        },
        {
            "agentId": "claude",
            "provider": "anthropic",
            "temperature": 0.3,
            "multiplicity": 1
        },
        {
            "agentId": "kavach",
            "provider": "anthropic",
            "temperature": 0.2,
            "multiplicity": 1
        }
    ]
    
    print("Agents configured:")
    for agent in custom_agents:
        print(f"  • {agent['agentId'].upper()}")
        print(f"    Provider: {agent['provider']}")
        print(f"    Temperature: {agent['temperature']}")
        print(f"    Multiplicity: {agent['multiplicity']}\n")
    
    # Generate content with custom agents
    print("Generating story with custom agents...\n")
    
    result = await generateNarrative(
        "A detective investigates a time-travel murder",
        GenerationOptions(customAgents=custom_agents)
    )
    
    if result.success:
        print("✅ Story generated successfully!\n")
        print(f"Title: {result.title}")
        print(f"Content length: {result.metadata.wordCount} words")
        print(f"Quality score: {result.metadata.qualityScore:.2f}/1.0")
        print(f"Ethical approval: {'✓' if result.metadata.ethicalApproval else '✗'}")
        print(f"\nAgent contributions:")
        for agent_name, contribution in result.metadata.agentContributions.items():
            print(f"  • {agent_name}: {contribution['provider']}")
    else:
        print(f"❌ Error: {result.error}")


if __name__ == "__main__":
    asyncio.run(main())
