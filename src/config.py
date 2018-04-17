# Define the application directory
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
CSRF_ENABLED = True
CSRF_SESSION_KEY = "X7T33uk#EmO6b8a3UW!RFKq8FiQC6gYcM!qSkPUj44@2iPlYepM*a*q$x8zXJse6"
SECRET_KEY = "67IqDOqpdT3HB#L7O*TmqVb14xf&hKI&x1yT22uexIU8RBgp3IlNLAnMqNvxnz*T"

UPLOAD_FOLDER = os.path.join(BASE_DIR, '/app/forecast/input'