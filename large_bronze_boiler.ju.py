# %%
from sympy import symbols, nsolve, lambdify
fire_casing = symbols('fire_casing')
plate = symbols('plate')
rod = symbols('rod')
frame = symbols('frame')
pipe = symbols('pipe')

frame = 4*rod

fire_casing = 4*plate + 4*rod + frame
fire_casing

pipe_casing = 4*plate + 4*pipe + frame

brick = 6*plate

controller = fire_casing

result = 4*fire_casing + 32*brick + controller + 3*pipe_casing
result


# %%
# Number of bronze required.
f = lambdify([pipe, plate, rod], result)
f(3, 1, 1)
