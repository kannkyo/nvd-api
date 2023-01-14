# CVE APIの制約事項

| 項目              | 制約                      |
| ----------------- | ------------------------- |
| cvssV2Metrics     | cvssV3Metrics と併用不可  |
| cvssV2Severity    | cvssV2Severity と併用不可 |
| cvssV3Metrics     | cvssV2Metrics と併用不可  |
| cvssV3Severity    | cvssV3Severity と併用不可 |
| isVulnerable      | cpeName 必須              |
| keywordExactMatch | keywordSearch 必須        |
| lastModStartDate  | lastModEndDate 必須       |
| lastModEndDate    | lastModStartDate 必須     |
| pubStartDate      | pubEndDate 必須           |
| pubEndDate        | pubStartDate 必須         |
| versionEnd        | versionEndType 必須       |
| versionEndType    | versionEnd 必須           |
| versionStart      | versionStartType 必須     |
| versionStartType  | versionStart 必須         |
