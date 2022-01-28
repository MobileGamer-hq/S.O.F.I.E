import list
from playsound import playsound

hau = list.HAU
targets = list.target
projects = list.projects
villains = list.villains


def addTarget():
    file = open("Files/targets.txt", "a")
    targets.sort()
    for items in targets:
        file.write('%s\n' % items)

    file.close()
    print("done.....")


def addProjects():
    file = open("Files/projects.txt", "a")
    projects.sort()

    for items in projects:
        file.write('%s\n' % items)

    file.close()
    print("done.....")


def addVillains():
    file = open("Files/villains.txt", "a")
    villains.sort()

    for items in villains:
        file.write('%s\n' % items)

    file.close()
    print("done.....")


target_file = open("Files/targets.txt", "r")
target_list = target_file.readlines()
target_file.close()

villain_file = open("Files/villains.txt", "r")
villain_list = villain_file.readlines()
villain_file.close()

project_file = open("Files/projects.txt", "r")
project_list = project_file.readlines()
project_file.close()

compliment_file = open("Files/compliments.txt", "r")
compliment = compliment_file.readlines()
compliment_file.close()
