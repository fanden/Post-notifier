
import requests
import time
import playsound
  
URL= "https://sporing.posten.no/tracking/api/fetch/"
sporingsNummer = ""
notifyOption = False

def update() :    
    r= requests.get(url = URL + sporingsNummer)
    data = r.json()
    currentStatus = data['consignmentSet'][0]['packageSet'][0]['eventSet'][0]['status']
    lastChange = data['consignmentSet'][0]['packageSet'][0]['eventSet'][0]['displayTime']
    startChange = lastChange
    print('Status: ' + currentStatus)
    print('Sist endret: ' + lastChange)

    if startChange == lastChange:
        return False

    if startChange != lastChange & notifyOption == True:
        playsound('notify.wav')
        return True


contValue = True

while(contValue):
    update()
    time.sleep(300)
