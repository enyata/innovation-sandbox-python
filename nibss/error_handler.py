
def error(e):
    if e == 400:
        data = "Bad Reequest"

    elif e == 401:
        data = "Unauthorized. PLease check your credentials " + str(e)
    elif e == 503:
        data = "Service temporarily unavailable " + str(e)
    elif e == 500:
        data = "Error executing methodName please raise an issue on github "+ str(e)
    else:
        data = "error"
    return data
