import pytest

from proyecto_final.src.elements import inventory_items
from proyecto_final.src.elements.inventory_item import InventoryItem
from proyecto_final.src.pages.check_out import CheckOutPage
from proyecto_final.src.pages.login import LoginPage
from proyecto_final.tests.common.test_base import TestBase

_DEF_VALID_USER = 'standard_user'

_DEF_PASSWORD = 'secret_sauce'

INVALID_PASSWORD_MSG = 'Epic sadface: Username and password do not match any user in this service'

USERNAME_IS_REQUIRED_MSG = 'Epic sadface: Username is required'


class TestFinalTestCases(TestBase):

    def test_tc_01(self):
        """Test valid login, inventory page is displayed."""
        page = LoginPage(self.driver)
        page.open()
        inventory = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        assert inventory.get_label() == 'PRODUCTS', 'Inventory page label should be Products'

    def test_tc_02(self):
        """Test invalid login, invalid message is displayed."""
        page = LoginPage(self.driver)
        page.open()
        page.login('standard_user', 'invalid_password')
        error_msg = page.get_error_message()
        assert error_msg is not None, 'Error message should be displayed for invalid login'
        assert error_msg == INVALID_PASSWORD_MSG, f'Error message should be {INVALID_PASSWORD_MSG}'

    def test_tc_03(self):
        """Test login with no username, invalid message is displayed."""
        page = LoginPage(self.driver)
        page.open()
        page.login('', 'invalid_password')
        error_msg = page.get_error_message()
        assert error_msg is not None, 'Error message should be displayed for invalid login'
        assert error_msg == USERNAME_IS_REQUIRED_MSG, f'Error message should be {USERNAME_IS_REQUIRED_MSG}'

    def test_tc_04(self):
        """Test valid login, then user is logged out."""
        page = LoginPage(self.driver)
        page.open()
        inventory = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        header = inventory.header
        header.open_menu()
        header.log_out()
        assert page.get_current_url() == 'https://www.saucedemo.com/'

    def test_tc_05(self):
        """Test that all elements in inventory page have image, title, description, price and button."""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        items = inventory_page.products
        for item in items:
            print(f'Title: {item.get_title()}')
            print(f'Description: {item.get_description()}')
            print(f'Price: {item.get_price()}')
            print(f'Price: {item.get_btn()}')
            assert item.get_title() or item.get_description() or item.get_price() or item.get_btn() is not ""

    def test_tc_06(self):
        """Test that all user is redirected to details page when clicking on image."""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.click_on_image()
        print(f'Title: {details_page.get_title()}')
        print(f'Description: {details_page.get_description()}')
        print(f'Price: {details_page.get_price()}')

    def test_tc_07(self):
        """Test that all user is redirected to details page when clicking on title."""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[1]
        first_item: InventoryItem
        details_page = first_item.click_on_title()
        print(f'Title: {details_page.get_title()}')
        print(f'Description: {details_page.get_description()}')
        print(f'Price: {details_page.get_price()}')

    def test_tc_08(self):
        """Test that all products are sorted from A-Z"""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        sort_value = inventory_page.get_sort_value()
        assert sort_value == 'az'
        items = inventory_page.products
        items2 = items
        items2.sort()
        print(items)
        print(items2)
        assert items == items2

    def test_tc_09(self):
        """Test that all products are sorted from Z-A"""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        inventory_page.sort_by('za')
        items = inventory_page.products
        items2 = items
        items2.reverse_sort()
        assert items == items2
        for item in items:
            print(f'Title: {item.get_title()}')

    def test_tc_10(self):
        """Test that all products are sorted from low-high"""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        inventory_page.sort_by('lohi')
        items = inventory_page.products
        items2 = items
        items2.sort_by_price()
        assert items == items2
        for item in items:
            print(f'Title: {item.get_title()}')
            print(f'Title: {item.get_price()}')

    def test_tc_11(self):
        """Test that all products are sorted from low-high"""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        inventory_page.sort_by('hilo')
        items = inventory_page.products
        items2 = items
        items2.sort_by_reverse_price()
        assert items == items2
        for item in items:
            print(f'Title: {item.get_title()}')
            print(f'Title: {item.get_price()}')

    def test_tc_12(self):
        """"Test that user is able to add items from inventory page"""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        first_item.add_to_cart()
        assert inventory_page.header.get_total_cart_items() == 1

    def test_tc_13(self):
        """"Test that user is able to add items from details page"""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        first_item = inventory_page.products[0]
        first_item: InventoryItem
        details_page = first_item.click_on_title()
        details_page.add_to_cart()
        assert inventory_page.header.get_total_cart_items() == 1

    def test_tc_14(self):
        """"Test that user is able to add multiple items from inventory page"""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        items = inventory_page.products
        for item in range(3):
            inventory_page.products[item].add_to_cart()
            items.reload()
        assert inventory_page.header.get_total_cart_items() == 3

    def test_tc_15(self):
        """"Test that user is able to add multiple items from details page"""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        items = inventory_page.products
        for item in range(3):
            details_page = items[item].click_on_title()
            details_page.add_to_cart()
            details_page.back()
            items.reload()
        assert inventory_page.header.get_total_cart_items() == 3

    def test_tc_16(self):
        """"Test that items selected on inventory page match checkout page items"""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        items = inventory_page.products
        items_title = []
        for item in items:
            item.add_to_cart()
            items_title.append(item.get_title())
            print(item.get_title())
        print('***********')
        checkout_page = inventory_page.header.goto_cart()
        cart = checkout_page.products
        cart_title = []
        for item in cart:
            cart_title.append(item.get_title())
            print(item.get_title())
        assert items_title == cart_title

    def test_tc_17(self):
        """"Test that user can navigate back to inventory page"""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        checkout_page = inventory_page.header.goto_cart()
        inventory_page = checkout_page.continue_shopping()
        assert inventory_page.get_label() == 'PRODUCTS', 'Inventory page label should be Products'

    def test_tc_18(self):
        """"Test that user can navigate to checkout page"""
        page = LoginPage(self.driver)
        page.open()
        inventory_page = page.login(_DEF_VALID_USER, _DEF_PASSWORD)
        checkout_page = inventory_page.header.goto_cart()
        checkout_page.check_out()
        assert self.driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html'



