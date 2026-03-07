#!/usr/bin/env python3
"""Minimal test for hjkl key bindings."""

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.widgets import Static
from textual.containers import Container


class KeyTestApp(App):
    """Test app for key bindings."""

    CSS = """
    #status {
        height: 100%;
        content-align: center middle;
    }
    """

    BINDINGS = [
        Binding("h", "move_left", "Move Left", show=True),
        Binding("j", "move_down", "Move Down", show=True),
        Binding("k", "move_up", "Move Up", show=True),
        Binding("l", "move_right", "Move Right", show=True),
        Binding("left", "move_left", "Move Left", show=True),
        Binding("right", "move_right", "Move Right", show=True),
        Binding("up", "move_up", "Move Up", show=True),
        Binding("down", "move_down", "Move Down", show=True),
        Binding("q", "quit", "Quit", show=True),
    ]

    def __init__(self):
        super().__init__()
        self.messages = []

    def compose(self) -> ComposeResult:
        """Create the UI."""
        yield Static("Key Test - Press hjkl or arrows\n\n", id="status")

    def on_mount(self):
        """Log when mounted."""
        self.add_message("App mounted. Try pressing hjkl or arrows!")
        self.add_message(f"Focused widget: {self.focused}")

    def on_key(self, event) -> None:
        """Capture all key presses."""
        focused_name = self.focused.__class__.__name__ if self.focused else "None"
        self.add_message(f"🔑 Key: '{event.key}' - Focus: {focused_name}")

    def action_move_left(self):
        """Move left."""
        self.add_message("⬅️  LEFT ACTION TRIGGERED")

    def action_move_right(self):
        """Move right."""
        self.add_message("➡️  RIGHT ACTION TRIGGERED")

    def action_move_up(self):
        """Move up."""
        self.add_message("⬆️  UP ACTION TRIGGERED")

    def action_move_down(self):
        """Move down."""
        self.add_message("⬇️  DOWN ACTION TRIGGERED")

    def add_message(self, msg):
        """Add a message to the display."""
        self.messages.append(msg)
        # Keep last 20 messages
        if len(self.messages) > 20:
            self.messages = self.messages[-20:]

        # Update display
        status = self.query_one("#status", Static)
        status.update("\n".join(self.messages))


if __name__ == "__main__":
    app = KeyTestApp()
    app.run()
