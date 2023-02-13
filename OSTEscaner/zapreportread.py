import json 
with open('myresaults2.json', 'r') as convert_file:
     myresault=json.load(convert_file)
#     convert_file.write(json.dumps(zap.core.alerts(baseurl=url)))
     print("length:",len(myresault))
 #    for j in myresault[0]:
#         print(j)
     for i in myresault:
          print(i['alert'])
#     print(myresault[0])
