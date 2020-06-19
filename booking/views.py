from rest_framework import viewsets
from rest_framework.response import Response
from datetime import datetime, timezone, timedelta
import time

from .models import Booking
from .serializers import BookingSerializer
from djangoscheduler.scheduler.schedule_job import job_scheduler
from djangoscheduler import task_scheduler

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all().order_by('name')
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        print("----------------------\n")
        print(request.data["date"])
        # print(datetime.strptime(request.data["date"], '%Y-%m-%d %H:%M:%S'))
        print(datetime.fromisoformat(request.data["date"]))
        # now = (datetime.now(timezone.utc)  + timedelta(seconds=3)).strftime('%Y-%m-%d %H:%M:%S')
        # task_scheduler.add_job(job_scheduler,"interval", start_date=now, end_date=now)
        # print("scheduling end")
        return super(BookingViewSet, self).create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return super(BookingViewSet, self).update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return super(BookingViewSet, self).delete(request, *args, **kwargs)

    # def getUpdatedHour(hour): 
    #     if "PM" in hour: