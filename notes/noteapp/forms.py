from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Note


class TagForm(ModelForm):

    name = CharField(min_length=1, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ["name"]


class NoteForm(ModelForm):

    name = CharField(min_length=1, max_length=50, required=True, widget=TextInput())
    description = CharField(
        min_length=10, max_length=150, required=True, widget=TextInput()
    )

    class Meta:
        model = Note
        fields = ["name", "description"]
        exclude = ["tags"]
