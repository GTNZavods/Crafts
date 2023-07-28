# %% [markdown]
# # High Pressure Solar Boiler
# Calculating distilled water requirements
# https://github.com/GTNewHorizons/GT5-Unofficial/pull/487

# %%
from math import ceil

# %%
def num_of_basic_turbines_required(voltage):
    return voltage / 32

SOLAR_BOILER_OUTPUT = 360

# %%
water_required_for_solar_boiler = SOLAR_BOILER_OUTPUT / 160
water_required_for_solar_boiler

# %% [markdown]
# Calculating production power required for that via simple water distillation.

# %%
distilled_water_generated_per_sec = 5 / 0.8
distilled_water_generated_per_sec

# %%
number_of_distillaries_for_one_boiler = water_required_for_solar_boiler / distilled_water_generated_per_sec
number_of_distillaries_for_one_boiler

# %% [markdown]
# For our amount of solar boilers we will need:

# %%
NUM_OF_BOILERS = 24
number_of_distillaries = ceil(NUM_OF_BOILERS * number_of_distillaries_for_one_boiler)

# %% [markdown]
# Each distillery costs 10 EU/t

# %%
total_voltage_required = number_of_distillaries * 10
total_voltage_required

# %%
num_of_basic_turbines_required(total_voltage_required)

# %% [markdown]
# It will be almost half of what we get:

# %%
basic_turbine_per_solar_boiler = SOLAR_BOILER_OUTPUT / 1552
basic_turbine_per_solar_boiler

# %%
total_basic_turbines = NUM_OF_BOILERS * basic_turbine_per_solar_boiler
total_basic_turbines

# %% [markdown]
# Calculating production power required for
# that via electrolyzer and distillery combo.

# %%
from sympy import symbols
distilled_water = symbols('distilled_water')

distilled_water = (500 * oxygen + 1000 * hydrogen) / 500 # 1 L

distilled_water_t = symbols('distilled_water_t')

# distilled_water_t = 500 / 0.25 + oxygen_t + hydrogen_t

# distilled_water, distilled_water_t

# %% [markdown]
# 54 L of distilled_water for 24 boilers to run them for 1s.
# 
# Therefore one chemical reactor will be enough for `distilled_water_t`:

# %%
distilled_water_t = ( 500 / 0.25 ) / 54
distilled_water_t

# %% [markdown]
# For that you will need to supply it with 30 EU/t:

# %%
total_voltage_required = 0
total_voltage_required += 30

# %% [markdown]
# Also you'll need `hydrogen` L of hydrogen and `oxygen` L of oxygen to
# perform this operation. Both of these can be acquired through electrolysis:

# %%
oxygen, hydrogen = symbols('oxygen, hydrogen')
oxygen_t, hydrogen_t = symbols('oxygen_t, hydrogen_t')
oxygen = 500 * 4
hydrogen = 1000 * 4

# %% [markdown]
# Time needed to get these amount in electrolyzer:

# %%
oxygen_t = 50 * 4
hydrogen_t = oxygen_t

# %% [markdown]
# For that operation you'll need 30 EU/t:

# %%
number_of_electrolyzers = ceil(oxygen_t / distilled_water_t)
number_of_electrolyzers

# %%
total_voltage_required += 30 * number_of_electrolyzers

# %% [markdown]
# Finally, resources and time needed:

# %%
total_voltage_required
