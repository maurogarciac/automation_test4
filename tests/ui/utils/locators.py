

def get_button_selector(text: str) -> str:
    """Generate a xpath button selector string based on the provided text

        :param text: The string inside the button's internal span (case-sensitive)

        :returns: xpath selector string
    """
    return f'//ancestor::button[span[text()="{text}"]]'


def get_contained_button_selector(text: str, container_selector: str) -> str:
    """Generate a xpath button selector string based on the provided text

        :param text: The string inside the button's internal span (case-sensitive)
        :param container_selector: Selector for object that contains the button

        :returns: xpath selector string
    """
    return f'{container_selector}//ancestor::button[span[text()="{text}"]]'
