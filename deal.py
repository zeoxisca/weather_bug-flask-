import json
area_file = open('areas.txt', 'r')
areas = json.loads(area_file.read())
keys = list(areas.keys())
for key in keys:
    areas[key[:-1]] = areas[key]
    del areas[key]

area_file.close()
area_file = open('areas.txt', 'w')
area_file.write(json.dumps(areas))
area_file.close()
