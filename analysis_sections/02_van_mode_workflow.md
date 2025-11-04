# VAN Mode Workflow Analysis

## Overview

VAN (Initialization) mode is the **entry point** for the entire cursor-memory-bank system. It performs project initialization, platform detection, file verification, and most critically, **complexity determination** that drives workflow routing.

## File References

- **Entry Point**: `custom_modes/van_instructions.md` (lines 1-247)
- **Workflow Map**: `.cursor/rules/isolation_rules/visual-maps/van_mode_split/van-mode-map.mdc`

## Activation Flow

When you type `VAN` or `van`:

```
Command → "OK VAN" response
  ↓
Check Memory Bank (MANDATORY)
  ↓
Load: van-mode-map.mdc
  ↓
Platform Detection (Windows/Mac/Linux)
  ↓
Basic File Verification
  ↓
Complexity Determination (KEY DECISION POINT)
  ├─ Level 1 → Continue in VAN → Initialize → Done
  └─ Level 2-4 → FORCE EXIT to PLAN mode
```

## Critical Steps

### 1. Command Detection (lines 8-26)
Recognizes both original and custom commands:
- Original: `VAN`, `PLAN`, `CREATIVE`, `IMPLEMENT`, `QA`, `REFLECT`, `ARCHIVE`
- Custom: `van`, `plan`, `arh`, `do`, `qa`, `sum`

### 2. Immediate Response (lines 28-34)
Returns confirmation: "OK VAN"

### 3. Memory Bank Check (lines 37-43)
**MANDATORY** - verifies memory bank exists before proceeding

### 4. Rule Loading (lines 46-52)
Loads mode-specific visual maps from `.cursor/rules/isolation_rules/visual-maps/`

### 5. Platform Detection
Detects operating system (Windows/Mac/Linux) and adapts commands accordingly

### 6. File Verification
Verifies essential files exist:
- Memory bank structure
- Documentation files
- Project configuration

## Complexity Determination (THE KEY MECHANISM)

**File Reference**: `van-mode-map.mdc:39-42`

This is the **core workflow control mechanism**. VAN mode analyzes the task and determines complexity:

### Complexity Levels

#### Level 1: Quick Bug Fix
- **Scope**: Single file modification
- **Risk**: Low impact
- **Effort**: Minutes
- **Examples**:
  - Fix typo in error message
  - Correct simple configuration value
  - Update comment or documentation
- **Workflow**: Can implement directly in VAN mode

#### Level 2: Simple Enhancement
- **Scope**: Few files, isolated change
- **Risk**: Low to medium impact
- **Effort**: Hours
- **Examples**:
  - Add new utility function
  - UI tweak to existing component
  - New simple API endpoint
- **Workflow**: **FORCES transition to PLAN mode**

#### Level 3: Intermediate Feature
- **Scope**: Multiple files, new component
- **Risk**: Medium impact
- **Effort**: Days
- **Examples**:
  - New feature with UI + backend
  - New component with state management
  - API endpoint with database interaction
- **Workflow**: **FORCES transition to PLAN → CREATIVE modes**

#### Level 4: Complex System
- **Scope**: Multiple subsystems, architectural change
- **Risk**: High impact
- **Effort**: Weeks
- **Examples**:
  - Major architectural refactor
  - New authentication system
  - Database migration
  - Multi-service integration
- **Workflow**: **FORCES full workflow** (VAN → PLAN → CREATIVE → IMPLEMENT)

## The Force Exit Mechanism

**Critical Lines**: `van-mode-map.mdc:39-42`

When VAN mode detects Level 2-4 complexity:

```
🚫 LEVEL [2-4] TASK DETECTED
Implementation in VAN mode is BLOCKED
This task REQUIRES PLAN mode
You MUST switch to PLAN mode for proper documentation and planning
Type 'PLAN' to switch to planning mode
```

**This is enforced workflow control** - the system prevents proceeding without proper planning.

## Complexity Analysis Criteria

VAN mode evaluates tasks based on:

1. **Scope**: Single file vs. multiple subsystems
2. **Risk**: Low vs. high impact changes
3. **Effort**: Minutes vs. hours/days
4. **Dependencies**: Isolated vs. cross-cutting concerns
5. **Architecture**: Simple change vs. structural modification

## Memory Bank Initialization

For Level 1 tasks that continue in VAN:

1. Create/verify memory bank structure:
   - `tasks.md`: Task description and status
   - `activeContext.md`: Current focus
   - `projectbrief.md`: Project overview

2. Platform-specific setup:
   - Detect OS
   - Configure path separators
   - Set appropriate commands

3. File verification:
   - Check project structure
   - Verify dependencies
   - Validate configuration

## Output from VAN Mode

### For Level 1:
- Memory bank initialized
- Task documented in `tasks.md`
- Ready to proceed with implementation

### For Level 2-4:
- Complexity level recorded
- Task documented with complexity flag
- **Forced transition to PLAN mode**
- User prompted to type `PLAN`

## Integration with Other Modes

VAN mode is the only mode that can:
- Initialize a new task
- Determine complexity level
- Set up the memory bank structure
- Route to appropriate workflow path

All other modes assume VAN has already:
- Created memory bank
- Determined complexity
- Documented initial task requirements

---

**Document**: Part 2 of 7
**Previous**: [Executive Summary](01_executive_summary.md)
**Next**: [PLAN Mode Workflow](03_plan_mode_workflow.md)
**Date**: 2025-11-04
**Author**: Claude (Sonnet 4.5)
