def get_keys(path='keys.txt'):
    with open(path,'r') as f:
        lines = f.readlines()
        keys={}
        for line in lines:
            items = line.split(':',maxsplit=1)
    #         print("items :",items)
            if '\n' in items[1]:
                items[1] = items[1].replace('\n','')
            keys[items[0]]=items[1]
#             cmd = "%s = \'%s\'"% (items[0],items[1])
#             exec(cmd)
            print("%s was loaded"%items[0])
    return keys
