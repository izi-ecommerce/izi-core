from decimal import Decimal as D

from izi.apps.shipping.methods import Free, FixedPrice
from izi_shipping.methods import SelfPickup, ApiBased
from izi.apps.shipping.repository import Repository as CoreRepository


class Repository(CoreRepository):
    """
    This class is included so that there is a choice of shipping methods.
    IZI's default behavior is to only have one which means you can't test
    the shipping features of PayPal.
    """
    # Here we will list all the supported shipping method... , ApiBased()
    methods = [Free(), FixedPrice(D('10.00'), D('10.00')), SelfPickup(), ]
