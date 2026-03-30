"""
Content Workflow Engine

Orchestrates content generation and distribution workflows combining
Helix Narrative Engine with Helix Spirals.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional, Literal
from enum import Enum
import uuid
import logging
import asyncio
from datetime import datetime

logger = logging.getLogger(__name__)


class TriggerType(str, Enum):
    """Workflow trigger types"""
    MANUAL = "manual"
    SCHEDULE = "schedule"
    EVENT = "event"


class StepType(str, Enum):
    """Workflow step types"""
    GENERATE = "generate"
    FORMAT = "format"
    PUBLISH = "publish"
    ARCHIVE = "archive"
    ANALYTICS = "analytics"


@dataclass
class WorkflowStep:
    """A single step in a workflow"""
    type: StepType
    config: Dict[str, Any] = field(default_factory=dict)


@dataclass
class WorkflowConfig:
    """Configuration for a content workflow"""
    name: str
    trigger: TriggerType
    steps: List[WorkflowStep]
    schedule: Optional[str] = None
    description: Optional[str] = None
    tags: List[str] = field(default_factory=list)


class Workflow:
    """
    A content workflow that orchestrates generation and distribution.
    
    Combines Helix Narrative Engine for content generation with
    Helix Spirals for multi-platform distribution.
    """
    
    def __init__(self, config: WorkflowConfig):
        """Initialize a workflow"""
        self.config = config
        self.workflow_id = f"wf_{int(datetime.now().timestamp() * 1000)}_{uuid.uuid4().hex[:9]}"
        self.is_running = False
        self.scheduler_task: Optional[asyncio.Task] = None
        
        logger.info(f"[Workflow] Created workflow {self.workflow_id}: {config.name}")
    
    async def execute(self, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Execute the workflow once.
        
        Args:
            context: Optional context data to pass through workflow
            
        Returns:
            Workflow execution result
        """
        logger.info(f"[Workflow] Executing {self.workflow_id}")
        
        execution_id = f"exec_{int(datetime.now().timestamp() * 1000)}_{uuid.uuid4().hex[:9]}"
        result = {
            "workflowId": self.workflow_id,
            "executionId": execution_id,
            "startTime": datetime.now().isoformat(),
            "steps": [],
            "success": True,
            "error": None,
        }
        
        try:
            step_context = context or {}
            
            for i, step in enumerate(self.config.steps):
                logger.info(f"[Workflow] Step {i+1}/{len(self.config.steps)}: {step.type.value}")
                
                try:
                    step_result = await self._execute_step(step, step_context)
                    result["steps"].append({
                        "index": i,
                        "type": step.type.value,
                        "success": True,
                        "result": step_result,
                    })
                    
                    # Pass step output to next step
                    step_context.update(step_result)
                    
                except Exception as e:
                    logger.error(f"[Workflow] Step {i+1} failed: {e}")
                    result["steps"].append({
                        "index": i,
                        "type": step.type.value,
                        "success": False,
                        "error": str(e),
                    })
                    result["success"] = False
                    result["error"] = str(e)
                    break
            
            result["endTime"] = datetime.now().isoformat()
            logger.info(f"[Workflow] Execution {execution_id} completed")
            return result
            
        except Exception as e:
            logger.error(f"[Workflow] Execution {execution_id} failed: {e}")
            result["success"] = False
            result["error"] = str(e)
            result["endTime"] = datetime.now().isoformat()
            return result
    
    async def start(self) -> None:
        """Start the workflow scheduler for recurring execution"""
        if self.config.trigger != TriggerType.SCHEDULE:
            raise ValueError("Only scheduled workflows can be started")
        
        if not self.config.schedule:
            raise ValueError("Schedule is required for scheduled workflows")
        
        self.is_running = True
        logger.info(f"[Workflow] Starting scheduler for {self.workflow_id}")
        
        # Parse cron expression and schedule
        self.scheduler_task = asyncio.create_task(self._scheduler_loop())
    
    async def stop(self) -> None:
        """Stop the workflow scheduler"""
        self.is_running = False
        logger.info(f"[Workflow] Stopping scheduler for {self.workflow_id}")
        
        if self.scheduler_task:
            self.scheduler_task.cancel()
            try:
                await self.scheduler_task
            except asyncio.CancelledError:
                pass
    
    async def _scheduler_loop(self) -> None:
        """Scheduler loop for recurring execution"""
        from croniter import croniter
        
        cron = croniter(self.config.schedule)
        
        while self.is_running:
            try:
                # Calculate next execution time
                next_run = cron.get_next(datetime)
                now = datetime.now()
                wait_seconds = (next_run - now).total_seconds()
                
                if wait_seconds > 0:
                    logger.info(f"[Workflow] Next execution in {wait_seconds:.0f}s")
                    await asyncio.sleep(wait_seconds)
                
                if self.is_running:
                    await self.execute()
                    
            except Exception as e:
                logger.error(f"[Workflow] Scheduler error: {e}")
                await asyncio.sleep(60)  # Wait before retry
    
    async def _execute_step(
        self,
        step: WorkflowStep,
        context: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Execute a single workflow step"""
        
        if step.type == StepType.GENERATE:
            return await self._step_generate(step, context)
        elif step.type == StepType.FORMAT:
            return await self._step_format(step, context)
        elif step.type == StepType.PUBLISH:
            return await self._step_publish(step, context)
        elif step.type == StepType.ARCHIVE:
            return await self._step_archive(step, context)
        elif step.type == StepType.ANALYTICS:
            return await self._step_analytics(step, context)
        else:
            raise ValueError(f"Unknown step type: {step.type}")
    
    async def _step_generate(
        self,
        step: WorkflowStep,
        context: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Generate content using Narrative Engine"""
        from helix_narrative_engine import generateNarrative, GenerationOptions
        
        config = step.config
        prompt = config.get("prompt", "")
        preset = config.get("preset", "balanced")
        
        logger.info(f"[Workflow] Generating content: {prompt[:50]}...")
        
        result = await generateNarrative(
            prompt,
            GenerationOptions(preset=preset)
        )
        
        if not result.success:
            raise RuntimeError(f"Generation failed: {result.error}")
        
        return {
            "generatedContent": {
                "title": result.title,
                "content": result.content,
                "generationId": result.generationId,
                "metadata": result.metadata,
            }
        }
    
    async def _step_format(
        self,
        step: WorkflowStep,
        context: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Format content for target platform"""
        config = step.config
        target = config.get("target", "twitter")
        
        generated = context.get("generatedContent", {})
        content = generated.get("content", "")
        
        logger.info(f"[Workflow] Formatting for {target}")
        
        if target == "twitter":
            formatted = self._format_twitter(content, config)
        elif target == "linkedin":
            formatted = self._format_linkedin(content, config)
        elif target == "discord":
            formatted = self._format_discord(content, config)
        elif target == "multi":
            formatted = self._format_multi(content, config)
        else:
            formatted = content
        
        return {
            "formattedContent": {
                "target": target,
                "content": formatted,
            }
        }
    
    async def _step_publish(
        self,
        step: WorkflowStep,
        context: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Publish content to platforms via Spirals"""
        config = step.config
        platforms = config.get("platforms") or [config.get("platform", "twitter")]
        
        formatted = context.get("formattedContent", {})
        content = formatted.get("content", "")
        
        logger.info(f"[Workflow] Publishing to {platforms}")
        
        published = {}
        for platform in platforms:
            try:
                # In production, this would call Helix Spirals connectors
                url = f"https://{platform}.com/post/{uuid.uuid4().hex[:8]}"
                published[platform] = {
                    "success": True,
                    "url": url,
                    "timestamp": datetime.now().isoformat(),
                }
                logger.info(f"[Workflow] Published to {platform}: {url}")
            except Exception as e:
                logger.error(f"[Workflow] Failed to publish to {platform}: {e}")
                published[platform] = {
                    "success": False,
                    "error": str(e),
                }
        
        return {
            "published": published
        }
    
    async def _step_archive(
        self,
        step: WorkflowStep,
        context: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Archive content to storage platform"""
        config = step.config
        platform = config.get("platform", "notion")
        
        generated = context.get("generatedContent", {})
        title = generated.get("title", "Untitled")
        
        logger.info(f"[Workflow] Archiving to {platform}")
        
        # In production, this would call Notion API or other storage
        archived = {
            "platform": platform,
            "title": title,
            "archivedAt": datetime.now().isoformat(),
            "url": f"https://{platform}.com/archive/{uuid.uuid4().hex[:8]}",
        }
        
        return {
            "archived": archived
        }
    
    async def _step_analytics(
        self,
        step: WorkflowStep,
        context: Dict[str, Any],
    ) -> Dict[str, Any]:
        """Track analytics and engagement"""
        config = step.config
        track = config.get("track", ["engagement", "reach"])
        report_to = config.get("reportTo", "notion")
        
        logger.info(f"[Workflow] Tracking analytics: {track}")
        
        analytics = {
            "tracked": track,
            "reportTo": report_to,
            "metrics": {
                "engagement": 0,
                "reach": 0,
                "sentiment": 0,
            },
            "reportedAt": datetime.now().isoformat(),
        }
        
        return {
            "analytics": analytics
        }
    
    @staticmethod
    def _format_twitter(content: str, config: Dict[str, Any]) -> str:
        """Format content for Twitter"""
        max_length = config.get("maxLength", 280)
        include_hashtags = config.get("includeHashtags", True)
        
        # Truncate to max length
        if len(content) > max_length:
            content = content[:max_length-3] + "..."
        
        if include_hashtags:
            content += "\n\n#AI #Creative #Automation"
        
        return content
    
    @staticmethod
    def _format_linkedin(content: str, config: Dict[str, Any]) -> str:
        """Format content for LinkedIn"""
        # LinkedIn allows longer content
        if len(content) > 3000:
            content = content[:3000]
        
        return content
    
    @staticmethod
    def _format_discord(content: str, config: Dict[str, Any]) -> str:
        """Format content for Discord"""
        # Discord has 2000 char limit per message
        if len(content) > 2000:
            content = content[:1997] + "..."
        
        return content
    
    @staticmethod
    def _format_multi(content: str, config: Dict[str, Any]) -> Dict[str, str]:
        """Format content for multiple platforms"""
        platforms = config.get("platforms", ["twitter", "linkedin", "discord"])
        
        formatted = {}
        for platform in platforms:
            if platform == "twitter":
                formatted[platform] = Workflow._format_twitter(content, {})
            elif platform == "linkedin":
                formatted[platform] = Workflow._format_linkedin(content, {})
            elif platform == "discord":
                formatted[platform] = Workflow._format_discord(content, {})
            else:
                formatted[platform] = content
        
        return formatted


def createContentWorkflow(config_dict: Dict[str, Any]) -> Workflow:
    """
    Create a new content workflow.
    
    Args:
        config_dict: Workflow configuration dictionary
        
    Returns:
        Workflow instance
    """
    # Parse trigger
    trigger_str = config_dict.get("trigger", "manual")
    trigger = TriggerType(trigger_str)
    
    # Parse steps
    steps = []
    for step_dict in config_dict.get("steps", []):
        step_type = StepType(step_dict.get("type", "generate"))
        step_config = {k: v for k, v in step_dict.items() if k != "type"}
        steps.append(WorkflowStep(type=step_type, config=step_config))
    
    # Create config
    config = WorkflowConfig(
        name=config_dict.get("name", "Untitled Workflow"),
        trigger=trigger,
        steps=steps,
        schedule=config_dict.get("schedule"),
        description=config_dict.get("description"),
        tags=config_dict.get("tags", []),
    )
    
    return Workflow(config)
