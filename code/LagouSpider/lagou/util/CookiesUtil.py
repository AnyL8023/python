import datetime

class CookiesUtil(object):

    def getCookies(self):
        time = datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
        cookies = {
            'user_trace_token': time,
            'LGUID': time,
        }
        return cookies;