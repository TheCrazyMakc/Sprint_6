from selenium.webdriver.common.by import By


class MainPageLocators:
    # Баян. Это «параметризованный локатор», {0} — плейсхолдер для подстановки.
    # На странице элементы аккордеона имеют одинаковые id с разными числами на конце
    # Чтобы не писать 16 отдельных локаторов, используем шаблон.
    QUESTION_TEMPLATE = (By.XPATH, "//div[@id='accordion__heading-{0}']")
    ANSWER_TEMPLATE = (By.XPATH, "//div[@id='accordion__panel-{0}']")

    # Кнопка заказа вверху страницы
    ORDER_BUTTON_HEADER = (By.XPATH, '//button[contains('
                                     '@class, "Button_Button") and contains('
                                     'text(), "Заказать")]')
    # Класс кнопки Button_Button__ra12g, но хэш ra12g может меняться
    # Поэтому строгий локатор лучше не использовать
    # (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    # Вместо этого используем contains здесь и далее


    # Кнопка заказа в середине страницы
    ORDER_BUTTON_MIDDLE = (By.XPATH, '//button[contains(@class,'
                                     ' "Button_Button") and contains('
                                     '@class, "Button_Middle") and contains('
                                     'text(), "Заказать")]')
