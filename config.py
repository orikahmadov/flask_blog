"""Configuration of the app are defined here """

# Statement for enabling the development environment
DEBUG = True

#File Upload Folder
UPLOAD_PATH = "app/static"


# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Define the database - we are working with
# SQLite for this example
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db' + '?check_same_thread=False')
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = True
# Application threads. A common general assumption is
# using 2 per available processor cores - to handle
# incoming requests using one and performing background
# operations using the other.
# THREADS_PER_PAGE = 2

# Enable protection agains *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED     = True

# Use a secure, unique and absolutely secret key for
# signing the data.
#use import secrets and secrets.token_hex(16)
CSRF_SESSION_KEY = "fc8499fe398d1204c796cd57688d36e3"
# Secret key for signing cookies
SECRET_KEY = "48038481696c0cb7cf51dec8eb820c1f"
RECAPTCHA_PUBLIC_KEY  ='6LctD3AaAAAAAJxle81ia1KTIk56oC5D9sNLlajs'
RECAPTCHA_PRIVATE_KEY ='6LctD3AaAAAAAEIDtSw6-ziNCumu9gcXnRV-7QrZ'

#Flask Debugger Configurations
DEBUG_TB_ENABLED = True
DEBUG_TB_INTERCEPT_REDIRECTS = False
DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True

#Email Config
MAIL_HOSTNAME = "localhost Hostname or IP address of the email server" #Default Localhost
MAIL_PORT = 25  #Default 25
MAIL_SERVER = "smtp.googlemail.com"
MAIL_USE_TLS = False #False by Default
MAIL_USE_SSL = False #False by Default
MAIL_USERNAME = None #None by default
MAIL_PASSWORD = None #None by default