

class TimeError:
    # Returns difference in seconds between the time on an external server
    # and the time on this computer
    def __init__(self, requests, time):
        self.request = requests
        self.time = time
        
    def error(self):
        return self._get_server_time() - self.time.time()

    # The underscore denotes this is a private method not to be called from the
    # outside. You also shouldn't stub it in your tests. So if your tests contain
    # the words `get_server_time`, you're on the wrong track.
    def _get_server_time(self):
        response = self.request.get("https://worldtimeapi.org/api/ip")
        json = response.json()
        return json["unixtime"]

