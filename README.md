bashPhone
=========
 
	 ------------------------------------------------------------------------------
	|  _______________________________                                             │
	│ /                               \                                            │
	│|                                 |        +-------------------+              │
	│| [`````] [`````] [`````] [`````] |        | BASHPHONE APPS    |              │
	│| [  B  ] [  A  ] [  S  ] [  H  ] |        |___________________|              │
	│| [_____] [_____] [_____] [_____] |        |Type|     ...to run|              │
	│|                                 |        |-------------------|              │
	│| [`````] [`````] [`````] [`````] |        | B | BBC News      |              │
	│| [ PH  ] [  O  ] [  N  ] [  E  ] |        | n | New York Times|              │
	│| [_____] [_____] [_____] [_____] |        | f | Fortune       |              │
	│|                                 |        | b | Blackjack     |              │
	│| [`````] [`````] [`````] [`````] |        | s | Spotify       |              │
	│| [BBC  ] [NY   ] [Fort-] [Black] |        | w | Weather       |              │
	│| [News_] [Times] [__une] [Jack_] |        | c | Calendar      |              │
	│|                                 |        | t | Today's ToDo's|              │
	│| [`````] [`````] [`````] [`````] |        | q | Quit          |              │
	│| [Sptfy] [Wthr ] [ Cal ] [ToDo ] |        +-------------------+              │
	│| [_____] [_____] [_____] [_____] |                                           │
	│|                                 |                                           │
	│|                ([])             |                                           │
	│|                                 |                                           │
	│ \_______________________________/                                            |
	--------------------------------------------------------------------------------

This is an in-development ascii art implementation of iphone-like "apps" for Bash. In other words, this program is meant to emulate a smartphone with apps. The apps are all bash scripts/aliases. Future plans include creating ability to add or remove "apps" or create your own.

Installation
===================
** Note: This is an alpha. Future plans include an install file.*

**1.**  Download bashphone.py and put it somewhere (doesn't matter!). Edit your bash profile (instructions for doing it with the OS X terminal editor nano are below, but you could also use sublimetext, atom, etc). Add an alias to launch bashphone using the nano text editor (or editor of your choice). The alias bashphone line can be anywhere in your .bash-profile file. Of course, replace path/to with the path to the location of the downloaded bashphone.py file.

    cd
    nano .bash_profile
    alias bashphone="python ~/path/to/bashphone.py

**2.**  Some of the Bashphone apps are really just command line shell scripts, others are downloaded packages, and others are python scripts. If you want the same ones I have currently, you need to download or install them yourself. Some require [Homebrew](http://brew.sh/) package manager to install.

* [Blackjack](https://github.com/michaelrbock/blackjack) python command line game.
* [Mopidy](https://docs.mopidy.com/en/latest/installation/osx/) and [Spotify](https://github.com/mopidy/mopidy-spotify) python programs (to play Spotify music with a premium account).
* Google Command Line tools (via Brew or [github](https://github.com/Homebrew/homebrew/blob/master/Library/Formula/googlecl.rb))
* [Fortune](https://github.com/guivinicius/fortune-api) and [Cowsay](https://gist.github.com/evnm/1308428) via Brew.

**3.**  Create your own "apps" by writing your own aliases and editing the python program. At some point I'll post these programs too. Would be nice to turn these into installable "apps."
 
To Do
=====
*  ability to install and deinstall "apps" scripts
*  Need to find/write more programs!
*  Find better weather and news clippers.
