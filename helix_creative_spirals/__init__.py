"""
Helix Creative Spirals
AI-powered social media automation with creative content generation

Combines Helix Narrative Engine with Helix Spirals for automated
content generation and multi-platform distribution.
"""

from .workflow import (
    createContentWorkflow,
    Workflow,
    WorkflowConfig,
    WorkflowStep,
)
from .templates import (
    TwitterStoryTemplate,
    LinkedInContentTemplate,
    MultiPlatformTemplate,
    EngagementMonitorTemplate,
)

__version__ = "1.0.0"
__author__ = "Helix Team"
__license__ = "Apache 2.0"

__all__ = [
    "createContentWorkflow",
    "Workflow",
    "WorkflowConfig",
    "WorkflowStep",
    "TwitterStoryTemplate",
    "LinkedInContentTemplate",
    "MultiPlatformTemplate",
    "EngagementMonitorTemplate",
]
