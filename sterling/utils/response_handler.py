def response(response):
    if response.status_code == 200:
        data = response.text
    elif response.status_code == 400:
        data = "Bad Request"
    elif response == 401:
        data = "Unauthorized. Please check your credentials " + str(response.status_code)
    elif response.status_code == 503:
        data = "Service temporarily unavailable " + str(response.status_code)
    elif response.status_code == 500:
        data = "Error executing methodName please raise an issue on github "+ str(response.status_code)
    else:
        data = "Error"
    return data