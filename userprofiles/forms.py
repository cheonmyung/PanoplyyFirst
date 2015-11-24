from django import forms



from .models import Profile



class ProfileForm(forms.ModelForm):

	class Meta:
		model = Profile
		fields = [
			#"user",
			#"industry",
			"overview",
			"picture",
			]
		#widgets={
			#"name":forms.TextInput(attrs={'placeholder':'Name','name':'Name','id':'common_id_for_imputfields','class':'input-class_name'}),
		#	"overview":forms.TextInput(attrs={'placeholder':'About Your Company...'}),

		#}  