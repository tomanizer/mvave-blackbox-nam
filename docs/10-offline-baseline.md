# Offline baseline: V20 and NAM reference

Checked 2026-10-11. This is a read-only host investigation; no pedal was connected and no Blackbox code was built.

## V20 comparison

The locally downloaded official `BlackBox.fwsc` is 700,436 bytes and has SHA-256 `c0fef191b860d3b20f77fc492a24986eef2d12df44bb5e38355684820e26cb08` (S05). The marker `AC791N_STORY` is at file offset 1,060. These are independently reproduced observations of the **outer update file**.

[jakino0/mvave-blackbox-reverse-engineering](https://github.com/jakino0/mvave-blackbox-reverse-engineering), revision `20d6d77a122474e2d6160c0a48586a9128148b77`, publishes a much more detailed, read-only V20 analysis. It reports an outer flash payload starting at FWSC offset `0x414`, length `0xA5000`; an application image of 655,712 bytes with SHA-256 `0c62e3f1805be684e087e017ac80a2c1836790034bb50483829ec7db99917fce`; and application-to-runtime mapping `runtime = app_offset + 0x02000120`. The outer range fits inside the official file, but this project has **not yet independently decrypted and hashed the application**. Do not equate that application hash with the outer FWSC hash. See the upstream [address map](https://github.com/jakino0/mvave-blackbox-reverse-engineering/blob/20d6d77a122474e2d6160c0a48586a9128148b77/docs/address-map-v20.md) and [manifest](https://github.com/jakino0/mvave-blackbox-reverse-engineering/blob/20d6d77a122474e2d6160c0a48586a9128148b77/analysis/v20/generated/manifest.json).

The same project's [USB Audio analysis](https://github.com/jakino0/mvave-blackbox-reverse-engineering/blob/20d6d77a122474e2d6160c0a48586a9128148b77/docs/usb-audio.md) reports two-channel, 24-bit, 44.1 kHz USB descriptors. This does not establish the analog guitar path's sample rate or buffer size. Its [MaskROM-entry analysis](https://github.com/jakino0/mvave-blackbox-reverse-engineering/blob/20d6d77a122474e2d6160c0a48586a9128148b77/docs/research/maskrom-entry-v20.md) reports an unreferenced boot-marker writer and a separate stock OTA route. Static absence of a stock call path does not rule out a physical recovery route. Neither report has been reproduced from the decrypted bytes here.

**Next reproducible step:** use a pinned read-only FWSC unpack/decrypt implementation on the local official update, compare the application size and SHA-256 above, and run upstream's `tools/blackbox_inspect.py` on that extracted application. Keep decrypted bytes and disassembly local. Then compare only independently matched V20 revisions; don't duplicate the existing address map without a new question.

## Host NAM reference

Cloned [TONE3000 embedded](https://github.com/tone-3000/embedded) at `b84b60c652cb386ea341be50b8c665ae8a489cff`. From its `example/` directory, `make check-all` completed with exit code 0 on this x86-64 Linux host. The checked-in A2-Lite example capture (`weights/a2lite.namb`, 7,980 bytes, SHA-256 `0fa82c41815f7553b6f02820b12827a3a09ac22101e090ba82cc55aa191baa1d`) and 96,000-frame golden input passed against the bundled NeuralAmpModelerCore reference. The reported A2-Lite maximum absolute error was `2.38e-07` and ESR approximately `-134.9 dB`, including block sizes 1, 16, 32, 48, 64 and varying block boundaries. The full check also exercised upstream's A2-Full example, but the first proposed pedal model remains A2-Lite. The [upstream NOTICE](https://github.com/tone-3000/embedded/blob/b84b60c652cb386ea341be50b8c665ae8a489cff/NOTICE) attributes its example captures and golden outputs to NeuralAmpModelerCore tests. This repository does not copy those assets.

This establishes a working **host** reference for the upstream example, not a TONE3000 catalog capture, PI32v2 binary, target numerical result, or real-time timing result. The runtime assumes 48 kHz for these test vectors. Reconcile that assumption with the Blackbox's measured internal path before interpreting port results. A reported [A2 `SlimmableContainer` conversion incompatibility](https://github.com/tone-3000/nam-pedal/issues/9) in a separate pinned `nam-pedal` toolchain means a current catalog download must be tested explicitly; a format conversion is not architecture reduction.

## Remaining gates

1. Match the decrypted application hash and independently inspect relevant V20 descriptors and audio initialization.
2. Confirm actual Blackbox board, SoC package, memory, audio rate and clocking from device-specific evidence.
3. Obtain a supported catalog capture with provenance and permission, or continue using upstream's example strictly as an engineering test vector.
4. Compile the portable C engine for PI32v2, compare output with this host reference, then measure target RAM, cycles and full audio-path latency.
5. Establish a Blackbox-specific backup and independent recovery path before any persistent write.
