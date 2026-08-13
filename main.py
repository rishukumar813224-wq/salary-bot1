from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8681947461:AAFIkboxP7rk851CUL6T0euxz5wrE33F3vY"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ Salary Bot Online\n\nEnglish + Indonesian Ready"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()