# Pydantic AI Replication - Complete Code

## Architecture Overview

```
MemoryBankSystem/
├── agents/
│   ├── __init__.py
│   ├── van_agent.py          # VAN mode agent
│   ├── plan_agent.py         # PLAN mode agent
│   ├── creative_agent.py     # CREATIVE mode agent
│   └── implement_agent.py    # IMPLEMENT mode agent
├── orchestrator.py           # Main workflow controller
├── lazy_loader.py           # Lazy rule loading system
├── models.py                # Pydantic models
├── exceptions.py            # Custom exceptions
├── memory_bank/             # State directory
│   ├── tasks.md
│   ├── activeContext.md
│   └── progress.md
└── rules/                   # Rule files (lazy loaded)
    ├── core/
    │   ├── platform_awareness.md
    │   └── file_verification.md
    └── modes/
        ├── van/
        ├── plan/
        └── creative/
            ├── architecture.md
            ├── algorithm.md
            └── uiux.md
```

## 1. Models (models.py)

```python
from enum import Enum
from typing import Dict, Optional
from pydantic import BaseModel

class ComplexityLevel(Enum):
    LEVEL_1 = 1  # Quick fix
    LEVEL_2 = 2  # Simple enhancement
    LEVEL_3 = 3  # Intermediate feature
    LEVEL_4 = 4  # Complex system

class MemoryBankState(BaseModel):
    """Persistent state across agents"""
    tasks: Dict[str, any] = {}
    complexity: Optional[ComplexityLevel] = None
    current_mode: str = "VAN"
    platform: str = ""
    memory_bank_files: Dict[str, any] = {}
    rule_loader: Optional[any] = None  # Will be set by orchestrator

    class Config:
        arbitrary_types_allowed = True
```

## 2. Custom Exceptions (exceptions.py)

```python
class ForceTransitionToPlan(Exception):
    """Exception raised to force transition from VAN to PLAN mode"""
    def __init__(self, message: str, next_mode: str, state):
        self.message = message
        self.next_mode = next_mode
        self.state = state
        super().__init__(self.message)

class ForceTransitionToCreative(Exception):
    """Exception raised to force transition from PLAN to CREATIVE mode"""
    def __init__(self, message: str, next_mode: str, components: list):
        self.message = message
        self.next_mode = next_mode
        self.components = components
        super().__init__(self.message)

class ForceTransitionToImplement(Exception):
    """Exception raised to force transition from CREATIVE to IMPLEMENT mode"""
    def __init__(self, message: str, next_mode: str):
        self.message = message
        self.next_mode = next_mode
        super().__init__(self.message)
```

## 3. Lazy Rule Loader (lazy_loader.py)

```python
from pathlib import Path
from typing import Callable, Dict

class LazyRuleLoader:
    """
    Replicates cursor's hierarchical rule loading system.
    Achieves 78% token reduction through lazy loading.
    """

    def __init__(self):
        self.loaded_rules: Dict[str, str] = {}
        self.lazy_loaders: Dict[str, Callable[[], str]] = {}

        # Load core rules immediately
        self._load_core_rules()

    def _load_core_rules(self):
        """Load essential rules immediately (~5,000 tokens)"""
        core_rules = [
            "platform_awareness",
            "file_verification",
            "command_execution"
        ]
        for rule in core_rules:
            filepath = f"rules/core/{rule}.md"
            if Path(filepath).exists():
                self.loaded_rules[rule] = self._read_rule_file(filepath)
            else:
                print(f"Warning: Core rule {filepath} not found")

    def register_lazy_rule(self, rule_name: str, loader_func: Callable[[], str]):
        """
        Register a rule to be loaded on-demand.

        This is the key to lazy loading - rules are registered but NOT loaded
        until explicitly requested.
        """
        self.lazy_loaders[rule_name] = loader_func

    def get_rule(self, rule_name: str) -> str:
        """
        Load rule only when requested (lazy loading!)

        First call: Loads from file
        Subsequent calls: Returns cached version
        """
        # Check if already loaded
        if rule_name not in self.loaded_rules:
            # Load on first request
            if rule_name in self.lazy_loaders:
                print(f"[Lazy Loading] Loading rule: {rule_name}")
                self.loaded_rules[rule_name] = self.lazy_loaders[rule_name]()
            else:
                raise ValueError(f"Rule '{rule_name}' not registered")

        return self.loaded_rules[rule_name]

    def _read_rule_file(self, filepath: str) -> str:
        """Helper to read rule files"""
        return Path(filepath).read_text()

    def get_loaded_rules_count(self) -> int:
        """Get count of currently loaded rules (for monitoring)"""
        return len(self.loaded_rules)

    def get_loaded_rules_list(self) -> list:
        """Get list of loaded rule names"""
        return list(self.loaded_rules.keys())
```

## 4. VAN Agent (agents/van_agent.py)

```python
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.anthropic import AnthropicModel
from models import MemoryBankState, ComplexityLevel
from exceptions import ForceTransitionToPlan

van_agent = Agent(
    model=AnthropicModel("claude-sonnet-4"),
    system_prompt="""You are the VAN initialization agent.

Your role:
1. Verify memory bank exists (check state.memory_bank_files)
2. Detect platform (Windows/Mac/Linux) - already set in state.platform
3. Perform file verification
4. Analyze task complexity based on:
   - Scope: Single file vs. multiple subsystems
   - Risk: Low vs. high impact changes
   - Effort: Minutes vs. hours/days
   - Dependencies: Isolated vs. cross-cutting

5. Determine complexity level:
   - LEVEL_1: Quick bug fix, typo correction, simple config change
   - LEVEL_2: Simple enhancement, new utility function, UI tweak
   - LEVEL_3: Intermediate feature, new component, API endpoint
   - LEVEL_4: Complex system, architecture change, major refactor

6. FOR LEVEL 2-4: Return result indicating forced transition needed
7. FOR LEVEL 1: Complete initialization and return success

Always include 'complexity_level' in your result as an integer (1-4).
""",
    result_type=dict
)

@van_agent.result_validator
async def check_complexity_level(ctx: RunContext[MemoryBankState], result: dict) -> dict:
    """
    This replicates the FORCE EXIT mechanism in VAN mode.

    Equivalent to van-mode-map.mdc lines 39-42:
    - If Level 2-4 detected, VAN mode blocks implementation
    - Forces transition to PLAN mode
    """
    complexity_value = result.get('complexity_level')

    if not complexity_value:
        # Default to Level 2 if not specified
        complexity_value = 2

    # Convert to ComplexityLevel enum
    complexity = ComplexityLevel(complexity_value)

    # Update state
    ctx.deps.complexity = complexity
    ctx.deps.memory_bank_files['complexity'] = complexity_value

    if complexity in [ComplexityLevel.LEVEL_2, ComplexityLevel.LEVEL_3, ComplexityLevel.LEVEL_4]:
        # This is the key workflow control mechanism!
        raise ForceTransitionToPlan(
            message=f"🚫 LEVEL {complexity.value} TASK DETECTED\n"
                   f"Implementation in VAN mode is BLOCKED\n"
                   f"This task REQUIRES PLAN mode\n"
                   f"Automatically transitioning to PLAN mode...",
            next_mode="PLAN",
            state=ctx.deps
        )

    # Level 1 - allow VAN mode to continue
    return result
```

## 5. PLAN Agent (agents/plan_agent.py)

```python
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.anthropic import AnthropicModel
from models import MemoryBankState, ComplexityLevel
from exceptions import ForceTransitionToCreative

plan_agent = Agent(
    model=AnthropicModel("claude-sonnet-4"),
    system_prompt="""You are the PLAN agent.

Your role:
1. Read tasks.md and complexity level from memory bank
2. Create appropriate planning based on complexity:
   - Level 2: Simplified planning (overview, files, steps, challenges)
   - Level 3: Comprehensive planning + identify creative components
   - Level 4: Phased implementation + architectural diagrams

3. For Level 3-4: Identify components requiring creative phases:
   - Architecture decisions (system structure, component design)
   - Algorithm design (performance-critical logic)
   - UI/UX design (user interface components)

4. Update tasks.md with the plan
5. Return result indicating if creative phases are required

Always include:
- 'requires_creative_phase' (boolean)
- 'creative_components' (list of components needing design)
- 'plan_summary' (string summary of the plan)
""",
    result_type=dict
)

@plan_agent.result_validator
async def check_creative_requirement(ctx: RunContext[MemoryBankState], result: dict) -> dict:
    """
    Forces transition to CREATIVE if components need design decisions.

    Equivalent to plan-mode-map.mdc lines 46-49:
    - Check if creative phases required
    - If yes, force transition to CREATIVE mode
    """
    if result.get('requires_creative_phase'):
        components = result.get('creative_components', [])

        # Update state
        ctx.deps.memory_bank_files['creative_components'] = components

        raise ForceTransitionToCreative(
            message=f"🎨 CREATIVE PHASES REQUIRED\n"
                   f"The following components need design decisions:\n" +
                   "\n".join(f"  - {c}" for c in components) +
                   f"\n\nAutomatically transitioning to CREATIVE mode...",
            next_mode="CREATIVE",
            components=components
        )
    return result
```

## 6. CREATIVE Agent (agents/creative_agent.py)

```python
from pydantic_ai import Agent, RunContext
from pydantic_ai.models.anthropic import AnthropicModel
from models import MemoryBankState
from exceptions import ForceTransitionToImplement
from pathlib import Path

creative_agent = Agent(
    model=AnthropicModel("claude-sonnet-4"),
    system_prompt="""You are the CREATIVE design agent.

Your role:
1. Read tasks.md and creative_components from memory bank
2. For each component, determine the type:
   - Architecture Design
   - Algorithm Design
   - UI/UX Design

3. Use the appropriate tool to load specialized guidance:
   - load_architecture_guidance() for architecture decisions
   - load_algorithm_guidance() for algorithm design
   - load_uiux_guidance() for UI/UX design

4. For each component:
   - Generate 2-4 design options
   - Analyze pros/cons of each option
   - Select and justify recommended approach
   - Document implementation guidelines

5. Update memory bank with design decisions

Use the load_*_guidance tools to access specialized design knowledge
only when needed for specific component types.
""",
    result_type=dict
)

@creative_agent.tool
async def load_architecture_guidance(ctx: RunContext[MemoryBankState]) -> str:
    """
    Lazy load architecture design rules (only when needed).

    This is called only when architecture design is actually needed!
    """
    loader = ctx.deps.rule_loader
    return loader.get_rule("creative-phase-architecture")

@creative_agent.tool
async def load_algorithm_guidance(ctx: RunContext[MemoryBankState]) -> str:
    """
    Lazy load algorithm design rules (only when needed).
    """
    loader = ctx.deps.rule_loader
    return loader.get_rule("creative-phase-algorithm")

@creative_agent.tool
async def load_uiux_guidance(ctx: RunContext[MemoryBankState]) -> str:
    """
    Lazy load UI/UX design rules (only when needed).
    """
    loader = ctx.deps.rule_loader
    return loader.get_rule("creative-phase-uiux")

@creative_agent.tool
async def save_design_decision(ctx: RunContext[MemoryBankState],
                               component: str,
                               design_decision: str) -> str:
    """Save design decision to memory bank"""
    if 'design_decisions' not in ctx.deps.memory_bank_files:
        ctx.deps.memory_bank_files['design_decisions'] = {}

    ctx.deps.memory_bank_files['design_decisions'][component] = design_decision

    # Also write to file for persistence
    decisions_file = Path("memory_bank/design_decisions.md")
    decisions_file.parent.mkdir(exist_ok=True)

    with open(decisions_file, 'a') as f:
        f.write(f"\n## {component}\n\n{design_decision}\n")

    return f"Design decision for '{component}' saved"

@creative_agent.result_validator
async def check_creative_complete(ctx: RunContext[MemoryBankState], result: dict) -> dict:
    """Check if all creative phases are complete"""
    components = ctx.deps.memory_bank_files.get('creative_components', [])
    decisions = ctx.deps.memory_bank_files.get('design_decisions', {})

    all_complete = all(comp in decisions for comp in components)

    if all_complete:
        raise ForceTransitionToImplement(
            message=f"✅ CREATIVE MODE COMPLETE\n"
                   f"All design decisions documented.\n"
                   f"Automatically transitioning to IMPLEMENT mode...",
            next_mode="IMPLEMENT"
        )

    return result
```

## 7. Orchestrator (orchestrator.py)

```python
import asyncio
import platform as platform_module
from typing import Optional
from pathlib import Path

from models import MemoryBankState
from lazy_loader import LazyRuleLoader
from exceptions import (
    ForceTransitionToPlan,
    ForceTransitionToCreative,
    ForceTransitionToImplement
)
from agents.van_agent import van_agent
from agents.plan_agent import plan_agent
from agents.creative_agent import creative_agent

class MemoryBankOrchestrator:
    """
    Main workflow controller - replaces cursor's custom mode switching.

    Handles:
    - Command detection and routing
    - Automatic mode transitions (forced transitions)
    - Memory bank state management
    - Lazy rule loading coordination
    """

    def __init__(self):
        self.state = MemoryBankState(
            tasks={},
            complexity=None,
            current_mode="VAN",
            platform=self._detect_platform(),
            memory_bank_files={}
        )

        self.rule_loader = LazyRuleLoader()
        self.state.rule_loader = self.rule_loader

        # Register lazy loaders for specialized rules
        self._register_lazy_loaders()

    def _detect_platform(self) -> str:
        """Detect operating system"""
        return platform_module.system()  # Returns 'Windows', 'Darwin', or 'Linux'

    def _register_lazy_loaders(self):
        """
        Register lazy loaders for all specialized rules.

        Rules are registered but NOT loaded until explicitly requested.
        This achieves the 78% token reduction.
        """
        # Creative phase specialized rules
        self.rule_loader.register_lazy_rule(
            "creative-phase-architecture",
            lambda: Path("rules/modes/creative/architecture.md").read_text()
        )
        self.rule_loader.register_lazy_rule(
            "creative-phase-algorithm",
            lambda: Path("rules/modes/creative/algorithm.md").read_text()
        )
        self.rule_loader.register_lazy_rule(
            "creative-phase-uiux",
            lambda: Path("rules/modes/creative/uiux.md").read_text()
        )

        # Level-specific planning rules
        self.rule_loader.register_lazy_rule(
            "planning-comprehensive",
            lambda: Path("rules/modes/plan/comprehensive.md").read_text()
        )

    async def run(self, user_command: str, task_description: Optional[str] = None):
        """Main entry point - replicates cursor's command detection"""
        command = user_command.upper()

        if command == "VAN":
            print(f"OK VAN - Beginning Initialization Process")
            return await self._run_van_mode(task_description)

        elif command == "PLAN":
            print(f"OK PLAN - Beginning Task Planning")
            return await self._run_plan_mode()

        elif command == "CREATIVE":
            print(f"OK CREATIVE - Beginning Design Phase")
            return await self._run_creative_mode()

        else:
            raise ValueError(f"Unknown command: {user_command}")

    async def _run_van_mode(self, task_description: str):
        """Execute VAN mode with automatic transition handling"""
        try:
            result = await van_agent.run(
                f"Initialize project and analyze task: {task_description}",
                deps=self.state
            )

            # If we get here, it's Level 1
            self.state.current_mode = "VAN_COMPLETE"
            print(f"\n✅ VAN MODE COMPLETE - Level 1 task\n")
            return result

        except ForceTransitionToPlan as e:
            # Level 2-4 detected - automatic transition!
            print(f"\n{e.message}\n")
            self.state.current_mode = "PLAN"
            return await self._run_plan_mode()

    async def _run_plan_mode(self):
        """Execute PLAN mode with automatic transition handling"""
        try:
            result = await plan_agent.run(
                "Create implementation plan based on complexity level",
                deps=self.state
            )

            self.state.current_mode = "PLAN_COMPLETE"
            print(f"\n✅ PLAN MODE COMPLETE\n")
            return result

        except ForceTransitionToCreative as e:
            # Creative phases required!
            print(f"\n{e.message}\n")
            self.state.current_mode = "CREATIVE"
            return await self._run_creative_mode()

    async def _run_creative_mode(self):
        """Execute CREATIVE mode"""
        print(f"📊 Loaded rules: {self.rule_loader.get_loaded_rules_count()}")

        try:
            result = await creative_agent.run(
                "Perform design decisions for flagged components",
                deps=self.state
            )

            self.state.current_mode = "CREATIVE_COMPLETE"
            print(f"\n✅ CREATIVE MODE COMPLETE\n")
            print(f"📊 Final loaded rules: {self.rule_loader.get_loaded_rules_count()}")
            return result

        except ForceTransitionToImplement as e:
            print(f"\n{e.message}\n")
            self.state.current_mode = "IMPLEMENT"
            return {"status": "ready_for_implementation"}

    def get_status(self) -> dict:
        """Get current system status"""
        return {
            "current_mode": self.state.current_mode,
            "complexity": self.state.complexity.value if self.state.complexity else None,
            "platform": self.state.platform,
            "loaded_rules_count": self.rule_loader.get_loaded_rules_count(),
            "loaded_rules": self.rule_loader.get_loaded_rules_list(),
            "memory_bank_files": list(self.state.memory_bank_files.keys())
        }
```

## 8. Example Usage (example.py)

```python
import asyncio
from orchestrator import MemoryBankOrchestrator

async def main():
    orchestrator = MemoryBankOrchestrator()

    # Example 1: Simple bug fix (Level 1)
    print("="*60)
    print("Example 1: Level 1 Task (Bug Fix)")
    print("="*60)

    result = await orchestrator.run(
        "VAN",
        "Fix typo in error message on line 42 of auth.py"
    )
    print(f"\nStatus: {orchestrator.get_status()}\n")

    # Example 2: Feature with design decisions (Level 3)
    print("\n" + "="*60)
    print("Example 2: Level 3 Task (Feature with Design)")
    print("="*60)

    orchestrator2 = MemoryBankOrchestrator()
    result = await orchestrator2.run(
        "VAN",
        "Add user authentication system with JWT tokens and session management"
    )
    print(f"\nStatus: {orchestrator2.get_status()}\n")

if __name__ == "__main__":
    asyncio.run(main())
```

---

**Document**: Part 5 of 7
**Previous**: [Lazy Loading Deep Dive](04_lazy_loading_implementation.md)
**Next**: [Implementation Guide](06_implementation_guide.md)
**Date**: 2025-11-04
**Author**: Claude (Sonnet 4.5)
