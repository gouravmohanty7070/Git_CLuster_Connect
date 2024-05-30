# Git_CLuster_Connect


## Project Overview

This Django application includes two main features:

1\. **GitHub Connect**: Allows users to connect to their GitHub account, authorize the application, and fetches their public and private repositories.

2\. **Cluster Data API**: Provides an API endpoint to fetch cluster details stored in the database.

## Features

### GitHub Connect

- Connects to GitHub using OAuth authentication.

- Fetches all public and private repositories of the authenticated user.

- Stores the repository details in a Django model.

### Cluster Data API

- Provides an endpoint that returns cluster data in JSON format.

- Stores cluster details in a Django model with fields such as `ClusterId`, `ClusterName`, `Region`, etc.

## Setup Instructions

### Prerequisites

- Python 3.x

- Django 3.x or later

- A GitHub account

### Steps

1\. **Clone the repository:**
      
  
    git clone https://github.com/gouravmohanty7070/Git_CLuster_Connect.git
    cd Git_Cluster_Connect
    

2\. **Create a virtual environment and activate it:**
      
    python -m venv env
    source env/bin/activate  
    # On Windows use `env\Scripts\activate`

3\. **Install the dependencies:**
    
    pip install -r requirements.txt
    
4\. **Create a `.env` file in the root directory of the project (where `manage.py` is located) and add your GitHub credentials:**

    GITHUB_CLIENT_ID=your_client_id
    GITHUB_CLIENT_SECRET=your_client_secret
    

5\. **Set the User authorization callback URL in your GitHub App settings to:**
    
    http://127.0.0.1:8080/github-connect/
    
6\. **Run the migrations:**
    
    python manage.py makemigrations
    python manage.py migrate

7\. **Create a superuser to access the Django admin interface where you can see all the repos and cluster data:**
     
    python manage.py createsuperuser

8\. **Run the Django development server:**
    
    python manage.py runserver 8080

9\. **Access the GitHub Connect module:**

    - Visit `http://127.0.0.1:8080/github-connect/` in your browser.

    - You will be redirected to GitHub to authorize the application.

    - After authorization, you will be redirected back to your application, and the repositories will be fetched and stored.

10\. **Access the Cluster Data API:**

    - Visit `http://127.0.0.1:8080/cluster/` to see the JSON response of the cluster details.

11\. **Access the Django admin interface:**

    - Visit `http://127.0.0.1:8080/admin/` to view and manage the stored repositories and cluster details.

## Populating Cluster Data

To populate the `ClusterDetails` model with sample data, you can either use the Django admin interface or run a custom management command.

### Option 1: Using Django Admin Interface

- Ensure the `ClusterDetails` model is registered in the admin interface.

  ```python

  # myapp/admin.py

  from django.contrib import admin

  from .models import ClusterDetails

  admin.site.register(ClusterDetails)

  ```

- Run the Django development server and log in to the admin interface at `http://127.0.0.1:8080/admin/`.

- Add some sample data to the `ClusterDetails` model.

### Option 2: Using a Script

Write a Django management command to populate the database with sample data.

```python

# myapp/management/commands/populate_clusters.py

from django.core.management.base import BaseCommand

from myapp.models import ClusterDetails

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

```

Run the command to populate the database:

```bash

python manage.py populate_clusters

```

By following these steps, you will have a fully functional Django application that can connect to GitHub, retrieve repository information, and display it, as well as provide an API endpoint for cluster data.

If you encounter any issues or have any questions, feel free to reach out for assistance!

---
