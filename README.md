Nemo Rsync

A lightweight Nemo extension for Linux Mint Cinnamon's file manager that adds an **"Rsync to..."** and **"Rsync to SSH..."**context menu entries.

It behaves like Nemo's Copy To..., but performs the transfer using rsync while displaying a small progress terminal.

The goal is not to replace rsync, nor to become another graphical rsync frontend.

The goal is simply to make one of Linux's most reliable file copy tools available directly from Nemo.

**Nemo Rsync stores no configuration, no transfer history, and no passwords.**


## Prerequisites

Install the required Nemo Python extension support from the Software Manager or through the terminal as follows:

```bash
sudo apt install nemo-python
```

After installation, restart Nemo:

```bash
nemo -q
```

Then launch Nemo again.


## How to install

2. Right-click install.sh
3. Choose Properties → Permissions
4. Enable "Allow executing file as program"
5. Open a terminal in the folder where install.sh is located
6. type "./install.sh" without quotes and press enter

## Development

For development, run:

    install-dev.sh

This will create symbolic links from your project directory to the appropriate plugins folders.



## Features

• Right-click "Rsync to..."
• Right-click "Rsync to SSH..."
• Native GTK destination dialogs
• Supports multiple selected files and folders
• Uses rsync directly
• Uses the system terminal emulator
• Live transfer progress
• SSH password or SSH key authentication
• Closing the terminal immediately cancels the transfer

This project intentionally does not provide:
• rsync option editor
• preferences dialog
• bookmarks manager
• favourites
• scheduled transfers
• synchronization jobs
• background daemon
• queue manager
• advanced rsync flags

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
**The plugin should adapt to the user's system, not ask the user to adapt to the plugin.**

Whenever possible it should automatically use:
• the user's preferred GTK theme
• the system file chooser
• an available terminal emulator
• existing Linux tools

without requiring any configuration.

## Architecture

Nemo
 │
 ▼
Context Menu
 │
 ▼
Local GTK Dialog
    │
    ├──────────────┐
    ▼              ▼
Folder Picker   SSH Dialog
        │          │
        └────┬─────┘
             ▼
      Python Launcher
             │
             ▼
     Terminal Emulator
             │
             ▼
           rsync





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


## License

MIT License