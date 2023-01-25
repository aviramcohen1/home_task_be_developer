def Price_Check(products, productPrices, productSold, soldPrice):
    '''

    :param products: each products[i] is the name of an item for sale
    :param productPrices: each productPrices[i] is the price of products[i]
    :param productSold: each productSold[j] is the name of a product sold
    :param soldPrice: each soldPrice[j] contains the sale price recorded for productSold[j]
    :return: The number of sale prices that were entered incorrectly
    '''
    incorrect_prices = 0
    try:
        if len(productSold) != len(soldPrice):
            raise ValueError("The number of products sold and sold prices must be the same.")
        if len(products) != len(productPrices):
            raise ValueError("The number of products and prices must be the same.")
        if len(productSold) < 1 or len(productSold) > 99:
            raise ValueError("The number of products sold must be between 1 and 99.")
        if len(products) < 1 or len(products) > 99:
            raise ValueError("The number of products must be between 1 and 99.")
        product_prices = dict(zip(products, productPrices))#union 2 list do dict for
        # used to map the products' names to their respective prices
        for i in range(len(productSold)):
            if soldPrice[i] < 1.00 or soldPrice[i] > 100000.00:
                raise ValueError("The sold prices must be between 1.00 and 100000.00.")
            if productPrices[i] < 1.00 or productPrices[i] > 100000.00:
                raise ValueError("The product prices must be between 1.00 and 100000.00.")
            if productSold[i] not in products:
                raise ValueError(f"{productSold[i]} is not in products list.")
            correct_price = product_prices[productSold[i]]
            if soldPrice[i] != correct_price:
                incorrect_prices += 1
    except ValueError as error:
        print(error)
    return incorrect_prices



