import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "11803287")

API_HASH = os.environ.get("API_HASH", "3e4675d0f6f9b23b9872c45188d274c7")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6034388899:AAEOsIApiqXy-Ki8cgke3emVNSiinCx13Jo") 

FORCE_SUB = os.environ.get("FORCE_SUB", "A_F_MOVIES") 

DB_NAME = os.environ.get("DB_NAME","Cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://aflahk80:aflah12345@cluster0.h7rhn.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/AF-THE-RENAMER-04-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '1814803065').split()]

PORT = os.environ.get("PORT", "8080")

LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001593625135"))
