## A discord bot in a docker image.

### Creating this in a docker image
- Make a discord bot at https://discord.com/developers/applications and put your bot token in a `config.json` file.
- Build a new docker image with `docker build -t yourname/bot-name:latest .`

### Running on your machine
- Install Python 3.10
- Install required packages with `pip3 install -r requirements.txt`
- Run `main.py`