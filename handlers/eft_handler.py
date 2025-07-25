from telegram.ext import CommandHandler
from utils.binance_utils import get_etf_report
from utils.csv_utils import log_etf_signal

async def eft_command(update, context):
    result = await get_etf_report(context.args)
    log_etf_signal(result)
    await update.message.reply_text(result)

def register_eft(app):
    app.add_handler(CommandHandler("eft", eft_command))
