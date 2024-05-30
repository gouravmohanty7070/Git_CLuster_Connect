from django.db import models

class Repository(models.Model):
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    private = models.BooleanField()
    html_url = models.URLField()
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __str__(self):
        return self.name
    
class ClusterDetails(models.Model):
    cluster_id = models.CharField(max_length=100)
    cluster_name = models.CharField(max_length=100)
    connection_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    backend_key = models.CharField(max_length=100)
    cluster_version = models.CharField(max_length=100)
    disk_size = models.IntegerField()
    min_size = models.IntegerField()
    max_size = models.IntegerField()
    desired_size = models.IntegerField()
    instance_type = models.CharField(max_length=100)
    vpc_name = models.CharField(max_length=100)
    vpc_id = models.CharField(max_length=100)
    public_subnets = models.JSONField()
    private_subnets = models.JSONField()
    public_subnet_cidr = models.JSONField()
    private_subnet_cidr = models.JSONField()
    domain_names = models.JSONField()
    cluster_endpoint = models.CharField(max_length=100)
    has_created = models.BooleanField()
    lb_url = models.CharField(max_length=100)

    def __str__(self):
        return self.cluster_name

