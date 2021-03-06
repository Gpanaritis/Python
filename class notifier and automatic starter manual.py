#Nektar
import webbrowser
import datetime
import time

today = datetime.datetime.now().strftime("%A")

class Mathima:
  def __init__(self, name, link, day, starting_hour, ending_hour):
    self.name = name
    self.link = link
    self.day = day
    self.starting_hour = starting_hour
    self.ending_hour = ending_hour

list = []

#---------------------------------------------------

# ΒΑΛΕ ΕΔΩ ΜΙΑ ΓΡΑΜΜΗ ΓΙΑ ΚΑΘΕ ΜΑΘΗΜΑ ΠΟΥ ΘΕΣ ΝΑ ΚΑΝΕΙΣ ΜΕΣ ΤΗΝ ΒΔΟΜΑΔΑ
# (ΑΝ ΕΝΑ ΜΑΘΗΜΑ ΕΧΕΙΣ ΚΑΘΕ ΤΡΙΤΗ ΚΑΙ ΠΕΜΠΤΗ , ΠΡΕΠΕΙ ΝΑ ΤΟ ΒΑΛΕΙΣ 2 ΦΟΡΕΣ)
# (ΜΙΑ ΤΡΙΤΗ ΚΑΙ ΜΙΑ ΠΕΜΠΤΗ. ΜΕ ΤΙΣ ΟΡΕΣ ΠΟΥ ΕΧΕΙΣ ΤΗΝ ΚΑΘΕ ΜΕΡΑ)
# LIST.APPEND( MATHIMA("ena onoma","LINK ZOOM / WEBEX / WHATEVER,ARXIZEI STIS 5,TELEIONEI STIS 7"))

# MATHIMATA 4ou EKSAMINOU
list.append( Mathima("Arithmitikh Analysh kai perivalonta hlopoihshs","https://upatras-gr.zoom.us/j/99385546396?pwd=WVY0c1FQVVBjc2VIQWdiWWFsN1pWQT09","Monday",14,17) )
list.append( Mathima("Theoria Shmaton kai Systhmaton","https://upatras-gr.zoom.us/j/3189977126?pwd=a05FV3hrYnZhTDVGY3ptVE5nNElIdz09","Monday",17,19) )
list.append( Mathima("Psifiaka Hlektronika","https://teams.microsoft.com/l/team/19%3a5050395caf7f46f787e9a1943fcd842b%40thread.tacv2/conversations?groupId=a4a5fb9f-8233-4249-8d30-ad570390d224&tenantId=5a52ab58-42d0-4bb4-b3fc-713dd6822d20","Tuesday",13,15) )
list.append( Mathima("Domes Dedomenon","https://upatras-gr.zoom.us/j/92396242820?pwd=Tlk1QmNjYks3ZmFJc2UwVEtHTE0yUT09","Tuesday",15,17) )
list.append( Mathima("Arithmitikh Analysh kai perivalonta hlopoihshs","https://upatras-gr.zoom.us/j/99385546396?pwd=WVY0c1FQVVBjc2VIQWdiWWFsN1pWQT09","Tuesday",17,19) )
list.append( Mathima("Sygxrona Themata Arxitektonikhs","https://upatras.webex.com/webappng/sites/upatras/meeting/download/e8f24ebb3e0c44418328b32f89a955bc?siteurl=upatras&MTID=m0d3fd5550d06bccd835ac86330d80337","Wednesday",17,18) )
list.append( Mathima("Theoria Shmaton kai Systhmaton","https://upatras-gr.zoom.us/j/3189977126?pwd=a05FV3hrYnZhTDVGY3ptVE5nNElIdz09","Wednesday",18,21) )
list.append( Mathima("Domes Dedomenon","https://upatras-gr.zoom.us/j/92396242820?pwd=Tlk1QmNjYks3ZmFJc2UwVEtHTE0yUT09","Thursday",15,17) )
list.append( Mathima("Sygxrona Themata Arxitektonikhs","https://upatras.webex.com/webappng/sites/upatras/meeting/download/e8f24ebb3e0c44418328b32f89a955bc?siteurl=upatras&MTID=m0d3fd5550d06bccd835ac86330d80337","Thursday",17,19) )
list.append( Mathima("Psifiaka Hlektronika","https://teams.microsoft.com/l/team/19%3a5050395caf7f46f787e9a1943fcd842b%40thread.tacv2/conversations?groupId=a4a5fb9f-8233-4249-8d30-ad570390d224&tenantId=5a52ab58-42d0-4bb4-b3fc-713dd6822d20","Thursday",19,21) )


# --------------------------------------------------

today_list = []

for obj in list:
    if obj.day == today :
        today_list.append(obj)

today_list.sort(key=lambda x: x.starting_hour, reverse=False)

inclass = False
def check(time_now):
    ora = time_now.hour
    lepta = time_now.minute
    for obj in today_list:
        if ora > obj.ending_hour:
            today_list.remove(obj)
            continue
        if ora > obj.starting_hour and ora < obj.ending_hour:
            inclass = True
            print("Exeis '" + obj.name + "'   (" + str(obj.starting_hour) + ' - ' + str(obj.ending_hour) + '). Anoigo to link : ')
            print(obj.link)
            webbrowser.open(obj.link, new = 2)
            break
    #OPEN OBS
    print("Next class in " + str(today_list[0].starting_hour-ora-1) + " ores kai " + str(60 - lepta) + " lepta...")


print("Shmerino programma : ")
for obj in list:
    if obj.day == today:
        print("||" + obj.name + "|| --> " + str(obj.starting_hour) + " - " + str(obj.ending_hour) + " <-- ")
print("\n\nAse Anoixto afto to parathiro kai ta mathimata tha anoiksoun aftomata\n\n")

check(datetime.datetime.now())
while True:
    if datetime.datetime.now().minute % 5 == 0: 
        if inclass == False :
            check(datetime.datetime.now())
    time.sleep(60)
