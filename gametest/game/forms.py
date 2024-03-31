from django import forms
from .models import Review,Phonedata,Gamedata,RATE_CHOICES


class ReviewForm(forms.ModelForm):
    phonecategory = forms.ModelChoiceField(queryset=Phonedata.objects.all(),label='機種')
    gamecategory = forms.ModelChoiceField(queryset=Gamedata.objects.all(),label="ゲーム名")
    title = forms.CharField(label='タイトル')
    rate = forms.ChoiceField(choices=RATE_CHOICES, label='評価')
    text = forms.CharField(widget=forms.Textarea,label='詳細')
    image = forms.ImageField(label='画像', required=False)


    class Meta:
        model = Review
        fields = ['phonecategory', 'gamecategory', 'title', 'rate', 'text','image'] 