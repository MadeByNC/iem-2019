import random
import time
import sys

array = []
koszyk1 = ['Rocket League','Fortnite','Trackmania','F1 2015','Warcraft3','Kreski']
koszyk2 = ['Starcraft 2','FIFA','CS GO','WoT','Quake 3','DSJ']
koszyk3 = ['Unreal Tournament','Sniper Elite 3','Micro Machines']
def progressBar():
    toolbar_width = 40
    sys.stdout.write("[%s]" % (" " * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1))
    for i in xrange(toolbar_width):
        time.sleep(0.1)
        sys.stdout.write("-")
        sys.stdout.flush()
    sys.stdout.write("\n\n\n")

def showKoszyk(array):
    raw_input()
    i = 0
    for game in array:
        print('\n     '+array[i])
        i += 1

print(">>>>> LOSOWANIE GIER NA IEM 2019 KATOWICE <<<<<")
print("\n\n>>>>> DO KOSZYKA NR 1 WPADAJA GRY: <<<<<")
showKoszyk(koszyk1)
print("\n\n>>>>> DO KOSZYKA NR 2 WPADAJA GRY: <<<<<")
showKoszyk(koszyk2)
raw_input()
print("\n\n>>>>> DO KOSZYKA NR 3 WPADNA POZOSTALEM GRY Z KOSZYKA NR 2 ORAZ PONIZSZE <<<<<")
showKoszyk(koszyk3)
raw_input()
print("\n\n\n >>>>> UWAGA <<<<< \n\n >>>>>PRZECHODZIMY DO LOSOWANIA GIER Z KOSZYKA NR 2 !! <<<<<\n")
raw_input()
progressBar()

lotteryNumbers = []
koszyk2Usun = []

for i in range (0,2):
  number = random.randint(0,5)
  while number in lotteryNumbers:
    number = random.randint(0,5)
  lotteryNumbers.append(number)

for num in lotteryNumbers:
    print(koszyk2[num])
    koszyk1.append(koszyk2[num])
    koszyk2Usun.append(num)

for r in range (len(koszyk2Usun)):
    #print('r to : '+str(r))
    #print('koszyk usun ' +str(koszyk2Usun[r]))
    del koszyk2[koszyk2Usun[r]]

for koszyk3game in range (0,len(koszyk2)):
    koszyk3.append(koszyk2[koszyk3game])


print ("\n>>>>> KOSZYK NR 1 PREZENTUJE SIE NASTEPUJACO <<<<< \n")
showKoszyk(koszyk1)

print("\n\n\n >>>>> UWAGA <<<<< \n\n >>>>>PRZECHODZIMY DO LOSOWANIA GIER Z KOSZYKA NR 3 !! <<<<<\n")
raw_input()
progressBar()

pick = random.randint(0,len(koszyk3)-1)
print(koszyk3[pick])
koszyk1.append(koszyk3[pick])

print ("\n>>>>> KOSZYK NR 1 PREZENTUJE SIE NASTEPUJACO <<<<< \n")
showKoszyk(koszyk1)
