import discord
import json
import os
import aiohttp
from discord.ext import commands
import asyncio
import time
import datetime

print(r"""
  __  __           _        _             _____             _ _ 
 |  \/  |         | |      | |           |  __ \           (_|_)
 | \  / | __ _  __| | ___  | |__  _   _  | |  | |_   ___  ___ _ 
 | |\/| |/ _` |/ _` |/ _ \ | '_ \| | | | | |  | | | | \ \/ / | |
 | |  | | (_| | (_| |  __/ | |_) | |_| | | |__| | |_| |>  <| | |
 |_|  |_|\__,_|\__,_|\___| |_.__/ \__, | |_____/ \__,_/_/\_\_|_|
                                   __/ |                        
                                  |___/                                                  
""")

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

default_config = {
    "token": "",
    "channels": [
        {
            "id": "123456789101112131415",
            "message": "Example message 1",
            "attachments": ["C:\\Users\\REPLACE_THIS_WITH_UR_GIF_OR_PNG_PATH\\Desktop\\MyLovelyBannerTest.gif"]
        },
        {
            "id": "123456789101112131415",
            "message": "Example message 2",
            "attachments": [""]
        }
    ],
    "delay_in_minutes": 1,
    "webhook_url": ""
}

packages = [
    "discord.py==1.7.3",
    "aiohttp",
    "asyncio",
    "datetime"
]

license_text = """
By using this program, you agree to the following terms:

1. Usage of this program is at your own risk. We do not take responsibility for any actions taken against you, including bans or restrictions applied by Discord or any other platform.
2. Leaking or sharing this program without authorization will result in a permanent blacklist from accessing future updates or related services.
3. If your account is banned or restricted, it is not our responsibility. As per Discord's policies, using self-bots is prohibited.
4. By continuing to use this software, you acknowledge and accept these terms.
"""

config_file = 'configs.json'
requirements_file = 'requirements.txt'
license_file = 'LICENSE.txt'
if not os.path.exists(config_file):
    with open(config_file, 'w') as f:
        json.dump(default_config, f, indent=4)
    print(f"{RED}No 'configs.json' found. A new 'configs.json' has been created with default values.{RESET}")
    print(f"{YELLOW}Please customize it with your token, channel IDs, messages, and other settings.{RESET}")

if not os.path.exists(requirements_file):
    with open(requirements_file, 'w') as r:
        for package in packages:
            r.write(f"{package}\n")
    print(f"{GREEN}Created 'requirements.txt', please install the required modules.{RESET}")

if not os.path.exists(license_file):
    with open(license_file, 'w') as l:
        l.write(license_text.strip())
    print(f"{GREEN}A 'LICENSE.txt' file has been created. Please read the terms before using this program.{RESET}")
    exit()

with open('configs.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

token = config["token"]
channels = config["channels"]
delay_in_minutes = config["delay_in_minutes"]
webhook_url = config["webhook_url"]

delay_in_seconds = delay_in_minutes * 60
start_time = time.time()
status = "Running ✅"

client = commands.Bot(command_prefix='your_prefix_but_not_needed', intents=discord.Intents.all(), self_bot=True)

async def send_to_webhook(user_id, channel_id, delay, uptime, status):
    formatted_delay = f"{delay} minute{'s' if delay != 1 else ''}"

    current_time = datetime.datetime.now(datetime.timezone.utc)
    formatted_timestamp = current_time.isoformat()

    async with aiohttp.ClientSession() as session:
        elapsed_time = int(time.time() - start_time)

        hours = elapsed_time // 3600
        minutes = (elapsed_time % 3600) // 60
        seconds = elapsed_time % 60

        if hours > 0:
            uptime_formatted = f"{hours} hour{'s' if hours > 1 else ''}, {minutes} minute{'s' if minutes != 1 else ''}, {seconds} second{'s' if seconds != 1 else ''}"
        elif minutes > 0:
            uptime_formatted = f"{minutes} minute{'s' if minutes > 1 else ''}, {seconds} second{'s' if seconds != 1 else ''}"
        else:
            uptime_formatted = f"{seconds} second{'s' if seconds > 1 else ''}"

        webhook_data = {
            "content": "",
            "embeds": [
                {
                    "title": "📌 Auto Post Logs 📌",
                    "description": f"- **Thanks for using our Auto Poster 🎉**\n\n**User 👨🏻‍💻**\n<@{user_id}>\n\n**Channel 📝**\n<#{channel_id}>\n\n**Delay ⌛**\n{formatted_delay}\n\n**Uptime ⏰**\n{uptime_formatted}\n\n**Status 🔎**\n{status}\n\n*Invite 5 People to our Discord Server and get Rewards! [Click Here!](https://dsc.gg/cpsscripts)*",
                    "color": None,
                    "footer": {
                        "text": "Auto Post by Duxii & Screamy"
                    },
                    "timestamp": formatted_timestamp,
                    "image": {
                        "url": "https://media.discordapp.net/attachments/1297259902280142889/1303378099336908850/standard.gif?ex=672b88f2&is=672a3772&hm=4fee8c3599292b7172d5181067e93f7028500d014fc17864661ff2cb4421c98e&width=500&height=128&"
                    },
                    "thumbnail": {
                        "url": "https://media.discordapp.net/attachments/1297259902280142889/1303381989507858523/a_0dddc192f7f6ae93750c68f3526cc6d4.gif?ex=672b8c91&is=672a3b11&hm=da3d9cd551be17f5ea1dc2a314926549637d3fd97321da5aceb858e26bb26655&=&width=108&height=108"
                    }
                }
            ],
            "attachments": []
        }
        
        async with session.post(webhook_url, json=webhook_data) as response:
            if response.status == 204:
                print(f"{GREEN}Successfully sent logs to webhook.{RESET}")
                status = "Running ✅"
            else:
                print(f"{RED}Failed to send message to webhook. Status code: {response.status}{RESET}")
                status = "Error ❌"

channels_dict = {int(channel_info["id"]): channel_info for channel_info in channels}

@client.event
async def on_ready():
    print(f"{YELLOW}Logged in as {client.user}{RESET}")

    async def send_message(channel_id, message_content, attachments):
        global status
        try:
            channel = client.get_channel(channel_id)
            if channel is None:
                print(f"{RED}Channel with ID {channel_id} not found.{RESET}")
                return

            await channel.send(
                content=message_content,
                files=[discord.File(attachment) for attachment in attachments if os.path.exists(attachment)]
            )
            print(f"{GREEN}Sent message to channel: {channel.name}{RESET}")
            if webhook_url:
                await send_to_webhook(client.user.id, channel.id, delay_in_minutes, "N/A", status)
                delay_textwebhook = "minute" if delay_in_minutes == 1 else "minutes"
                print(f"{YELLOW}Waiting for {delay_in_minutes} {delay_textwebhook} before attempting to send messages again...{RESET}")

        except Exception as e:
            print(f"{RED}Failed to send message to channel {channel_id}: {e}{RESET}")

    async def send_messages():
        global status
        while True:
            for channel_info in channels:
                channel_id = int(channel_info["id"])
                message_content = channel_info["message"]
                attachments = channel_info.get("attachments", [])
                asyncio.create_task(send_message(channel_id, message_content, attachments))

            delay_text = "minute" if delay_in_minutes == 1 else "minutes"
            await asyncio.sleep(delay_in_seconds)

    client.loop.create_task(send_messages())

try:
    client.run(token, bot=False)
except discord.errors.LoginFailure:
    if os.path.exists(config_file):
        print(f"{RED}Invalid or missing token in 'configs.json'. Please check and update your token.{RESET}")
        input("Press any key to close.")
        exit()