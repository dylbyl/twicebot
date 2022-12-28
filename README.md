Deployed to fly.io via instructions [here](https://jonahlawrence.hashnode.dev/hosting-a-python-discord-bot-for-free-with-flyio)

To add to the bot:
- Clone this repo
- Install flyctl in your CLI: `curl -L https://fly.io/install.sh | sh`
- Run `flyctl auth signup` and/or `flyctl auth login` to sign up for fly.io or login (this is using Dyl's account, so he may need to log in for you)
- Run `flyctl deploy` to deploy the app from your machine
- Make sure to push to GitHub if you make changes!

What I did for first-time setup, for future reference:
- Clone this repo
- Install flyctl in your CLI: `curl -L https://fly.io/install.sh | sh`
- Run `flyctl auth signup` and/or `flyctl auth login` to sign up for fly.io or login (this is using Dyl's account, so he may need to log in for you)
- Create a `Dockerfile` with the following:
```
FROM python:3.10
WORKDIR /bot
COPY requirements.txt /bot/
RUN pip install -r requirements.txt
COPY . /bot
CMD python bot.py
```
- NOT NEEDED UNLESS DOING FROM SCRATCH: Run `flyctl launch` - Creates a `fly.toml` file telling Fly how to deploy the app.
- Set secrets with `flyctl secrets set DISCORD_TOKEN=My.TOken.3213.example DISCORD_GUILD=1234567890`
- Run `flyctl deploy` to deploy the app from your machine
- Make sure to push to GitHub if you make changes!
	- I had to set `discord.py` version to 1.7.3 to avoid an error I was having during deployment. I don't know enough about Python or Discord bots to properly debug rn