#!python2.7.13

def applyDatabaseChanges(serverName):
    print ('Applying database changes on ' + serverName)

def cleanData(serverName):
    print ('Cleaning sensitive data on ' + serverName)

def deployAppCode(serverName):
    print ('Deploying Application code to ' + serverName)

def deployStaticWebAssets(serverName):
    print ('Deploying Static Web Assets for ' + serverName)

def minifyCSSJS(serverName):
    print('Minifying CSS and JS on ' + serverName)

def getServerList(filepath):
    with open(filepath, "r+") as report:

        serverList = []

        ###grabs lines in txt file and creates array
        for line in report:
            ldata = line.split('-') # split line into parts
            serverList.append(ldata)

        for x in serverList:
            if len(x) == 3:
                x[2] = x[2].replace("\r\n", "")
        # print serverList
        return serverList

def prodServer(serverName):
    deployAppCode(serverName)
    deployStaticWebAssets(serverName)
    minifyCSSJS(serverName)

def qaServer(serverName):
    deployAppCode(serverName)
    deployStaticWebAssets(serverName)
    cleanData(serverName)

def betaServer(serverName):
    deployAppCode(serverName)
    deployStaticWebAssets(serverName)
    minifyCSSJS(serverName)
    cleanData(serverName)

#####['PR', 'NATALIE', '44\r\n']

getServerList('servers_matt.txt')

serverList = getServerList('servers_matt.txt')
for x in serverList:
    if len(x) == 3:
        if len(x[2]) == 2 and len(x[1]) <= 8:
            if x[0] == 'PR':
                if x[2] == '01':
                    applyDatabaseChanges(x[1])
                prodServer(x[1])
                print
            elif x[0] == 'QA':
                if x[2] == '01':
                    applyDatabaseChanges(x[1])
                qaServer(x[1])
                print
            elif x[0] == 'BE':
                if x[2] == '01':
                    applyDatabaseChanges(x[1])
                betaServer(x[1])
                print
            else:
                print 'ERROR: server environment incorrect format, ' + str(x[0] + '-' + x[1]+'-' + x[2])
        else:
            print 'ERROR: server name or number lengths incorrect, ' + str(x[0] + '-' + x[1]+'-' + x[2])
    else:
        print 'ERROR: not all server inputs given to locate this server, ' + str(x)
        print
