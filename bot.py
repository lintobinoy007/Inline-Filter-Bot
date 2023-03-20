python
import telegram
from telegram.ext import Updater, CommandHandler

# Create a new Telegram bot using your token
bot = telegram.Bot(token="6260545100:AAG9V73zvSbJz40fJQ_UxiMgd0Vrl0hUUTo")

# Create a handler function for the /start command
def start(update, context):
    update.message.reply_text("Hello, world!")

# Set up an Updater object with your bot token
updater = Updater(token="6260545100:AAG9V73zvSbJz40fJQ_UxiMgd0Vrl0hUUTo", use_context=True)

# Set up a CommandHandler for the /start command
updater.dispatcher.add_handler(CommandHandler('start', start))

# Start your bot
updater.start_polling()
updater.idle()
