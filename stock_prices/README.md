# Stock Prices

You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock.

Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices.

## Testing

Run the test file by executing `python test_stock_prices.py`.

You can also test your implementation manually by executing `python stock_prices.py [integers_separated_by_a_single_space]`

## Hints

For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices.

So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`?

function find_max_profit(list_of_stock_prices)
should return maximum profit from single buy and sell, must buy(find) lowest first before selling(find) highest
highest should minus lowest to find profit

    current_min_price = list_of_stock_prices[0]
    max_profit_so_far = list_of_stock_prices[1] - list_of_stock_prices[0]

    go over a list of the prices
      for i in list_of_stock_prices starting on the second item since first is assigned
         check to see if the current index minus the current min is greater then current max profit
         if it is, set it as the current max profit
         if it isn't, set i as the current min price

         if i - current_min > max_profit
            max_profit = i - current_min
         if i < current_min
            current_min = i
