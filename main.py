from sources import LazadaBot


bot = LazadaBot()
# bot.scrap(keyword="iphone", n_data=200, output_file="iphone_data", file_type="xlsx")
bot.scrap(keyword="iphone", n_data=50, output_file="iphone_price", file_type='txt')