import pymongo

# project/cluster/database
client = pymongo.MongoClient("mongodb+srv://user:password0@cluster0.pa3o1.mongodb.net/project0?retryWrites=true&w=majority")

collection = client['database0']['collection0']

collection.delete_many({})
for i in range(50):
    collection.insert_one( {"key":"n"+str(i),"value":i} )