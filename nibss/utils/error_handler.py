def error(e):
    if e == 400:
        data = "Bad Request"
    elif e == 401:
        data = "Unauthorized. Please check your credentials " + str(e)
    elif e == 503:
        data = "Service temporarily unavailable " + str(e)
    elif e == 500:
        data = "Error executing methodName please raise an issue on github "+ str(e)
    else:
        data = "Error"
    return data
