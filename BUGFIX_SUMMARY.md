# Movement Keys Bug Fix - 2026-02-13

## Problem
- hjkl vim-style movement keys didn't work
- Left/Right arrow keys didn't work
- Up/Down arrow keys worked fine

## Root Causes

### Issue 1: Textual Action Parsing Bug
**Problem**: Textual 7.0.1 cannot parse negative numbers in binding action strings.

**Example**:
```python
Binding("left", "move(-1,0)", ...)  # FAILS - negative number breaks parser
Binding("right", "move(1,0)", ...)  # WORKS
```

**Solution**: Changed from parameterized actions to individual named actions:
```python
# Before (broken):
Binding("left", "move(-1,0)", ...)
Binding("h", "move(-1,0)", ...)

# After (fixed):
Binding("left", "move_left", ...)
Binding("h", "move_left", ...)

# And created individual action methods:
async def action_move_left(self):
    await self.action_move(-1, 0)
```

### Issue 2: ChatInput Widget Stealing Focus
**Problem**: The ChatInput widget's Input field had focus even when hidden, consuming all letter keypresses before they could reach the app-level key bindings.

**Evidence**: Debug logs showed `focused = Input(classes='-valid')` even though ChatInput was supposed to be hidden.

**Solution**: Disabled focus on the Input widget by default:
```python
# In ChatInput.compose():
self._input = Input(placeholder="Type your message...")
self._input.can_focus = False  # Disabled by default
yield self._input

# In ChatInput.show():
self._input.can_focus = True   # Enable only when showing

# In ChatInput.hide():
self._input.can_focus = False  # Disable when hiding
```

## Files Modified

1. **src/ui/textual/app.py**
   - Changed BINDINGS from parameterized to named actions
   - Added individual action methods: `action_move_left`, `action_move_right`, etc.

2. **src/ui/textual/widgets/chat_input.py**
   - Set `can_focus = False` on Input widget by default
   - Enable focus only when chat is shown
   - Disable focus when chat is hidden

3. **src/core/actions/move_action.py**
   - No functional changes (only temporary debug code, now removed)

## Testing
Created `test_keys.py` - minimal Textual app to test key bindings in isolation.
This confirmed the issue was specific to Veinborn's code, not Textual/terminal.

## Result
✅ All movement keys now work:
- hjkl (vim-style)
- Arrow keys (all directions)
- yubn (diagonals)
