import logging

import azure.functions as func

from articles import get_rec_articles

import json

nb_results = 5

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    user = req.params.get('user')
    if not user:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            user = req_body.get('user')

    if user:
        articles = get_rec_articles(user)
        rec_articles = {'user': user,
                        'articles':{'1': articles[0][0],
                                    '2': articles[1][0],
                                    '3': articles[2][0],
                                    '4': articles[3][0],
                                    '5': articles[4][0],}
                        }
        rec_articles_json = json.dumps(rec_articles)

        return func.HttpResponse(rec_articles_json, mimetype='text/json')
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a user in the query string or in the request body for a personalized response.",
             status_code=200
        )
