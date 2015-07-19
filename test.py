import os
import time
import logging

def find_config():
    config_path = 'config.json'
    if os.path.exists(config_path):
        return config_path
    config_path = os.path.join(os.path.dirname(__file__), '../', 'config.json')
    if os.path.exists(config_path):
        return config_path
    return None


config_path = find_config()
while True:
          time.sleep(3)
          logging.error(os.path.abspath('.'))
          logging.error( os.path.dirname(__file__))
          logging.error(config_path)
