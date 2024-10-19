from typing import Iterable
from django.db import models
from django.contrib.auth.models import User


class Business(models.Model):
    """Simple business model with employers and employees."""

    name = models.CharField(max_length=64)
    employers = models.ManyToManyField(User)

    def employees(self) -> Iterable[User]:
        # Double for loop, must be a more efficient way to do this
        return [c.employee for j in self.jobs.prefetch_related("contracts") for c in j.contracts]


class Job(models.Model):
    """A description of a particular job type."""

    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    hourly_wage = models.FloatField()
    name = models.CharField(max_length=64)


class Contract(models.Model):
    """A contract for an employee doing a job in a particular time period."""

    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    period_start = models.DateField()
    period_end = models.DateField()
    hours_worked = models.IntegerField()
    hours_total = models.IntegerField()
    salary_total = models.FloatField()
    salary_total = models.FloatField()
