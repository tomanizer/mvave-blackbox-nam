# Research log

## 2026-10-11: initial baseline

The chosen objective is native open-source NAM inference on the M-Vave guitar Blackbox using compatible TONE3000 captures. Earlier discussion supplied FM-1, JieLi, editor and FCC leads. They are retained in the source catalog with explicit status.

Retrieved and visually inspected the 2024 FCC internal-photo PDF. Its SHA-256 matches the indexed exhibit. Confirmed the board, logic-chip and display-board labels and JieLi branding; did not assign an unreadable processor model. Located the later 2025 photo exhibit but did not retrieve or compare its bytes in this pass.

Retrieved the official Blackbox update and GB18030 release note. Recorded size and SHA-256, scanned selected ASCII markers and confirmed the AC791N-family string. This is initial container inspection, not a flash dump, decompilation or proof of board compatibility.

Read the current TONE3000 embedded README, A2-Lite header/C path, C binary reader and license. Verified that an allocation-free C candidate exists, but optimized kernels target ARM. Read the binary-loader and NAM core references. No target benchmark or on-pedal NAM result was produced.

Checked the FM-1 architecture, Felucca build guide, incomplete Ghidra module, JieLi SDK, bootloader and Blackbox editor references. Pinned verified GitHub repository revisions in `research/upstream-revisions.json`. GitHub metadata retrieval was rate-limited for some additional repositories; unpinned leads are labelled accordingly.

Retrieved candidate AC7911B/AC7913A6/AC7916A, ST7789V and 74HC595 datasheets for inspection. The JieLi and Sitronix documents contain explicit restrictions on reproduction; the public package links to them and records their hashes instead of copying them. No candidate processor datasheet is presented as the exact Blackbox part.

Corrected the generic Highleap article citation, the claimed LVGL UI, the 74HC595 button-reading explanation, the universal four-ADC/four-DAC assertion and the claimed turnkey recovery path. The [claim register](02-claims-and-corrections.md) records remaining uncertainties.

## What has not happened

No pedal was opened or measured in this research pass; the source photographs are FCC filing photographs. No firmware was flashed. No debug pins, Blackbox address map or full BOM were established. No API account was connected to TONE3000 and no user model library was downloaded. The repository contains research and read-only utilities, not a working replacement firmware.

## Next checkpoint

Complete BB-01, BB-03 and BB-06, then review target resources and the independent recovery path before deciding whether the hardware merits a full port.

## 2026-10-11: offline follow-up

Compared the outer V20 update with an independent Blackbox V20 research repository. Its decrypted application mapping, USB descriptors and boot-entry analysis are useful upstream reports, but the application hash and findings have not yet been reproduced from decrypted local bytes. Ran TONE3000's pinned `make check-all` host suite with its supplied example captures and reference audio; the A2-Lite tests passed. See [offline baseline](10-offline-baseline.md) for exact revisions, hashes, limits and next checks. BB-03 and BB-06 have partial evidence; neither is complete.
