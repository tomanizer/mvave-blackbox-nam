# Source catalog

Baseline: **2026-10-11**. Source IDs are stable within this baseline. Status describes what was actually checked, not whether every claim in a source is true.

Repository revisions are recorded separately in [upstream-revisions.json](../research/upstream-revisions.json). File fingerprints and download filenames are in [sources.json](sources.json).

## Primary and directly checked sources

| ID | Source | Status | Use and qualification |
| --- | --- | --- | --- |
| S01 | [FCC 2024 internal-photo catalog, exhibit 7467092](https://fccid.io/2ARCP-BLACKBOX/Internal-Photos/Internal-photos-7467092) | metadata-verified | FCC ID 2ARCP-BLACK-BOX; applicant Sinco Intelligent Technology Co., Ltd.; original filing 2024-07-11. |
| S02 | [FCC 2025 internal-photo catalog, exhibit 8052662](https://fccid.io/2ARCP-BLACKBOX/Internal-Photos/Internal-Photo-8052662) | metadata-verified | FCC ID 2ARCP-BLACKBOX, 2025-02-17. PDF not retrieved or compared locally. |
| S03 | [FCC 2024 internal-photo PDF](https://fccid.io/2ARCP-BLACK-BOX/Internal-Photos/Internal-photos-7467092.pdf) | retrieved-and-inspected | Five pages; hash verified locally. Limited excerpts accompany analysis; complete PDF not republished. |
| S04 | [M-Vave official downloads](https://www.m-vave.com/download) | verified | Lists ANNBLACKBOX V20 dated 2026-01-31. Also lists ANN format conversion software; conversion does not establish native NAM. |
| S05 | [Official BlackBox.fwsc update](https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/firmware/BlackBox.fwsc) | retrieved-and-scanned | Mutable vendor URL. Record applies to bytes retrieved on 2026-10-11; update is not a full device backup. |
| S06 | [Official Blackbox release note](https://yms-file-store.oss-cn-hongkong.aliyuncs.com/software/releaseNote/firmware/BlackBox.txt) | retrieved-and-inspected | GB18030 text; V20 adds AM4 support. Earlier entries describe MIDI, latency and format changes. |
| S07 | [Sinco ANN white paper](https://yms-file-store.oss-cn-hongkong.aliyuncs.com/manual/white-paper/ANN.pdf) | retrieved-and-inspected | Vendor explanation of proprietary ANN; not executable model-format or inference implementation documentation. |
| S08 | [TONE3000 embedded A2 runtime](https://github.com/tone-3000/embedded) | verified | MIT runtime candidate; ARM-specific optimized kernels and portable C paths. Not a demonstrated Blackbox port. |
| S09 | [TONE3000 nam-binary-loader](https://github.com/tone-3000/nam-binary-loader) | verified | MIT binary serialization and desktop conversion tools; serialization does not make all models compatible with a fixed-shape engine. |
| S10 | [NeuralAmpModelerCore](https://github.com/sdatkinson/NeuralAmpModelerCore) | verified | MIT C++ reference inference library; use as numerical reference. |
| S11 | [TONE3000 A2 guide](https://www.tone3000.com/guides/nam-a2-the-complete-guide) | verified | Architecture/model-selection context; check downloaded model configuration rather than relying on a title. |
| S12 | [M-Vave FM-1 community resource hub](https://github.com/aroum/fm1-custom-fw) | verified | FM-1 ecosystem and tooling directory. Linked project existence is not proof of Blackbox compatibility. |
| S13 | [FM-1 firmware architecture research](https://github.com/AL-255/FM-1-RE/blob/main/docs/architecture.md) | verified | FM-1 V13 architecture: AC791N/WL82, msfa-derived sound engine and JieLi ui_core; not a Blackbox map. |
| S14 | [Felucca firmware](https://github.com/hugelton/Felucca) | verified | Leo Kuroshita / Hügelton Instruments FM-1 firmware. GPL project with separately licensed packaged assets. |
| S15 | [Felucca build guide](https://github.com/hugelton/Felucca/blob/main/BUILDING.md) | verified | Vendor PI32v2 compiler and Gitee AC79 SDK; FM-1-specific build/install instructions. |
| S16 | [Ghidra JieLi processor module](https://github.com/kagaimiq/ghidra-jieli) | verified | README calls PI32v2 support very early; cross-check unsupported instruction handling. |
| S17 | [JieLi miscellaneous tools](https://github.com/kagaimiq/jl-misctools) | verified | Container tooling candidate. Exact Blackbox variant has not been unpacked in this baseline. |
| S18 | [Official JieLi AC79 AIoT SDK](https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK) | verified | Official Gitee source, WL82 target and package-specific resources; not a Blackbox BSP. |
| S19 | [Official JieLi AC79 documentation](https://doc.zh-jieli.com/AC79/zh-cn/master/index.html) | verified | Vendor SDK documentation entry point. |
| S20 | [AC79 SDK GitHub mirror](https://github.com/jeffreywugz/fw-AC79_AIoT_SDK) | verified | Third-party mirror, release/AC79NN_SDK_V1.0.3; candidate datasheets checked. Not official GitHub hosting. |
| S21 | [JieLi fw-Bootloader](https://github.com/Jieli-Tech/fw-Bootloader) | verified | Vendor bootloader source; target applicability requires separate verification. |
| S22 | [FM-1 Transporter](https://github.com/kurogedelic/FM-1-transporter) | verified | FM-1 ROM entry, flash and RAM-execution research. Blackbox compatibility untested. |
| S23 | [M-Vave Blackbox web editor](https://github.com/jvsobrinho/mvave-blackbox-edit) | verified | MIT Web Bluetooth editor for stock Blackbox; protocol source, not replacement audio firmware. |
| S24 | [Nexperia 74HC/HCT595 datasheet](https://assets.nexperia.com/documents/data-sheet/74HC_HCT595.pdf) | retrieved-and-inspected | Reference for 74HC595 family; actual device manufacturer/electrical specification still needs identification. |
| S25 | [Sitronix ST7789V datasheet hosted by Newhaven](https://newhavendisplay.com/content/datasheets/ST7789V.pdf) | retrieved-and-inspected | ST7789-family reference. Document has reproduction restrictions; link only in public repository. |
| S26 | [JieLi AC7913A6 datasheet, SDK mirror](https://raw.githubusercontent.com/jeffreywugz/fw-AC79_AIoT_SDK/release/AC79NN_SDK_V1.0.3/doc/datasheet/AC791N%E8%A7%84%E6%A0%BC%E4%B9%A6/datasheet/AC7913A6_Datasheet_V1.0.pdf) | retrieved-and-inspected | Candidate variant, not identified as the exact Blackbox chip. Explicit reproduction restrictions; public package links only. |
| S27 | [JieLi AC7911B datasheet, SDK mirror](https://raw.githubusercontent.com/jeffreywugz/fw-AC79_AIoT_SDK/release/AC79NN_SDK_V1.0.3/doc/datasheet/AC791N%E8%A7%84%E6%A0%BC%E4%B9%A6/datasheet/AC7911B_Datasheet_V1.1.pdf) | retrieved-and-inspected | Candidate variant, not identified as the exact Blackbox chip. Explicit reproduction restrictions; public package links only. |
| S28 | [JieLi AC7916A datasheet, SDK mirror](https://raw.githubusercontent.com/jeffreywugz/fw-AC79_AIoT_SDK/release/AC79NN_SDK_V1.0.3/doc/datasheet/AC791N%E8%A7%84%E6%A0%BC%E4%B9%A6/datasheet/AC7916A_Datasheet_V1.0.pdf) | retrieved-and-inspected | Candidate variant, not identified as the exact Blackbox chip. Explicit reproduction restrictions; public package links only. |
| S29 | [TONE3000 API integration guide](https://github.com/tone-3000/api) | located | Later editor integration lead; not required for first standalone model. |
| S30 | [TONE3000 model catalog](https://www.tone3000.com) | located | User-selected model source; no individual capture downloaded in this baseline. |
| S31 | [FM-1 PI32v2 toolchain setup script](https://github.com/AL-255/FM-1-RE/blob/main/scripts/setup_toolchain.sh) | located | Pin and inspect script before running; vendor compiler is distinct from generic ARM tools. |
| S32 | [FCC 2025 internal-photo PDF mirror](https://device.report/m/92b7148405d54baa367da5aa8d161a635d4235d3af740ef9c113a30f3403d919.pdf) | metadata-verified | Hash/size are catalog values; bytes not retrieved locally. |
| S33 | [FCC 2024 internal-photo PDF alternative mirror](https://device.report/m/f1779277680549124da59de20a534594ee7559f49b43a94aea681a97cba66386.pdf) | metadata-verified | Same exhibit hash as S03. Direct retrieval from this host was blocked; S03 was retrieved successfully. |
| S34 | [FCC Blackbox user manual](https://fcc.report/FCC-ID/2ARCP-BLACK-BOX/7467094.pdf) | located | Official product manual exhibit; direct retrieval was blocked in this pass. |
| S35 | [Highleap Black Box PCB Reverse Engineering](https://hilelectronic.com/black-box-pcb-reverse-engineering/) | rejected-as-device-evidence | Generic reverse-engineering services article, not an M-Vave teardown. Preserved to explain the correction. |
| S36 | [Melodee](https://github.com/keremimo/melodee) | listed-in-verified-hub | Felucca-related FM-1 project; not Felucca canonical hosting. |
| S37 | [SLOOP FM-1](https://github.com/isod89/sloop-fm1) | listed-in-verified-hub | FM-1 groovebox reference; no Blackbox applicability established. |
| S38 | [X0X FM-1](https://github.com/charlesvestal/fm1-x0x) | listed-in-verified-hub | FM-1 synth/groovebox reference. |
| S39 | [Groove OS](https://www.groove-os.com/) | listed-in-verified-hub | FM-1 product lead, not a Blackbox runtime. |
| S60 | [Independent Blackbox V20 research](https://github.com/jakino0/mvave-blackbox-reverse-engineering) | upstream-report | Read-only V20 application mapping, USB audio and OTA analysis; compare independently with the local official update. Pinned revision and qualifications in [offline baseline](../docs/10-offline-baseline.md). |
| S61 | [TONE3000 nam-pedal A2 conversion issue](https://github.com/tone-3000/nam-pedal/issues/9) | upstream-issue | A reported mismatch between current A2 `SlimmableContainer` downloads and an older converter; test the exact model and toolchain. |

## Earlier citations retained for follow-up

These links preserve the earlier research trail. They have not been used to establish hardware facts or a working recovery method.

| ID | Earlier citation | Qualification |
| --- | --- | --- |
| S40 | [Hacker News FM-1 discussion](https://news.ycombinator.com/item?id=49994065) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S41 | [Reddit FM-1VA discussion](https://www.reddit.com/r/synthesizers/comments/1wraimy/fm1va_for_the_mvave_fm1_is_live/) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S42 | [Synth Anatomy X0X coverage](https://synthanatomy.com/2026/10/charles-vestal-x0x-custom-firmware-turns-the-m-vave-fm-1-into-a-rebirth-like-groovebox.html) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S43 | [Synth Anatomy Groove OS coverage](https://synthanatomy.com/2026/10/groove-os-turns-the-m-vave-fm-1-into-an-8-track-groovebox.html) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S44 | [Reddit Blackbox protocol discussion](https://www.reddit.com/r/guitarpedals/comments/1whg0ek/reverseengineering_the_mvave_blackbox_full/) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S45 | [Reddit Blackbox best-practice discussion](https://www.reddit.com/r/guitarpedals/comments/1f4v8g1/mvave_blackbox_best_practice_hints/) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S46 | [Quarkslab firmware reverse-engineering article](https://blog.quarkslab.com/nerd-life-weeks-firmware-teardown-we-were-right.html) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S47 | [ElectronicCats JieLi SDK build notes](https://github.com/ElectronicCats/jieli-ble-badge-research/blob/main/docs/jieli-sdk-build.md) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S48 | [ElectronicCats JieLi flash-dump notes](https://github.com/ElectronicCats/jieli-ble-badge-research/blob/main/docs/dump-firmware.md) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S49 | [Older JieLi AC690X recovery issue](https://github.com/christian-kramer/JieLi-AC690X-Familiarization/issues/11) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. AC690X is a different chip family. |
| S50 | [Electrodragon JieLi component notes](https://w2.electrodragon.com/Chip-cn-dat/jieli-dat/jieli-dat.md) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S51 | [Cuvave ANN Blackbox product page](http://www.cuvave.com/product?id=annblack-box) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S52 | [M-Vave video previously cited for teardown](https://www.youtube.com/watch?v=ZfxioIpo3TM) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S53 | [M-Vave video previously cited for teardown](https://www.youtube.com/watch?v=Czc9MuiVjwE) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S54 | [Video previously cited for firmware extraction](https://www.youtube.com/watch?v=0qvot1ttonU) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S55 | [Video previously cited for display/control research](https://www.youtube.com/watch?v=YPALS8W4XNY&t=205) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S56 | [Video previously cited for alternate firmware](https://www.youtube.com/watch?v=V5xKD7XsGoI) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S57 | [M-Vave Blackbox panel video](https://www.facebook.com/mvaveofficialis/videos/m-vave-blackbox-panel-introductionblackbox-function-introduction-sampling-rate-4/1375920873796244/) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S58 | [Gearnews custom-firmware article](https://www.gearnews.com/custom-firmware-is-booming-synths/) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. |
| S59 | [1010music Blackbox mod article](https://synthanatomy.com/2026/10/justin-joe-blackbox-mod-custom-firmware.html) | Preserved from earlier discussion; content/claim not independently verified in this baseline. Do not use as primary Blackbox evidence. This names the 1010music sampler, a different product. |

## Access and missing-source notes

- The official JieLi SDK is on Gitee. The previously suggested official GitHub SDK URL returned 404.
- Some FCC mirror and official attachment requests returned 403. The 2024 S03 PDF was successfully retrieved from its public catalog PDF path, and its hash matches the filing catalog.
- The later FCC photo exhibit was located but not compared. Do not assume it documents the same retail board revision.
- No public complete Blackbox schematic, BOM or demonstrated Blackbox NAM firmware was established by these sources.
- The `jieli-linux-toolchains` name in earlier discussion was not resolved to a verified canonical repository; use the pinned FM-1/Felucca setup references until one is verified.
