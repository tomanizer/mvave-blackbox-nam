# M-Vave Blackbox NAM

Research and development towards running open-source **Neural Amp Modeler (NAM)** on the **M-Vave Blackbox guitar pedal**, using compatible captures from **TONE3000**.

**Status: research baseline, 11 October 2026. No Blackbox firmware has been built, installed or benchmarked by this project.**

The first prototype will process mono guitar input through one A2-Lite model and return mono audio. Model browsing, cabinet IRs, effects and a full replacement UI follow only after the audio engine meets its timing and memory requirements.

## Findings that matter

- The FCC filing provides internal photographs of a board marked `PD40 V04`, a JieLi-branded IC, a `74HC595D` and a display board marked `1.54TFT-SPI-ST7789`. See the [photograph guide](resources/photos/README.md).
- The official Blackbox V20 update contains the string `AC791N_STORY`. This supports investigating JieLi's AC791N / WL82 platform. The exact physical processor variant, available RAM and Blackbox pin assignments remain unverified.
- TONE3000 publishes an MIT-licensed embedded A2 runtime with portable C paths and ARM-specific optimized kernels. A PI32v2 port is a candidate, not a demonstrated solution.
- FM-1 firmware projects supply relevant toolchain, container and recovery research. Their board configuration, flash addresses and installers must not be applied to the Blackbox without validation.
- No recovery procedure has been demonstrated on the Blackbox by this project.

Source records, verification dates and qualifications are in the [source catalog](resources/SOURCES.md). The [claim register](docs/02-claims-and-corrections.md) preserves earlier leads and corrects unsupported statements.

## Documents

| Document | Purpose |
| --- | --- |
| [Project brief](docs/01-project-brief.md) | Objective, scope and first prototype acceptance criteria |
| [Claims and corrections](docs/02-claims-and-corrections.md) | Confirmed observations, hypotheses and rejected claims |
| [Hardware inventory](docs/03-hardware-inventory.md) | Components, photographs, confidence and missing measurements |
| [NAM feasibility](docs/04-nam-feasibility.md) | Model compatibility, memory, timing and numerical checks |
| [Proposed architecture](docs/05-proposed-architecture.md) | Audio, controls and desktop model preparation |
| [Firmware and tools](docs/06-firmware-and-toolchain.md) | V20 observations and reusable FM-1/JieLi tooling |
| [Backup and recovery](docs/07-backup-and-recovery.md) | Work required before any experimental flash write |
| [Development roadmap](docs/08-development-roadmap.md) | Deliverables and dependencies |
| [Research log](docs/09-research-log.md) | What was checked and what remains open |
| [Offline baseline](docs/10-offline-baseline.md) | Independent V20 work and reproduced NAM host test |
| [Third-party material](THIRD_PARTY.md) | Attribution and source distribution rules |
| [Datasheets](resources/datasheets/README.md) | Component-specific document links and applicability |
| [Photographs](resources/photos/README.md) | Three attributed detail excerpts and original exhibits |

## Reproduce the initial observations

Python 3.9 or newer is sufficient for these read-only utilities:

```sh
python3 tools/fetch_sources.py --id S05 --output research/downloads
python3 tools/inspect_firmware.py research/downloads/S05-BlackBox.fwsc
```

The downloader retrieves selected public source files into an ignored local directory and checks a recorded SHA-256 when available. It neither opens device connections nor installs firmware. Third-party firmware, full photo exhibits and vendor datasheets are referenced at their original locations rather than relicensed by this project.

## Contribute

Useful contributions are readable board photographs, complete IC markings, non-invasive USB enumeration, documented flash geometry, and reproducible PI32v2 CPU/RAM measurements. Record the board revision and distinguish a measurement from an inference. See [CONTRIBUTING.md](CONTRIBUTING.md).

Original documents and utilities are under the MIT license. Photograph excerpts retain their source owners' rights; see [THIRD_PARTY.md](THIRD_PARTY.md). This is an independent project, unaffiliated with M-Vave, Sinco, JieLi, NAM or TONE3000.
