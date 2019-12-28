from django.db import models


class ProjectInformation(models.Model):

    Application_Owner = models.CharField(max_length=1000, null=True, blank=True)
    Support_Team_Group_Name = models.CharField(max_length=1000, null=True, blank=True)
    Application_Server_Name = models.CharField(max_length=1000, null=True, blank=True)
    Application_Server_IP = models.CharField(max_length=1000, null=True, blank=True)
    Server_OS_Version = models.CharField(max_length=1000, null=True, blank=True)
    Database_Server_Name = models.CharField(max_length=1000, null=True, blank=True)
    Database_Server_IP = models.CharField(max_length=1000, null=True, blank=True)
    Database_Name = models.CharField(max_length=1000, null=True, blank=True)
    Database_Version = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return "ProjectInformation: {}".format(self.Application_Owner)


class ProductionProjectInformation(models.Model):

    Application_Owner = models.CharField(max_length=1000, null=True, blank=True)
    Support_Team_Group_Name = models.CharField(max_length=1000, null=True, blank=True)
    Application_Server_Name = models.CharField(max_length=1000, null=True, blank=True)
    Application_Server_IP = models.CharField(max_length=1000, null=True, blank=True)
    Server_OS_Version = models.CharField(max_length=1000, null=True, blank=True)
    Database_Server_Name = models.CharField(max_length=1000, null=True, blank=True)
    Database_Server_IP = models.CharField(max_length=1000, null=True, blank=True)
    Database_Name = models.CharField(max_length=1000, null=True, blank=True)
    Database_Version = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return "ProjectInformation: {}".format(self.Application_Owner)
