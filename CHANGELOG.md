# Changelog

## v0.1.0

- Initial project structure
- README
- GTK folder picker
- Python runner

## v0.2.0

- Finalized `rsync_runner.sh`
- Updated README

## v0.3.0

- Restructured project folders in preparation for v1.0

## v0.4.0

- Successfully integrated with Nemo's extension system
- Added first working context menu callback
- Verified Python extension loading and activation
- Added Rsync submenu
- Added local and SSH menu callbacks

## v0.5.0

- added install-dev script to simlink the working development directory to Nemo-Python/extensions directory
- Updated nemo_rsync_extension with simlink and debug capability

## v1.0

- Nemo integration
- "Rsync > Rsync to..." context menu
- Local rsync transfers

## V2.0

- Rsync to SSH added
- Install script added
- Updated README.md
- Updated plugin version to 2.0

---

# Roadmap

## v1.0

- Nemo integration
- "Rsync > Rsync to..." context menu
- Local rsync transfers

## v2.0

- Rsync to SSH

## v3.0

- Mirror

## v4.0

- Synchronize

## v5.0

- Mirror to SSH

## v6.0

- Synchronize to SSH

## v7.0

- Defaults / Settings dialog
- Plugin preferences
- `--dry-run` toggle



# Project Goal

Nemo Rsync is not intended to expose every rsync command-line option.

It provides a simple graphical workflow for the most common rsync operations while leaving advanced usage to the terminal.