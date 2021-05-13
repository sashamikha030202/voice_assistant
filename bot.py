import telebot
from utils import *
from config import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, 'Hey')


@bot.message_handler(content_types=['voice'])
def download_voice(message):
    file_info = bot.get_file(message.voice.file_id)
    down_file = bot.download_file(file_info.file_path)
    with open('new.oga', 'wb') as new:
        new.write(down_file)

    os.system('clear')
    rms = RecognizeSpeech()
    rms.recognize_my_speech()
    si = SystemInfo()
    us = UpdateSystem()

    print(recognized)

    if len(recognized) > 0:
        if 'information' in recognized[0]:
            if 'information about memory' in recognized[0]:
                print(si.ram_info())
            elif 'information about processor' in recognized[0]:
                print(si.central_processor_info())

        elif 'open soft' in recognized[0]:
            r = recognized[0][10:].split(' ')
            print(r)
            wws = WorkWithSystem()
            wws.open_soft(soft=r)
        elif 'open link' in recognized[0]:
            r = recognized[0][10:]
            print(r)
            wwb = WorkWithBrowser(r)
            wwb.open_link()

        elif 'download track' in recognized[0] or 'download music' in recognized[0]:
            print('hey')
            with Display():
                dl = DownloadMusic(recognized[0][15:])
                dl.open_link()
                dl.download_mp3()
                del recognized[0]

        elif 'update system' in recognized[0]:
            us.update_system()
        elif 'upgrade system' in recognized[0]:
            us.upgrade_system()
        elif 'new version of system' in recognized[0]:
            us.dist_upgrade()

        elif 'download libraries' in recognized[0]:
            msg = bot.send_message(message.chat.id, 'Enter names of libraries')
            bot.register_next_step_handler(msg, linux_libs)
        elif 'download python libraries' in recognized[0]:
            msg = bot.send_message(message.chat.id, 'Enter names of python libs')
            bot.register_next_step_handler(msg, python_libs)

        elif 'screenshot' in recognized[0]:
            wws = WorkWithSystem()
            file = open(wws.take_screenshot(), 'rb')
            bot.send_document(message.chat.id, file)
    else:
        print("I apologize, but didn't hear you. Can you repeat please? ")


@bot.message_handler(content_types=['text'])
def linux_libs(message):
    wws = WorkWithSystem()
    wws.download_libraries(message.text)

@bot.message_handler(content_types=['text'])
def python_libs(message):
    wws = WorkWithSystem()
    wws.download_python_libs(libs=message.text.split(' '))

bot.polling(none_stop=True)
