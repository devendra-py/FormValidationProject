from django import forms

# creating  a class in and extending forms class
class LengthException(Exception):
    pass
class ContactForm(forms.Form):
    Name=forms.CharField(required=True,max_length=30)
    Email=forms.EmailField(required=True)
    City=forms.ChoiceField(choices=[('hyderabad','HYD'),
                                   ('chennai','CHE'),
                                   ('bangalore','BAN')
                                   ]
                           )
    Mobile=forms.CharField(max_length=10)

# name Validation
def clean_Name(self):
    data=self.cleaned_data['Name']
    if len(data)<=3:
        raise forms.ValidationError('name must be at least 4 charecters')
    return  data
# Email Validation
def cleaned_Email(self):
    data=self.cleaned_data['Email']
    if not data.endswith(".com"):
        raise forms.ValidationError(' email Must me ends wih .com')
    return data

# validation for city
def clean_City(self):
    data=self.cleaned_data("City")
    if data=='None':
        raise forms.ValidationError('pls chose one city')
    return data

# validation For Mobile
def clean_Mobile(self):
    data=self.cleaned_data("Mobile")
    try:
        if len(data)!=10:
            raise LengthException('mobile no should be 10 digits ')
        else:
            data=int(data)

    except:
        raise forms.ValidationError('mobile No should be degits ')
    return data



