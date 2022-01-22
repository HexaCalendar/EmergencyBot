# EmergencyBot

## Introduction

이 봇은 최근 Team Circle을 비롯한 서버에서 토큰 등으로 피해를 받고 있어 피해를 막고자 긴급히 제작된 알트 계정을 밴할 수 있는 봇입니다.

## 사용법
### 0. Python 설치
컴퓨터에 먼저 Python3.8을 설치해 주세요.

### 1. TOKEN과 로그 채널 지정
config.py에 TOKEN에 Discord TOKEN, WEBHOOK에 로그할 채널의 웹후크를 입력해 주세요.<br>
* 봇의 작동만 로그하고, 실제 유저 정보를 로그하는 것은 해당 명령어를 실행한 채널에 로그됩니다.

### 2. 봇 초대
해당 토큰의 봇을 초대해 주세요.

### 3. 작동
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
