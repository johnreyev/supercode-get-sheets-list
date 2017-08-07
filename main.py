""" Import required libraries """
import json
import requests


URL = "https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_notation}?key={google_key}"


def main(spreadsheet_id, range_notation, google_key):
    """ Add new user to mailchimp subscription. """

    response = {}
    response["type"] = "error"

    headers = {"Content-Type": "application/json"}

    try:
        result = requests.get(
            URL.format(
                spreadsheet_id=spreadsheet_id,
                range_notation=range_notation,
                google_key=google_key
            ),
            headers=headers)

        result_json = json.loads(result.text)

        if result.status_code == 200:
            response["type"] = "success"
            response["data"] = result_json
        elif result.status_code in [400, 404]:
            response["error"] = {}
            response["error"]["message"] = result_json["detail"]
    except requests.exceptions.HTTPError as err:
        response["error"] = {}
        response["error"]["message"] = "Failed to connect."
    except Exception as err:
        response["error"] = {}
        response["error"]["message"] = str(err)

    return response
