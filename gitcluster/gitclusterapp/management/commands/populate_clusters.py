from django.core.management.base import BaseCommand
from gitclusterapp.models import ClusterDetails

class Command(BaseCommand):
    help = 'Populate the ClusterDetails model with sample data'

    def handle(self, *args, **kwargs):
        ClusterDetails.objects.create(
            cluster_id="cluster1",
            cluster_name="Test Cluster 1",
            connection_id="conn1",
            user_id="user1",
            region="us-east-1",
            backend_key="key1",
            cluster_version="1.0",
            disk_size=100,
            min_size=1,
            max_size=10,
            desired_size=5,
            instance_type="t2.medium",
            vpc_name="vpc1",
            vpc_id="vpc-12345",
            public_subnets=["subnet-123", "subnet-456"],
            private_subnets=["subnet-789", "subnet-012"],
            public_subnet_cidr=["10.0.1.0/24", "10.0.2.0/24"],
            private_subnet_cidr=["10.0.3.0/24", "10.0.4.0/24"],
            domain_names=["example.com"],
            cluster_endpoint="http://cluster1.example.com",
            has_created=True,
            lb_url="http://lb1.example.com"
        )
        self.stdout.write(self.style.SUCCESS('Successfully populated ClusterDetails'))
