import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import pinging_google

def start():
    scheduler = BackgroundScheduler({
        'apscheduler.timezone': pytz.timezone('Asia/Kolkata')
    })

    scheduler.add_job(pinging_google, 'cron', hour='23')
    # scheduler.add_job(pinging_google, 'cron', day_of_week='0-6', hour='23')
    scheduler.print_jobs() 
    scheduler.start()
