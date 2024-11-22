# Automated Channel Messenger

This Python script is a powerful tool for automating posts in specific channels!

## Features
- **Automatic Configuration:** On the first run, the script generates a `configs.json` file. Just fill it in with the required details, and you're ready to go!
  - **Token:** Enter your bot's token to enable authenticated posting.
  - **Channel ID:** Set the ID of the channel where you want to post.
  - **Message Content:** Customize the message you want the bot to send.
  - **Attachments:** Optionally attach a GIF or PNG for added visual appeal.
  - **Webhook URL:** Include a webhook to log all sent messages for tracking purposes.

## Usage
Simply run the script, configure the `configs.json` file, and your bot will begin posting in the specified channel as configured. 

> **Note:** Feel free to modify the script for personal use, but **reselling or redistributing it is strictly prohibited**.
> **Note:** A slight issue where it will try to create and search for the configs.json on your Desktop instead, that should be fixed where you need to simply just run the Python script only, and it should create a configs.json along with two other files on your Desktop**.
> 
If you have any questions or need support, join our Discord server: [https://dsc.gg/cpsscripts](https://dsc.gg/cpsscripts)

## Requirements
- Python 3.x
- discord.py==1.7.3
- aiohttp
- asyncio
- datetime

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/DuxiiYT/Auto-Poster/blob/main/Automated%20Channel%20Messenger/Auto-Poster.py
   ```
2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script and configure `configs.json` as prompted.

## Disclaimer
This script is for **educational purposes only**. Using self-bots on Discord is against Discord's Terms of Service, and it is **illegal** to use them. By using this script, you assume full responsibility for any consequences, including account bans or any other actions taken by Discord. **I am not liable for any issues or consequences that may arise from using this script.**
