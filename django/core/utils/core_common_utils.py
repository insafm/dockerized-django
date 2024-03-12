from django.utils import timezone
from django.contrib.auth import get_user_model

class CoreCommon():
	
    def get_current_time(self):
        return timezone.now()
    
    def make_timezone_aware(self, date):
        if type(date) == "str":
            date = timezone.datetime.strptime(
                    date,
                    "%Y-%m-%d %H:%M:%S"
                )
        return timezone.make_aware(date)
