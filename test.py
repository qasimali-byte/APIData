# import json
#
# r = {'is_claimed': 'True', 'rating': 3.5}
# r = json.dumps(r)
# loaded_r = json.loads(r)
# print(loaded_r['rating']) #Output 3.5
# print(type(r)) #Output str
# print(type(loaded_r) )#Output dict
def FormattheXmlFile():
    f = open('/home/qasim/APIData/Flask/Recivedconfigurationfromevc.xml', 'r')
    print(f)
    lines = f.readlines()
    print(lines)
    lineslength = len(lines)
    f.close()
    print(lineslength)
    f = open('/home/qasim/APIData/Flask/Recivedconfigurationfromevc.xml', 'w')
    f.write('\n'.join(lines[2:lineslength - 1]))
    f.close()