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

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, welcome to Lazada Bot!\n')


async def scrap(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    get_message = " ".join(context.args)

    patterns = r'"([^"]+)"'
    
    find_patterns = re.findall(patterns, get_message)

    keyword, n_data, file_name, type_file = find_patterns

    keyword = keyword.lower().strip()
    n_data = int(n_data)
    type_file = type_file.lower().strip()

    if type_file not in DATA_TYPE:
        await update.message.reply_text(f'Only support {DATA_TYPE}')
        return


    await update.message.reply_text(f'Data: {keyword}, {n_data}, {file_name}, {type_file}')


    await update.message.reply_text(f'Sccraping data...\nPleasee wait!!!!')


    path_file = os.path.join(os.path.dirname(__file__), 'files', f'{file_name}')

    if not os.path.exists(path_file):
        os.makedirs(path_file)


    my_bot = LazadaBot()
    my_bot.scrap(keyword, n_data, path_file, type_file)

    with open(f"{path_file}.{type_file}", 'rb') as file:
        await update.message.reply_document(file)
    
    # os.remove(path_file)
    
    await update.message.reply_text(f'Done!!!!!')


    print(f"{keyword}, {n_data}, {file_name}, {type_file}")


app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("scrap", scrap))

app.run_polling()