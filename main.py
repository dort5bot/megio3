from telegram.ext import ApplicationBuilder
from keep_alive import keep_alive
from handlers.io_handler import register_io
from handlers.nls_handler import register_nls
from handlers.npr_handler import register_npr
from handlers.eft_handler import register_eft
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
PORT = int(os.getenv("PORT", 8080))

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    register_io(app)
    register_nls(app)
    register_npr(app)
    register_eft(app)
    keep_alive()
    app.run_webhook(
        listen="0.0.0.0",
        port=PORT,
        url_path=TOKEN,
        webhook_url=f"{os.getenv('KEEP_ALIVE_URL')}/{TOKEN}"
    )

if __name__ == "__main__":
    main()
