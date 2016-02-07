import urllib.request
import json
import sys
import os

link = sys.argv[1] + "/_all_docs"
with urllib.request.urlopen(link) as url:
    allDocsString = url.read().decode('utf-8')
print(allDocsString, end="", file=open("_all_docs.json", "w"))
allDocs = json.loads(allDocsString)
for row in allDocs["rows"]:
    docUrl = sys.argv[1] + "/" + row["key"]
    with urllib.request.urlopen(docUrl) as url:
        docString = url.read().decode('utf-8')
        print(docString, end="", file=open(row["key"] + ".json", "w"))
        doc = json.loads(docString)
        for key, value in doc["_attachments"].items() :
            if not os.path.exists(row["key"]):
                os.makedirs(row["key"])
            with urllib.request.urlopen(docUrl + "/" + key) as url:
                attachmentBinary = url.read()
            f = open(row["key"] + "/" + key, 'wb')
            f.write(attachmentBinary)
