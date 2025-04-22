---

# 디스코드 봇: 계정 생성일 기준 자동 강퇴

이 디스코드 봇은 서버에 새로 가입하는 멤버의 계정 생성일을 확인하고, 설정된 기준(기본값: 120일)보다 생성일이 짧은 계정을 자동으로 강퇴합니다.

## 기능

- **계정 생성일 자동 확인**: 새로 가입한 멤버의 계정 생성일을 확인합니다.
- **자동 강퇴**: 계정 생성일이 설정된 기준(기본값: 120일) 이하일 경우 멤버를 자동으로 강퇴합니다.
- **콘솔 로그 출력**: 강퇴 결과를 콘솔에 기록합니다.

---

## 설치 방법

### 1. Python 및 필수 라이브러리 설치
이 프로젝트는 Python 3.8 이상과 `discord.py` 라이브러리를 필요로 합니다.

- Python 설치: [Python 공식 사이트](https://www.python.org/)에서 다운로드하세요.
- 라이브러리 설치:
  ```bash
  pip install discord.py
  ```

### 2. 디스코드 봇 생성
1. [디스코드 개발자 포털](https://discord.com/developers/applications)에서 새로운 봇을 만듭니다.
2. **토큰**을 복사하여 안전한 곳에 저장하세요.
3. 봇을 서버에 초대하고 **Kick Members** 권한을 부여합니다.

### 3. 코드 다운로드 및 설정
1. 이 저장소를 클론하거나 ZIP 파일로 다운로드하세요:
   ```bash
   git clone https://github.com/USERNAME/REPOSITORY_NAME.git
   ```
2. 코드 파일을 열고 `YOUR_BOT_TOKEN` 부분에 디스코드 봇 토큰을 입력하세요.

---

## 코드

아래는 봇의 주요 코드입니다:

```python
import discord
from datetime import datetime, timezone

intents = discord.Intents.default()
intents.members = True  # 멤버 관련 이벤트 활성화
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    account_age = (datetime.now(timezone.utc) - member.created_at).days
    if account_age <= 120:  # 계정 생성일 기준 (120일)
        try:
            await member.kick(reason="계정 생성일 120일 이하")
            print(f"{member.name} 강퇴 완료")
        except discord.Forbidden:
            print("봇에게 강퇴 권한이 없습니다.")
        except discord.HTTPException as e:
            print(f"강퇴 실패: {e}")

client.run("YOUR_BOT_TOKEN")  # 봇 토큰 입력
```

---

## 사용 방법

1. 디스코드 서버에 봇을 초대하고 실행합니다.
2. 새로 가입한 멤버의 계정 생성일이 기준(120일)보다 짧으면 자동으로 강퇴됩니다.
3. 강퇴 결과는 콘솔에 출력됩니다.

---

## 추가 정보

- **계정 생성일 기준 변경**: 코드에서 `account_age <= 120` 부분을 수정하여 강퇴 기준을 변경할 수 있습니다.
- **필수 권한**: 봇이 제대로 작동하려면 서버에서 `Kick Members` 권한을 활성화해야 합니다.

---

## 기여

버그 제보나 기능 제안은 [Issues](https://github.com/USERNAME/REPOSITORY_NAME/issues) 탭을 통해 가능합니다. Pull Request도 환영합니다!

---

이 README 파일을 저장소에 추가하시면 GitHub에서 바로 사용할 수 있습니다! 다른 요청사항이 있다면 말씀해주세요. 😊
