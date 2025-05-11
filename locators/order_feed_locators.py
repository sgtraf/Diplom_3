from selenium.webdriver.common.by import By


class OrderFeedPageLocators:

    CARD_ORDER_FEED = (By.XPATH, "//p[@class='text text_type_digits-default']")
    NUMBER_CARD_ORDER_FEED = (By.XPATH, ".//p[@class='text text_type_digits-default mb-10 mt-5']")
    CARD_ORDER_WINDOW_UPDATED = (By.XPATH, ".//div[@class='Modal_modal__P3_V5']")
    NUMBER_ORDER_UPDATED = (By.XPATH, "//h2[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m "
                                      "text text_type_digits-large mb-8']")
    LIST_OF_ORDER = (By.XPATH, "//ul[@class='OrderFeed_list__OLh59']/li[1]")
    TOTAL_ORDERS = (By.XPATH, ".//div[@class='undefined mb-15']/p[@class='OrderFeed_number__2MbrQ text "
                              "text_type_digits-large']")
    DAY_ORDERS = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/parent::*/p[@class='OrderFeed_number__2MbrQ "
                            "text text_type_digits-large']")
    IN_WORK = (By.XPATH, ".//ul[@class ='OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi']/li")
