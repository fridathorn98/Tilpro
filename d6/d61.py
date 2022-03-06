## LAB1


############################################################
#
#

# global variables

url = "https://cloud.timeedit.net/kth/web/public01/ri167499X83Z0QQ5Z16g3YZ5yQ086Y75Z0QgQY6Q5027o5p0ll55qnW67XwWa9WP16bx6ju.html"

scheduleFile = "DD1321.htm"    # Name of schedule html-file

############################################################
#
# imports and defs
#
import re, getopt, sys, urllib


class Schedule:
    def __init__(self):
        self.week = ''
        self.date = ''
        self.day = ''
        self.activity = []
        self.time = ''

    def __str__(self):
        s = "{} => {:3s}, {:>5s}, {:>3s}, {} ;".format( self.__class__.__name__, self.week, self.day, self.date, self.time )
        for h in self.activity:
            s += h + "; "
        return s

    def __contains__(self, x):
        if (x in self.week or x in self.date or x in self.day or x in self.activity or x in self.time):
            return True


###########################################################################
##
## parse_url_file
##
## IN - fildatan
##
## OUT - fildatan sorterad i aktivitet, veckor, tider, datum och veckodagar
##
def parse_url_file(file_content):
    vek = []

    reg_expr_w = re.compile('.*?td.*?class.*?headline.*?> *([MTOFL][a-zåäö]+) *20[12][0-9]-0?([123]?[0-9])-0?([123]?[0-9])<.*weekin.*> *(v.*?)<.', re.I)
    reg_expr_d = re.compile('.*?td.*?class.*?headline.*?>([MTOFL][a-zåäö]+) *20[12][0-9]-0?([123]?[0-9])-0?([123]?[0-9])<.')
    reg_expr_t = re.compile('.*?td +id="time.*?>(.+?)<.td')
    reg_expr_i = re.compile('.*?td.*?class.*?column[0-1].*?>(.*?)<.td', re.I)

    lines = file_content

    qq = Schedule()
    week_var = 0
    day_var = 0
    date_var = 0
    time_var = 0
    newEntry = False
    for j, line in enumerate(lines):

        #week
        m = reg_expr_w.match(line)
        if (m != None):
            week_var = m.group(4)
            qq.week = week_var
        else:
            qq.week = week_var
            next

        #date
        m = reg_expr_d.match(line)
        if (m != None) and newEntry:
            day_var = m.group(1)
            date_var = m.group(3) + "/" + m.group(2)
            qq.day = day_var
            qq.date = date_var
        else:
            qq.day = day_var
            qq.date = date_var
            next

        #time
        m = reg_expr_t.match(line)
        if (m != None):
            time_var = m.group(1)
            qq.time = time_var
            if newEntry == True:
                vek.append(qq)
                qq = Schedule()
        else:
            qq.time = time_var
            next

        #activity
        m  = reg_expr_i.match(line)
        if (m != None) and len(m.group(1)) > 0:
            qq.activity.append(m.group(1))
            if newEntry == False:
                newEntry = True
            next

    return vek


###########################################################################
##
## get file content
##
## IN  - String with the name of the requested file
##
## OUT - Vector with rows in the file (if it exists)
##
##
def get_file_content(file_name):
    infil = ''
    try:
        infil = open(file_name, 'r')
    except:
        print ("No such file", file_name, " please run with --update")
        print ("	python", sys.argv[0], "--update")
        sys.exit()

    file_content = infil.readlines()
    #file_content = infil.read()
    # print('file_content = ', file_content)
    return file_content

###########################################################################
##
## usage
##
## IN - inget
##
## OUT - info om hur man kör programmet
##
def usage():
    print ("Usage example:")
    print ("python" , sys.argv[0] ,  "--update ")
    print ("	updates Time Edit schedule")
    print ("python" , sys.argv[0] ,  '--check "v 49"')
    print ("	checks schedule for week 49")
    print ("python" , sys.argv[0])
    print ("	prints previously downloaded schedule")

###########################################################################
##
## parse_command_line_args
##
## IN
##  ingenting
## OUT
##  en dictionary med vad som ska testas i search_data
##      "Det som returneras är en dictionary där kommandoradsargument med
##      bindestreck i läggs som nycklar och det som kommer direkt efter som värde"
def parse_command_line_args():
    try:
        opts, rest = getopt.getopt(sys.argv[1:], "hc:u", ["help", "check=", "update"])
    except getopt.GetoptError:
        # print help information and exit:
        print ("Unknown option")
        usage()
        sys.exit(2)

    todo = {}
    for option, value in opts:
        if option in ("-h", "--help"):
            usage()
            sys.exit()
        elif option in ('--check', '-c'):
            todo["check"]=value
        elif option in ('--update', '-u'):
            todo["update"] = value

    return todo

###########################################################################
##
## print_schedule
##
## IN - datan
##
## OUT - schemat (print)
##
def print_schedule(data):
    print ("----------- Schedule -------------")
    for item in data:
        print (item)

###########################################################################
##
## search_data
##  anropa via t.ex python3 d61.py -c Mån
## IN
##  out från parse_command_line_args
## OUT
##  alla schemahändelser med det sökta argumentet skrivs ut

def search_data(what, dataset):
    found = False
    for item in dataset:
        if (what in item):
            found = True
            print (item)
    if (found == False):
        print ("Nothing happens", what)

###########################################################################
##
## main
##
## IN - ingenting
##
## OUT - utskrift via print_schedule
##
def main():

    global url

    # get command line options
    todo = parse_command_line_args()

    # update time edit file
    if 'update' in todo:
        print ("fetching url ...")
        webcontent = urllib.request.urlopen( url )
        with open( scheduleFile, "w") as fil:
            for row in webcontent:
                utf8line = row.decode('utf8')
                fil.write(utf8line)
        print ("         done")

    # Get schedule from disc
    filedata  = get_file_content(scheduleFile)
    sched = parse_url_file(filedata)

    # Do something
    if 'check' in todo:
        search_data(todo["check"], sched)
    else:
        print_schedule(sched)


###########################################################################

if __name__ == "__main__":
    main()

# td data och tr är rad
#reg_expr_w matchar med rad 3
#reg_expr_d matchar med rad
#reg_expr_t matchar med rad 8
#reg_expr_i matchar med rad 9 till 12

#kan bara söka efter hela ord
