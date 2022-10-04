from telegram import Update
from telegram.ext import ContextTypes
from view import get_number_operation
from write_read_file import read_file

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/1 - все фамилии\n/2 - все имена\n/3 - все № классов\n/4 - Ученики выбранного класса\n/5 - Вся таблица\n/6 - данные ученика\n/7 - даобавить ученика\n/8 - Выход')

async def all_lastname_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(get_number_operation(read_file('file.csv'), 1)))

async def all_firstname_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(get_number_operation(read_file('file.csv'), 2)))

async def all_classnumber_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(get_number_operation(read_file('file.csv'), 3)))

async def choice_class_pupils_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(get_number_operation(read_file('file.json'), 4)))

async def all_the_table_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(get_number_operation(read_file('file.json'), 5)))

async def pupil_data_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(get_number_operation(read_file('file.json'), 6)))

async def add_pupil_data_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(get_number_operation(read_file('file.json'), 7)))    

async def exit_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(str(get_number_operation(read_file('file.csv'), 8)))