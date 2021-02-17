import requests
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, RegexHandler, ConversationHandler)
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove

STATE1 = 1
STATE2 = 2


# Método comeco = Mensagem inicial
def comeco(update, context):
    message = "Olá " + update.message.from_user.first_name + ", eu sou um robô em aprendizado.\n\nAs ideias que eu já sei trocar com você estão listadas em '/assuntos'"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


# Método assuntos = Quais assuntos o bot já consegue falar
def assuntos(update, context):
    message = "/o_que_e_ux"
    print(message)
    context.bot.send_message(chat_id=update.effective_chat.id, text=message)


# Método o_que_e_ux = O que o bot já fala sobre o assunto
def o_que_e_ux(update, context):
    message = '''O que é UX?\n
    		1 - Descrição\n
    		2 - Objetivo'''
    print(message)
    update.message.reply_text(message, reply_markup=ReplyKeyboardMarkup([], one_time_keyboard=True))


def inputoqux2(update, context):
    oqux = (update.message.text).lower
    # print(oqux)

    if oqux == '1' or oqux == 'descrição':
        message = 'O(a) Designer UX (abreviação de User Experience ou “Experiência do Usuário”, em tradução literal) é responsável, como o próprio nome diz, por garantir que o design projetado atenda a todas as necessidades dos usuários.'
        context.bot.send_message(chat_id=update.effective_chat.id, text=message)
        return STATE2

    else:
        if oqux == '2' or oqux == 'objetivo':
            message = 'Garantir a satisfação do cliente ao interagir com a empresa, plataformas ou marcas.'
            context.bot.send_message(chat_id=update.effective_chat.id, text=message)
    return STATE2


def cancel(update, context):
    return ConversationHandler.END


def main():
    # Acesso ao bot
    token = 'token'
    updater = Updater(token=token, use_context=True)

    # Definindo comando /start
    updater.dispatcher.add_handler(CommandHandler('start', comeco))
    # Definindo comando /assuntos
    updater.dispatcher.add_handler(CommandHandler('assuntos', assuntos))
    # Definindo comando /o_que_e_ux

    conversation_handler = ConversationHandler(
        entry_points=[CommandHandler('o_que_e_ux', o_que_e_ux)],
        states={
            #STATE1: [MessageHandler(Filters.text, 'inputoqux')]
            STATE2: [MessageHandler(Filters.text, 'inputoqux2')]
        },
        fallbacks=[CommandHandler('cancel', cancel)])
    updater.dispatcher.add_handler(conversation_handler)

    updater.start_polling()
    print(str(updater))
    updater.idle()


if __name__ == "__main__":
    main()
