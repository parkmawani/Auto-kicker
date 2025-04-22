import discord
from datetime import datetime, timezone

intents = discord.Intents.default()
intents.members = True  # 멤버 관련 이벤트 활성화
client = discord.Client(intents=intents)

@client.event
async def on_member_join(member):
    account_age = (datetime.now(timezone.utc) - member.created_at).days
    if account_age <= 120:
        try:
            await member.kick(reason="계정 생성일 120일 이하")
            print(f"{member.name} 강퇴 완료")
        except discord.Forbidden:
            print("봇에게 강퇴 권한이 없습니다.")
        except discord.HTTPException as e:
            print(f"강퇴 실패: {e}")

client.run("YOUR_BOT_TOKEN")  # 봇 토큰 입력
