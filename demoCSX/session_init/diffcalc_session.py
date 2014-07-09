__author__ = 'arkilic'

from demoCSX.config.demo_confParser import *
from diffcalc.hkl.you.geometry import SixCircle, FourCircle
from diffcalc.hardware import DummyHardwareAdapter
from diffcalc.diffcalc_ import create_diffcalc


hardware = DummyHardwareAdapter(('delta', 'theta', 'chi', 'phi', 'mu', 'gamma'))
en = hardware.energy

if geometry == 'SixCircle':
    dc = create_diffcalc('you', SixCircle(), hardware)
else:
    raise ValueError('Geometry not supported')

#Create new ub calculation
dc.ub.newub(ub_name)

#Setup lattice
dc.ub.setlat(lattice_geometry, int(a), int(b), int(c), int(alpha), int(beta), int(gamma))

#Calculate two_theta (not necessary but used for demo purposes)

#Setup hardware position and reflections to map the transformation
hardware.position = hardware_positions_1

dc.ub.addref(reflection_1)

dc.ub.addref(reflection_2, hardware_positions_2, en)

dc.ub.ub()

dc.checkub()