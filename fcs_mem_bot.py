"""
bot for memes
"""
from random import randint
import os
import telebot
from telebot import types

bot = telebot.TeleBot(os.environ.get("TELEGRAM_BOT_TOKEN"))


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    """
    info message
    """
    bot.reply_to(message,
                 "У данного бота много функций:"
                 "\n Во-первых, бот умеет скидивать в чат рандомный мем/фото кота и тд\n"
                 "Во-вторых, в нем есть много мемов для ВП(важных переговоров),"
                 " которыми пользователь так же может "
                 "воспользоваться в чате, просто обратившись к боту с помошью @Fcs_mem_bot,\n "
                 "в-третьих, в чате с ботом встроена функция"
                 " эхо(отвечает на фаше сообщение тем же сообщение) "
                 "+ есть две особенные комманда( для первой просто попробуйте "
                 "поздороваться с ботом, а вот для второй надо"
                 " узнать фамилию любимого преподавателя моего одногруппника - "
                 "@nardzhiev и написать ее на русском с большой буквы)")


@bot.message_handler(commands=['hello_father'])
def hello_father(message):
    """
    hello,father meme
    """
    with open("bkjnJe_k5aM.jpeg", "rb") as father:
        bot.send_photo(message.chat.id, father)


@bot.inline_handler(func=lambda query: True)
def query_text(query):
    """
    Bot photos
    """
    # pylint: disable-msg=too-many-locals
    # pylint: disable-msg=too-many-branches
    # pylint: disable-msg=too-many-statements
    v_a = randint(0, 100)
    if 0 <= v_a <= 20:
        r_pic3 = types.InlineQueryResultPhoto(
            id='5',
            photo_url="https://i.imgur.com/zsMpvWW.jpg",
            thumb_url="https://i.imgur.com/zsMpvWWb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный кот",
            caption="кот 1"
        )
    elif 21 <= v_a <= 40:
        r_pic3 = types.InlineQueryResultPhoto(
            id='5',
            photo_url="https://i.imgur.com/7MHyZqt.jpg",
            thumb_url="https://i.imgur.com/zsMpvWWb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный кот",
            caption="кот 2"
        )
    elif 41 <= v_a <= 60:
        r_pic3 = types.InlineQueryResultPhoto(
            id='5',
            photo_url="https://i.imgur.com/043Hg5A.jpg",
            thumb_url="https://i.imgur.com/zsMpvWWb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный кот",
            caption="кот 3"
        )
    elif 61 <= v_a <= 80:
        r_pic3 = types.InlineQueryResultPhoto(
            id='5',
            photo_url="https://i.imgur.com/PWo5Hvw.jpg",
            thumb_url="https://i.imgur.com/zsMpvWWb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный кот",
            caption="кот 4"
        )
    else:
        r_pic3 = types.InlineQueryResultPhoto(
            id='5',
            photo_url="https://i.imgur.com/fiqwpHK.jpg",
            thumb_url="https://i.imgur.com/zsMpvWWb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный кот",
            caption="кот 5"
        )
    v_b = randint(0, 79)
    if 0 <= v_b <= 2:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/959lBTy.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 3 <= v_b <= 5:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/a0wr2ii.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 6 <= v_b <= 8:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/ETitthn.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 9 <= v_b <= 11:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/TOhnZGs.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 12 <= v_b <= 14:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/S0ZCuKH.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 73 <= v_b <= 74:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/WX1i0nx.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем",
            caption="Поздравляем,вам выпал эпический хоббит-воин-Мячин!"
        )
    elif 15 <= v_b <= 17:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/q9wKFXu.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 18 <= v_b <= 20:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/S1NCVM6.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 21 <= v_b <= 23:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/poRXpah.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 24 <= v_b <= 26:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/yJqKVDG.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 27 <= v_b <= 29:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/j8hnOUM.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 30 <= v_b <= 32:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/yYtEGG2.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 33 <= v_b <= 35:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/QQgaUxa.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 36 <= v_b <= 38:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/QN3KODk.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 39 <= v_b <= 41:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/b3ePV3X.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 42 <= v_b <= 44:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/hhXgA3Q.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 45 <= v_b <= 47:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/NJL6iSU.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 48 <= v_b <= 50:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/T49cILL.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 51 <= v_b <= 53:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/Uyh5SsA.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif v_b == 72:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/hGRIXQd.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем",
            caption="О ГОСПОДИ! Вам выпал ЛЕГЕНДАРНЫЙ РЕКУРСИВНЫЙ ТАГИР!"
        )
    elif 54 <= v_b <= 56:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/oP7LUuf.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 57 <= v_b <= 59:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/rtQJEnc.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 60 <= v_b <= 62:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/HRQk5mG.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 63 <= v_b <= 65:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/8YvFZtL.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 66 <= v_b <= 68:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/7lWxf5I.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 69 <= v_b <= 71:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/fHLV1R8.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    elif 75 <= v_b <= 77:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/qvYz2Ly.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем"
        )
    else:
        r_pic4 = types.InlineQueryResultPhoto(
            id='6',
            photo_url="https://i.imgur.com/3BjlCLm.jpg",
            thumb_url="https://i.imgur.com/YBQPdlwb.jpg",
            photo_width="50",
            photo_height="50",
            title="Случайный мем",
            caption="О, вам попался редкий Хранитель-пивного очага 2010!"
        )
    v_c = randint(0, 15)
    if v_c == 0:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/x9DZWEt.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 1:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/4AdbDjW.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 2:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/6QjPhew.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 3:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/vVthBor.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 4:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/ehP7iUy.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 5:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/MBY1gfJ.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 6:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/qOIq3Qh.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 7:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/s45WYuK.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 8:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/wwCYElg.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 9:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/FFAo6Am.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 10:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/ICTOd4I.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 11:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/3CoHAZm.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 12:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/KXqqn5J.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    elif v_c == 13:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/WOwy18v.jpg",
            thumb_url="https://i.imgur.com/s3EWbsTb.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    else:
        r_pic5 = types.InlineQueryResultPhoto(
            id='7',
            photo_url="https://i.imgur.com/WOwy18v.jpg",
            thumb_url="https://i.imgur.com/s3EWbsT.png",
            photo_width="50",
            photo_height="50",
            title="Случайный no horny meme"
        )
    r_pic2 = types.InlineQueryResultPhoto(
        id='2',
        title="Идеальная формула",
        photo_url="https://i.imgur.com/V9fzjQl.jpg",
        thumb_url="https://i.imgur.com/V9fzjQlb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic6 = types.InlineQueryResultPhoto(
        id='8',
        title="AAAAAAAA",
        photo_url="https://i.imgur.com/mkn1iSO.jpg",
        thumb_url="https://i.imgur.com/mkn1iSOb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic7 = types.InlineQueryResultPhoto(
        id='9',
        title="Видимое замешательство",
        photo_url="https://i.imgur.com/iiFwXg2.jpg",
        thumb_url="https://i.imgur.com/iiFwXg2b.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic8 = types.InlineQueryResultPhoto(
        id='10',
        title="Стандарты",
        photo_url="https://i.imgur.com/ijCyuw1.jpg",
        thumb_url="https://i.imgur.com/ijCyuw1b.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic9 = types.InlineQueryResultPhoto(
        id='11',
        title="Bugs",
        photo_url="https://i.imgur.com/dcAqRI2.jpg",
        thumb_url="https://i.imgur.com/dcAqRI2b.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic10 = types.InlineQueryResultPhoto(
        id='12',
        title="Хороший вопрос",
        photo_url="https://i.imgur.com/K7S6kPM.jpg",
        thumb_url="https://i.imgur.com/K7S6kPMb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic11 = types.InlineQueryResultPhoto(
        id='13',
        title="Xzibit",
        photo_url="https://i.imgur.com/hUxrYI8.jpg",
        thumb_url="https://i.imgur.com/hUxrYI8b.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic12 = types.InlineQueryResultPhoto(
        id='14',
        title="IQ",
        photo_url="https://i.imgur.com/184zcyA.jpg",
        thumb_url="https://i.imgur.com/184zcyAb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic13 = types.InlineQueryResultPhoto(
        id='15',
        title="Confused unga bunga",
        photo_url="https://i.imgur.com/hPEwNMg.jpg",
        thumb_url="https://i.imgur.com/hPEwNMgb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic14 = types.InlineQueryResultPhoto(
        id='16',
        title="Math",
        photo_url="https://i.imgur.com/fIa7nEk.jpg",
        thumb_url="https://i.imgur.com/fIa7nEkb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic15 = types.InlineQueryResultPhoto(
        id='17',
        title="Бог покинул нас",
        photo_url="https://i.imgur.com/egsRCeU.jpg",
        thumb_url="https://i.imgur.com/egsRCeUb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic16 = types.InlineQueryResultPhoto(
        id='18',
        title="Босс я устал",
        photo_url="https://i.imgur.com/8Wt0TsP.jpg",
        thumb_url="https://i.imgur.com/8Wt0TsPb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic17 = types.InlineQueryResultPhoto(
        id='19',
        title="Ищи себя",
        photo_url="https://i.imgur.com/kkIPEaN.jpg",
        thumb_url="https://i.imgur.com/kkIPEaNb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic18 = types.InlineQueryResultPhoto(
        id='20',
        title="Святая вода",
        photo_url="https://i.imgur.com/IHULwW8.jpg",
        thumb_url="https://i.imgur.com/IHULwW8b.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic19 = types.InlineQueryResultPhoto(
        id='21',
        title="Sad cat",
        photo_url="https://i.imgur.com/XqHisN5.jpg",
        thumb_url="https://i.imgur.com/XqHisN5b.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic20 = types.InlineQueryResultPhoto(
        id='22',
        title="Думай, Марк",
        photo_url="https://i.imgur.com/rMZ0peU.jpg",
        thumb_url="https://i.imgur.com/rMZ0peUb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic21 = types.InlineQueryResultPhoto(
        id='23',
        title="Monkey",
        photo_url="https://i.imgur.com/h7l6B6f.jpg",
        thumb_url="https://i.imgur.com/h7l6B6fb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_pic22 = types.InlineQueryResultPhoto(
        id='24',
        title="Perhaps",
        photo_url="https://i.imgur.com/tUIzEwR.jpg",
        thumb_url="https://i.imgur.com/tUIzEwRb.jpg",
        photo_width="50",
        photo_height="50"
    )
    r_gif = types.InlineQueryResultGif(
        id='3',
        gif_url="https://i.imgur.com/jvnpls0.mp4",
        thumb_url="https://i.imgur.com/jvnpls0b.jpg",
        gif_width="50",
        gif_height="50",
        title="Гифка с Косовым"
    )
    r_gif2 = types.InlineQueryResultGif(
        id='25',
        gif_url="https://i.imgur.com/k5vJ7fT.mp4",
        thumb_url="https://i.imgur.com/k5vJ7fTb.jpg",
        gif_width="50",
        gif_height="50",
        title="Merge"
    )
    r_gif3 = types.InlineQueryResultGif(
        id='26',
        gif_url="https://i.imgur.com/HixEsyX.mp4",
        thumb_url="https://i.imgur.com/HixEsyXb.jpg",
        gif_width="50",
        gif_height="50",
        title="Гифка с Косовым 2"
    )
    r_text = types.InlineQueryResultArticle(
        id='4', title="Инфо", description="Полезная информация",
        input_message_content=types.InputTextMessageContent(
            message_text="У данного бота много функций:"
                 "\n Во-первых, бот умеет скидивать в чат рандомный мем/фото кота и тд\n"
                 "Во-вторых, в нем есть много мемов для ВП(важных переговоров),"
                 " которыми пользователь так же может "
                 "воспользоваться в чате, просто обратившись к боту с помошью @Fcs_mem_bot,\n "
                 "в-третьих, в чате с ботом встроена функция эхо"
                 "(отвечает на фаше сообщение тем же сообщение) "
                 "+ есть две особенные комманда( для первой просто попробуйте "
                 "поздороваться с ботом, а вот для второй надо"
                 " узнать фамилию любимого преподавателя моего одногруппника - "
                 "@nardzhiev и написать ее на русском с большой буквы)")
    )
    bot.answer_inline_query(query.id,
                            [r_text, r_pic3, r_pic4, r_pic5, r_pic6,
                             r_pic7, r_pic8, r_pic9, r_pic10, r_pic11,
                              r_pic12, r_pic13, r_pic14, r_pic15, r_pic16, 
                             r_pic17, r_pic18, r_pic19, r_pic20, r_pic21, 
                             r_pic22, r_pic2, r_gif, r_gif2, r_gif3],
                              cache_time=1, is_personal=True)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """
    fcs - mem
    """
    if message.text == "fcs":
        bot.send_message(message.chat.id, "mem")
    elif message.text == "Зобнин":
        with open("2M44EqK.jpg", "rb") as zobnin:
            bot.send_photo(message.chat.id, zobnin)
            bot.send_message(message.chat.id,
                             "О господи, тебе было не лень написать Никите,"
                             " ну ладно, тогда вот твоя награда - уставший Зобнин")
    else:
        bot.reply_to(message, message.text)


bot.infinity_polling()
