class Union:
    def __init__(self, params):
        self.url = params['base_url']
        self.headers = {
            "Sandbox-Key": params['Sandbox-Key'],
            "Content-Type": params['Content-Type']
        }
