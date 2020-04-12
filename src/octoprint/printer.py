# System Imports
# import json
import random

# Framework / Library Imports
from octorest import OctoRest

# Application Imports

# Local Imports

class Printer:

    client = False

    def __init__(self, url, apikey):
        self.client = OctoRest(url=url, apikey=apikey)

    def status(self):
        try:
            job_info = self.client.job_info()
            # Can be used for testing
            # with open('api_data.json') as json_file:
            #     job_info = json.load(json_file)
            #     print(job_info)
        except RuntimeError as re:
            return 'off'

        state_text = job_info['state']
        if state_text == "Offline":
            return 'off'
        if state_text == "Operational":
            return 'idle'
        elif state_text == "Printing":
            return 'printing'
        elif state_text in ['Paused', 'Pausing']:
            return 'paused'
        elif state_text == 'Cancelling':
            return 'cancel'
        else:
            return 'other'

    def remaining(self):
        try:
            job_info = self.client.job_info()
            # Can be used for testing
            # with open('api_data.json') as json_file:
            #     job_info = json.load(json_file)
            #     print(job_info)
        except RuntimeError as re:
            return 0

        remaining = job_info['progress']['printTimeLeft']
        if remaining is None:
            print('remaining is none')
            return 0
        elif not isinstance(remaining, int):
            print('remaining is not int')
            return 1
        else:
            return remaining
