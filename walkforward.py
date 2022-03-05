import vectorbt as vbt
import numpy, pandas

vbt.settings.data['alpaca']['key_id'] = 'yourapikey'
vbt.settings.data['alpaca']['secret_key'] = 'yoursecretkey'

data = vbt.AlpacaData.download('SPY', start='2016-01-01', end='2021-12-15', timeframe='1d', limit=10000)
price = data.get('Close')

# plot the price
# figure = price.vbt.plot(trace_names=['Price'], width=1280, height=720)
# figure.show()

# show returns from optimizing
# windows = numpy.arange(10, 50)
# fast_ma, slow_ma = vbt.MA.run_combs(price, windows)
# entries = fast_ma.ma_crossed_above(slow_ma)
# exits = fast_ma.ma_crossed_below(slow_ma)
# portfolio = vbt.Portfolio.from_signals(price, entries, exits, freq='1d', direction='both')
# print(portfolio.total_return().sort_values())

# show how it performs poorly on data it hasn't seen
# future_data = vbt.AlpacaData.download('SPY', start='2021-06-01', timeframe='1d', limit=10000).get('Close')
# fast_ma = vbt.MA.run(future_data, 30)
# slow_ma = vbt.MA.run(future_data, 40)
# entries = fast_ma.ma_crossed_above(slow_ma)
# exits = fast_ma.ma_crossed_below(slow_ma)
# portfolio = vbt.Portfolio.from_signals(future_data, entries, exits, freq='1d', direction='both')
# print(portfolio.total_return())

# show split data on a figure
# figure = price.vbt.rolling_split(n=20, window_len=360, set_lens=(108,), left_to_right=False, plot=True)
# figure.update_layout(width=1280, height=720)
# figure.show()

# store split data in tuples
# (in_sample_prices, in_sample_dates), (out_sample_prices, out_sample_dates) = price.vbt.rolling_split(n=20, window_len=360, set_lens=(108,), left_to_right=False)

#print(in_sample_dates)
#print(out_sample_dates)
#print(out_sample_prices[19])

# run combinations on in sample dates, sort by sharpe ratio
# windows = numpy.arange(10, 50)
# fast_ma, slow_ma = vbt.MA.run_combs(in_sample_prices, windows)
# entries = fast_ma.ma_crossed_above(slow_ma)
# exits = fast_ma.ma_crossed_below(slow_ma)
# portfolio = vbt.Portfolio.from_signals(in_sample_prices, entries, exits, freq='1d', direction='both')
# performance = portfolio.sharpe_ratio()
# print(performance[performance.groupby('split_idx').idxmax()].index)
