# Hardware inventory

Evidence: 2024 FCC exhibit 7467092, checked 2026-10-11. This is a partial visual inventory, **not a complete bill of materials or schematic**. [Photo guide](../resources/photos/README.md); [machine-readable table](../research/components.csv).

| Item | Identification | Evidence | Confidence / missing information |
| --- | --- | --- | --- |
| Main board | `PD40 V04`, M-VAVE | FCC page 2, upper photo | High for photographed revision |
| Main SoC candidate | JieLi-branded square IC | FCC page 3, upper detail | High for branding; model marking insufficiently clear |
| Platform lead | AC791N / WL82 | `AC791N_STORY` in official update; vendor SDK target | Strong firmware-family lead; physical variant unconfirmed |
| Logic IC | `74HC595D` | FCC page 3, right of metal-can crystal | High for marking; GPIO connections and function unknown |
| Display board | `1.54TFT-SPI-ST7789`, `Ver:1.1` | FCC page 4, upper photo | High for module label; controller suffix and pixel geometry unverified |
| Display connection | Header carrying power and SPI-style signals | FCC pages 3-4 | Labels visible; Blackbox connector routing not mapped |
| Antenna | Red wire labelled BT/BLE antenna in exhibit | FCC page 3 | High for exhibit identification; preserve RF configuration during bring-up |
| Battery | Pouch battery, three-wire connector | FCC pages 4-5 | Battery chemistry/capacity and third-wire function require reliable label or measurements |
| Oscillator | Metal-can crystal beside main IC | FCC page 3 | Frequency not reliably identified |
| Input/output front end | Several small ICs around jack region | FCC pages 2-3 | Op-amp/codec identities and analog routing unresolved |
| Flash/storage | Not identified | No readable identification assigned | Capacity, voltage, physical location and protocol unknown |
| Controls | Two footswitches and rotary/button controls | FCC page 2 | Visible hardware; scan wiring and encoder behavior unresolved |
| USB/power | Connector region on board edge | FCC page 2 | Electrical routing, descriptors and recovery behavior unresolved |

## What the photographs do not show

A readable full processor marking, a complete trace map, component values, or proof of integrated versus external conversion. A small unrecognized IC cannot be labelled an op-amp, codec or flash device from package shape alone.

## Next measurements

1. Photograph both board faces and each IC at native resolution. Record board revision and orientation. Use a ruler for scale.
2. Read the full SoC and storage markings, then choose the matching datasheet. The [datasheet index](../resources/datasheets/README.md) contains candidate variants.
3. Trace unpowered continuity from the audio jacks through the analog front end and from the display/logic IC to the processor. Record uncertainty.
4. Capture normal USB descriptors and official-editor traffic without issuing writes. Identify normal update entry separately from independent recovery entry.
5. Measure power rails and confirm probe/programmer voltage compatibility before attaching equipment.

Do not treat GPIO names, peripheral addresses or flash sectors from the FM-1 as Blackbox measurements.
