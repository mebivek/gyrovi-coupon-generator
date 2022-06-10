from django.http import HttpResponse

class AllowOptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.method == "OPTIONS":
            mid_response = HttpResponse("ok", status=200)
            mid_response["Access-Control-Allow-Origin"] = "*"
            mid_response[
                "Access-Control-Allow-Methods"
            ] = "GET, POST, OPTIONS, PUT, DELETE"
            mid_response["Access-Control-Allow-Headers"] = "*"
            return mid_response
        return response

    def process_response(self, request, response):
        return response
