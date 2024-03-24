# ORATS Data col definitions
## ORATS Data col definitions

['ticker', 'cOpra', 'pOpra', 'stkPx', 'expirDate', 'yte', 'strike',
       'cVolu', 'cOi', 'pVolu', 'pOi', 'cBidPx', 'cValue', 'cAskPx', 'pBidPx',
       'pValue', 'pAskPx', 'cBidIv', 'cMidIv', 'cAskIv', 'smoothSmvVol',
       'pBidIv', 'pMidIv', 'pAskIv', 'iRate', 'divRate', 'residualRateData',
       'delta', 'gamma', 'theta', 'vega', 'rho', 'phi', 'driftlessTheta',
       'extVol', 'extCTheo', 'extPTheo', 'spot_px', 'trade_date']

These are the columns in ORATS data 

| Column Name    | Description                                                                           |
|----------------|---------------------------------------------------------------------------------------|
| ticker         | Ticker symbol of the underlying asset                                                  |
| cOpra          | Reference number or identifier for call options                                         |
| pOpra          | Reference number or identifier for put options                                          |
| stkPx          | Stock price or spot price of the underlying asset                                       |
| expirDate      | Expiration date of the options contracts                                                |
| yte            | Year To Expiration - Time to expiration of the options contracts in years               |
| strike         | Strike price of the options contracts                                                   |
| cVolu          | Volume (number of contracts traded) for call options                                    |
| cOi            | Call Open Interest - Total number of outstanding (open) call options contracts           |
| pVolu          | Volume for put options                                                                 |
| pOi            | Put Open Interest - Total number of outstanding (open) put options contracts             |
| cBidPx         | Bid price for call options                                                             |
| cAskPx         | Ask price for call options                                                             |
| cValue         | Value of call options traded                                                           |
| pBidPx         | Bid price for put options                                                              |
| pAskPx         | Ask price for put options                                                              |
| pValue         | Value of put options traded                                                            |
| cBidIv         | Bid implied volatility for call options                                                 |
| cMidIv         | Mid implied volatility for call options                                                 |
| cAskIv         | Ask implied volatility for call options                                                 |
| pBidIv         | Bid implied volatility for put options                                                  |
| pMidIv         | Mid implied volatility for put options                                                  |
| pAskIv         | Ask implied volatility for put options                                                  |
| smoothSmvVol   | Smoothed historical volatility                                                         |
| iRate          | Interest rate                                                                         |
| divRate        | Dividend rate                                                                         |
| residualRateData | Residual rate data (purpose unclear)                                                   |
| delta          | Delta - Sensitivity measure for options contracts                                       |
| gamma          | Gamma - Sensitivity measure for options contracts                                       |
| theta          | Theta - Sensitivity measure for options contracts                                       |
| vega           | Vega - Sensitivity measure for options contracts                                        |
| rho            | Rho - Sensitivity measure for options contracts                                         |
| phi            | Phi - Sensitivity measure for options contracts                                         |
| driftlessTheta | Driftless theta - Another sensitivity measure for options contracts                    |
| extVol         | External volatility                                                                    |
| extCTheo       | External call theoretical value                                                         |
| extPTheo       | External put theoretical value                                                          |
| spot_px        | Spot price of the underlying asset                                                      |
| trade_date     | Date on which the trades occurred                                                       |


These columns collectively provide various pieces of information about the options contracts traded on a particular trading day, including their prices, volumes, implied volatilities, Greeks, and other relevant details.


## What we can interpret from this mean implied volatility skew?
The mean implied volatility skew provides insight into the overall sentiment or behavior of options traders regarding the underlying asset. Here's what you can interpret from the mean implied volatility skew:

1. **Direction of Skew**:
   - Positive Skew: A positive mean implied volatility skew suggests that call options (OTM) tend to have higher implied volatility compared to put options (OTM). This could indicate bullish sentiment, as traders are more willing to pay higher premiums for call options, anticipating upward price movements.
   - Negative Skew: Conversely, a negative mean implied volatility skew indicates higher implied volatility for put options compared to call options. This might imply bearish sentiment, as traders are willing to pay higher premiums for put options, anticipating downward price movements.

2. **Market Sentiment**:
   - Bullish Sentiment: A positive mean implied volatility skew may suggest overall bullish sentiment in the market, as traders are more interested in buying call options to capitalize on potential price increases.
   - Bearish Sentiment: Conversely, a negative mean implied volatility skew may indicate bearish sentiment, with traders preferring to buy put options to hedge against potential price declines or speculate on downward movements.

3. **Risk Perception**:
   - Risk Perception: Implied volatility skew reflects traders' perception of risk. A steeper skew, whether positive or negative, indicates a greater perceived risk in one direction (up or down). For example, a steep positive skew suggests higher perceived risk of upside movements, while a steep negative skew indicates higher perceived risk of downside movements.

4. **Trading Strategies**:
   - Option Trading Strategies: Traders can use the information from implied volatility skew to formulate trading strategies. For example, they might consider selling overpriced options (calls or puts) with high implied volatility or constructing spreads to take advantage of the skew.

5. **Market Conditions**:
   - Market Conditions: Changes in the mean implied volatility skew over time can indicate shifts in market sentiment, changes in supply and demand dynamics for options, or adjustments in the perceived risk environment.

Overall, the mean implied volatility skew provides valuable information about market sentiment, risk perception, and potential trading opportunities in the options market. However, it's essential to consider other factors and conduct further analysis to make informed trading decisions.