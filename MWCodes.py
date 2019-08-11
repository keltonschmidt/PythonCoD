import time
import requests
from bs4 import BeautifulSoup
from threading import Thread

link = "https://profile.callofduty.com/cod/login"
redeemlink = "https://profile.callofduty.com/promotions/redeemCode"

threads = ['', '', '', '', '','', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '','', '', '',
           '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '','',
           '', '', '', '', '', '', '', '', '','', '', '', '', '', '', '', '', '', '','', '', '', '', '',
           '', '', '', '', '','', '', '', '', '', '', '', '', '', '','', '', '', '', '', ]

logindates = [" ", " "]
i = 0
j = 0
h = 0

working = []
notworking = []


loginfile = open("login.txt", 'r')
codesfile = open("COD MW CODES.txt", 'r')

for line in range(2):
    logindates[i] = loginfile.readline()
    i += 1
logindates[0] = logindates[0].strip('\n')
print("Login Infos: ", logindates)

number_lines = len(codesfile.readlines())
print("Codes Found: " + str(number_lines))

print("How many Threads?")
threadnumber = int(input())


class CoDThread(Thread):
    def __init__(self, name, time, numberlines, codes, curthreadnow, linestojump):
        Thread.__init__(self)
        self.name = name
        self.time = time
        self.numberlines = numberlines         # TOTAL LINES
        self.codelist = codes                  # LIST
        self.threadnum = curthreadnow          # CURRENT THREAD
        self.linestojump = linestojump         # LINES TO JUMP BASED ON NUMBER OF THREADS

    def run(self):
        # print ("Thread '" + self.name + "' inizio")
        m = 0

        for m in range(self.threadnum, number_lines):
            usedcode = codes_[m]
            payload = {'code': usedcode}
            r = requests.post(redeemlink, data=payload)
            html = r.content
            soup = BeautifulSoup(html, 'lxml')

            for tag in soup.select("p"):
                nametext_ = tag.text
                pos = nametext_.find("Please")

                if pos < 5 and len(nametext_) > 10:
                    # print(nametext_)
                    # self.notworkinglist.append(usedcode)
                    nwstring = "Code n^", m, ": ", usedcode, " is not working from thread."
                    # print(colored(nwstring, 'red'))
                    #print(nwstring)
                    print("Code n^", m, ": ", usedcode, " is not working from thread.")
                else:
                    print((usedcode, "IS WORKING."))

            # print("Not working: ", notworking)

            if r.status_code == 200:
                pass

        m = m + self.linestojump
        time.sleep(0.2)

        # print ("Thread '" + self.name + "' fine")

        return self.notworkinglist

codes_ = []

with open("COD MW CODES.txt", 'r') as cf:
    for k in range(number_lines):
        codes_.append((cf.readline()).strip(('\n')))

# print(codes_)

for _ in range(threadnumber):
    currentthread = ("Thread #" , _)
    threads[_] = CoDThread(currentthread, 1, number_lines, codes_, _, threadnumber)
    threads[_].start()
    threads[_].join()



for line in range(2):
    logindates[i] = loginfile.readline()
    i += 1
