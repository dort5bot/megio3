from telegram.ext import CommandHandler
from utils.binance_utils import get_npr_signal
from utils.csv_utils import log_signal

async def npr_command(update, context):
    args = context.args
    if args and args[0].isdigit():
        days = int(args[0])
    else:
        days = None
    coins = [a.upper() for a in args if not (a.isdigit())] if args else []
    result = await get_npr_signal(days=days, coins=coins)
    log_signal("NPR", result if not coins else None)
    await update.message.reply_text(result)

def register_npr(app):
    app.add_handler(CommandHandler("npr", npr_command))
