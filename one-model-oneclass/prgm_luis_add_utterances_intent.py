import os
import httplib2
import json
result = True
headers = {"Ocp-Apim-Subscription-Key": "7a59937e80dd423fa5415fdbd8289275", "Content-Type": "application/json"}
appid='406da671-5511-41de-b30c-f48911809b84'
dir=os.getcwd()
c=0
def addUtterances():
    configEntites = []
    result = True
    for file in os.listdir(dir):
        if result and file.endswith(".txt"):
                utterances = []
                intent = os.path.splitext(file)[0]
                print("Adding utterances for " + intent)
                with open(file, "r") as intentFile:
                    for example in intentFile:
                        entityLabels = []
                        utterances.append({"text": example.replace("(", "").replace(")", ""),
                                               "intentName": intent, "entityLabels": entityLabels})

                if len(utterances) > 0:
                    try:
                        print(len(utterances))
                        conn = httplib2.HTTPSConnectionWithTimeout("westus.api.cognitive.microsoft.com")

                        conn.request("POST", "/luis/api/v2.0/apps/{0}/versions/0.1/examples".format(appid), json.dumps(utterances),headers)
                        response = conn.getresponse()
                        print(response.status)
                        conn.close()
                        print(response.status)
                        result = response.status == 201
                    except Exception as e:
                        print(e)
                        result = False
    return result

addUtterances()