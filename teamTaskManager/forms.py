from django import forms


class TaskForm(forms.Form):
    name = forms.CharField(max_length=100)
    additional_info = forms.CharField(max_length=100)
    priority = forms.IntegerField(min_value=1, max_value=9)


class WorkerForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    role = forms.ChoiceField(choices=[('backend', 'Backend'), ('frontend', 'Frontend'), ('full stack', 'Full Stack')])
