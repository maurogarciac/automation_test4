from seleniumpagefactory.Pagefactory import PageFactory
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.by import By
from typing import Union


def _element_if_visible(element, visibility=True):
    return element if element.is_displayed() == visibility else False


def visibility_of_n_elements_located(locator: tuple[Union[By, str], str], total: int):
    """ An expectation to validate that the required number of elements are present on the DOM of a
    page and visible.
    'Visibility' implies that the element has a height and width that is greater than 0.

    :param locator: Selenium locator
    :param total: Total number of elements expected

    :returns: A list of {total} Visible WebElements.
    """

    def _predicate(driver):
        result = False
        try:
            [by, selector] = locator
            elements = driver.find_elements(by if isinstance(by, By) else PageFactory.TYPE_OF_LOCATORS[by.lower()],
                                            selector)
            if len(elements) >= total:
                result = []
                e_iter = iter(elements)
                while (element := next(e_iter, None)) is not None and len(result) < total:
                    if _element_if_visible(element):
                        result.append(element)
            result = False if len(result) < total else result
        except StaleElementReferenceException:
            result = False
        return result

    return _predicate
