import os
import csv
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

from datetime import datetime
from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()

def coin_plot(id, vs_currency):
    if not os.path.exists("images"):
        os.mkdir("images")


    price = cg.get_coin_ohlc_by_id(id=id, vs_currency=vs_currency, days=7)
    charts = map(lambda item: [str(datetime.fromtimestamp(item[0]/1000)), item[1], item[2], item[3], item[4]], price)

    # Convert
    fields = ['Time', 'Open', 'High', 'Low', 'Close']

    with open('MKT_test.csv', 'w') as mkt:
        write = csv.writer(mkt)

        write.writerow(fields)
        write.writerows(charts)

    df = pd.read_csv('MKT_test.csv')
    fig = go.Figure(data=[go.Candlestick(x=df['Time'],
                    open=df['Open'],
                    high=df['High'],
                    low=df['Low'],
                    close=df['Close'])])

    fig.update_layout(xaxis_rangeslider_visible=False)
    fig.write_image("images/fig1.png")

    return 

def coin_history(id, args):
    if not os.path.exists("images"):
        os.mkdir("images")

    price = cg.get_coin_market_chart_by_id(id=id, vs_currency=args[0], days=args[-1])

    charts = map(lambda item: [str(datetime.fromtimestamp(item[0]/1000)), item[1]], price['prices'])
    df = pd.DataFrame(charts)

    fig = px.line(df, x=0, y=1, title=f'History ({args[-1]} days)')
    fig.update_yaxes(title='Price')
    fig.update_xaxes(title='Days')
    fig.write_image('images/fig10.png')

    return 

def coin_range(id, vs_currency, s_day, e_day):
    if not os.path.exists("images"):
        os.mkdir("images")

    _from_t = datetime.strptime(s_day, "%d-%m-%Y")
    _to_t = datetime.strptime(e_day, "%d-%m-%Y")
    from_t = datetime.timestamp(_from_t)
    to_t = datetime.timestamp(_to_t)
    
    price = cg.get_coin_market_chart_range_by_id(id=id, vs_currency=vs_currency, from_timestamp=from_t, to_timestamp=to_t)

    charts = map(lambda item: [str(datetime.fromtimestamp(item[0]/1000)), item[1]], price['prices'])
    df = pd.DataFrame(charts)

    fig = px.line(df, x=0, y=1, title=f'History (From: {s_day} | To: {e_day})')
    fig.update_yaxes(title='Price')
    fig.update_xaxes(title='Days')
    fig.update_traces(line_color="#9a0c10")
    fig.write_image('images/fig20.png')

    return
