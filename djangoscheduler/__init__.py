from apscheduler.schedulers.background import BackgroundScheduler
#from django_apscheduler.jobstores import DjangoJobStore

task_scheduler = BackgroundScheduler()

task_scheduler.start()
