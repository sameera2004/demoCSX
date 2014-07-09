from __conf import conf_dict


def parseList(conf_list):
    conf_list = conf_list.replace('[', '')
    conf_list = conf_list.replace(']', '')
    env_list = list()
    temp_env_list = conf_list.split(',')
    for entry in temp_env_list:
        env_list.append(int(entry))
    return env_list

"""
Motor Config Import
"""
delta = conf_dict.get('motors', 'delta')
theta = conf_dict.get('motors', 'theta')
chi = conf_dict.get('motors', 'chi')
phi = conf_dict.get('motors', 'phi')
mu = conf_dict.get('motors', 'mu')
gamma = conf_dict.get('motors', 'gamma')


"""
Diffractometer Config Import
"""
geometry = conf_dict.get('diffractometer', 'geometry')
wavelength = conf_dict.get('diffractometer', 'wavelength')
ub_name = conf_dict.get('diffractometer', 'ub_name')
lattice_geometry = conf_dict.get('diffractometer', 'lattice_geometry')
a = conf_dict.get('diffractometer', 'a')
b = conf_dict.get('diffractometer', 'b')
c = conf_dict.get('diffractometer', 'c')
alpha = conf_dict.get('diffractometer', 'alpha')
beta = conf_dict.get('diffractometer', 'beta')
gamma = conf_dict.get('diffractometer', 'gamma')
two_theta = parseList(conf_dict.get('diffractometer', 'two_theta'))
hardware_positions_1 = parseList(conf_dict.get('diffractometer', 'hardware_positions_1'))
reflection_1 = parseList(conf_dict.get('diffractometer', 'reflection_1'))
hardware_positions_2 = parseList(conf_dict.get('diffractometer', 'hardware_positions_2'))
reflection_2 = parseList(conf_dict.get('diffractometer', 'reflection_2'))

"""
Detector Config Import
"""
detector_1 = conf_dict.get('detectors', 'detector_1')
detector_2 = conf_dict.get('detectors', 'detector_2')

