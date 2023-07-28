# %% [markdown]
# # Large Bronze Boiler

# %%
from sympy import symbols
fire_casing, plate, rod, frame, pipe = symbols('fire_casing, plate, rod, frame, pipe')

frame = 4*rod

fire_casing = 4*plate + 4*rod + frame
fire_casing

pipe_casing = 4*plate + 4*pipe + frame

brick = 6*plate

controller = fire_casing

result = 4*fire_casing + 32*brick + controller + 3*pipe_casing
result

# %% [markdown]
# Number of bronze required:

# %%

from sympy import lambdify

f = lambdify([pipe, plate, rod], result)
f(3, 1, 1)

# %% [markdown]
# Number of Water Tanks required:

# Source for humidity formula: https://gtnh.miraheze.org/wiki/Water_Tank

# %%
from math import ceil

boiler_water_input = 800 / 150

humidity = symbols('humidity')

tank_output = lambdify(humidity, humidity / 10 * 2.5 / 20)
tank_output_in_caniforous = tank_output(50)

number_of_water_tanks_required = ceil(boiler_water_input / tank_output_in_caniforous)
number_of_water_tanks_required

# %% [markdown]
# Materials needed for water tanks:

# %%

