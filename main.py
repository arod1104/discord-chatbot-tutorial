from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response
from logger import Logger

# Step 0: Load our token from somewhere safe
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# Step 1: Bot Setup
intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

# Step 2: Message Functionality
async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Message was empty because intents were not enabled probably')
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        Logger().log_error(e)
        # await message.channel.send(f'Error: {e}')

# Step 3: Handling The Startup for our Bot
@client.event
async def on_ready() -> None:
    Logger().log(f'{client.user} is now running!')


# Step 4: Handling Incoming Messages
@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    Logger().log(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


# Step 5: Main Entry Point
def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    main()