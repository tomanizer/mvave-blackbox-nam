# Development roadmap

The issue-ready tasks below are proposals. Research documents exist; hardware milestones remain open. IDs are local task identifiers, not GitHub issue numbers.

| ID | Deliverable | Depends on | Acceptance |
| --- | --- | --- | --- |
| BB-01 | Identify target board and processor | None | Both board faces, all IC markings, board revision and matched datasheets |
| BB-02 | Baseline stock behavior | None | USB descriptors, sample rate, analog latency and saved user presets |
| BB-03 | Offline V20 container analysis | None | Hash, segments, metadata, processor confirmation and confidence notes |
| BB-04 | Establish read-only recovery/backup path | BB-01, BB-03 | Blackbox-specific entry, verified full dumps and protected data ranges |
| BB-05 | Reproduce PI32v2 build | BB-01, BB-03 | Pinned SDK/compiler, ABI check and linker map; no device write required |
| BB-06 | NAM host reference harness | None | Compatible A2-Lite capture, golden input/output, model provenance and tolerances |
| BB-07 | Compile portable C NAM for PI32v2 | BB-05, BB-06 | No ARM instructions, actual structure sizes and target code size |
| BB-08 | Minimum hardware bring-up | BB-04, BB-05 | Demonstrated permitted execution path, clocks, timer and optional screen status |
| BB-09 | Verified mono ADC-to-DAC passthrough | BB-01, BB-08 | Gain/routing, sample format, continuous audio, measured latency and overrun counters |
| BB-10 | Target NAM CPU and RAM benchmark | BB-07, BB-08 | Numerical results, complete memory accounting and timing margin |
| BB-11 | Playable mono NAM prototype | BB-09, BB-10 | One supported model; endurance, analog latency and control-load checks |
| BB-12 | Validated capture transfer and presets | BB-11 | Bounds/CRC/config checks, unsupported-model rejection and muted swapping |
| BB-13 | Cabinet IR and optional effects | BB-11 | Explicit remaining CPU/RAM budget and justified capture/IR combination |
| BB-14 | Replacement UI and editor | BB-12 | Supported model selection, clear errors, state persistence and bounded audio impact |
| BB-15 | First public firmware release | BB-04, BB-11, BB-12 | Known hardware list, licenses, build reproduction, image hashes and tested recovery |

BB-03 and BB-06 are the first software tasks. BB-01 and BB-02 need access to actual hardware; BB-04 precedes experimental persistent writes. A screen demo should not delay host numerical checks or target compilation, and it is not proof that audio works.

## Immediate work packages

**Hardware identification (BB-01):** collect full-resolution marked-up photographs, identify storage and processor variant, and update `research/components.csv` with page/location, observation and confidence.

**Container analysis (BB-03):** start from the recorded V20 hash, pin a compatible unpacker, list sections without flashing, and compare SDK lineage with FM-1 references. Keep physical board claims separate from update metadata.

**NAM host reference (BB-06):** select a compatible A2-Lite capture with clear reuse rights, compare portable embedded output with a pinned NAM reference and retain the exact numerical tolerance and inputs.

**Recovery research (BB-04):** verify interfaces and electrical compatibility on the identified board, then document read-only chip information and repeatable backups before designing a write procedure.
