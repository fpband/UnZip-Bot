from unzipbot import app
from Config import Config
from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = "**Hii {}, I'm a Simple File Extractor Bot From Your Compressed Files (zip & rar files). \n\nI can unzip & unrar your files and upload them to you as your wish. \n\n 🤖 Developer : [Animesh Verma](https://t.me/Animesh941)**"


    # About Message
    ABOUT = "**About This Bot** \n\nThis is an open source Unzip bot by @MysteryBots \n\nSource : [Click Here](https://github.com/MysteryBots/UnzipBot) \n\nFramework : [Pyrogram](docs.pyrogram.org) \n\nLanguage : [Python](www.python.org) \n\nDeveloper : [Mყʂƚҽɾყ Bσყ](https://t.me/MysteryxD)"


    
    
    HELP = """
**Hello {} ❤️
Send any zip/rar file then choose a mode and your work is done!
I'll unzip/unrar it and return you it's contents.
I will also total the contents & number of files in the compressed file...**

**Available Commands :
/start - Check if bot is alive.
/help - This Message.
/about - About this bot and source code**

**Made with ♥ by Animesh ⚡**
**Join [Updates Channel](https://t.me/AVBotz) & [Support Group](https://t.me/AVBotz_Support)**
"""
    
    # Home Button
    home_button = [[InlineKeyboardButton(text="🏡 Home", callback_data="home")]]

   

    # Rest Buttons
    buttons = [
        [
            InlineKeyboardButton("😎 My Owner", url="https://t.me/Animesh941"),
            InlineKeyboardButton("🤖 About", callback_data="about")
        ],
        [InlineKeyboardButton("ℹ️ Help", callback_data="help")],
        [InlineKeyboardButton("⛔ Close", callback_data="deploy")]
    ]
