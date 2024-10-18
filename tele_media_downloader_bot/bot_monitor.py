import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class BotReloader(FileSystemEventHandler):
    def __init__(self, bot_script):
        self.bot_script = bot_script
        self.process = None
        self.restart_bot()

    def restart_bot(self):
        if self.process:
            print("Killing previous bot instance...")
            self.process.kill()

        print("Starting new bot instance...")
        self.process = subprocess.Popen(['python', self.bot_script])

    def on_modified(self, event):
        if event.src_path.endswith(self.bot_script):
            print(f"Detected changes in {self.bot_script}, restarting bot...")
            self.restart_bot()

if __name__ == "__main__":
    bot_script = './media_download_bot.py'  # Your bot script

    event_handler = BotReloader(bot_script)
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)

    print(f"Monitoring {bot_script} for changes...")

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

