import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from .tasks import ping_all_search_engines

def start():
    scheduler = BackgroundScheduler({
        'apscheduler.timezone': pytz.timezone('Asia/Kolkata')
    })
    scheduler.add_job(ping_all_search_engines('/sitemap.xml'), 'cron', hour='*/23')
    scheduler.print_jobs()
    scheduler.start()
