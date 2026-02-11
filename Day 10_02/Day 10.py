from deep_translator import GoogleTranslator

translated = GoogleTranslator(source='en', target='hi'.translate("good morning"))
print(translated)