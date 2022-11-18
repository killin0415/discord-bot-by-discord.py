import datetime

def get_date():
    x = datetime.datetime.now()
    y = x.year
    m = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
            'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][x.month - 1]
    d = x.day
    h = x.hour
    mi = x.minute
    s = x.second
    w = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu',
            'Fri', 'Sat'][(x.weekday() + 1) % 7]
    res = '{} {} {:02d} {} {:02d}:{:02d}:{:02d}'.format(
        y, m, d, w, h, mi, s)
    return res

def get_time(td: datetime.timedelta):
        d = td.days
        s = td.seconds
        m = s // 60
        s %= 60
        h = m // 60
        m %= 60
        
        return f"{d}d, {h}h, {m}min, {s}s."