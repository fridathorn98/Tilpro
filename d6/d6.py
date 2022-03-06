import json, urllib, urllib.request, sys, re

#Reguljärt uttryck för input på format YYYY-MM-DD
reg_expr_t = re.compile('202[01]-[0-1][0-2]-[0-3][0-9]')
# if (reg_expr_t.match(line) != None) #om match

schemaurl = "https://www.kth.se/social/api/schema/v2/course/"
if len(sys.argv)==2:
    course=sys.argv[1]
    start = "?startTime=2021-01-14"
    end   = "&endTime=2021-03-21"
elif len(sys.argv)==3 and (reg_expr_t.match(sys.argv[2]) != None):
        course=sys.argv[1]
        start="?startTime="+"".join(sys.argv[2])
        end   = "&endTime=2021-03-21"
elif len(sys.argv)==4 and (reg_expr_t.match(sys.argv[2]) != None) and (reg_expr_t.match(sys.argv[3]) != None):
    course=sys.argv[1]
    start="?startTime="+"".join(sys.argv[2])
    end   = "&endTime="+"".join(sys.argv[3])
else:
    course = "DD1321"
    start = "?startTime=2021-01-14"
    end   = "&endTime=2021-03-21"
    if len(sys.argv)>2: #om felinmatat någonstans
        print("FEL INMATNING\nInput 2&3 ska ges som YYYY-MM-DD, kör istället 2021-01-14 - 2021-03-21")

schemaurl += course + start + end

request_data = urllib.request.urlopen(schemaurl).read() # hämtar data från REST-servern
utf_data = request_data.decode('utf-8')                 # översätter u00f6 -> ö
schedule = json.loads(utf_data)                     # lägger in i en pythonstruktur

# print(schedule,"\n")

# Skriv ut schemat för kursen
print("Schema för ",course)
for activity in schedule["entries"]:
    print(activity["start"][0:-6],end='-')
    print(activity["end"][11:13],end='  ')
    print(activity["title"],end='   ')
    for x in activity["locations"]:
        print(x["name"],end=' ')
    print("\n")
