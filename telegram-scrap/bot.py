from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from sources import LazadaBot
from dotenv import load_dotenv
load_dotenv()
import re

DATA_TYPE = ['csv','txt','xlsx']


TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, welcome to Lazada Bot!\n')

async def scrap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    get_message = " ".join(context.args)

    patterns = r'"([^"]+)"'
    
    find_patterns = re.findall(patterns, get_message)

    keyword, n_data, file_name, type_file = find_patterns

    if type_file not in DATA_TYPE:
        await update.message.reply_text(f'Only support {DATA_TYPE}')

    n_data = int(n_data)


    my_bot = LazadaBot()
    my_bot.scrap(keyword, n_data, file_name, type_file)
    
    print(f"{keyword}, {n_data}, {file_name}, {type_file}")


app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("scrap", scrap))

app.run_polling()