import json


def lambda_handler(event, context):
    for i in range(100, -1, -1):
        print(i)

    print("Décollage !")

    return {"statusCode": 200, "body": json.dumps("Le jet est parti !")}
