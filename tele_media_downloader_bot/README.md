
# Tele Media Downloader Bot

Tele Media Downloader Bot is a Telegram bot that allows you to download videos from Instagram and YouTube directly to your device using simple commands. This bot provides an easy way to get your favorite videos with just a few clicks.

This bot is a part of the [KISS Tools](https://github.com/flightman69/kiss_tools) repository, a collection of simple and efficient tools designed to keep it short and simple.

## Features
- 📥 Download Instagram videos.
- 📥 Download YouTube videos.
- 🎯 Simple and easy-to-use interface.

## Prerequisites

Before you start, ensure you have the following installed:
- Python 3.7+
- pip (Python package installer)

## Getting Started

### 1. Clone the Repository
Navigate to the specific folder in the KISS Tools repository:
```bash
git clone -b flightman69/tele_media_downloader_bot https://github.com/flightman69/kiss_tools.git
cd kiss_tools/tele_media_downloader_bot
```

### 2. Install Dependencies
Install the required dependencies using:
```bash
pip install -r requirements.txt
```

### 3. Get Your Telegram API Key
- Open Telegram and search for the [BotFather](https://t.me/botfather).
- Use the `/newbot` command to create a new bot and get your API key.
- Save the API key for the next step.

### 4. Set Up Environment Variables
Create a file named `.env` in the root directory and add your API key:
```env
TOKEN = "your_api_key"
```

### 5. Run the Bot
Start the bot with the following command:
```bash
python3 media_download_bot.py
```

## Usage

- Send a YouTube or Instagram video link to the bot in Telegram.
- The bot will process the link and download the video for you.

## Contributing

We welcome contributions! To get started:
1. Fork the [KISS Tools repository](https://github.com/flightman69/kiss_tools).
2. Create a new branch for your feature or bug fix.
3. Make your changes in the `tele_media_downloader_bot` folder.
4. Submit a pull request with a detailed description of your updates.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgments

- Special thanks to the [Telegram Bot API](https://core.telegram.org/bots/api) for their amazing documentation.
- Inspired by the need for quick and easy video downloads.

---

Feel free to reach out if you have any questions or suggestions!

