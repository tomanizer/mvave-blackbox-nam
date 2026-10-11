# Claims and corrections

This register preserves research discussed before the repository existed. AI-generated statements are research leads, not independent evidence. Source IDs resolve in [SOURCES.md](../resources/SOURCES.md).

**Observed** means directly inspected in an artifact. **Upstream** means reported in primary project/vendor material. **Hypothesis** requires Blackbox measurements. **Corrected** means the earlier wording is inaccurate or exceeds its source.

| Claim | Status | Finding and next action |
| --- | --- | --- |
| FCC internal photographs exist for `2ARCP-BLACK-BOX` | Observed | Five-page exhibit 7467092 was retrieved and its SHA-256 matches the catalog. The 2025 `2ARCP-BLACKBOX` filing also lists exhibit 8052662. [S01-S03] |
| The Blackbox is definitely the identical AC791N chip as the FM-1 | Hypothesis, qualified | JieLi branding is visible and the V20 package contains `AC791N_STORY`. This supports a platform lead, not an exact silicon/package match. Read the physical marking and query supported identification interfaces. [S03, S05] |
| The board is `PD40 V04` | Observed | Visible in the 2024 FCC board photograph. This identifies that photographed revision, not every retail unit. [S03] |
| Display uses ST7789 | Observed label / hypothesis for exact controller | The module is labelled `1.54TFT-SPI-ST7789`. Verify controller variant, offsets, orientation and initialization on the actual board. [S03, S25] |
| The logic IC is a 74HC595D | Observed | Its marking is readable. Its actual connections remain unmapped. [S03] |
| 74HC595 reads extra buttons | Corrected | It is a serial-input output shift register with storage latches. It does not directly sample buttons; it could drive LEDs or matrix selection lines. [S24] |
| An external I2S codec must be initialized | Hypothesis | The AC791N SDK supports integrated audio and external interfaces. The Blackbox's actual conversion path is unverified. [S18-S20] |
| AC791N always has four ADC and four DAC channels | Corrected | Series-level SDK features and package-specific datasheets differ. The AC7913A6 sheet lists three audio ADC and two DAC channels. Exact Blackbox resources require the correct variant and board routing. [S26] |
| Named TL072 or RC4558 op-amps are fitted | Unverified | These were examples, not component identifications. Do not add them to the BOM without legible markings. |
| Stock FM-1 definitely uses LVGL | Corrected | The inspected architecture document describes JieLi `ui_core`; it identifies an msfa/Dexed-derived sound engine. It does not establish LVGL. [S13] |
| Only 26% of firmware needs reversing | Unverified | Function counts, code bytes and reverse-engineering effort are different quantities. No checked basis establishes this percentage for the Blackbox. |
| Felucca is hosted at `keremimo/melodee` | Corrected | Felucca is `hugelton/Felucca`, by Leo Kuroshita / Hügelton Instruments. Melodee is a separate related project. [S14, S36] |
| PI32v2 has ARM extensions and accepts ARM machine code | Corrected | Use the JieLi PI32v2 toolchain. The ARM assembly in the candidate NAM runtime is target-specific and cannot be assumed to run on JieLi. [S15-S16, S31] |
| Ghidra support is complete | Corrected | A processor module exists, but its own README describes PI32v2 support as very early. Cross-check critical instructions with vendor objdump output. [S16] |
| Pull a flash data line to ground to make the Blackbox unbrickable | Unverified | No Blackbox-specific evidence confirms this. Do not publish it as an operating procedure or short unidentified pins. |
| Standard ST-Link/SWD is the appropriate Blackbox debugger | Unverified | This was an ARM-based guess. Debug interface and supported equipment need identification. |
| Any custom crash inevitably hard-bricks the unit | Corrected | An application failure is not proof that ROM or another recovery path is inaccessible. Conversely, a ROM recovery path is not established on this Blackbox. |
| Synth audio is allowed to miss its block deadlines | Corrected | Synthesizers and effects both require timely buffer delivery. The pedal adds an input path and a round-trip latency requirement; neither system tolerates arbitrary deadline misses. |
| Tone3000 models all run on the candidate engine | Corrected | Start with the exact supported A2-Lite configuration; validate architecture and sample rate. Serialization conversion does not shrink a network into another architecture. [S08-S10] |
| Blackbox V20 is the current official download | Upstream / retrieved | The vendor page and release note list V20, 2026-01-31, adding AM4 support. This describes the public download checked on 2026-10-11. [S04-S06] |
| The cited Highleap article proves the Blackbox hardware BOM | Rejected | It is generic PCB reverse-engineering content. It supplies no M-Vave-specific board or component identification. [S35] |

The broader FM-1 ecosystem is useful precedent. It does not establish a working Blackbox NAM implementation. No supported Blackbox custom firmware or successful NAM port was verified in this research pass; this is not a claim that no unpublished work exists.
