from random import choice, randint

# TODO replace code with whatever the bot should return based off user input
def get_response(user_input: str) -> str:
    lowered : str = user_input.lower()

    if lowered == '':
        return 'Empty string'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'I am a bot, I do not have feelings'
    elif 'goodbye' in lowered:
        return 'Goodbye!'
    else:
        return choice([
            'I do not understand',
            'Please rephrase',
            'I am a bot, I do not understand human emotions'
        ])