from django import forms
from django.conf import settings

from izi.core.loading import get_model
from izi.forms.mixins import PhoneNumberMixin

UserAddress = get_model('address', 'useraddress')


class AbstractAddressForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """
        Set fields in IZI_REQUIRED_ADDRESS_FIELDS as required.
        """
        super().__init__(*args, **kwargs)
        field_names = (set(self.fields) &
                       set(settings.IZI_REQUIRED_ADDRESS_FIELDS))
        for field_name in field_names:
            self.fields[field_name].required = True


class UserAddressForm(PhoneNumberMixin, AbstractAddressForm):

    class Meta:
        model = UserAddress
        fields = [
            'title', 'first_name', 'last_name',
            'line1', 'line2', 'line3', 'line4',
            'state', 'postcode', 'country',
            'phone_number', 'notes',
        ]

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.instance.user = user
