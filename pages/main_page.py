import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    # Из шаблона делается конкретный локатор вопроса по индексу — например, 
    # для index=2 это accordion__heading-2.
    # То же самое для панели ответа — accordion__panel-2.
    # Скроллит страницу вниз — аккордеон находится в нижней части главной.
    # Кликает по заголовку вопроса → панель раскрывается.
    # Читает текст из панели ответа.
    # Возвращает этот текст.
    @allure.step('Получаем текста ответа для вопроса {index}')
    def get_answer_text(self, index):
        question_locator = self.format_locators(
            MainPageLocators.QUESTION_TEMPLATE, index)
        answer_locator = self.format_locators(
            MainPageLocators.ANSWER_TEMPLATE, index)
        self.scroll_page_down()
        self.click_to_element(question_locator)
        answer_text = self.get_text_from_element(answer_locator)

        return answer_text
