from telegram.ext import ApplicationBuilder, CommandHandler
from telegram_bot_commands import *

from view import get_number_operation
from  write_read_file import read_file     




app = ApplicationBuilder().token("5609999761:AAGp-4qf_bDTCkVp6WqP1GWlDC1KLriRW7s").build()

app.add_handler(CommandHandler("f1", help_command))          # Выберите номер категории
app.add_handler(CommandHandler("1", all_lastname_command))   # 1 - показать все фамилии
app.add_handler(CommandHandler("2", all_firstname_command))   # 2 - показать все имена
app.add_handler(CommandHandler("3", all_classnumber_command)) # 3 - показать все № классов
app.add_handler(CommandHandler("4", choice_class_pupils_command))  # 4 - показать учеников выбранного класса\
app.add_handler(CommandHandler("5", all_the_table_command))   # 5 - показать всю таблицу
app.add_handler(CommandHandler("6", pupil_data_command))       # 6 - показать информацию по ученику
app.add_handler(CommandHandler("7", add_pupil_data_command))   # 7 - добавить ученика
app.add_handler(CommandHandler("8", exit_command))           # 8 - выход

print('server start')

app.run_polling()