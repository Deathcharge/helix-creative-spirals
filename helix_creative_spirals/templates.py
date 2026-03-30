"""
Pre-built Workflow Templates

Common workflow patterns for content generation and distribution.
"""

from typing import List, Optional, Dict, Any
from .workflow import createContentWorkflow, Workflow, TriggerType, StepType


class TwitterStoryTemplate:
    """Generate and publish short stories to Twitter"""
    
    def __init__(
        self,
        prompt: str,
        schedule: str = "0 9 * * *",
        include_thread: bool = True,
    ):
        """
        Initialize Twitter story template.
        
        Args:
            prompt: Story prompt
            schedule: Cron expression for scheduling
            include_thread: Whether to break into thread format
        """
        self.prompt = prompt
        self.schedule = schedule
        self.include_thread = include_thread
    
    def create(self) -> Workflow:
        """Create the workflow"""
        return createContentWorkflow({
            "name": "Twitter Story Generator",
            "trigger": "schedule",
            "schedule": self.schedule,
            "steps": [
                {
                    "type": "generate",
                    "engine": "narrative",
                    "prompt": self.prompt,
                    "preset": "creative",
                },
                {
                    "type": "format",
                    "target": "twitter",
                    "maxLength": 280,
                    "includeHashtags": True,
                },
                {
                    "type": "publish",
                    "platform": "twitter",
                },
                {
                    "type": "archive",
                    "platform": "notion",
                },
            ]
        })


class LinkedInContentTemplate:
    """Generate and publish professional content to LinkedIn"""
    
    def __init__(
        self,
        topic: str,
        schedule: str = "0 8 * * 1-5",
        include_images: bool = False,
    ):
        """
        Initialize LinkedIn content template.
        
        Args:
            topic: Content topic
            schedule: Cron expression for scheduling
            include_images: Whether to include images
        """
        self.topic = topic
        self.schedule = schedule
        self.include_images = include_images
    
    def create(self) -> Workflow:
        """Create the workflow"""
        return createContentWorkflow({
            "name": "LinkedIn Content Scheduler",
            "trigger": "schedule",
            "schedule": self.schedule,
            "steps": [
                {
                    "type": "generate",
                    "engine": "narrative",
                    "prompt": f"Professional insight about: {self.topic}",
                    "preset": "quality",
                },
                {
                    "type": "format",
                    "target": "linkedin",
                },
                {
                    "type": "publish",
                    "platform": "linkedin",
                },
                {
                    "type": "analytics",
                    "track": ["engagement", "reach"],
                    "reportTo": "notion",
                },
            ]
        })


class MultiPlatformTemplate:
    """Generate once and distribute to multiple platforms"""
    
    def __init__(
        self,
        prompt: str,
        platforms: List[str] = ["twitter", "linkedin", "discord"],
        schedule: str = "0 12 * * *",
    ):
        """
        Initialize multi-platform template.
        
        Args:
            prompt: Content prompt
            platforms: List of platforms to publish to
            schedule: Cron expression for scheduling
        """
        self.prompt = prompt
        self.platforms = platforms
        self.schedule = schedule
    
    def create(self) -> Workflow:
        """Create the workflow"""
        return createContentWorkflow({
            "name": "Multi-Platform Distributor",
            "trigger": "schedule",
            "schedule": self.schedule,
            "steps": [
                {
                    "type": "generate",
                    "engine": "narrative",
                    "prompt": self.prompt,
                    "preset": "balanced",
                },
                {
                    "type": "format",
                    "target": "multi",
                    "platforms": self.platforms,
                },
                {
                    "type": "publish",
                    "platforms": self.platforms,
                },
                {
                    "type": "archive",
                    "platform": "notion",
                },
            ]
        })


class EngagementMonitorTemplate:
    """Generate content and track engagement metrics"""
    
    def __init__(
        self,
        prompt: str,
        tracking_platforms: List[str] = ["twitter", "linkedin"],
        report_to: str = "notion",
        schedule: str = "0 9 * * *",
    ):
        """
        Initialize engagement monitor template.
        
        Args:
            prompt: Content prompt
            tracking_platforms: Platforms to track engagement on
            report_to: Where to report analytics
            schedule: Cron expression for scheduling
        """
        self.prompt = prompt
        self.tracking_platforms = tracking_platforms
        self.report_to = report_to
        self.schedule = schedule
    
    def create(self) -> Workflow:
        """Create the workflow"""
        return createContentWorkflow({
            "name": "Engagement Monitor",
            "trigger": "schedule",
            "schedule": self.schedule,
            "steps": [
                {
                    "type": "generate",
                    "engine": "narrative",
                    "prompt": self.prompt,
                    "preset": "balanced",
                },
                {
                    "type": "format",
                    "target": "multi",
                    "platforms": self.tracking_platforms,
                },
                {
                    "type": "publish",
                    "platforms": self.tracking_platforms,
                },
                {
                    "type": "analytics",
                    "track": ["engagement", "reach", "sentiment"],
                    "reportTo": self.report_to,
                },
            ]
        })


class QuickTweetTemplate:
    """Quick one-off tweet generation"""
    
    def __init__(self, prompt: str):
        """
        Initialize quick tweet template.
        
        Args:
            prompt: Tweet prompt
        """
        self.prompt = prompt
    
    def create(self) -> Workflow:
        """Create the workflow"""
        return createContentWorkflow({
            "name": "Quick Tweet",
            "trigger": "manual",
            "steps": [
                {
                    "type": "generate",
                    "engine": "narrative",
                    "prompt": self.prompt,
                    "preset": "fast",
                },
                {
                    "type": "format",
                    "target": "twitter",
                    "maxLength": 280,
                },
                {
                    "type": "publish",
                    "platform": "twitter",
                },
            ]
        })


class ContentSeriesTemplate:
    """Generate and publish a series of related content"""
    
    def __init__(
        self,
        base_prompt: str,
        num_posts: int = 5,
        schedule: str = "0 9 * * *",
        platforms: List[str] = ["twitter"],
    ):
        """
        Initialize content series template.
        
        Args:
            base_prompt: Base prompt for series
            num_posts: Number of posts in series
            schedule: Cron expression for scheduling
            platforms: Platforms to publish to
        """
        self.base_prompt = base_prompt
        self.num_posts = num_posts
        self.schedule = schedule
        self.platforms = platforms
    
    def create(self) -> Workflow:
        """Create the workflow"""
        return createContentWorkflow({
            "name": "Content Series Generator",
            "trigger": "schedule",
            "schedule": self.schedule,
            "steps": [
                {
                    "type": "generate",
                    "engine": "narrative",
                    "prompt": f"{self.base_prompt} (Part {i+1} of {self.num_posts})",
                    "preset": "balanced",
                }
                for i in range(self.num_posts)
            ] + [
                {
                    "type": "format",
                    "target": "multi" if len(self.platforms) > 1 else self.platforms[0],
                    "platforms": self.platforms,
                },
                {
                    "type": "publish",
                    "platforms": self.platforms,
                },
            ]
        })
