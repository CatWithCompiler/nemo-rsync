Nemo Rsync

A lightweight Nemo extension that adds an "Rsync to..." context menu entry.

It behaves like Nemo's Copy To..., but performs the transfer using rsync while displaying a small progress terminal.

The goal is not to replace rsync, nor to become another graphical rsync frontend.

The goal is simply to make one of Linux's most reliable file copy tools available directly from Nemo.

Features
Right-click Rsync to... context menu entry.
Native GTK folder selection dialog.
Uses rsync for all transfers.
Small terminal window displaying:
Overall progress
Amount transferred
Transfer speed
Estimated remaining time
Closing the terminal window immediately cancels the transfer.
Supports copying one or multiple selected files/folders.
Non-Goals

This project intentionally does not provide:
rsync option editor
preferences dialog
bookmarks manager
favourites
scheduled transfers
synchronization jobs
background daemon
queue manager
advanced rsync flags

Nemo Rsync intentionally does not:
• Replace rsync
• Replace SSH
• Store passwords
• Become a synchronization suite
• Run background services
• Hide terminal output
• Invent its own transfer protocol

If you need advanced rsync functionality, use rsync directly from the terminal.

Design Principles:
1. No settings unless absolutely necessary.
2. No feature should require reading a manual.
3. Behave like Nemo whenever possible.
4. Let rsync do the heavy lifting.
5. If a feature adds complexity without helping the core workflow, don't add it.
6. Explain first, diagnose second. Present technical details in human language whenever possible. Keep diagnostic information available, but secondary.
7. Never hide useful information. Organize it.

Project Philosophy:
The plugin should adapt to the user's system, not ask the user to adapt to the plugin.

Whenever possible it should automatically use:

the user's preferred GTK theme
the system file chooser
an available terminal emulator
existing Linux tools

without requiring any configuration.

Planned Architecture
Nemo
 │
 ▼
Context Menu
 │
 ▼
Folder Picker (GTK)
 │
 ▼
Python Launcher
 │
 ▼
Terminal Emulator
 │
 ▼
rsync


Version Roadmap:

v0.1.0
Project skeleton
GTK folder picker
Runner script

v0.2.0
Launch terminal
Launch rsync
Display progress

v0.3.0
Nemo integration
Right-click context menu

v1.0.0
First stable release.
Feature complete.

Future Development
Bug fixes.
Compatibility updates.

Nothing else unless it clearly improves the core workflow.

License

(To be decided)


# The "Grandma Test"

The plugin should be simple enough that someone who already knows
how to use "Copy To..." in Nemo can immediately understand
"Rsync to..." without reading documentation.

If a new feature would cause this statement to become false,
it probably does not belong in the project.


# Why another rsync frontend?

Many graphical rsync frontends already exist.

This project intentionally takes a different approach.

Instead of exposing the full rsync feature set, Nemo Rsync focuses on one workflow:

Right click → Rsync to... → Select destination → Copy.

Nothing more.

The goal is to feel like a natural extension of Nemo rather than a separate application.