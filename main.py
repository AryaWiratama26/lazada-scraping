from sources import LazadaBot


bot = LazadaBot()
bot.scrap(keyword="iphone", n_data=40, output_file="iphone_price", file_type="csv")
# bot.scrap(keyword="iphone", n_data=40, output_file="iphone_price", file_type='txt')