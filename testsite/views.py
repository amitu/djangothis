from importd import d

@d("/idx")
def index(request):
    return d.HttpResponse("idx")
