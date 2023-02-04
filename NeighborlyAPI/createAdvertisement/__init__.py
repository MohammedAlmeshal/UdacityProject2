import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://proj-2-db:a2vdIiLkF4sEHZxSndyx7LmYoyrdw7UTl9FpBS5undTND20d19SRtQdX6yfYhnwp5qMfQCk7VNxcACDbTm45Pg==@proj-2-db.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@proj-2-db@"
            client = pymongo.MongoClient(url)
            database = client['proj-2-database']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )