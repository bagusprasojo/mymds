from django import forms
from store.models import Product

class ProductForm(forms.ModelForm):
    #rapikan file input
    image = forms.ImageField(required=False, error_messages={'Invalid':{"Image File  Only"}}, widget=forms.FileInput)

    class Meta:
        model = Product
        fields = ('product_name','product_description','is_available','image','category')

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            # print(field)

            if field == 'is_available':
                self.fields[field].widget.attrs["class"] = 'form-check-input'
            else:
                self.fields[field].widget.attrs["class"] = 'form-control'

            if field == 'product_description':
                self.fields[field].widget.attrs["rows"] = '3'
                print(self.fields[field].widget.attrs)
