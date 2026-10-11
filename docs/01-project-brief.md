# Project brief

Research baseline: **2026-10-11**.

## Objective

Replace the M-Vave Blackbox's proprietary amp inference engine with an open-source NAM implementation that can load a defined subset of TONE3000 captures. Preserve the existing enclosure and analog hardware where practical.

The selected direction is a custom on-device firmware project. An external MIDI/Bluetooth controller can help inspect the existing pedal but cannot replace the audio inference engine.

## First prototype

One mono input, one compatible A2-Lite capture, one mono output, at the capture's supported sample rate. Provide bounded input/output gain and a mute control. Keep the first audio demonstration independent of a complete UI or effects chain.

| Requirement | Acceptance evidence |
| --- | --- |
| Correct model | Configuration, sample rate and weight count match the pinned embedded engine |
| Correct output | Identical test input compared against a pinned NAM reference; tolerances and error metrics published |
| Continuous audio | No observed overruns during a specified endurance run and deliberate control/display activity |
| Timing | Worst observed complete callback time remains below the block period, with documented margin |
| Memory | Target linker map, actual structure sizes, stack/heap use and DMA buffers fit the verified board |
| Latency | Analog input-to-output measurement, with sample rate and block size recorded |
| Recovery | A Blackbox-specific restore procedure and a matching backup are demonstrated before experimental flash writes |

The suggested latency target is at most 5 ms for the first playable prototype; it is a project target, not a known Blackbox capability. Target a substantial CPU margin, initially 25% or more, then revise from worst-case measurements.

## Later scope

Compatible model import, preset selection, cabinet IRs where required, bypass behavior, MIDI control, a replacement screen UI and additional effects. Each feature spends CPU, RAM or flash and must be budgeted.

Do not promise support for every `.nam` capture, every NAM architecture, A2-Full, or every Blackbox board revision. A model can fit its file format and still exceed the device's processing budget.

## Current unknowns

Exact processor variant and clock; physical flash and usable RAM; peripheral pinout; ADC/DAC routing and gain; normal and recovery USB descriptors; update packaging and integrity checks; Blackbox-specific restore capability; PI32v2 NAM performance. The [roadmap](08-development-roadmap.md) turns these into measurable tasks.
