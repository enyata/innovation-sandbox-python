class Sterling:
    def __init__(self, params):
        self.sandbox_key = params['Sandbox-Key']
        self.sub_key = params['Ocp-Apim-Subscription-Key']
        self.trace = params['Ocp-Apim-Trace']
        self.appId = params['Appid']
        self.content_type = params['Content-Type']
        self.ipval = params['ipval']
        self.url = params["base_url"]

        self.headers = {
            "Sandbox-Key": self.sandbox_key,
            "Ocp-Apim-Subscription-Key": self.sub_key,
            "Ocp-Apim-Trace": self.trace,
            "Appid": self.appId,
            "Content-Type": self.content_type,
            "ipval": self.ipval
        }