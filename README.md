# EmergencyBot

## Introduction

이 봇은 최근 Team Circle을 비롯한 서버에서 토큰 등으로 피해를 받고 있어 피해를 막고자 긴급히 제작된 알트 계정을 밴할 수 있는 봇입니다.

## 사용법
### 0. Python 설치
컴퓨터에 먼저 `Python3.8`을 설치해 주세요.

### 1. 모듈 설치
```sh
python3 -m pip install -r requirements.txt
```
로 모듈을 설치해 주세요.

### 2. TOKEN과 로그 채널, 봇 관리자 지정
`config.py`에 `TOKEN`에 Discord TOKEN, `owner_ids`에 관리자의 아이디를, `WEBHOOK`에 로그할 채널의 웹후크를 입력해 주세요.<br>
* 매 유저가 들어올 때 마다 로그되는 채널의 Topic(채널 주제)에 `-AltLog`을 입력해 주세요.

* 웹훅은 봇의 작동만 로그하고, 실제 유저 정보를 로그하는 것은 아래 채널에 로그됩니다.<br>
  * 매 유저가 들어올 때 로그 되는 채널: `-AltLog`이 있는 채널<br>
  * `!alts` 명령어가 실행될 때 로그 되는 채널: 해당 명령어가 실행된 채널<br>

* 관리자 아이디는 아래와 같이 배열 형태로 넣어주세요.
* `[902700864748273704, 734332844037505064]`

### 3. 봇 초대
해당 토큰의 봇을 초대해 주세요.

### 4. 작동
```sh
python3 bot.py
```
을 입력하여 봇을 작동 시켜주세요.

### 4. 사용
봇이 가동되면 매 유저가 들어올 때 마다 자동으로 해당 유저의 가입일을 확인하고 30일 미만이면 자동 차단됩니다.<br>
기존 유저도 확인하고 싶을 경우, `!alts` 를 입력하면 해당 채널에 자동적으로 작동이 로그되며,<br>
모든 유저에 대하여 위와 동일하게 작동됩니다.

## 문의
[SSKATE](https://discord.com/users/902700864748273704) ([me@sskate.me](mailto:me@sskate.me), [kms0219kms@kakao.com](mailto:kms0219kms@kakao.com))
