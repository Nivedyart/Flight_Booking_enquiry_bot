class APIResponse:
    def __init__(self, status, data=None, error=None):
        self.status = status
        self.data = data
        self.error = error

