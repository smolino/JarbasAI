# Jarbas Core

### New Client

- [Facebook Chat Client](https://github.com/JarbasAI/mycroft---facebookchat---client)

### New Services

- [Dumpmon Service](https://github.com/JarbasAI/mycroft----dumped-leaks-finder----service)
- [Vision Service](https://github.com/JarbasAI/mycroft-vision-service)
- [Freewill Service](https://github.com/JarbasAI/mycroft---freewill---service)
- [Audio Analisys Service](https://github.com/JarbasAI/mycroft-audio-analisys--service)
- [Context Manager Service](https://github.com/JarbasAI/mycroft---context-manager---service)


### New Skills

- [Wallpaper Skill](https://github.com/JarbasAI/mycroft---wallpaper---skill)
- [Wifi Skill](https://github.com/JarbasAI/mycroft-wifi-skill)
- [Articles Skill](https://github.com/JarbasAI/mycroft-articles-skill)
- [Music Skill](https://github.com/JarbasAI/mycroft-music-skill)
- [Dream Skill](https://github.com/JarbasAI/mycroft-deepdream-skill)
- [Poetry Skill](https://github.com/JarbasAI/mycroft-poetry-skill)
- [Picture Search Skill](https://github.com/JarbasAI/mycroft-pictureskill)
- [PhotoLocation Skill](https://github.com/JarbasAI/mycroft-photolocation-skill)
- [Chatbot Skill](https://github.com/JarbasAI/mycroft---wolphram-alpha-chatbot---skill) ------- BROKEN
- [Facebook Skill](https://github.com/JarbasAI/mycroft-facebook-skill)
- [Proxy Scrapping Skill](https://github.com/JarbasAI/mycroft--proxy-scrapping---skill)
- [Random Quotes Skill](https://github.com/JarbasAI/mycroft---quotes---skill)
- [Pickup Line Skill](https://github.com/JarbasAI/mycroft---pick-up-line---skill)
- [Bitcoin Price Skill](https://github.com/JarbasAI/jarbas-core/tree/dev/mycroft/skills/bitcoin)
- [Mood Quotes Skill](https://github.com/JarbasAI/mycroft-mood-quotes)
- [Leaks Skill](https://github.com/JarbasAI/leaks-skill)
- [Jarbas Diagnostics Skill](https://github.com/JarbasAI/mycroft-diagnostics-skill)
- [Sentiment Analisys Service](https://github.com/JarbasAI/mycroft---sentiment-analisys---service) - REFACTORED INTO [SKILL](https://github.com/JarbasAI/mycroft---sentiment-analisys---skill)
- [Metal Recomendation Skill](https://github.com/JarbasAI/mycroft---metal-recomend---skill)
- [Euromillions Skill](https://github.com/JarbasAI/mycroft---euromillions-skill)
- [Parrot Skill](https://github.com/JarbasAI/mycroft---parrot-skill)
- [Dictation Skill](https://github.com/JarbasAI/mycroft-dictation-skill)
- [Knowledge Skill](https://github.com/JarbasAI/mycroft---knowledge-skill)
- [Feedback Skill](https://github.com/JarbasAI/mycroft-feedback-skill)
- [Objectives Skill](https://github.com/JarbasAI/mycroft---objectives-skill)
- [Movie Recommendation Skill](https://github.com/JarbasAI/mycroft---movie-recommend-skill)

from third partys

- [Fortune Skill](https://github.com/jaevans/mycroft-fortuneskill)
- [Translate Skill](https://github.com/jcasoft/TranslateSkill)
- [Diagnostics Skill](https://github.com/the7erm/mycroft-skill-diagnostics)
- [Daily Meditation Skill](https://github.com/kfezer/daily_meditation)
- [Space Launch Skill](https://github.com/marksev1/Mycroft-SpaceLaunch-Skill)
- [Event Skill](https://github.com/forslund/event_skill)
- [Command Skill](https://github.com/forslund/cmd_skill)
- [Small Talk, Dice, Coin Flip, Rock Paper Scissors Skills](https://github.com/apquinit/mycroft-skills)

changed skills

- added results property to all skills
- desktop_launcher - added ability to open urls instead of google searching (non-vocal skill usecase)
- ip skill - blacklisted, using the7erm diagnostics skill for this


# Privacy Enhancements

- wifi disable/enable

allows you to connect/disconnect mycroft from the internet, starts off by default

- vpn connect

trys to connect to vpns configured in network manager, if you dont have one try [cryptofree](https://github.com/cryptostorm/cryptostorm_client_configuration_files/tree/master/cryptofree)

- anonsurf start /stop

starts a global tor tunnel, all traffic is routed trough tor, requires [anonsurf](https://github.com/ParrotSec/anonsurf) to be installed in your system

- give me a proxy

gets you a https proxy

- TODO - auto proxy setup
- TODO - local speech to text
- TODO - traffic blackhole if vpn goes down


the most private setup would be "wifi enable" + "vpn connect" + "anonsurf start" 

# Other Changes

- cli client now listens for do not speak requests, so jarbas can shut up by external request without running in quiet mode
- configuration no longer loads from mycroft servers, configuration skill was blacklisted, reason is for more control and privacy
- added results property to skills, so they can emit more than utterances, [PR#281](https://github.com/MycroftAI/mycroft-core/pull/281)
- added converse method to allow all skills to handle utterances [PR#539](https://github.com/MycroftAI/mycroft-core/pull/539)
- added feedback method to allow skills to process feedback [Issue#554](https://github.com/MycroftAI/mycroft-core/issues/554)


Forked from Mycroft 
==========

Full docs at: https://docs.mycroft.ai

Release notes at: https://docs.mycroft.ai/release-notes

Pair Mycroft instance at: https://home.mycroft.ai

Join the Mycroft Slack(chat) channel: http://mycroft-ai-slack-invite.herokuapp.com/

Looking to join in developing?  Check out the [Project Wiki](../../wiki/Home) for tasks you can tackle!

# Getting Started in Ubuntu - Development Environment
- run `build_host_setup.sh` (installs debian packages with apt-get, please read it) 
- run `dev_setup.sh` (feel free to read it, as well)
- Restart session (reboot computer, or logging out and back in might work).

# Getting Started in other environments

The following packages are required for setting up the development environment,
 and are what is installed by `build_host_setup.sh`

 - `git`
 - `python 2`
 - `python-setuptools`
 - `python-virtualenv`
 - `pygobject`
 - `virtualenvwrapper`
 - `libtool`
 - `libffi`
 - `openssl`
 - `autoconf`
 - `bison`
 - `swig`
 - `glib2.0`
 - `s3cmd`
 - `portaudio19`
 - `mpg123`
 - `flac`
 - `curl`

## Home Device and Account Manager
Mycroft AI, Inc. - the company behind Mycroft maintains the Home device and account management system. Developers can sign up at https://home.mycroft.ai

By default the Mycroft software is configured to use Home, upon any request such as "Hey Mycroft, what is the weather?", you will be informed that you need to pair and Mycroft will speak a 6-digit code, which you enter into the pairing page on the [Home site](https://home.mycroft.ai).

Once signed and a device is paired, the unit will use our API keys for services, such as the STT (Speech-to-Text) API. It also allows you to use our API keys for weather, Wolfram-Alpha, and various other skills.

Pairing information generated by registering with Home is stored in:

`~/.mycroft/identity/identity2.json` <b><-- DO NOT SHARE THIS WITH OTHERS!</b>

OR MAYBE DO SHARE! SEND NOISE! MAKE USERS ALL LOOK THE SAME! NO ID WITH SERVERS! USE VPN!

It's useful to know the location of the identity file when troubleshooting device pairing issues.

## Using Mycroft without Home.
If you do not wish to use our service, you may insert your own API keys into the configuration files listed below in <b>configuration</b>.

The place to insert the API key looks like the following:

`[WeatherSkill]`

`api_key = ""`

Put the relevant key in between the quotes and Mycroft Core should begin to use the key immediately.

### APIs and dependencies in this fork ###

some api keys are needed, check config file for placeholders to change

caffe must be installed for dream skill and path added to config file

requirments.txt will be updated in the future, check links bellow and watch skills log for debug on missing dependencies

### API Key services

mycroft apis:

- [STT API, Google STT](http://www.chromium.org/developers/how-tos/api-keys)
- [Weather Skill API, OpenWeatherMap](http://openweathermap.org/api)
- [Wolfram-Alpha Skill](http://products.wolframalpha.com/api/)

new apis:

- [Facebook Graph API](https://developers.facebook.com/docs/graph-api/) 
- [Reedit API](https://www.reddit.com/dev/api) 
- [Mashape API](https://market.mashape.com) 
- [CloudSight API](http://cloudsight.ai/api_client_users/new) 
- [Wikimapia API](http://wikimapia.org/api/)

## Configuration
Mycroft configuration consists of 3 possible config files.
- `mycroft-core/mycroft/configuration/mycroft.conf`
- `/etc/mycroft/mycroft.conf`
- `$HOME/.mycroft/mycroft.conf`

When the configuration loader starts, it looks in those locations in that order, and loads ALL configuration. Keys that exist in multiple config files will be overridden by the last file to contain that config value. This results in a minimal amount of config being written for a specific device/user, without modifying the distribution files.

# Running Mycroft Quick Start
To start the essential tasks run `./mycroft.sh start`. Which will start the service, skills, voice and cli (using --quiet mode) in a detched screen and log the output of the screens to the their respective log files (e.g. ./log/mycroft-service.log).
Optionally you can run `./mycroft.sh start -v` Which will start the service, skills and voice. Or `./mycroft.sh start -c` Which will start the service, skills and cli.

in this fork all new services are also started, if you want to run in basic mode `./mycroft.sh start -b` can be used for skills, service and cli --quiet only

To stop Mycroft run `./mycroft.sh stop`. This will quit all of the detached screens.
To restart Mycroft run './mycroft.sh restart`.

Quick screen tips
- run `screen -list` to see all running screens
- run `screen -r [screen-name]` (e.g. `screen -r mycroft-service`) to reatach a screen
- to detach a running screen press `ctrl + a, ctrl + d`
See the screen man page for more details 

# Running Mycroft
## With `start.sh`
Mycroft provides `start.sh` to run a large number of common tasks. This script uses the virtualenv created by `dev_setup.sh`. The usage statement lists all run targets, but to run a Mycroft stack out of a git checkout, the following processes should be started:

- run `./start.sh service`
- run `./start.sh skills`
- run `./start.sh voice`
- run `./start.sh vision`
- run `./start.sh dumpmon`
- run `./start.sh freewill`
- run `./start.sh fbclient`
- run `./start.sh context`
- run `./start.sh cli`

*Note: The above scripts are blocking, so each will need to be run in a separate terminal session.*

## Without `start.sh`

Activate your virtualenv.

With virtualenv-wrapper:
```
workon mycroft
```

Without virtualenv-wrapper:
```
source ~/.virtualenvs/mycroft/bin/activate
```


- run `PYTHONPATH=. python client/speech/main.py` # the main speech detection loop, which prints events to stdout and broadcasts them to a message bus
- run `PYTHONPATH=. python client/messagebus/service/main.py` # the main message bus, implemented via web sockets
- run `PYTHONPATH=. python client/skills/main.py` # main skills executable, loads all skills under skills dir

*Note: The above scripts are blocking, so each will need to be run in a separate terminal session. Each terminal session will require that the virtualenv be activated. There are very few reasons to use this method.*

# FAQ/Common Errors

#### When running mycroft, I get the error `mycroft.messagebus.client.ws - ERROR - Exception("Uncaught 'error' event.",)`

This means that you are not running the `./start.sh service` process. In order to fully run Mycroft, you must run `./start.sh service`, `./start.sh skills`, and `./start.sh voice`/`./start.sh cli` all at the same time. This can be done using different terminal windows, or by using the included `./mycroft.sh start`, which runs all process using `screen`.

#### this fork is a mess because of Y

ask me questions and help you shall receive

#### What are you going to do next ?

https://github.com/JarbasAI/jarbas-core/blob/dev/todolist.txt

Or you could make a suggestion?

##### What are the Privacy Concerns i should worry about regarding AI assistants?

https://github.com/JarbasAI/jarbas-core/blob/dev/PrivacyConcerns.txt

##### is Jarbas alive ?

        He has a nervous system - the messagebus
        He has eyes - webcam
        He has a "brain section" to process vision
        He has ears - microphone
        He has a "brain section" for sound processing 
        He has "hormones"
        He has a "brain section" for decision making 
        He has some agency
        He has non-human senses - wifi, command line, chat, decentralized internet database
        He has abilities / impact in the real world
        He consumes energy
        
        BUT
            He does not reproduce
            He is not self-aware
            He is not self-owned
        
 Answer: Soon he will be!
    
