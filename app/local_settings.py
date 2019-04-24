import os

# DO NOT use "DEBUG = True" in production environments
DEBUG = True

# DO NOT use Unsecure Secrets in production environments
# Generate a safe one with:
#     python -c "from __future__ import print_function; import string; import random; print(''.join([random.choice(string.ascii_letters + string.digits + string.punctuation) for x in range(24)]));"
SECRET_KEY = 'This is an UNSECURE Secret. CHANGE THIS for production environments.'