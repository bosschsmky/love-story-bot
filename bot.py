from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import random
import os

TOKEN = os.getenv("BOT_TOKEN")

keyboard = [
    ["💌 Лист від мене"],
        ["🌹 Комплімент", "❤️ Чому я тебе люблю"],
            ["🤗 Обійми", "😘 Поцілунок"],
                ["🎁 Сюрприз"]
                ]

                compliments = [
                    "Ти неймовірна ❤️",
                        "Твоя усмішка — це магія 🌸",
                            "Ти робиш цей світ кращим 💖",
                                "Я пишаюсь тобою ✨"
                                ]

                                reasons = [
                                    "Бо ти особлива для мене ❤️",
                                        "Бо з тобою мені добре 💖",
                                            "Бо ти — мій найкращий вибір 🌸",
                                                "Бо я тебе дуже люблю 🤍"
                                                ]

                                                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

                                                async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                                    await update.message.reply_text(
                                                            "💖 Love Story Bot 💖\n\nЯ тут, щоб дарувати тобі тепло ❤️",
                                                                    reply_markup=reply_markup
                                                                        )

                                                                        async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                                                            text = update.message.text

                                                                                if text == "🌹 Комплімент":
                                                                                        await update.message.reply_text(random.choice(compliments))

                                                                                            elif text == "❤️ Чому я тебе люблю":
                                                                                                    await update.message.reply_text(random.choice(reasons))

                                                                                                        elif text == "🤗 Обійми":
                                                                                                                await update.message.reply_text("🤗 Я тебе міцно обіймаю ❤️")

                                                                                                                    elif text == "😘 Поцілунок":
                                                                                                                            await update.message.reply_text("😘 Цьом ❤️")

                                                                                                                                elif text == "🎁 Сюрприз":
                                                                                                                                        await update.message.reply_text("🎁 Ти — мій найкращий сюрприз 💖")

                                                                                                                                            elif text == "💌 Лист від мене":
                                                                                                                                                    await update.message.reply_text(
                                                                                                                                                                "💌 Лист:\n\n"
                                                                                                                                                                            "Ти дуже важлива для мене ❤️\n"
                                                                                                                                                                                        "Я хочу, щоб ти завжди посміхалась 💖"
                                                                                                                                                                                                )

                                                                                                                                                                                                app = Application.builder().token(TOKEN).build()

                                                                                                                                                                                                app.add_handler(CommandHandler("start", start))
                                                                                                                                                                                                app.add_handler(MessageHandler(filters.TEXT, handle))

                                                                                                                                                                                                app.run_polling()from telegram import Update, ReplyKeyboardMarkup
                                                                                                                                                                                                from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
                                                                                                                                                                                                import random
                                                                                                                                                                                                import os

                                                                                                                                                                                                TOKEN = os.getenv("BOT_TOKEN")

                                                                                                                                                                                                keyboard = [
                                                                                                                                                                                                    ["💌 Лист від мене"],
                                                                                                                                                                                                        ["🌹 Комплімент", "❤️ Чому я тебе люблю"],
                                                                                                                                                                                                            ["🤗 Обійми", "😘 Поцілунок"],
                                                                                                                                                                                                                ["🎁 Сюрприз"]
                                                                                                                                                                                                                ]

                                                                                                                                                                                                                compliments = [
                                                                                                                                                                                                                    "Ти неймовірна ❤️",
                                                                                                                                                                                                                        "Твоя усмішка — це магія 🌸",
                                                                                                                                                                                                                            "Ти робиш цей світ кращим 💖",
                                                                                                                                                                                                                                "Я пишаюсь тобою ✨"
                                                                                                                                                                                                                                ]

                                                                                                                                                                                                                                reasons = [
                                                                                                                                                                                                                                    "Бо ти особлива для мене ❤️",
                                                                                                                                                                                                                                        "Бо з тобою мені добре 💖",
                                                                                                                                                                                                                                            "Бо ти — мій найкращий вибір 🌸",
                                                                                                                                                                                                                                                "Бо я тебе дуже люблю 🤍"
                                                                                                                                                                                                                                                ]

                                                                                                                                                                                                                                                reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

                                                                                                                                                                                                                                                async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                                                                                                                                                                                                                                    await update.message.reply_text(
                                                                                                                                                                                                                                                            "💖 Love Story Bot 💖\n\nЯ тут, щоб дарувати тобі тепло ❤️",
                                                                                                                                                                                                                                                                    reply_markup=reply_markup
                                                                                                                                                                                                                                                                        )

                                                                                                                                                                                                                                                                        async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
                                                                                                                                                                                                                                                                            text = update.message.text

                                                                                                                                                                                                                                                                                if text == "🌹 Комплімент":
                                                                                                                                                                                                                                                                                        await update.message.reply_text(random.choice(compliments))

                                                                                                                                                                                                                                                                                            elif text == "❤️ Чому я тебе люблю":
                                                                                                                                                                                                                                                                                                    await update.message.reply_text(random.choice(reasons))

                                                                                                                                                                                                                                                                                                        elif text == "🤗 Обійми":
                                                                                                                                                                                                                                                                                                                await update.message.reply_text("🤗 Я тебе міцно обіймаю ❤️")

                                                                                                                                                                                                                                                                                                                    elif text == "😘 Поцілунок":
                                                                                                                                                                                                                                                                                                                            await update.message.reply_text("😘 Цьом ❤️")

                                                                                                                                                                                                                                                                                                                                elif text == "🎁 Сюрприз":
                                                                                                                                                                                                                                                                                                                                        await update.message.reply_text("🎁 Ти — мій найкращий сюрприз 💖")

                                                                                                                                                                                                                                                                                                                                            elif text == "💌 Лист від мене":
                                                                                                                                                                                                                                                                                                                                                    await update.message.reply_text(
                                                                                                                                                                                                                                                                                                                                                                "💌 Лист:\n\n"
                                                                                                                                                                                                                                                                                                                                                                            "Ти дуже важлива для мене ❤️\n"
                                                                                                                                                                                                                                                                                                                                                                                        "Я хочу, щоб ти завжди посміхалась 💖"
                                                                                                                                                                                                                                                                                                                                                                                                )

                                                                                                                                                                                                                                                                                                                                                                                                app = Application.builder().token(TOKEN).build()

                                                                                                                                                                                                                                                                                                                                                                                                app.add_handler(CommandHandler("start", start))
                                                                                                                                                                                                                                                                                                                                                                                                app.add_handler(MessageHandler(filters.TEXT, handle))

                                                                                                                                                                                                                                                                                                                                                                                                app.run_polling()
