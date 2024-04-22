from characterai import PyCAI

# Initialisierung der beiden Chatbot-Instanzen
client1 = PyCAI('API Key')  # Bot 1
client2 = PyCAI('API Key')  # Bot 2 (API-Key für Bot 2 hier einfügen)

def talkWithBot(message, bot_choice):
    # Bestimmen des ausgewählten Bots
    if bot_choice == 1:
        bot = client1
        char = 'PI-yy9XtEhZ-UfUcMtYpE2Z52z0rWcjOBsme3CyF3Fc'  # ID für Bot 1
    elif bot_choice == 0:
        bot = client2
        char = '9ERZhJWq-Yea6Olx9ChRZJGR5CNt8cnbLe-mclZav9g'  # ID für Bot 2 hier einfügen
    else:
        return "Ungültige Bot-Auswahl!"

    # Abrufen des Chatobjekts für den entsprechenden Bot
    chat = bot.chat.get_chat(char)

    # Bestimmen des Ziels (menschlicher Teilnehmer im Chat)
    participants = chat['participants']
    if not participants[0]['is_human']:
        tgt = participants[0]['user']['username']
    else:
        tgt = participants[1]['user']['username']

    # Senden der Nachricht an den Chat
    data = bot.chat.send_message(
        chat['external_id'], tgt, message
    )

    # Extrahieren der Antwort des Bots
    text = data['replies'][0]['text']

    return text

