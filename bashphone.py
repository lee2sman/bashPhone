#!/usr/bin/env python

from os import system
import curses

def get_param(prompt_string):
    screen.clear()
    screen.border(0)
    screen.addstr(2, 2, prompt_string)
    screen.refresh()
    input = screen.getstr(10, 10, 60)
    return input

def execute_cmd(cmd_string):
    system("clear")
    a = system(cmd_string)
    print ""
    if a != 0:
        print "Command terminated with error"
    raw_input("Press enter")
x = 0

while x != ord('4'):
    screen = curses.initscr()
    screen.clear()
    screen.border(0)
    screen.addstr(1, 1, "  _______________________________")
    screen.addstr(2, 1, " /                               \ ")
    screen.addstr(3, 1, "|                                 |        +-------------------+")
    screen.addstr(4, 1, "| [`````] [`````] [`````] [`````] |        | BASHPHONE APPS    |")
    screen.addstr(5, 1, "| [  B  ] [  A  ] [  S  ] [  H  ] |        |___________________|")
    screen.addstr(6, 1, "| [_____] [_____] [_____] [_____] |        |Type|     ...to run|")
    screen.addstr(7, 1, "|                                 |        |-------------------|")
    screen.addstr(8, 1, "| [`````] [`````] [`````] [`````] |        | B | BBC News      |")
    screen.addstr(9, 1, "| [ PH  ] [  O  ] [  N  ] [  E  ] |        | n | New York Times|")
    screen.addstr(10, 1, "| [_____] [_____] [_____] [_____] |        | f | Fortune       |")
    screen.addstr(11, 1, "|                                 |        | b | Blackjack     |")
    screen.addstr(12, 1, "| [`````] [`````] [`````] [`````] |        | s | Spotify       |")
    screen.addstr(13, 1, "| [BBC  ] [NY   ] [Fort-] [Black] |        | w | Weather       |")
    screen.addstr(14, 1, "| [News_] [Times] [__une] [Jack_] |        | c | Calendar      |")
    screen.addstr(15, 1, "|                                 |        | t | Today's ToDo's|")
    screen.addstr(16, 1, "| [`````] [`````] [`````] [`````] |        | q | Quit          |")
    screen.addstr(17, 1, "| [Sptfy] [Wthr ] [ Cal ] [ToDo ] |        +-------------------+")
    screen.addstr(18, 1, "| [_____] [_____] [_____] [_____] | ")
    screen.addstr(19, 1, "|                                 | ")
    screen.addstr(19, 1, "|                                 | ")
    screen.addstr(20, 1, "|                ([])             | ")
    screen.addstr(21, 1, "|                                 | ")
    screen.addstr(22, 1, " \_______________________________/")
    screen.refresh()
    x = screen.getch()
    if x == ord("q"): break
    elif x == ord('B'):
        curses.endwin()
        execute_cmd("lynx -term=vt100 http://news.bbc.co.uk/text_only.stm")
    elif x == ord('n'):
        curses.endwin()
        execute_cmd("lynx -term=vt100 http://nytimes.com/pages/todayspaper/index.html#nytfrontpage")
    elif x == ord('f'):
        curses.endwin()
        execute_cmd("fortune | cowsay")
    elif x == ord('b'):
        curses.endwin()
        execute_cmd("python ~/Documents/pythonprograms/blackjack.py")
    elif x == ord('s'):
        curses.endwin()
        execute_cmd("ncmpcpp")
    elif x == ord('w'):
        curses.endwin()
        execute_cmd("lynx -dump -term=vt100 https://weather.yahoo.com/united-states/pennsylvania/philadelphia-12765511/")
    elif x == ord('c'):
        curses.endwin()
        execute_cmd("google calendar list | less -FX")
    elif x == ord('l'):
        curses.endwin()
        execute_cmd("sl")
    elif x == ord('t'):
        curses.endwin()
        execute_cmd("google calendar list --date today")
curses.endwin()
execute_cmd("clear")
