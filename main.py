class WebPush:

    def __init__(self, Platform = "Chrome", optin = "True", global_frequency_capping = "Three_views_in_24hours", start_date ="09.19.2021", end_date = "10.19.2021", language = "ENG", push_type = "Web Push"):

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

    def __init__(self, push_type):

        self.push_type = push_type
        Trigger_page = "Homepage"
        WebPush.send_push(self)

class BulkPush(WebPush):

    def __init__(self, push_type):

        self.push_type = push_type
        send_date = int(51)
        WebPush.send_push(self)

class SegmentPush(WebPush):

    def __init__(self, push_type):

        self.push_type = push_type

        segment_name = str("Book Searchers")
        WebPush.send_push(self)

class PriceAlertPush(WebPush):

    def __init__(self, push_type):

        self.push_type = push_type
        WebPush.send_push(self)

    @classmethod
    def discountPrice(cls, price_info, discount_rate):

        price_info = price_info
        discount_rate = price_info * discount_rate

        return discount_rate

class InstockPush(WebPush):

    def __init__(self, push_type):

        self.push_type = push_type
        WebPush.send_push(self)

    @classmethod
    def stockUpdate(cls, stock_info):

        stock_info = stock_info.lower()

        if (stock_info == "true"):
            stock_info = "false"

        elif (stock_info == "false"):
            stock_info = "true"

        return stock_info

Web_Push_Nesne = WebPush("Web Push")
Web_Push_Nesne.send_push()
Trigger_Push_Nesne = TriggerPush("Trigger Push")
Bulk_Push_Nesne = BulkPush("Bulk Push")
Segment_Push_Nesne = SegmentPush("Segment Push")
Price_Alert_Nesne = PriceAlertPush("Price Alert Push")


PriceInfo_ = int(input("Please enter Price Info:"))
DiscountRate_ = float(input("Please enter Discount Rate:"))
stock_info = input("Please enter Stock Info Update:")


Instock_Push_Nesne = InstockPush("Instock Push")
updated = Instock_Push_Nesne.stockUpdate(stock_info)

print(updated)

AbouttheDiscount = PriceAlertPush.discountPrice(PriceInfo_, DiscountRate_)

print(AbouttheDiscount)


