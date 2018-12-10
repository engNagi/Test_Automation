# importing Libraries
import os
import datetime
import shutil
from subprocess import *
from xml.dom import minidom


# TODO Running the diffkit with only Tst.xml given.1- in progress
# TODO Sink file name + Timestamp. ->2
# TODO console log printing in separate file.->3
# TODO Rebuild should used the same uploaded file as before.->4
# TODO summary of diffkit in seperate file.->5




# functions
# JavaWrapperFunction
def jarWrapper(*args):
    process = Popen(['java', '-jar'] + list(args), stdout=PIPE, stderr=PIPE)
    ret = []
    while process.poll() is None:
        line = process.stdout.readline()
        if line != '' and line.endswith('\n'):
            ret.append(line[:-1])
    stdout, stderr = process.communicate()
    ret += stdout.split('\n')
    if stderr != '':
        ret += stderr.split('\n')
    ret.remove('')
    return ret


# Test.xml Parser
def test_xml_parse(diffkit_test_xml):
    test_xml = minidom.parse(diffkit_test_xml)
    test_xml_tags = test_xml.getElementsByTagName('property')
    lhs_file_path = test_xml_tags[0].attributes['value'].value
    rhs_file_path = test_xml_tags[1].attributes['value'].value
    test_sink_diff = test_xml_tags[2].attributes['value'].value
    return lhs_file_path, rhs_file_path, test_sink_diff


x, y, z = test_xml_parse('test9.plan.xml')
print(x)
print(y)
print(z)


# create new directory
def create_directory():
    build = os.environ['BUILD_TAG']
    date = datetime.datetime.now().strftime("%d-%m-%Y_%H:%M")
    timestamp_folder = build + date
    os.mkdir(timestamp_folder)
    return timestamp_folder


# Copyfile
def copy_files(source, destination_directory, destination):
    shutil.move(source, destination_directory + '/' + destination)


destination_directory = create_directory()
print(destination_directory)

# Copying files
copy_files('Test.Plan.xml', destination_directory, os.environ['Test.Plan.xml'])
copy_files('Test.lhs.csv', destination_directory, os.environ['Test.lhs.csv'])
copy_files('Test.rhs.csv', destination_directory, os.environ['Test.rhs.csv'])

os.chdir(destination_directory)

# Diffkit.jar arguments
args = ['../diffkit-app.jar', '-planfiles', os.environ['Test.Plan.xml']]

# Running Difkit
result = jarWrapper(*args)

# Print the output
for rest in result:
    print(rest)
