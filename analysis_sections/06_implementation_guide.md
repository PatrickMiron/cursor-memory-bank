# Implementation Guide

## Step-by-Step Setup

### Prerequisites

- Python 3.10+
- `pydantic-ai` library
- Anthropic API key

### Step 1: Project Structure

```bash
mkdir memory_bank_system
cd memory_bank_system

# Create directory structure
mkdir -p agents
mkdir -p memory_bank
mkdir -p rules/core
mkdir -p rules/modes/van
mkdir -p rules/modes/plan
mkdir -p rules/modes/creative

# Create initial files
touch agents/__init__.py
touch agents/van_agent.py
touch agents/plan_agent.py
touch agents/creative_agent.py
touch orchestrator.py
touch lazy_loader.py
touch models.py
touch exceptions.py
touch example.py
```

### Step 2: Install Dependencies

```bash
pip install pydantic-ai anthropic python-dotenv
```

### Step 3: Create Rule Files

Create minimal rule files for testing:

**rules/core/platform_awareness.md**:
```markdown
# Platform Awareness

Detect operating system and adapt commands:
- Windows: Use `dir`, `type`, backslash paths
- Mac/Linux: Use `ls`, `cat`, forward slash paths
```

**rules/core/file_verification.md**:
```markdown
# File Verification

Verify essential files exist:
- Check project structure
- Verify dependencies
- Validate configuration
```

**rules/core/command_execution.md**:
```markdown
# Command Execution

Guidelines for executing commands:
- Use platform-appropriate commands
- Chain commands efficiently
- Handle errors gracefully
```

**rules/modes/creative/architecture.md**:
```markdown
# Architecture Design Guidance

When designing system architecture:
1. Define requirements and constraints
2. Generate 2-4 architecture options
3. Analyze pros/cons of each
4. Consider: scalability, maintainability, performance
5. Select and justify recommendation
6. Document implementation guidelines
```

**rules/modes/creative/algorithm.md**:
```markdown
# Algorithm Design Guidance

When designing algorithms:
1. Define requirements and constraints
2. Generate 2-4 algorithm options
3. Analyze time/space complexity
4. Consider edge cases
5. Select and justify recommendation
6. Document implementation guidelines
```

**rules/modes/creative/uiux.md**:
```markdown
# UI/UX Design Guidance

When designing user interfaces:
1. Define user needs and constraints
2. Generate 2-4 design options
3. Analyze UX quality and accessibility
4. Consider consistency with design system
5. Select and justify recommendation
6. Document implementation guidelines
```

### Step 4: Set Up Environment

Create `.env` file:
```
ANTHROPIC_API_KEY=your_api_key_here
```

### Step 5: Initialize Memory Bank

```python
# memory_bank/initialize.py
from pathlib import Path

def initialize_memory_bank():
    """Create initial memory bank structure"""
    memory_bank = Path("memory_bank")
    memory_bank.mkdir(exist_ok=True)

    # Create tasks.md
    (memory_bank / "tasks.md").write_text("""# Tasks

## Current Task
[Task description will be added by VAN mode]

## Complexity Level
[Will be determined by VAN mode]

## Status
Pending initialization
""")

    # Create activeContext.md
    (memory_bank / "activeContext.md").write_text("""# Active Context

## Current Phase
VAN - Initialization

## Focus
[Will be set during mode execution]
""")

    # Create progress.md
    (memory_bank / "progress.md").write_text("""# Progress

## Implementation Status
Not started

## Completed Tasks
None

## Pending Tasks
[Will be updated during execution]
""")

    print("✅ Memory bank initialized")

if __name__ == "__main__":
    initialize_memory_bank()
```

Run initialization:
```bash
python memory_bank/initialize.py
```

### Step 6: Copy Code Files

Copy the code from Part 5 (Pydantic AI Complete Code) into the appropriate files:
- `models.py`: Copy the Models section
- `exceptions.py`: Copy the Custom Exceptions section
- `lazy_loader.py`: Copy the Lazy Rule Loader section
- `agents/van_agent.py`: Copy the VAN Agent section
- `agents/plan_agent.py`: Copy the PLAN Agent section
- `agents/creative_agent.py`: Copy the CREATIVE Agent section
- `orchestrator.py`: Copy the Orchestrator section
- `example.py`: Copy the Example Usage section

### Step 7: Test the System

```bash
python example.py
```

Expected output:
```
============================================================
Example 1: Level 1 Task (Bug Fix)
============================================================
OK VAN - Beginning Initialization Process

✅ VAN MODE COMPLETE - Level 1 task

Status: {'current_mode': 'VAN_COMPLETE', 'complexity': 1, ...}

============================================================
Example 2: Level 3 Task (Feature with Design)
============================================================
OK VAN - Beginning Initialization Process

🚫 LEVEL 3 TASK DETECTED
Implementation in VAN mode is BLOCKED
This task REQUIRES PLAN mode
Automatically transitioning to PLAN mode...

OK PLAN - Beginning Task Planning

🎨 CREATIVE PHASES REQUIRED
The following components need design decisions:
  - Authentication System (Architecture)
  - JWT Token Management (Algorithm)

Automatically transitioning to CREATIVE mode...

OK CREATIVE - Beginning Design Phase
📊 Loaded rules: 3
[Lazy Loading] Loading rule: creative-phase-architecture
[Lazy Loading] Loading rule: creative-phase-algorithm

✅ CREATIVE MODE COMPLETE

📊 Final loaded rules: 5

Status: {'current_mode': 'CREATIVE_COMPLETE', 'complexity': 3, ...}
```

## Advanced Features

### Custom Agent Tools

Add custom tools to agents:

```python
@creative_agent.tool
async def generate_diagram(ctx: RunContext[MemoryBankState],
                           diagram_type: str) -> str:
    """Generate Mermaid diagram for design"""
    # Implementation here
    return f"Generated {diagram_type} diagram"
```

### Persistence Layer

Add database storage:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DatabaseMemoryBank:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)

    def save_task(self, task_data: dict):
        # Implementation here
        pass

    def load_task(self, task_id: str):
        # Implementation here
        pass
```

### Metrics Tracking

Track token usage and performance:

```python
class MetricsTracker:
    def __init__(self):
        self.token_usage = {}
        self.mode_transitions = []
        self.lazy_loads = []

    def record_token_usage(self, mode: str, tokens: int):
        if mode not in self.token_usage:
            self.token_usage[mode] = 0
        self.token_usage[mode] += tokens

    def record_transition(self, from_mode: str, to_mode: str):
        self.mode_transitions.append({
            "from": from_mode,
            "to": to_mode,
            "timestamp": datetime.now()
        })

    def record_lazy_load(self, rule_name: str):
        self.lazy_loads.append({
            "rule": rule_name,
            "timestamp": datetime.now()
        })

    def generate_report(self) -> str:
        return f"""
Metrics Report:
--------------
Token Usage: {self.token_usage}
Transitions: {len(self.mode_transitions)}
Lazy Loads: {len(self.lazy_loads)}
"""
```

### Web Interface

Create a FastAPI web interface:

```python
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

orchestrator = MemoryBankOrchestrator()

@app.get("/")
async def get():
    return HTMLResponse("""
    <html>
        <head><title>Memory Bank System</title></head>
        <body>
            <h1>Memory Bank System</h1>
            <div id="status"></div>
            <script>
                // WebSocket connection for real-time updates
            </script>
        </body>
    </html>
    """)

@app.post("/api/run/{command}")
async def run_command(command: str, task_description: str = None):
    result = await orchestrator.run(command, task_description)
    return {"result": result, "status": orchestrator.get_status()}

@app.get("/api/status")
async def get_status():
    return orchestrator.get_status()
```

## Integration with Claude Code

### As a Skill

Create `.claude/skills/memory-bank/main.py`:

```python
from orchestrator import MemoryBankOrchestrator

class MemoryBankSkill:
    """Claude Code skill for memory bank workflow"""

    def __init__(self):
        self.orchestrator = MemoryBankOrchestrator()

    async def init_task(self, task_description: str):
        """
        Initialize a new task

        Usage: /memory-bank init "Add user authentication"
        """
        return await self.orchestrator.run("VAN", task_description)

    async def plan(self):
        """
        Create implementation plan

        Usage: /memory-bank plan
        """
        return await self.orchestrator.run("PLAN")

    async def design(self):
        """
        Make design decisions

        Usage: /memory-bank design
        """
        return await self.orchestrator.run("CREATIVE")

    async def status(self):
        """Get current status"""
        return self.orchestrator.get_status()
```

### As a Slash Command

Create `.claude/commands/van.md`:
```markdown
Initialize a new task using VAN mode

Usage:
/van Fix bug in authentication
/van Add user profile feature
```

## Troubleshooting

### Common Issues

#### 1. Import Errors
```
ModuleNotFoundError: No module named 'pydantic_ai'
```

Solution:
```bash
pip install pydantic-ai
```

#### 2. API Key Errors
```
Error: ANTHROPIC_API_KEY not found
```

Solution:
```bash
export ANTHROPIC_API_KEY=your_key_here
# Or add to .env file
```

#### 3. Rule File Not Found
```
FileNotFoundError: rules/modes/creative/architecture.md
```

Solution: Create the missing rule file with minimal content

#### 4. Agent Not Responding
Check that:
- API key is valid
- Model name is correct (`claude-sonnet-4`)
- System prompts are properly formatted
- Result validators are not throwing unexpected exceptions

### Debugging

Enable detailed logging:

```python
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# In orchestrator:
logger.debug(f"Running {command} mode")
logger.debug(f"State: {self.state}")
logger.debug(f"Loaded rules: {self.rule_loader.get_loaded_rules_list()}")
```

## Testing

### Unit Tests

```python
import pytest
from orchestrator import MemoryBankOrchestrator

@pytest.mark.asyncio
async def test_van_mode_level1():
    orch = MemoryBankOrchestrator()
    result = await orch.run("VAN", "Fix typo")
    assert orch.state.complexity.value == 1
    assert orch.state.current_mode == "VAN_COMPLETE"

@pytest.mark.asyncio
async def test_van_to_plan_transition():
    orch = MemoryBankOrchestrator()
    result = await orch.run("VAN", "Add new feature")
    assert orch.state.complexity.value >= 2
    assert orch.state.current_mode == "PLAN_COMPLETE"

@pytest.mark.asyncio
async def test_lazy_loading():
    orch = MemoryBankOrchestrator()
    initial_count = orch.rule_loader.get_loaded_rules_count()

    # Run creative mode
    orch.state.memory_bank_files['creative_components'] = ["test"]
    await orch._run_creative_mode()

    final_count = orch.rule_loader.get_loaded_rules_count()
    assert final_count > initial_count
```

Run tests:
```bash
pytest -v
```

---

**Document**: Part 6 of 7
**Previous**: [Pydantic AI Complete Code](05_pydantic_ai_complete_code.md)
**Next**: [Comparison & Conclusion](07_comparison_conclusion.md)
**Date**: 2025-11-04
**Author**: Claude (Sonnet 4.5)
