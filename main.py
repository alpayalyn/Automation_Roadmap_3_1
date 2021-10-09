class WebPush:

    def __init__(self, Platform, optin, global_frequency_capping, start_date, end_date, language, push_type):

        self.Platform = Platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print("‘Push gönderildi!{}’".format(self.push_type))

class TriggerPush(WebPush):

    def __init__(self, Platform, optin, global_frequency_capping, start_date, end_date, language, push_type):

        super().__init__(Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        Trigger_page = "Homepage"
        WebPush.send_push(self)

class BulkPush(WebPush):

    def __init__(self, Platform, optin, global_frequency_capping, start_date, end_date, language, push_type):

        super().__init__(Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        send_date = int(51)
        WebPush.send_push(self)

class SegmentPush(WebPush):

    def __init__(self, Platform, optin, global_frequency_capping, start_date, end_date, language, push_type):

        super().__init__(Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        segment_name = str("Book Searchers")
        WebPush.send_push(self)

class PriceAlertPush(WebPush):

    def discountPrice(price_info, discount_rate):


        discount_rate = price_info * discount_rate

        return discount_rate

class InstockPush(WebPush):

    def __init__(self, Platform, optin, global_frequency_capping, start_date, end_date, language, push_type):

        super().__init__(Platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        WebPush.send_push(self)

    def stockUpdate(stock_info):

        if(stock_info == True):

            stock_info = False

        else:
            stock_info = True

        return stock_info

Web_Push_Nesne = WebPush("Chrome", True, "Three_views_in_24hours", "09.19.2021", "10.19.2021", "ENG", "Trigger Push")
Trigger_Push_Nesne = TriggerPush("Chrome", True, "Three_views_in_24hours", "09.19.2021", "10.19.2021", "ENG", "Trigger Push")
Bulk_Push_Nesne = BulkPush("Chrome", True, "Three_views_in_24hours", "09.19.2021", "10.19.2021", "ENG", "Bulk Push")
Segment_Push_Nesne = SegmentPush("Chrome", True, "Three_views_in_24hours", "09.19.2021", "10.19.2021", "ENG", "Segment Push")

PriceInfo_ = int(input("Please enter Price Info:"))
DiscountRate_ = float(input("Please enter Discount Rate:"))
stock_info = bool(input("Please enter Stock Info Update:"))

Instock_Push_Nesne = InstockPush("Chrome", True, "Three_views_in_24hours", "09.19.2021", "10.19.2021", "ENG", "Instock Push")

AbouttheDiscount = PriceAlertPush.discountPrice(PriceInfo_, DiscountRate_)
print(AbouttheDiscount)

