from django.forms import ModelForm
from backup.models import Jobs

class JobsForm(ModelForm):
    class Meta:
        model = Jobs
        fields = ['name', 'type', 'email', 'hostname', 'username', 'password', 'port', 'remotepath', 'ssl']