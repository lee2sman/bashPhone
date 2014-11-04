# my bash aliases to run programs
#
# this is custom to my system!
# it won't work on yours!
# you need to configure this for your own computer!
# You do this by putting the correct path to your own programs below.

alias bashphone='cat ~/Documents/github\ projects/bashPhone/iphoneWithApps.txt'
alias blackjack="python ~/Documents/pythonprograms/blackjack.py"
alias spotify='ncmpcpp'
alias bbc='lynx -term=vt100 http://news.bbc.co.uk/text_only.stm'
alias nytimes='lynx -term=vt100 http://nytimes.com/pages/todayspaper/index.html#nytfrontpage'
alias weather='lynx -dump -term=vt100 https://weather.yahoo.com/united-states/pennsylvania/philadelphia-12765511/'
alias sked='google calendar list | less -FX'
alias today='google calendar list --date today'

# fixing the calc function
calc(){ awk "BEGIN{ print $* }" ;}
