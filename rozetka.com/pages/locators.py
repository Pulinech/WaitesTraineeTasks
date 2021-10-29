from selene import query


class SearchPageLocators:
    open_computers_and_notebooks = s("//ul[contains(@class, 'menu-categories_type_main')]"
                                     "//a[contains(@href, 'computers-notebooks')]")
    open_notebooks = s("//div[@class='tile-cats']//a[contains(@href, 'notebooks')]")
