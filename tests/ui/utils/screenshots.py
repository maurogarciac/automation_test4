import datetime
import os


def make_screenshots_dir(request) -> str:
    """ 
        Create a directory to store screenshots for a test (if it doesn't exist already) 

        Params:
        @request: Pytest request fixture

        Return:
    """
    # Name of the new directory
    new_dir_name: str = f"{datetime.date.today()}-{datetime.datetime.now().hour}hs-{datetime.datetime.now().minute}mins-{request.node.name}"
    cwd: str = os.getcwd()
    screenshots_directory: str = os.path.join(cwd, "screenshots")
    os.makedirs(screenshots_directory, exist_ok = True)
    new_path: str = os.path.join(screenshots_directory, new_dir_name)
    # Checks if a directory exists, and creates it
    candidate: str = new_path
    created: bool = False
    i = 0
    while not created:
        try:
            os.mkdir(candidate)
            created = True
        except:
            i += 1
            candidate = f"{new_path}_{i}"
    return candidate


def save_picture(request, driver: webdriver) -> None:
    # Takes a screenshot of the page, and 
    if driver is not None:
        step_name: str = f"{request.node.name}"
        if context.step.table is not None:
            step_name = f"{step_name}_{context.step.table.iteration}"
        screenshot_file_name_prefix: str = os.path.join(f"{context.current_screenshot_dir}", f"{context.scenario.name}-{context.step.line}")
        driver.find_element_by_tag_name("body").screenshot(f"{screenshot_file_name_prefix}-full.png")
        driver.save_screenshot(f"{screenshot_file_name_prefix}.png")