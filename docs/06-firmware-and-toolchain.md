# Firmware and toolchain research

## Official Blackbox update

The [vendor download page](https://www.m-vave.com/download) lists ANNBLACKBOX V20 dated **2026-01-31**. Its release note states that V20 adds AM4-format files for the AMP module. The checked update URL is public but mutable; identify the file by its hash.

| Item | Value |
| --- | --- |
| Update filename | `BlackBox.fwsc` |
| Bytes retrieved | 700,436 |
| SHA-256 | `c0fef191b860d3b20f77fc492a24986eef2d12df44bb5e38355684820e26cb08` |
| Retrieval date | 2026-10-11 |
| Public URL | [BlackBox.fwsc](https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/firmware/BlackBox.fwsc) |
| Release-note URL | [BlackBox.txt](https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/releaseNote/firmware/BlackBox.txt) |
| Release-note encoding observed | GB18030 |

An initial read-only byte scan found:

| Literal | Offset in update package (decimal) |
| --- | --- |
| `AC791N_STORY` | 1,060 |
| `uboot.` | 690,122 |
| `*.ufw` | 700,105 |
| `JLUFW` | 700,420 |

Offsets belong to the downloaded **update container**, not CPU addresses or physical flash sectors. The package has not been fully unpacked here. A firmware update is not a complete backup of flash, presets, calibration, device identity or recovery components. The short `uboot.` match does not establish a valid bootloader layout.

Reproduce with [inspect_firmware.py](../tools/inspect_firmware.py); [initial inspection JSON](../research/firmware-inspection.json).

## Reusable upstream work

| Source | Use | Blackbox limitation |
| --- | --- | --- |
| [AL-255/FM-1-RE](https://github.com/AL-255/FM-1-RE) | Architecture notes, image extraction, function mapping and PI32v2 setup | FM-1 addresses, SDK linkage and board functions require fresh verification |
| [Felucca BUILDING.md](https://github.com/hugelton/Felucca/blob/main/BUILDING.md) | PI32v2 compiler and AC79 SDK packaging references | Toolchain is vendor-derived; firmware is for FM-1 |
| [JieLi AC79 SDK](https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK) | WL82 register definitions, audio examples and board support | Not a Blackbox BSP; some resources are package-specific |
| [ghidra-jieli](https://github.com/kagaimiq/ghidra-jieli) | Processor language support | PI32v2 implementation is explicitly incomplete |
| [jl-misctools](https://github.com/kagaimiq/jl-misctools) | Container inspection and unpacking | Confirm actual container variant before interpreting results |
| [JieLi fw-Bootloader](https://github.com/Jieli-Tech/fw-Bootloader) | Vendor bootloader reference | A repository's existence does not prove Blackbox compatibility |
| [FM-1 Transporter](https://github.com/kurogedelic/FM-1-transporter) | ROM-entry, flash read and RAM-execution research | Hardware and commands have not been validated on Blackbox |
| [Blackbox web editor](https://github.com/jvsobrinho/mvave-blackbox-edit) | Existing BLE control protocol implementation | Controls stock firmware; does not provide a NAM engine or full audio driver |

The official SDK lives on Gitee. `jeffreywugz/fw-AC79_AIoT_SDK` is a third-party GitHub mirror. The previously cited `github.com/Jieli-Tech/fw-AC79_AIoT_SDK` URL returned 404 during this pass.

## Next offline analysis

Pin tools and SDK revisions. Unpack a copy of the recorded update, inventory segments and identify processor/platform from independent metadata. Compare recognizable SDK functions with FM-1 references. Cross-check disassembly, constants and register accesses before assigning GPIO or audio roles. Record exact offsets, source hashes and confidence.

Finding ST7789 command bytes such as `0x36` or `0x3A` alone is insufficient: they occur in many unrelated data sequences. Require a coherent initialization table, its call path and actual panel behavior.
