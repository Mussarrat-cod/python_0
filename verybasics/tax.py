async def calculate_tax(price):
    tax_rate = 0.10  # 10% tax
    return price * tax_rate

async def process_checkout(item_price):
    # await pauses process_checkout, runs calculate_tax, and brings back the result
    tax_amount = await calculate_tax(item_price)
    
    total_price = item_price + tax_amount
    return total_price


