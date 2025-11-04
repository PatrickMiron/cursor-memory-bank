# Memory Bank Command Customization

## Overview

// Start of Selection
This fork adds customization of Memory Bank mod commands while maintaining full backward compatibility. Users can use both the original commands and the new custom commands

## New Commands

| Original Command | New Command | Mode | Description |
|-------------------|-------------|------|-------------|
| `VAN` | `van` | VAN | Project initialization |
| `PLAN` | `plan` | PLAN | Task planning |
| `CREATIVE` | `arh` | CREATIVE | Creative phase |
| `IMPLEMENT` | `do` | IMPLEMENT | Implementation |
| `QA` | `qa` | QA | Testing |
| `REFLECT` | `sum` | REFLECT | Reflection |

## Backward Compatibility

✅ **All original commands continue to work:**
- `VAN` → VAN Mode
- `PLAN` → PLAN Mode
- `CREATIVE` → CREATIVE Mode
- `IMPLEMENT` → IMPLEMENT Mode
- `QA` → QA Mode
- `REFLECT` → REFLECT Mode
- `ARCHIVE` → ARCHIVE Mode

## Technical Changes

### Modified File
- `custom_modes/van_instructions.md`

### Added Sections
```mermaid
%% New Custom Commands
CommandDetect -->|"van"| VAN
CommandDetect -->|"plan"| Plan
CommandDetect -->|"arh"| Creative
CommandDetect -->|"do"| Implement
CommandDetect -->|"qa"| QA
CommandDetect -->|"sum"| Reflect
```

### REFLECT & ARCHIVE Support
```mermaid
CommandDetect -->|"REFLECT"| Reflect["REFLECT Mode"]
CommandDetect -->|"ARCHIVE"| Archive["ARCHIVE Mode"]
```

## Installation

### Automatic Installation
```bash
chmod +x install.sh
./install.sh
```

### Manual Installation
1. Copy `custom_modes/van_instructions.md` to your system
2. Create a backup of the original file
3. Replace the file with the modified version

## Testing

### Checking New Commands
```bash
# In Cursor, enter commands:
van    # Should activate VAN Mode
plan   # Should activate PLAN Mode
arh    # Should activate CREATIVE Mode
do     # Should activate IMPLEMENT Mode
qa     # Should activate QA Mode
sum    # Should activate REFLECT Mode
```

### Checking Backward Compatibility
```bash
# Original commands should continue to work:
VAN       # VAN Mode
PLAN      # PLAN Mode
CREATIVE  # CREATIVE Mode
IMPLEMENT # IMPLEMENT Mode
QA        # QA Mode
REFLECT   # REFLECT Mode
ARCHIVE   # ARCHIVE Mode
```

## Advantages

### For Users
- **Flexibility**: Choice between original and custom commands
- **Convenience**: Short commands for quick access
- **Safety**: Original commands are always available

### For Developers
- **Minimal Changes**: Only one file modified
- **Low Risk**: All functionality preserved
- **Easy Maintenance**: Easy to update and maintain

## Architecture

### Implementation Approach
- **Minimal Approach**: Only `van_instructions.md` modified
- **Centralized Control**: All commands in one place
- **Extensibility**: Easy to add new commands

### Command Structure
```
CommandDetect
├── Original Commands (VAN, PLAN, CREATIVE, etc.)
└── Custom Commands (van, plan, arh, etc.)
    └── All point to same mode handlers
```

## Recovery

### Restoring Original File
```bash
cp cursor-memory-bank/custom_modes/van_instructions.md.backup \
   cursor-memory-bank/custom_modes/van_instructions.md
```

### Checking Recovery
```bash
# After recovery, original commands should work
# New commands will stop working
```

## Change History

### Version 1.0.0 (2024-12-19)
- ✅ Added new commands: van, plan, arh, do, qa, sum
- ✅ Maintained backward compatibility
- ✅ Added REFLECT & ARCHIVE support
- ✅ Created documentation and installation scripts
- ✅ Added test files

## Support

### Issues and Solutions
1. **Commands don't work**
   - Check installation correctness
   - Ensure van_instructions.md file is correct

2. **Conflicts with other modifications**
   - Create backup before installation
   - Check compatibility

3. **System Recovery**
   - Use backup copy
   - Reinstall original Memory Bank

### Feedback
- Create Issue in repository
- Describe problem in detail
- Attach error logs

## Future Improvements

### Planned Features
- [ ] Additional commands
- [ ] Configuration file for commands
- [ ] Automatic updates
- [ ] Integration with other tools

### Suggestions
- Send suggestions through Issues
- Describe use cases
- Suggest new commands

## License

This fork follows the license of the original Memory Bank project. All changes are compatible with the original license.