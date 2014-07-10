__author__ = 'arkilic'


from diffcalc.diffcalc_ import create_diffcalc
from diffcalc.hardware import DummyHardwareAdapter
from diffcalc.hkl.you.geometry import SixCircle


def setUB(ub_name, diffractometer_geometry, lattice_geometry, a, b, c, alpha, beta, gamma, hardware_positions_1,
          hardware_positions_2, reflection_1, reflection_2):
    hardware = DummyHardwareAdapter(('delta', 'theta', 'chi', 'phi', 'mu', 'gamma'))
    en = hardware.energy

    if diffractometer_geometry == 'SixCircle':
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

    return dc


def create_diffractometer(diffractometer_geometry):
    """
    Create  a diffractometer object in order to perform reciprocal space calculations
    :param diffractometer_geometry: SixCircle or FourCircle
    :return: diffcalc.diffcalc object
    """
    hardware = DummyHardwareAdapter(('delta', 'theta', 'chi', 'phi', 'mu', 'gamma'))
    if diffractometer_geometry == 'SixCircle':
        dc = create_diffcalc('you', SixCircle(), hardware)
    else:
        raise ValueError('Geometry not supported')
    return dc


def set_lattice(diffractometer, lattice_geometry, a, b, c, alpha, beta, gamma):
    """
    :param diffractometer: diffcalc.diffcalc object
    :param lattice_geometry: cubic, tetragona, custom, etc...
    :param a: crystal param 1
    :param b: crystal param 2
    :param c: crystal param 3
    :param alpha: crystal angle param 1
    :param beta: crystal angle param 2
    :param gamma: crystal angle param 3
    :return: diffcalc.diffcalc object
    """
    diffractometer.ub.setlat(lattice_geometry, int(a), int(b), int(c), int(alpha), int(beta), int(gamma))
    return diffractometer


def c2th(diffractometer, coordinates):
    """
    Calculates two-theta
    :param diffractometer: diffractometer object used for performing reciprocal space calculations
    :param coordinates:
    :return: result
    """
    if isinstance(coordinates, list):
        result = diffractometer.c2th(coordinates)
    else:
        raise TypeError('Coordinates must be a python list')
    return result


def add_reflection(diffractometer, reflection, hardware_position=None, energy=None):
    """
    Adds a reflection to calculate ub matrix
    :param diffractometer:
    :param reflection:
    :param hardware_position:
    :param energy:
    :return: diffcalc.diffcalc object
    """
    if hardware_position is None and energy is None:
        diffractometer.ub.addref(reflection)
    elif hardware_position is None and energy is not None:
        diffractometer.ub.addref(reflection, energy)
    elif hardware_position is not None and energy is None:
        diffractometer.ub.addref(reflection, hardware_position)
    else:
        diffractometer.ub.addref(reflection, hardware_position, energy)
    return diffractometer


def checkub(diffractometer):
    """
    Provides information regarding UB calculations performed

    :param diffractometer: diffcalc.diffcalc object
    :return: None
    """
    diffractometer.checkub()

def angles_to_hkl(diffractometer, angles, energy=None):
    if energy is not None:
        result = diffractometer.angles_to_hkl(angles, energy)
    else:
        result = diffractometer.angles_to_hkl(angles)
    return result


def constraints(diffractometer, angle, value=None):
    """
    Set hardware constraints in order to
    :param diffractometer:
    :param angle:
    :param value:
    :return:
    """
    if value is None:
        diffractometer.hkl.con(angle)
    else:
        diffractometer.hkl.con(angle, value)
    return diffractometer


def hkl_to_angles(diffractometer, hkl):
    """
    Convert hkl into motor coordinates
    :param diffractometer: diffcalc.diffcalc object
    :param hkl: hkl coordinates list
    :return:hkl coordinates dictionary
    """
    if isinstance(hkl, list):
        result = diffractometer.hkl_to_angles(hkl)
    else:
        raise TypeError('hkl must be a python list')
    return result


