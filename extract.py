import sys
import xmltodict

if (len(sys.argv) == 1):
    print("Usage:\n" + sys.argv[0] + " [file location] ( [sent | received | both] ( [phone number] ))")
    exit()

xmlfile = open(sys.argv[1], "r")
doc = xmltodict.parse(xmlfile.read())
smses = list(doc["smses"]["sms"])

if (len(sys.argv) == 2):
    for item in smses:
        print(item["@readable_date"] + " - " + item["@address"], end = " - ")
        if (item["@type"] == "1"): print("Received")
        else: print("Sent")
        print(item["@body"], end = "\n\n")
elif (len(sys.argv) == 3):
    if (sys.argv[2] == "received"):
        for item in smses:
            if (item["@type"] == "1"):
                print(item["@readable_date"] + " - " + item["@address"] + "\n" + item["@body"], end = "\n\n")
    elif (sys.argv[2] == "sent"):
        for item in smses:
            if (item["@type"] == "2"):
                print(item["@readable_date"] + " - " + item["@address"] + "\n" + item["@body"], end = "\n\n")
    elif (sys.argv[2] == "both"):
        for item in smses:
            print(item["@readable_date"] + " - " + item["@address"], end = " - ")
            if (item["@type"] == "1"): print("Received")
            else: print("Sent")
            print(item["@body"], end = "\n\n")
elif (len(sys.argv) == 4):
    if (sys.argv[2] == "received"):
        for item in smses:
            if (item["@type"] == "1" and item["@address"] == sys.argv[3]):
                print(item["@readable_date"] + "\n" + item["@body"], end = "\n\n")
    elif (sys.argv[2] == "sent"):
        for item in smses:
            if (item["@type"] == "2" and item["@address"] == sys.argv[3]):
                print(item["@readable_date"] + "\n" + item["@body"], end = "\n\n")
    elif (sys.argv[2] == "both"):
        for item in smses:
            if (item["@address"] == sys.argv[3]):
                print(item["@readable_date"], end = " - ")
                if (item["@type"] == "1"): print("Received")
                else: print("Sent")
                print(item["@body"], end = "\n\n")