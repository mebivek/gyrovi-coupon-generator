

from django.http import JsonResponse

def api_send_cors(response):
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS, PUT, DELETE"
    response["Access-Control-Allow-Headers"] = "*"
    response["Allow"] = "GET, POST, OPTIONS, PUT, DELETE"
    return response

def send_response(dict_data, status_code):
    response = JsonResponse(dict_data)
    response.status_code = status_code
    return api_send_cors(response)

def error_json_response(message, status_code=500):
    res = {
        "success": False,
        "message": message,
    }
    return send_response(res, status_code)

def success_json_response(message, status_code=200, data=None):
    res = {
        "success": True,
        "message": message,
        "data": data
    }
    return send_response(res, status_code)
