from telegram.ext import CommandHandler
from utils.binance_utils import get_nls_signal
from utils.csv_utils import log_signal

async def nls_command(update, context):
    pattern = " ".join(context.args).upper() if context.args else ""
    result = await get_nls_signal(pattern)
    log_signal("NLS", result)
    await update.message.reply_text(result)

def register_nls(app):
    app.add_handler(CommandHandler("nls", nls_command))
