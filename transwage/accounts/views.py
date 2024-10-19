from rest_framework import viewsets
from . import models, serializers


class JobViewSet(viewsets.ModelViewSet):

    queryset = models.Job.objects.all()
    serializer_class = serializers.JobSerializer

    def get_queryset(self):
        jobs = super().get_queryset()
        business = self.request.GET.get("business", None)
        if business:
            jobs = jobs.filter(business__name=business)
        return jobs


class ContractViewSet(viewsets.ModelViewSet):

    queryset = models.Contract.objects.all()
    serializer_class = serializers.ContractSerializer

    def get_queryset(self):
        contracts = super().get_queryset()
        business = self.request.GET.get("business", None)
        if business:
            contracts = contracts.filter(jobs__business__name=business)
        return contracts
