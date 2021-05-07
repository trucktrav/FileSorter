import os
import re
import sys
from threading import  Thread
from datetime import datetime
import subprocess
import pickle as cPickle
dict1 = {}


def get_drives():
    response = os.popen("wmic logicaldisk get caption")
    list1 = []
    total_file = []
    t1 = datetime.now()
    for line in response.readlines():
        line = line.strip("\n")
        line = line.strip("\r")
        line = line.strip(" ")
        if line == "Caption" or line == "":
            continue
        list1.append(line)
    return list1


def search1(drive):
    for root, dir, files in os.walk(drive, topdown=True):
        for file in files:
            file = file.lower()
            if file in dict1:
                file = file +'_1'
                dict1[file] = root
            else:
                dict1[file] = root


def create():
    t1 = datetime.now()
    list2 = []  # empty list is created
    l_drives = get_drives()
    print(l_drives)
    # for drive in l_drives:
    #     process1 = Thread(target=search1, args=(drive,))
    #     process1.start()
    #     list2.append(process1)
    #
    # for t in list2:
    #     t.join()  # Terminate the threads

    search1('H:\\Documents\\FAD')

    pickle_write = open('finder_data', 'wb')
    cPickle.dump(dict1, pickle_write)
    pickle_write.close()
    t2 = datetime.now()
    total = t2 - t1
    print('Time taken to create ', total)
    print('Thanks for using L4wisdom.com')


def main():
    file_dict = {}
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print('Please use proper format')
        print('Use < finder - c > to create database file')
        print('Use < finder file - name > to search file')
        print('Thanks for using L4wisdom.com')
    elif sys.argv[1] == '-c':
        create()
    else:
        print('search')
        t1 = datetime.now()
        try:
            pickle_file = open('finder_data', 'rb')
            file_dict = cPickle.load(pickle_file)
            pickle_file.close()
        except IOError:
            create()
        except Exception as e:
            print(e)
            sys.exit()

        file_to_be_searched = sys.argv[1].lower()
        list1 = []
        print('Path \t\t: File - name')

        for key in file_dict:
            if re.search(file_to_be_searched, key):
                str1 = file_dict[key]+' : '+key
                list1.append(str1)
        list1.sort()
        for each in list1:
            print(each)
            print('-----------------------')
        t2 = datetime.now()
        total = t2-t1
        print('Total files are', len(list1))
        print('Time taken to search ' , total)
        print('Thanks for using L4wisdom.com')


if __name__ == '__main__':
    main()
