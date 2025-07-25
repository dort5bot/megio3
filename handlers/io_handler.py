from telegram.ext import CommandHandler
from utils.binance_utils import get_io_report
from utils.csv_utils import log_io_signal
import asyncio

async def io_command(update, context):
    report, data_to_log = await get_io_report()
    log_io_signal(data_to_log)
    await update.message.reply_text(report)

def register_io(app):
    app.add_handler(CommandHandler("io", io_command))
