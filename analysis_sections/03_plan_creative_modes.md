# PLAN and CREATIVE Modes Analysis

## PLAN Mode Workflow

### Overview
PLAN mode creates complexity-appropriate implementation plans and identifies components requiring creative design decisions.

### File References
- **Instructions**: `custom_modes/plan_instructions.md`
- **Workflow Map**: `.cursor/rules/isolation_rules/visual-maps/plan-mode-map.mdc`

### Activation Flow

When you type `PLAN` or `plan`:

```
Command → "OK PLAN" response
  ↓
Check Memory Bank
  ↓
Load: plan-mode-map.mdc
  ↓
Read tasks.md (get complexity level)
  ↓
Determine Planning Approach based on Complexity
  ├─ Level 2 → Simplified planning
  ├─ Level 3 → Comprehensive planning + flag creative components
  └─ Level 4 → Phased implementation + architectural diagrams
  ↓
Update tasks.md with plan
  ↓
Check if creative phases required
  ├─ Yes → Recommend CREATIVE mode
  └─ No → Recommend IMPLEMENT mode
```

### Planning by Complexity Level

#### Level 2: Simplified Planning
Creates basic plan with:
- **Overview of changes**: What needs to be modified
- **Files to modify**: List of affected files
- **Implementation steps**: Ordered tasks
- **Potential challenges**: Known issues to watch for
- **Testing strategy**: How to verify changes

#### Level 3-4: Comprehensive Planning
Creates detailed plan with:
- **Requirements analysis**: What the feature must accomplish
- **Components affected**: All systems impacted
- **Architecture considerations**: Design decisions needed
- **Implementation strategy**: Phased approach
- **Detailed steps**: Granular task breakdown
- **Dependencies**: What must be done first
- **Challenges & mitigations**: Risks and solutions
- **Creative phase components**: Which parts need design exploration

### Creative Phase Identification

PLAN mode flags components that require creative problem-solving:

#### When to Flag for CREATIVE:
- **Architecture Decisions**: System structure choices
- **Algorithm Design**: Performance-critical logic
- **UI/UX Design**: User interface components
- **Complex Integration**: Multiple system interactions
- **Novel Solutions**: No established pattern exists

#### Example Flagging:
```markdown
## Components Requiring Creative Phase

1. **Authentication Flow** (Architecture)
   - Need to decide between session-based vs. JWT
   - Consider refresh token strategy
   - Evaluate security implications

2. **Search Algorithm** (Algorithm)
   - Need efficient full-text search
   - Consider fuzzy matching approach
   - Evaluate performance vs. accuracy

3. **Dashboard Layout** (UI/UX)
   - Multiple data visualization options
   - Need to balance information density
   - Consider responsive design patterns
```

### Force Transition to CREATIVE

**File Reference**: `plan-mode-map.mdc:46-49`

When PLAN identifies components needing creative phases:

```
🎨 CREATIVE PHASES REQUIRED
The following components need design decisions:
  - Authentication Flow (Architecture)
  - Search Algorithm (Algorithm)
  - Dashboard Layout (UI/UX)

Type 'CREATIVE' to begin design phase
```

---

## CREATIVE Mode Workflow

### Overview
CREATIVE mode performs structured design exploration for flagged components, generating multiple options and selecting the best approach.

### File References
- **Instructions**: `custom_modes/creative_instructions.md`
- **Workflow Map**: `.cursor/rules/isolation_rules/visual-maps/creative-mode-map.mdc`
- **Specialized Rules** (lazy loaded):
  - `creative-phase-architecture.mdc`
  - `creative-phase-algorithm.mdc`
  - `creative-phase-uiux.mdc`

### Activation Flow

```
Command → "OK CREATIVE" response
  ↓
Check Memory Bank
  ↓
Load: creative-mode-map.mdc (essential only)
  ↓
Read components flagged for creative phases
  ↓
For each component:
  ├─ Determine creative phase type
  │   ├─ Architecture → Lazy load: creative-phase-architecture.mdc
  │   ├─ Algorithm → Lazy load: creative-phase-algorithm.mdc
  │   └─ UI/UX → Lazy load: creative-phase-uiux.mdc
  ├─ Generate 2-4 design options
  ├─ Analyze pros/cons of each
  ├─ Select and justify recommended approach
  ├─ Document implementation guidelines
  └─ Verify against requirements
  ↓
Update Memory Bank with all design decisions
  ↓
Check for more components
  ├─ Yes → Process next component
  └─ No → Recommend IMPLEMENT mode
```

### Creative Phase Types

#### 1. Architecture Design
**Focus**: System structure, component relationships, technical foundations

**Process**:
1. Define requirements and constraints
2. Generate 2-4 architecture options
3. Document pros/cons of each
4. Evaluate against criteria:
   - Scalability
   - Maintainability
   - Performance
   - Security
   - Cost
   - Time to market

**Example Output**:
```markdown
### Option 1: Microservices Architecture
**Pros**:
- Independent scaling of services
- Technology flexibility per service
- Fault isolation

**Cons**:
- Increased operational complexity
- Network latency between services
- Distributed debugging challenges

**Evaluation**: High scalability, Medium maintainability
```

#### 2. Algorithm Design
**Focus**: Efficiency, correctness, time/space complexity

**Process**:
1. Define requirements and constraints
2. Generate 2-4 algorithm options
3. Analyze each:
   - Time complexity (Big O)
   - Space complexity
   - Edge case handling
   - Scalability characteristics

**Example Output**:
```markdown
### Option 1: Binary Search Tree
**Time Complexity**: O(log n) average, O(n) worst
**Space Complexity**: O(n)
**Pros**: Fast average case, simple to implement
**Cons**: Degrades to O(n) without balancing
**Edge Cases**: Empty tree, single node, skewed tree
```

#### 3. UI/UX Design
**Focus**: User experience, accessibility, design patterns

**Process**:
1. Define user needs and constraints
2. Generate 2-4 design options
3. Analyze each:
   - User experience quality
   - Accessibility (WCAG compliance)
   - Consistency with design system
   - Component reusability

**Example Output**:
```markdown
### Option 1: Card-Based Layout
**UX**: Familiar pattern, easy to scan
**Accessibility**: High - semantic HTML, keyboard nav
**Consistency**: Matches existing design system
**Reusability**: Cards can be reused across views
```

### Creative Phase Documentation Format

Each creative phase produces structured documentation:

```markdown
🎨🎨🎨 ENTERING CREATIVE PHASE: [Architecture/Algorithm/UI-UX]

## Component: [Name]

### Description
[What this component does]

### Requirements & Constraints
- Requirement 1
- Requirement 2
- Constraint 1

### Option 1: [Name]
**Description**: [Brief description]
**Pros**: [List]
**Cons**: [List]
**Technical Fit**: [High/Medium/Low]

### Option 2: [Name]
...

### Recommended Approach
**Selection**: Option [N]
**Rationale**: [Why this option was chosen]

### Implementation Guidelines
1. [Step-by-step guidance]
2. [Code patterns to follow]
3. [Testing approach]

### Verification
✓ Requirement 1 met
✓ Requirement 2 met
✓ Constraints satisfied

🎨🎨🎨 EXITING CREATIVE PHASE
```

### Lazy Loading in CREATIVE Mode

This is where lazy loading shines!

**Initial Load** (~3,000 tokens):
- `creative-mode-map.mdc` (essential workflow only)
- Core creative phase rules

**Lazy Loaded** (only when needed):
- `creative-phase-architecture.mdc` (~5,000 tokens)
  - Loaded only if Architecture design needed
- `creative-phase-algorithm.mdc` (~4,000 tokens)
  - Loaded only if Algorithm design needed
- `creative-phase-uiux.mdc` (~3,000 tokens)
  - Loaded only if UI/UX design needed

**Token Savings**:
- Without lazy loading: 15,000 tokens
- With lazy loading: 3,000 + (5,000 for what's actually needed)
- Typical savings: 7,000-9,000 tokens (47-60% reduction)

### Memory Bank Updates

CREATIVE mode creates:
- `creative-[component-name].md`: Design decisions for each component
- Updates `tasks.md` with design status
- Updates `activeContext.md` with current component being designed

### Transition to IMPLEMENT

After all creative phases complete:

```
✅ CREATIVE MODE COMPLETE - Design decisions documented

All components have completed creative phases:
✓ Authentication Flow - Architecture decisions documented
✓ Search Algorithm - Algorithm design selected
✓ Dashboard Layout - UI/UX design finalized

Ready to proceed to IMPLEMENT mode
Type 'IMPLEMENT' to begin implementation
```

---

**Document**: Part 3 of 7
**Previous**: [VAN Mode Workflow](02_van_mode_workflow.md)
**Next**: [Lazy Loading Deep Dive](04_lazy_loading_deep_dive.md)
**Date**: 2025-11-04
**Author**: Claude (Sonnet 4.5)
