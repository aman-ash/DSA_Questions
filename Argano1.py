def priceCheck(products, productPrices, productSold, soldPrice):
    d = {}
    for i in range(len(products)):
        d[products[i]] = productPrices[i]
    
    count = 0
    for i, product in enumerate(productSold):
        if d[product] != soldPrice[i]:
            count += 1
    
    return count
 
print(priceCheck(['a','b'],[1, 2], ['a'], ['3']))