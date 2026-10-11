# NAM feasibility and benchmark plan

Candidate: [TONE3000 embedded runtime, pinned revision](https://github.com/tone-3000/embedded/tree/b84b60c652cb386ea341be50b8c665ae8a489cff). Desktop reference: [NeuralAmpModelerCore](https://github.com/sdatkinson/NeuralAmpModelerCore). Format tools: [nam-binary-loader](https://github.com/tone-3000/nam-binary-loader).

## Supported model comes first

The candidate provides fixed-shape A2-Lite and A2-Full engines, runtime-loaded weights and a C binary reader. Its ARM-tuned paths have portable C alternatives. For the first PI32v2 attempt, select portable C explicitly and inspect compiler output. No ARM kernel has been ported here.

Start with a standalone, mono, 48 kHz A2-Lite model matching the upstream shape and weight count. The runtime header identifies 1,871 weights and a 6,347-sample prewarm. Arbitrary A1/LSTM/ConvNet, conditioned or larger A2 models are outside the first supported subset. If a download is a container of several model sizes, explicitly export/select the supported leaf before conversion. Reject unsupported configuration rather than guessing.

`.nam` is a model description plus weights; `.namb` is a binary serialization. `nam2namb` is a desktop format conversion, not a way to turn a larger model into A2-Lite. Retain the original model URL, creator, configuration, hash and permission information.

## Memory

Upstream reports roughly 7.3 KB for A2-Lite weights and 100 KB for state at maximum block 48; the state grows to roughly 109 KB at the default maximum block 64. These are upstream estimates, not Blackbox measurements. `sizeof` and a target linker map are authoritative because pointer sizes, alignment and block settings affect layouts.

Budget code, weights, histories, scratch, DMA buffers, stacks, SDK tasks, display buffers and model-transfer staging together. Reserve capacity for model loading or use a deliberate muted swap. `.namb` file-size reduction does not eliminate recurrent history buffers.

## Timing

For sample rate `fs` and block size `B`, the available callback period is `B / fs` seconds. At 48 kHz:

| Block samples | Period | Nominal cycles at 240 MHz | Nominal cycles at 320 MHz |
| --- | --- | --- | --- |
| 16 | 0.333 ms | 80,000 | 106,667 |
| 32 | 0.667 ms | 160,000 | 213,333 |
| 48 | 1.000 ms | 240,000 | 320,000 |
| 64 | 1.333 ms | 320,000 | 426,667 |

Clock columns are scenarios, **not verified Blackbox clocks**. Measure actual elapsed time with an identified timer or counter, including scheduling and conversion work. A Cortex-M7 benchmark cannot be transferred by scaling its clock to PI32v2: instructions, memory behavior and DSP scheduling differ.

Record engine-only and complete callback timings, distribution and maximum, underruns/overruns, cold/warm cache conditions and competing UI/USB work. A finite endurance run provides evidence, not a proof of all possible worst cases. Do not sum two core frequencies as if they doubled a serial network's budget.

## Numerical and listening checks

Use the same model and mono input for the port and a pinned NAM reference. Report maximum absolute error and energy-normalized error. Include silence, decays, impulses, sine sweeps and recorded guitar at several levels. Test state across changing block boundaries, reset/prewarm, and long runs. Choose the tolerance before judging an optimized build; fused operations and fast-math can change results.

The 6,347-sample prewarm is startup work; the receptive field is model history, not automatically 132 ms of streaming delay. Mute while loading/resetting/prewarming. Measure actual analog round-trip latency independently of the block period.

For an amp-only capture, a cabinet IR may be required for the desired monitored tone. A full-rig capture may already include that response. The first experiment must identify which one is used.

## Decision

Proceed to live NAM audio only after numerical agreement, target memory fit and measured timing margin. If the portable path misses the budget, profile kernels and data placement before adding effects or increasing model size. No feasible Blackbox NAM configuration has yet been demonstrated.
