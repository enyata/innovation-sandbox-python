class Sterling:
    def __init__(self, params):
        self.url = params["base_url"]
        self.headers = {
            "Sandbox-Key": params['Sandbox-Key'],
            "Ocp-Apim-Subscription-Key": params['Ocp-Apim-Subscription-Key'],
            "Ocp-Apim-Trace": params['Ocp-Apim-Trace'],
            "Appid": params['Appid'],
            "Content-Type": params['Content-Type'],
            "ipval": params['ipval']
        }