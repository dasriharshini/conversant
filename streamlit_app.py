import cohere
import conversant

co = cohere.Client("YOUR_API_KEY_HERE")
bot = conversant.PromptChatbot.from_persona("fantasy-wizard", client=co)
print(bot.reply("Hello!"))
