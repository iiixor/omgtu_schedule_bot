import datetime

def even_odd():
    date = datetime.datetime.now().replace(second=0, microsecond=0)
    wk = date.isocalendar()[1]
    if (wk % 2 == 0):
        return "Нижняя неделя"
    else:
        return "Верхняя неделя"
