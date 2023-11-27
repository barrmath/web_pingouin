from dotenv import load_dotenv
import os

load_dotenv()

#recup clé secrete dans un fichier .env
SECRET_KEY = os.getenv("SECRET_KEY")
type_server = os.getenv("type_server")