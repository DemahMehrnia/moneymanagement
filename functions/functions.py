import datetime
def fillterbymonthanduser(MyContent,req):
    return MyContent.filter(user= req,date__month=datetime.datetime.now().strftime("%m"))