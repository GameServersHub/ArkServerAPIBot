# This takes advantage of the hikari framework to rapidly create modern discord bots using modern framework. https://github.com/hikari-py/hikari/
import hikari
# This takes advantage of the lightbulb framework to rapidly create modern discord bots using modern framework. https://github.com/tandemdude/hikari-lightbulb
import lightbulb
# This allows us to grab the data from inside the config.json file
import yaml

config = yaml.safe_load(open("GameServersHub/configuration.yml"))

# This line of code simply allows the bot to initiate by reading the bot token and slash prefix.
bot = lightbulb.BotApp(token=f"{config}", prefix="/")

# This section creates the commands needed for the bot to operate and function.
@bot.command
@lightbulb.command("setchannel", "Please enter your channel ID here this will auto generate updates inside that channel.")
@lightbulb.option(name="resourceid", description="Please enter the full resourceID into this option field. Example: ark-server-api.12", required=True)
@lightbulb.implements(lightbulb.SlashCommand)

async def ping(ctx: lightbulb.Context) -> None:
    # This creates a variable that can be referenced in other files on what choice the discord user choose when selecting the resource id name.
    userChoice = ctx.options.resourceid
    await ctx.respond("Pong!")

    # This creates a global variable that will be used inside the api file.
    def globalUserChoice():
        userChoice
    globalUserChoice()

# This is the ending line that tells the bot to run the code listed above.
# The code inside the bot run tells the bot to play a activity message.
bot.run(
    activity=hikari.Activity(
        name="Join GameServersHub.com",
        type=hikari.ActivityType.LISTENING
    )
)