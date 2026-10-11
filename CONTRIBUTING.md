# Contributing

Start with the [roadmap](docs/08-development-roadmap.md) and [claim register](docs/02-claims-and-corrections.md).

For hardware findings, record board revision, photograph location, readable marking, observation, source and confidence. For firmware findings, record the image hash, tool version, relevant offset/address and enough context to reproduce the conclusion. Say which device a finding applies to.

For NAM work, pin the model and runtime, validate numerical output against a reference and record actual target memory and timing. Do not call a host benchmark a Blackbox benchmark.

Add public references to `resources/sources.json` and keep `resources/SOURCES.md` consistent. Resolve uncertainty explicitly; preserve corrections instead of silently promoting earlier guesses.

Keep device-specific backups, radio identifiers, serial numbers, credentials, model-library tokens and private user files out of commits. Include a clear license for contributed photographs and code; retain third-party copyright notices.

A firmware contribution needs a Blackbox-specific backup and recovery record before anyone is asked to install it. Ordinary research documentation and offline tools do not need to wait for hardware access.
