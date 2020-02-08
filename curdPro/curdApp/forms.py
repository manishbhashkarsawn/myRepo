from django import forms
class InsertingDataForm(forms.Form):
    product_id=forms.IntegerField(
        label='Enter Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )
    product_name=forms.CharField(
        label='Enter Product Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Name'
            }
        )
    )
    product_cost=forms.IntegerField(
        label='Enter Product cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product Cost'
            }
        )
    )
    product_color=forms.CharField(
        label='Enter Product color',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product color'
            }
        )

    )
    product_class=forms.CharField(
        label='Enter Product Class',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product class'
            }
        )
    )
    customer_name=forms.CharField(
        label='Enter Customer Name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Name'
            }
        )
    )
    customer_mobile=forms.IntegerField(
        label='Enter Mobile Number',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Mobile Number'
            }
        )
    )
    customer_email=forms.EmailField(
        label='Enter Email ID',
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Customer Email'
            }
        )
    )


class UpdatingDataForm(forms.Form):
    product_id=forms.IntegerField(
        label='Enter Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )
    product_cost=forms.IntegerField(
        label='Enter Product Cost',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product cost'
            }
        )
    )


class DeletingDataForm(forms.Form):
    product_id=forms.IntegerField(
        label='Enter Product ID',
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Product ID'
            }
        )
    )