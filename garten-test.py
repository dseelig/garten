from time import sleep

prog1 = {'name' : 'gwg', 'state' : 0, 'seconds' : 5, "gpio" : "12"}
prog2 = {'name' : 'gwvl', 'state' : 0, 'seconds' : 5, "gpio" : "13"}
prog3 = {'name' : 'gwvr', 'state' : 0, 'seconds' : 5, "gpio" : "14"}
prog4 = {'name' : 'hb1', 'state' : 0, 'seconds' : 2, "gpio" : "15"}
prog5 = {'name' : 'hb2', 'state' : 0, 'seconds' : 3, "gpio" : "16"}
prog6 = {'name' : 'ter', 'state' : 1, 'seconds' : 10, "gpio" : "17"}

progs = [prog1, prog2, prog3, prog4, prog5, prog6]
runableProgs = []

timeCnt = 0
runableCnt = 0
runBW = 0


for prog in progs:
    if prog['state'] == 1:
        runableProgs.append(prog)

if len(runableProgs) > 0:
    runBW = 1

if runBW == 1:
    print('Activate pump and wait 15 seconds for building pressure.')
    
    sleep(15)

    print('Pressure build is complete: start BW')

    for run in runableProgs:
        print(run['name'] + ' - GPIO ' + run['gpio'] + ' high')
        sleep(run['seconds'])
        print(run['name'] + ' - GPIO ' + run['gpio'] + ' low')
        timeCnt += run['seconds']
        runableCnt += 1
    
    print('The system run ' + str(timeCnt) + ' seconds:')
    print(str(runableCnt) + ' BW successful executed.')

else:
    print('No active BW programs found.')
