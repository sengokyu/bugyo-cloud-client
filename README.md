# OBC Bugyo Cloud client

OBC 奉行クラウド Pythonクライアント

# Usage

BugyoCloudClientのインスタンスを作成します。

```python
import bugyocloudclient as bcc


tenant_code = 'The first part of URL path.'
client = bcc.BugyoCloudClient(tenant_code)
```

最初にLoginTaskを実行して、ログイン状態にします。

```python
auth_info = bcc.AuthInfo('login id', 'password')
login_task = bcc.LoginTask(auth_info)
client.exec(login_task)
```

ログインしてから、別のタスクを実行します。
（今は打刻タスクしかありません）。

```python
punch_info = bcc.PunchInfo()
punch_info.clock_type = clock_type
punch_task = bcc.PunchTask(punch_info)
client.exec(punch_task)
```


# Installing poetry

```console
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
```

Changing python command name from 'python' to 'python3'.

```console
vi ~/.poetry/bin/poetry
```


# Creating environment

```console
poetry install
```


# Testing

```console
poetry run pytest
```

# Build & Publish

```console
poetry buid
poetry publish -r testpypi
poetry publish
```


# 画面あるいはAPI

## 認証画面

* URL: https://id.obc.jp/{{テナント?}}/
* METHOD: GET
* Response:
  * Headers:
    * Content-Type: text/html; charset=utf-8


## 認証方法チェック

* URL: https://id.obc.jp/{{テナント?}}/login/CheckAuthenticationMethod
* METHOD: POST
* Headers:
  * __RequestVerificationToken: 認証画面のフォームにあるhidden value
  * Content-Type: application/x-www-form-urlencoded; charset=UTF-8
  * X-Requested-With: XMLHttpRequest
* Content:
  * "OBCiD" : ログインID
  * "isBugyoCloud" : "false"
* Response:
  * Headers:
    * Content-Type: application/json; charset=utf-8
  * Content:
    * AuthenticationMethod
    * SAMLButtonText
    * PasswordButtonText


## 認証

* URL: https://id.obc.jp/{{テナント?}}/login/login/?Length=5
* METHOD: POST
* Headers:
  * Content-Type: application/x-www-form-urlencoded; charset=UTF-8
* Content:
  * "btnLogin" : ""
  * "OBCID" : ログインID
  * "Password_d1" : ""
  * "Password_d2" : ""
  * "Password_d3" : ""
  * "Password" : パスワード
  * "__RequestVerificationToken" : 認証画面のフォームにあるinput hidden value
  * "X-Requested-With" : "XMLHttpRequest"
* Response:
  * Headers:
    * Content-Type: application/json; charset=utf-8
  * Content:
    * RedirectURL
    * LoginOBCiD


レスポンスにあるRedirectURLをGETすると302が返ります。
302に従うと、ユーザ初期画面へ遷移します。URLは、https://hromssp.obc.jp/{{テナント？}}/{{ユニーク文字列？}}/ のようになります。

## ユーザ初期画面

* URL: https://hromssp.obc.jp/{{テナント？}}/{{ユニーク文字列？}}/
* METHOD: GET

認証後の302応答に従うとたどり着きます。

ユニーク文字列の部分を、このあとの処理で使います。


## 打刻画面

* URL: https://hromssp.obc.jp/{{テナント？}}/{{ユーザ初期画面URLより}}/timeclock/punchmark/
* METHOD: GET
* Response:
  * Headers:
    * Content-Type: text/html; charset=utf-8



## 打刻

* URL: https://hromssp.obc.jp/{{テナント？}}/{{ユーザ初期画面URLより}}/TimeClock/InsertReadDateTime/
* METHOD: POST
* Headers:
  * __RequestVerificationToken: 打刻画面にあるinput hidden value
  * Content-Type: application/x-www-form-urlencoded; charset=UTF-8
* Content:
  * "ClockType" : 打刻種類
  * "LaborSystemID" : "0"
  * "LaborSystemCode" : ""
  * "LaborSystemName" : ""
  * "PositionLatitude" : 緯度
  * "PositionLongitude" : 経度
  * "PositionAccuracy" : "0"

### 打刻種類

* "ClockIn" : 出勤
* "ClockOut" : 退出

