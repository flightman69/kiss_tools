import os
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import instaloader
import yt_dlp
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN, parse_mode=None)

# Ensure the downloads directory exists
if not os.path.exists('downloads'):
    os.makedirs('downloads')

# Message handler for any text message
@bot.message_handler(func=lambda message: True)
def download_handler(message):
    url = message.text
    if "youtube.com" in url or "youtu.be" in url:
        markup = InlineKeyboardMarkup(row_width=2)
        video_button = InlineKeyboardButton("Video+Audio", callback_data=f"video")
        audio_button = InlineKeyboardButton("Audio only", callback_data=f"audio")
        markup.add(video_button, audio_button)
        bot.send_message(message.chat.id, message.text, reply_markup=markup)
        # download_yt(message, url)  # Call the YouTube download function
    elif "instagram.com" in url:
        username = os.getenv("fuckme")  
        password = os.getenv("yessdaddy")  
        download_insta(username, password, message, url)  # Call the Instagram download function
    else:
        bot.send_message(message.chat.id, "Unsupported URL. Please send a valid YouTube or Instagram link.")
@bot.callback_query_handler(func = lambda call: True)
def youtube_handler(call):
    url = str(call.message.text)
    print(url)

    if call.data == "video":
        # bot.send_message(message.chat.id, "Download Video wait")
        download_yt(call.message, url)
    elif call.data == "audio":
        # bot.send_message(message.chat.id, "Download audio wait")
        download_yt_audio_only(call.message, url)
# Instagram downloader function
def download_insta(username, password, message, url):
    try:
        bot.send_message(message.chat.id, "Downloading Instagram reel...")

        ytdl_opts = {
            'username': username,
            'password': password,
            'format': 'bestvideo+bestaudio/best',  
            'outtmpl': 'downloads/%(title)s.%(ext)s',  
            'cookiefile': 'cookies.txt'  # Optional: Save session cookies for faster future logins
        }
        with yt_dlp.YoutubeDL(ytdl_opts) as ytdl:
            info_dict = ytdl.extract_info(url, download=True)
            file_path = ytdl.prepare_filename(info_dict)

        with open(file_path, 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)

        # Optional: Cleanup the downloaded file after sending it
        os.remove(file_path)

    except Exception as e:
        bot.send_message(message.chat.id, f"An error occurred while downloading: {str(e)}")

# YouTube downloader function
def download_yt(message, url):
    try:
        bot.send_message(message.chat.id, "Downloading YouTube video...")

        # Define download options for yt-dlp
        ydl_opts = {

            'format': 'mp4',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict)

        # Send the video file to the user
        bot.send_message(message.chat.id, "Download successfull sending video...")
        with open(file_path, 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)

        # Cleanup the downloaded file after sending it
        os.remove(file_path)

    except Exception as e:
        bot.send_message(message.chat.id, f"An error occurred while downloading: {str(e)}")

def download_yt_audio_only(message, url):
    try:
        bot.send_message(message.chat.id, "Downloading YouTube audio...")

        # Define download options for yt-dlp
        ydl_opts = {

            'format': 'bestaudio',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info_dict)

        # Send the video file to the user
        bot.send_message(message.chat.id, "Download successfull sending audio...")
        with open(file_path, 'rb') as video_file:
            bot.send_video(message.chat.id, video_file)

        # Cleanup the downloaded file after sending it
        os.remove(file_path)

    except Exception as e:
        bot.send_message(message.chat.id, f"An error occurred while downloading: {str(e)}")

# Start polling to receive messages
bot.polling()

