# OBC Bugyo Cloud client

OBC 奉行クラウド Pythonクライアント

# Testing

```console
poetry run pytest
```

# API

## 打刻

* URL: https://hromssp.obc.jp/{{テナント？}}/{{？？}}/TimeClock/InsertReadDateTime/
* METHOD: POST
* Headers:
  * __RequestVerificationToken: 内容未確認
  * Content-Type: application/x-www-form-urlencoded; charset=UTF-8
* Content:
  * "ClockType" : 打刻種類
  * "LaborSystemID" : "0"
  * "LaborSystemCode" : ""
  * "LaborSystemName" : ""
  * "PositionLatitude" : 緯度
  * "PositionLongtitude" : 経度
  * "PositionAccuracy" : "0"

### 打刻種類

* "ClockIn" : 出勤
* "ClockOut" : 退出


```console
poetry run pytest
```
