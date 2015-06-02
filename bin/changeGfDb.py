#!/c/dev/GitTools/Python27/python

from xml.dom.minidom import parse
import sys, os
import subprocess

DOMAIN_XML = 'c:\\DEV\\{0}\\3.1.2-6_H08\\glassfish\\domains\\domain1\\config\\domain.xml'
poolsForUpdate = { 'GLOBE_APP-Pool', 'GLOBE_LOG-Pool', 'GLOBE_READ-Pool' }

instances = {
    'EDIF3P' : {
        'user' : 'HSDGDS_EDIF_3P',
        'url'  : 'jdbc:oracle:thin:@//bresl906.hsdg-ad.int:1521/D02GLB',
        'pass' : 'HSDGDS_EDIF_3P'
    },
    'EDIFMP' : {
        'user' : 'HSDGDS_EDIF_MASTERP',
        'url'  : 'jdbc:oracle:thin:@//bresl906.hsdg-ad.int:1521/D02GLB',
        'pass' : 'HSDGDS_EDIF_MASTERP'
    },
    'BKNG3P' : {
        'user' : 'HSDGDS_BKNG_3P',
        'url'  : 'jdbc:oracle:thin:@//bresl906.hsdg-ad.int:1521/D02GLB',
        'pass' : 'HSDGDS_BKNG_3P'
    },
    'BKNGMP' : {
        'user' : 'HSDGDS_BKNG_MASTERP',
        'url'  : 'jdbc:oracle:thin:@//bresl906.hsdg-ad.int:1521/D02GLB',
        'pass' : 'HSDGDS_BKNG_MASTERP'
    },
    'AF120' : {
        'user' : 'HSDGUS_ENV_AF120',
        'url'  : 'jdbc:oracle:thin:@//hamsl620.ham.hamburgsud.com:1521/T03GLB.WORLD',
        'pass' : 'HSDGUS_ENV_AF120'
    },
    'AF121' : {
        'user' : 'HSDGUS_ENV_AF121',
        'url'  : 'jdbc:oracle:thin:@//hamsl620.ham.hamburgsud.com:1521/T03GLB.WORLD',
        'pass' : 'HSDGUS_ENV_AF121'
    },
    'AF122' : {
        'user' : 'HSDGUS_ENV_AF122',
        'url'  : 'jdbc:oracle:thin:@//hamsl620.ham.hamburgsud.com:1521/T03GLB.WORLD',
        'pass' : 'AF122'
    },
    'AF123' : {
        'user' : 'HSDGUS_ENV_AF123',
        'url'  : 'jdbc:oracle:thin:@//bresl904.ham.hamburgsud.com:1521/T05GLB',
        'pass' : 'AF123'
    },
    'AF124' : {
        'user' : 'HSDGUS_ENV_AF124',
        'url'  : 'jdbc:oracle:thin:@//bresl904.ham.hamburgsud.com:1521/T05GLB',
        'pass' : 'AF124'
    },
    'AF042' : {
        'user' : 'HSDGUS_ENV_AF042',
        'url'  : 'jdbc:oracle:thin:@//hamsl620.ham.hamburgsud.com:1521/T03GLB.WORLD',
        'pass' : 'AF042'
    },
    'DD201' : {
        'user' : 'HSDGUS_ENV_DD201',
        'url'  : 'jdbc:oracle:thin:@//bresl904.ham.hamburgsud.com:1521/T05GLB',
        'pass' : 'DD201'
    },
    'DD202' : {
        'user' : 'HSDGUS_ENV_DD202',
        'url'  : 'jdbc:oracle:thin:@//hamsl620.ham.hamburgsud.com:1521/T03GLB.WORLD',
        'pass' : 'DD202'
    },
    'DD203' : {
        'user' : 'HSDGUS_ENV_DD203',
        'url'  : 'jdbc:oracle:thin:@//hamsl620.ham.hamburgsud.com:1521/T03GLB.WORLD',
        'pass' : 'DD203'
    },
    'OF003' : {
        'user' : 'HSDGUS_ENV_OF003',
        'url'  : 'jdbc:oracle:thin:@//hamsl615.ham.hamburgsud.com:1521/T04GLB.world',
        'pass' : 'ixFDgpd2o5sQk'
    }
}

def changeDbInstance(newInstance):
    dom = parse(getDomainXmlPath())
    jdbcs = dom.getElementsByTagName('jdbc-connection-pool')
    for jdbc in jdbcs:
        print 'JDBC Connection Pool: {0}'.format(jdbc.attributes.getNamedItem('name').value)
        if jdbc.attributes.getNamedItem('name').value in poolsForUpdate:
            changeDbProperty(jdbc, newInstance)

    print 'Writing xml to output file...'
    dom.writexml( open(getDomainXmlPath(), 'w') )

def changeDbProperty(jdbc, newInstance):
    print 'Changing properties for a jdbc tag...'
    properties = jdbc.getElementsByTagName('property')
    for prop in properties:
        print 'Property is {0}'.format(prop.attributes.getNamedItem('name').value)
        if prop.attributes.getNamedItem('name').value == 'user':
            changeDbUser(prop, newInstance)
        if prop.attributes.getNamedItem('name').value == 'url':
            changeDbUrl(prop, newInstance)
        if prop.attributes.getNamedItem('name').value == 'password':
            changeDbPassword(prop, newInstance)

def changeDbUser(prop, newInstance):
    print 'Change user to {0}'.format(getUser(newInstance)) 
    prop.attributes.getNamedItem('value').value = getUser(newInstance)

def changeDbUrl(prop, newInstance):
    print 'Change url to {0}'.format(getUrl(newInstance)) 
    prop.attributes.getNamedItem('value').value = getUrl(newInstance)
    
def changeDbPassword(prop, newInstance):
    print 'Change password to {0}'.format(getPassword(newInstance)) 
    prop.attributes.getNamedItem('value').value = getPassword(newInstance)
    
def getUser(newInstance):
    if newInstance in instances:
        return instances[newInstance]['user']
    
def getUrl(newInstance):
    if newInstance in instances:
        return instances[newInstance]['url']

def getPassword(newInstance):
    if newInstance in instances:
        return instances[newInstance]['pass']

def printInstanceNames():
    for key in sorted(instances.keys()):
        print '    {0}'.format(key)

def printUsage():
    print '  Currently available are:'
    printInstanceNames()
    print ''
    print '  Usage example:'
    print '    {0} {1}'.format(os.path.basename(__file__), instances.keys()[0])

def printCurrentConfig():
    print 'Current configuration:'
    dom = parse(getDomainXmlPath())
    jdbcs = dom.getElementsByTagName('jdbc-connection-pool')
    for jdbc in jdbcs:
        print '  JDBC Connection Pool: {0}'.format(jdbc.attributes.getNamedItem('name').value)
        properties = jdbc.getElementsByTagName('property')
        for prop in properties:
            if prop.attributes.getNamedItem('name').value == 'user':
                print '    User:     {0}'.format(prop.attributes.getNamedItem('value').value)
            if prop.attributes.getNamedItem('name').value == 'url':
                print '    URL:      {0}'.format(prop.attributes.getNamedItem('value').value)
            if prop.attributes.getNamedItem('name').value == 'password':
                print '    Password: {0}'.format(prop.attributes.getNamedItem('value').value)

def getDomainXmlPath():
    glassfishVersion = 'glassfish'
    # Windows CMD noch /bin/bash ! :(
    #getBranchBash = subprocess.Popen('getBranch', stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #autoBranch = getBranchBash.communicate()
    #print 'Branch from bash: {0}'.format(autoBranch)
    if len(sys.argv) == 3:
        if (sys.argv[2] == 'master'):
            glassfishVersion = ''.join([glassfishVersion, '-2.2.0'])
    path = DOMAIN_XML.format(glassfishVersion)
    print '> domain.xml location {0}'.format(path)
    return path

def printInformationOnUnknownArguments():
    printCurrentConfig()
    print ''
    print ''
    print 'You have to give the name of the db instance!'
    printUsage()
    
if (len(sys.argv) != 2 and len(sys.argv) != 3):
    printInformationOnUnknownArguments()
    sys.exit(2)

if sys.argv[1] not in instances.keys():
    print 'Given instance not found!'
    if len(sys.argv) == 2:
        sys.argv.append(sys.argv[1])
        print 'Using the parameter as branch information to display current configuration...'
    
    printInformationOnUnknownArguments()
    sys.exit(2)

changeDbInstance(sys.argv[1])
