# Backup and recovery requirements

**No Blackbox recovery procedure has been established by this project.** This document describes required evidence before experimental writes; it is not a flashing guide.

## Distinguish the paths

Normal stock application update entry, a flash-resident loader and immutable ROM recovery are separate mechanisms. An updater that works while stock firmware runs is not proof that a broken application can be restored.

FM-1 Transporter documents an FM-1 ROM-entry and read/write workflow. It is a candidate reference for the Blackbox, not authorization to reuse its wiring, USB key, loader, sector range or commands.

## Before the first write

| Requirement | Evidence to retain |
| --- | --- |
| Identify board and storage | Board revision, readable component markings, flash size and voltage |
| Establish independent recovery entry | Exact equipment and procedure, observed descriptors and successful repeated entry on this revision |
| Obtain a complete backup | Read ranges, tool revision, two independent matching dumps and hashes |
| Preserve unique data | Identified calibration, configuration, identity and radio data kept privately |
| Understand image layout | Separate container offsets, flash offsets, CPU addresses and protected ranges |
| Validate a restore plan | Verified source image, compatible programmer/loader and readable verification results |
| Try non-persistent execution where available | Documented RAM loading with known memory ranges and exit behavior |

Do not infer that removing read protection preserves flash: some devices erase when protection changes. Do not perform blind erases or overwrite a running application without a proven recovery path. A spare unit is appropriate for destructive experiments, but its identity/calibration data are not a substitute for the target unit's backup.

## Release requirements

Publish a supported-board list, image hash, layout constraints, demonstrated restore method and explicit status of any untested revision. Never advertise the device as unbrickable. An application crash alone is not a hard brick; inaccessible recovery or overwritten device data can be materially worse.

No flash-data shorting procedure, ST-Link recipe or speculative pin diagram is approved or implemented in this baseline.
