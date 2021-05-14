from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from proyecto_final.src.elements.inventory_item import InventoryItem


class InventoryItems:
    """Represents any input text element."""
    def __init__(self, loc: tuple, wait: WebDriverWait = None):
        self._wait = wait
        self._loc = loc
        self.__elements = []

    def reload(self):
        """Force reload of inventory items."""
        self.__elements.clear()
        elements = self._wait.until(EC.visibility_of_all_elements_located(self._loc))
        for element in elements:
            inv_item = InventoryItem(self._wait, element)
            self.__elements.append(inv_item)

    def __getitem__(self, key):
        if not self.__elements:
            self.reload()
        return self.__elements[key]

    def __iter__(self):
        self.reload()
        return iter(self.__elements)

    def __len__(self):
        return len(self.__elements)

    def sort(self):
        return self.__elements.sort()

    def reverse_sort(self):
        return self.__elements.sort(reverse=True)

    def get_price(self) -> str:
        self.get_price.get_text()

    def sort_by_price(self):
        return self.__elements.sort(key=self.get_price)

    def sort_by_reverse_price(self):
        return self.__elements.sort(reverse=True, key=self.get_price)