#importing Libraries
import os
import datetime
import shutil
from subprocess import *


#JavaWrapperFunction
def jarWrapper(*args):
    process = Popen(['java', '-jar']+list(args), stdout=PIPE, stderr=PIPE)
    ret = []
    while process.poll() is None:
        line = process.stdout.readline()
        if line != '' and line.endswith('\n'):
            ret.append(line[:-1])
    stdout, stderr = process.communicate()
    ret += stdout.split('\n')
    if stderr != '':
        ret += stderr.split('\n')
    for rets in ret:
        print rets
    ret.remove('')
    return ret

#File Parameters
print"this is the uploaded file " + os.environ['Test.Plan.xml']
print"this is the uploaded file " + os.environ['Test.lhs.csv']
print"this is the uploaded file " + os.environ['Test.rhs.csv']

#print"this is the Jenkins BUILD_TAG" + os.environ['BUILD_TAG']
#x = os.listdir('/var/lib/jenkins/workspace/Local_Diffkit/diffkit-app.jar')
#print x

currentDir = os.getcwd()
print "this is the current working Dir" + currentDir

desDir = os.environ['BUILD_TAG'] + datetime.datetime.now().strftime("%d-%m-%Y_%H:%M")
print "Making directory " + desDir
os.mkdir(desDir)

shutil.move('Test.Plan.xml', desDir + '/'+ os.environ['Test.Plan.xml'])
print 'hello'
shutil.move('Test.lhs.csv', desDir + '/' + os.environ['Test.lhs.csv'])
print 'hello'
shutil.move('Test.rhs.csv', desDir + '/' + os.environ['Test.rhs.csv'])
print 'hello'

os.chdir(desDir)

afterDirchange = os.getcwd()
print "this is the current working Dir" + afterDirchange

# Any number of args to be passed to the jar file

args = ['../diffkit-app.jar', '-planfiles', os.environ['Test.Plan.xml']]

# Running Difkit
result = jarWrapper(*args)

# Print the output
for rest in result:
    print rest

y = os.path.join(os.getcwd())
x = os.listdir(y)




