import azure.functions as func
import pymongo
from bson.objectid import ObjectId


def main(req: func.HttpRequest) -> func.HttpResponse:

    id = req.params.get('id')

    if id:
        try:
            url = "mongodb://proj-2-db:a2vdIiLkF4sEHZxSndyx7LmYoyrdw7UTl9FpBS5undTND20d19SRtQdX6yfYhnwp5qMfQCk7VNxcACDbTm45Pg==@proj-2-db.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@proj-2-db@"
            client = pymongo.MongoClient(url)
            database = client['proj-2-database']
            collection = database['advertisements']
            
            query = {'_id': ObjectId(id)}
            result = collection.delete_one(query)
            return func.HttpResponse("")

        except:
            print("could not connect to mongodb")
            return func.HttpResponse("could not connect to mongodb", status_code=500)

    else:
        return func.HttpResponse("Please pass an id in the query string",
                                 status_code=400)
