__author__ = 'arkilic'

from demoCSX.config.demo_confParser import *
from demoCSX.commands.diffcalc_commands import *

diffractometer = setUB(ub_name=ub_name, diffractometer_geometry=geometry, lattice_geometry=lattice_geometry, a=a,
                       b=b, c=c, alpha=alpha, beta=beta, gamma=gamma, hardware_positions_1=hardware_positions_1,
                       hardware_positions_2=hardware_positions_2, reflection_1=reflection_1, reflection_2=reflection_2)

