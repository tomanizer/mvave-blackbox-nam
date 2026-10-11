# Datasheet index

All entries checked or located on **2026-10-11**. The processor part is not yet identified precisely. Candidate datasheets must not be substituted for a verified Blackbox pinout.

| Component / candidate | Document | Applicability and status |
| --- | --- | --- |
| 74HC595D logic IC | [Nexperia 74HC/HCT595 PDF](https://assets.nexperia.com/documents/data-sheet/74HC_HCT595.pdf) [S24] | Retrieved. Describes serial-input output register and latches; check actual manufacturer/package before relying on electrical limits |
| ST7789 display family | [Sitronix ST7789V PDF hosted by Newhaven](https://newhavendisplay.com/content/datasheets/ST7789V.pdf) [S25] | Retrieved. Module label supports family; V variant is a reference until confirmed |
| AC7913A6 candidate | [JieLi PDF in public SDK mirror](https://raw.githubusercontent.com/jeffreywugz/fw-AC79_AIoT_SDK/release/AC79NN_SDK_V1.0.3/doc/datasheet/AC791N%E8%A7%84%E6%A0%BC%E4%B9%A6/datasheet/AC7913A6_Datasheet_V1.0.pdf) [S26] | Retrieved. Example package-specific resource limits; not identified as Blackbox's exact part |
| AC7911B candidate | [JieLi PDF in public SDK mirror](https://raw.githubusercontent.com/jeffreywugz/fw-AC79_AIoT_SDK/release/AC79NN_SDK_V1.0.3/doc/datasheet/AC791N%E8%A7%84%E6%A0%BC%E4%B9%A6/datasheet/AC7911B_Datasheet_V1.1.pdf) [S27] | Retrieved; candidate reference |
| AC7916A candidate | [JieLi PDF in public SDK mirror](https://raw.githubusercontent.com/jeffreywugz/fw-AC79_AIoT_SDK/release/AC79NN_SDK_V1.0.3/doc/datasheet/AC791N%E8%A7%84%E6%A0%BC%E4%B9%A6/datasheet/AC7916A_Datasheet_V1.0.pdf) [S28] | Retrieved; candidate reference |
| AC791N / WL82 SDK | [Official Gitee SDK](https://gitee.com/Jieli-Tech/fw-AC79_AIoT_SDK) [S18], [official documentation](https://doc.zh-jieli.com/AC79/zh-cn/master/index.html) [S19] | SDK platform/register context; not a Blackbox board schematic |

Hashes and download filenames are in [sources.json](../sources.json). The local downloader can retrieve selected PDFs for personal engineering inspection, for example:

```sh
python3 tools/fetch_sources.py --id S24 --id S25 --output research/downloads
```

JieLi and Sitronix sheets contain explicit restrictions on reproduction. Accordingly the public repository indexes them rather than copying their PDFs. Preserve vendor notices and obtain appropriate permission before republishing. A public mirror's root software license does not override a document's own notice.

The complete Blackbox schematic and BOM have not been found. The FCC catalogs list schematic/block-diagram metadata, but do not provide those confidential exhibits as public downloadable documents.
