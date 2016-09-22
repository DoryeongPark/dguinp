from django import forms
from .models import Detail, Comment
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote import fields as summer_fields

class PostForm(forms.ModelForm):
    detail_error = {'required':(u'상세정보를 입력해주세요'),}
    #detail = summer_fields.SummernoteTextFormField(error_messages=detail_error)
    class Meta:
        model = Detail
        fields = ('name','issue','class_detail','file')
        widgets = {
            'summernote': SummernoteWidget(),
            'summernoteinplace': SummernoteInplaceWidget(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
