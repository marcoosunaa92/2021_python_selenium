import pytest

from proyecto_final.src.elements.inventory_item import InventoryItem
from proyecto_final.src.pages.inventory import InventorySortOptions
from proyecto_final.src.pages.login import LoginPage
from proyecto_final.tests.common.test_base import TestBase

_DEF_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'

VALID_PRICES = ['$29.99', '$9.99', '$15.99', '$49.99', '$7.99', '$15.99']


class TestInventory(TestBase):

    @pytest.mark.skip
    def test_prices(self):
        """Test inventory prices"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        for index, item in enumerate(inventory.products):
            item: InventoryItem
            assert item.get_price() == VALID_PRICES[index], f'Price for item {index} should be {VALID_PRICES[index]}'
            print('\n')
            print(item.get_title())
            print(item.get_description())
            print(item.get_price())
            print('*' * 80)

    @pytest.mark.skip
    def test_label(self):
        """Test production label."""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        assert inventory.get_label() == 'PRODUCTS', 'Inventory page label should be Products'

    @pytest.mark.skip
    def test_sort(self):
        """Test sort products"""
        login = LoginPage(self.driver)
        login.open()
        inventory = login.login(_DEF_USER, _DEF_PASSWORD)
        inventory.get_sort_value() == InventorySortOptions.A_TO_Z.value, 'Default sort should be A to Z'
        for option in InventorySortOptions:
            inventory.sort_by(option)
            inventory.get_sort_value() == option.value, f'Default sort should be {option.value}'