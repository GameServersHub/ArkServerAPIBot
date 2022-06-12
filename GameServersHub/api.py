# This imports the "requests" python module that allows the REST API requst below to work correctly.
import requests

# This stores the websites REST API endpoint into a python readable variable
gameServersHubUrl = "https://gameservershub.com/forums/api/resource-updates/turret-filler.128/"

# This data below adds the xenforo 2 forum software requirement for header request to validate the link above.
payload={}
headers = {
  'XF-Api-Key': '6w9BT6rekqwV644v__KuxX7CBvImfW1j'
}

# Creates a variable to store the JSON formatting results into a readable variable that the discord bot can pull from and validate.
webResponse = requests.request("GET", gameServersHubUrl, headers=headers, data=payload)
