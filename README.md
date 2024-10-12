Exponential Growth Forecast Model: Electric Vehicle (EV) Registrations
This script is designed to model and forecast the growth of electric vehicle (EV) registrations using an exponential growth curve. It fits historical EV registration data (up to the year 2023) and forecasts EV registrations for the next five years using an exponential growth model.

1)Data Preparation

The dataset ev_registration_counts is filtered to include only years up to and including 2023, assuming that data for these years is complete.
The dataset is indexed by year, and the values represent the number of EV registrations for each year.

Exponential Growth Function

The exponential growth function is defined as:
𝑦 = 𝑎⋅𝑒𝑏⋅𝑥
y=a⋅e 
b⋅x
where:
x is the year (adjusted to start from year zero),
a and b are the parameters to be fitted.

This function models exponential growth in EV registrations.
Using the curve_fit method from scipy.optimize, the script fits the historical EV registration data to the exponential growth function.
Parameters a and b are estimated through the fitting process.

Forecasting

With the fitted exponential growth model, the script generates forecasts for EV registrations for the years 2024 through 2029 (next 6 years).
The forecasted values are stored in a dictionary for easy reference, with keys as the forecasted years and values as the predicted EV registrations.
