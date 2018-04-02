#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, run_async
from random import sample, randrange
from datetime import timedelta
import os
import time
import sys
import logging
import re
import json

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


@run_async
def fullw(bot, update, args):
    if not args:
        update.message.reply_text("Usage: /fullw [text]")
    else:
        chardict = {".": ". ", "?": "? ", ", ": ", ", " ": "  ", "1": "１", "2": "２", "3": "３", "4": "４", "5": "５",
                    "6": "６", "7": "７", "8": "８", "9": "９", "0": "０", "q": "ｑ", "w": "ｗ", "e": "ｅ", "r": "ｒ", "t": "ｔ",
                    "y": "ｙ", "u": "ｕ", "i": "ｉ", "o": "ｏ", "p": "ｐ", "a": "ａ", "s": "ｓ", "d": "ｄ", "f": "ｆ", "g": "ｇ",
                    "h": "ｈ", "j": "ｊ", "k": "ｋ", "l": "ｌ", "z": "ｚ", "x": "ｘ", "c": "ｃ", "v": "ｖ", "b": "ｂ", "n": "ｎ",
                    "m": "ｍ", "Q": "Ｑ", "W": "Ｗ", "E": "Ｅ", "R": "Ｒ", "T": "Ｔ", "Y": "Ｙ", "U": "Ｕ", "I": "Ｉ", "O": "Ｏ",
                    "P": "Ｐ", "A": "Ａ", "S": "Ｓ", "D": "Ｄ", "F": "Ｆ", "G": "Ｇ", "H": "Ｈ", "J": "Ｊ", "K": "Ｋ", "L": "Ｌ",
                    "Z": "Ｚ", "X": "Ｘ", "C": "Ｃ", "V": "Ｖ", "B": "Ｂ", "N": "Ｎ", "M": "Ｍ"}
        stuff = ""
        for a in " ".join(args):
            try:
                stuff += chardict[a]
            except:
                stuff += a+" "
        update.message.reply_text(stuff)


@run_async
def ball(bot, update, args):
    foof = ["It is certain", "It is decidedly so", "Without a doubt", " Yes definitely", "You may rely on it",
            "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Signs point to yes",
            "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now",
            "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no",
            "Outlook not so good", "Very doubtful"
            ]
    x = (sample(foof, 1))
    if not args:
        update.message.reply_text("Please, answer me something! (/8ball [Question]")
    else:
        update.message.reply_text(x[0])


@run_async
def fortune(bot, update):
    foof = ["Reply hazy, try again", "Excellent Luck", "Good Luck", "Average Luck", "Bad Luck",
            "Good news will come to you by mail", "You will meet a dark handsome stranger", "Better not tell you now",
            "Outlook good", "Very Bad Luck", "Godly Luck"]
    x = (sample(foof, 1))
    update.message.reply_text(x[0])


def collatz(bot, update, args):
    if not args:
        update.message.reply_text("Usage: /collatz [Number] or /collatz info for explaination")
    elif args[0] == "info":
        update.message.reply_text(
            "The Collatz conjecture is a conjecture in mathematics named after Lothar Collatz. It can be summarized as "
            "follows. Take any positive integer n. If n is even, divide it by 2 to get n / 2. If n is odd, multiply it "
            "by 3 and add 1 to obtain 3n + 1. Repeat the process indefinitely. The conjecture states that no matter wha"
            "t number you start with, you will always eventually reach 1. Nobody has actually managed to prove if this "
            "is true of false. Try to find a value that disproves the conjecture! (note: Telegram has a 4069 characters"
            " limit per message, so the bot won't show all the steps with massive numbers")
    else:
        start_time = time.time()
        try:
            x = int(args[0])
            i = 0
            mem = args[0]+"\n"
            hi = x

            x, i, mem, hi = collatzcalc(x, i, mem, hi, start_time)
            if x == 'FUCK YOU':
                update.message.reply_text("THat took too long, ssry. Use a smaller value.")
                return

            try:
                update.message.reply_text(
                   "You lost!\n" + mem + "\nnumber of iterations: " + str(i) + "\nHightest number reached:"
                   + str(hi) + "\nThat took " + str(time.time() - start_time) + "s to execute.")
            except:
                update.message.reply_text(
                    "You lost!\nnumber of iterations: " + str(i) + "\nHightest number reached:"
                    + str(hi) + "\nThat took " + str(time.time() - start_time) + "s to execute.")

        except ValueError:
            update.message.reply_text("That's not a positive integer")


def collatzcalc(x, i, mem, hi, start_time):
    while x != 1:
        if x % 2 == 0:
            x = x // 2
            if x > hi:
                hi = x
        else:
            x = (x * 3 + 1) // 2
            if x * 2 > hi:
                hi = x
            i += 1
            mem += str(x * 2) + "\n"
        i += 1
        mem += str(x) + "\n"
        if time.time() - start_time > 5:
            x = "FUCK YOU"
            return x, i, mem, hi

    return x, i, mem, hi


def roll(bot, update, args):
    if not args:
        update.message.reply_text("Rolls a random number. Usage: /roll [number] (between 0 and [number], or /roll "
                                  "[number] / [number]")
    elif len(args) == 2 or len(args) > 4:
        update.message.reply_text("Usage: /roll [number] (between 0 and [number], or /roll "
                                  "[number] / [number]")
    elif "/" in args:
        slash = args.index("/")
        x = (args[slash-1])
        y = (args[slash+1])

        try:
            x = int(x)
            y = int(y)
            update.message.reply_text(randrange(x, y))
        except ValueError:
            update.message.reply_text("Usage: /roll [number] (between 0 and [number], or /roll "
                                      "[number] / [number]")
    elif len(args) == 1:
        try:
            update.message.reply_text(randrange(int(args[0])+1))
        except ValueError:
            update.message.reply_text("Usage: /roll [number] (between 0 and [number], or /roll "
                                      "[number] / [number]")



@run_async
def lychrel(bot, update, args):
    if not args:
        update.message.reply_text("Usage: /lychrel [Number] or /lychrel info for explaination")
    elif args[0] == "info":
        update.message.reply_text(
            "A Lychrel number is a natural number that cannot form a palindrome through the iterative process of repeat"
            "edly reversing its digits and adding the resulting numbers. This process is sometimes called the 196-algor"
            "ithm, after the most famous number associated with the process. In base ten, no Lychrel numbers have been "
            "yet proved to exist, but many, including 196, are suspected on heuristic and statistical grounds. The name"
            " \"Lychrel\" was coined by Wade Van Landingham as a rough anagram of Cheryl, his girlfriend's first name.T"
            "ry to find a value that disproves the conjecture!")
    else:
        start_time = time.time()
        try:
            x = int(args[0])
            i = 0
            mem = args[0] + "\n"
            while str(x) != str(x)[::-1] and i < 200:
                x = int(x) + int(str(x)[::-1])
                i += 1
            update.message.reply_text("Your final number is a palindrome! Or you reached the max number of iterations."
                                      "\nFinal number: "+str(x)+"\nIterations:"+str(i)+"\nThat took " +
                                      str(time.time() - start_time) + "s to execute."
                                      "\nIf your number isnt a palindrome yet and you wish to continue, just use the "
                                      "command again with your final number as input."
                                      "\nIf it gets like, super fucking big, the bot won't be able to reply.")
        except ValueError:
            update.message.reply_text("That's not a positive integer")


@run_async
def happy(bot, update, args):
    if not args:
        update.message.reply_text("Usage: /happy [Number] or /happy info for explaination")
    elif args[0] == "info":
        update.message.reply_text("A happy number is defined by the following process: Starting with any positive integ"
                                  "er, replace the number by the sum of the squares of its digits in base-ten, and repe"
                                  "at the process until the number either equals 1 (where it will stay), or it loops en"
                                  "dlessly in a cycle that does not include 1. Those numbers for which this process end"
                                  "s in 1 are happy numbers, while those that do not end in 1 are unhappy numbers (or s"
                                  "ad numbers).")
    else:
        start_time = time.time()
        if not args[0].isdigit():
            update.message.reply_text("That's not even a number what fuck!!!")
        if ishappy(args[0], start_time):
            update.message.reply_text("Yes!!! "+args[0]+" is a happy number!!")
        else:
            update.message.reply_text("Your number is unhappy :(")


def ishappy(x, start_time):
    i = 0
    while x != 1 and i < 200 and x != 4:
        x = sum(int(i)**2 for i in str(x))
        i = + 1
        if time.time() - start_time > 5:
            return False
    if x == 1:
        return True
    if x == 4:
        return False


# on-trigger
#Fucking awful, working on it
def imperial_scan(bot, update):

    message = update.message.text
    matches = re.findall(r'([+\-])?(\d+([.,]\d+)?)\s?(\'|"|feet|miles|ft|F|inches|in|mi|pounds|lbs)(?!\w)', message,
                         re.I)
    resultlist = []
    if len(matches) > 0:
        for i in matches:
            num = i[0] + i[1]
            result = ""
            if i[3] in ("\"", "inches", "in"):
                result = int(num) * 2.54
                result = str("{:1.2f}".format(result)) + "cm"
            if i[3] in ("\'", "feet", "ft"):
                result = int(num) * 30.48
                result = str("{:1.2f}".format(result)) + "cm"
            if i[3] == "F":
                result = (int(num) - 32) * 1.80
                result = str("{:1.2f}".format(result)) + "C"
            if i[3] in ("miles", "mi"):
                result = int(num) * 1.60
                result = str("{:1.2f}".format(result)) + "Km"
            if i[3] in ("lbs", "pounds"):
                result = int(num) * 0.45
                result = str("{:1.2f}".format(result)) + "Kg"
                print("ok")
            resultlist.append(result)

        if len(matches) > 1:
            update.message.reply_text("By the way that's " + ', '.join(resultlist) + ".")
        else:
            update.message.reply_text("By the way that's " + resultlist[0])


# Gay shit
@run_async
def info(bot, update):
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds=uptime_seconds))
    update.message.reply_text("I am RaphE's own bot, running on a raspbi model B \n"
                              "Uptime: "+uptime_string[:-7] +
                              "\n Im made of Python and you can personally check my horrible code at " \
                              "https://github.com/RaphyJake/aiwaifubot !!!!!")


@run_async
def helpme(bot, update, args):
    try:
        command = "".join(args).replace("/", "")
    except:
        command = args[0]
    commanddict = {"start": "Self explaintory.",
                   "help": "Helpception.",
                   "8ball": "Accurate fortune teller. Usage: /8ball [question]",
                   "fortune": "Another accurate fortune teller, but with no question needed!",
                   "dev": "Hot singles in your area",
                   "fullw": "converts your text into full-width version for extra aestethicc",
                   "secret": "Other command which lack of an help page:\n/ping\n/collatz\n/debug",
                   "happy": "Check if number is happy or not",
                   "collatz": "Collatz conjecture!!!!"
                   }

    try:
        update.message.reply_text(commanddict[command])
    except:
        update.message.reply_text("Memes\n"
                                  "Write /help [command] for syntax. \n Commands: \n/start \n/help \n"
                                  "/8ball\n/fortune\n/dev\n/fullw\n/lychrel\n/collatz\n/happy")


@run_async
def start(bot, update):
    update.message.reply_text("Hi I am raphys own testing bot yuo can abuse and try to exploit me all of that is "
                              "welcomed")


@run_async
def dev(bot, update, args):
    if not args:
        update.message.reply_text("Usage: /dev [Your complaints, compliments regarding the bot or death threats.]"
                                  "It's totally anonymous, trust me!")
    else:
        stuff = " ".join(args)
        bot.send_message(chat_id=data['errorid'], text=(data['username'] + ", someone said: \n" + stuff))


@run_async
def ping(bot, update):
    update.message.reply_text("Pong")


def error(bot, update, error):
    errr = ('Update "%s" caused error "%s"' % (update, error))
    logger.warning(errr)
    bot.send_message(chat_id=data['errorid'], text=errr)


def restart(bot, update):

    if update.effective_user["id"] == data['id']:
        bot.send_message(update.message.chat_id, "Bot is restarting...")
        time.sleep(0.2)
        os.execl(sys.executable, sys.executable, *sys.argv)


def debug(bot, update, args, chat_data, user_data):
    update.message.reply_text('You said "' + (''.join(args)) + '", message lenght is ' + str(len((''.join(args)))))
    update.message.reply_text(str(update.effective_user))
    update.message.reply_text(str(update.effective_chat))


def unknown(bot, update):
    if update.effective_chat["type"] == "private":
        bot.send_message(chat_id=update.message.chat_id, text="What fuck??")


def workingon(bot, update):
    update.message.reply_text("Working on it, sorry :( Use /dev to get in touch, it's anonymous but you can send me"
                              " contact information")


def printsettings(bot, update):
    update.message.reply_text(str(data['id']))


def main():

    # Edit the bot.json file accordingly.
    global data
    try:
        data = json.load(open(os.path.dirname(__file__) + '/bot.json'))
    except FileNotFoundError:
        print("bot.json wasn't found, aborting.")
        exit(0)
    token = data['token']


    updater = Updater(token)

    dp = updater.dispatcher

    dp.add_error_handler(error)

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", helpme, pass_args=True))
    dp.add_handler(CommandHandler("8ball", ball, pass_args=True))
    dp.add_handler(CommandHandler("fullw", fullw, pass_args=True))
    dp.add_handler(CommandHandler("info", info))
    dp.add_handler(CommandHandler("fortune", fortune))
    dp.add_handler(CommandHandler("ping", ping))
    dp.add_handler(CommandHandler("r", restart))
    dp.add_handler(CommandHandler("roll", roll, pass_args=True))
    dp.add_handler(CommandHandler("dev", dev, pass_args=True))
    dp.add_handler(CommandHandler("collatz", collatz, pass_args=True))
    dp.add_handler(CommandHandler("lychrel", lychrel, pass_args=True))
    dp.add_handler(CommandHandler("happy", happy, pass_args=True))
    dp.add_handler(CommandHandler("json", printsettings))
    dp.add_handler(CommandHandler("debug", debug, pass_args=True, pass_user_data=True, pass_chat_data=True))
    if data['imperial_scan'] == "True":
        dp.add_handler(MessageHandler(Filters.text, imperial_scan))
    dp.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling(clean=True)

    updater.idle()


if __name__ == '__main__':
    main()
