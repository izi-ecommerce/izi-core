from django.test import TestCase

from izi.apps.customer.models import ProductAlert
from izi.core.compat import get_user_model
from izi.test.factories import create_product
from izi.test.factories import UserFactory


User = get_user_model()


class TestAnAlertForARegisteredUser(TestCase):

    def setUp(self):
        user = UserFactory()
        product = create_product()
        self.alert = ProductAlert.objects.create(user=user,
                                                 product=product)

    def test_defaults_to_active(self):
        self.assertTrue(self.alert.is_active)
