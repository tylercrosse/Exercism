import datetime

def add(moment):
    gs = datetime.timedelta(seconds = 1000000000)
    gs_bday = moment + gs
    return gs_bday
