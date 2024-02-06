from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse

class TagCreatorView:
    '''
        Responsability for interacting with HTTP
    '''
    def validate_and_create(self, http_request: HttpRequest) -> HttpResponse:
        # body = http_request.body
        # product_code = body["product_code"]

        # lógica de regra de negócio
        print(http_request)

        # retorn http
        return HttpResponse(status_code=201, body={ "helo": "world" })