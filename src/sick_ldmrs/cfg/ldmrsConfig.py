## *********************************************************
## 
## File autogenerated for the sick_ldmrs package 
## by the dynamic_reconfigure package.
## Please do not edit.
## 
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'upper': 'DEFAULT', 'lower': 'groups', 'srcline': 233, 'name': 'Default', 'parent': 0, 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'cstate': 'true', 'parentname': 'Default', 'class': 'DEFAULT', 'field': 'default', 'state': True, 'parentclass': '', 'groups': [], 'parameters': [{'srcline': 259, 'description': 'The angle of the first range measurement.', 'max': 50, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'start_angle', 'edit_method': '', 'default': 50, 'level': 1, 'min': -59, 'type': 'int'}, {'srcline': 259, 'description': 'The angle of the last range measurement.', 'max': 49, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'end_angle', 'edit_method': '', 'default': -50, 'level': 1, 'min': -60, 'type': 'int'}, {'srcline': 259, 'description': 'Scan frequency, 0 = 12.5Hz, 1 = 25 Hz, 2 = 50 Hz', 'max': 2, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'scan_frequency', 'edit_method': '', 'default': 2, 'level': 1, 'min': 0, 'type': 'int'}, {'srcline': 259, 'description': 'Sychronization offset angle in degrees', 'max': 179, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'sync_angle_offset', 'edit_method': '', 'default': 0, 'level': 1, 'min': -180, 'type': 'int'}, {'srcline': 259, 'description': 'Constant or focussed angular resolution type (focussed valid for 12.5Hz scan freq only)', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'constant_angular_res', 'edit_method': '', 'default': True, 'level': 1, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'Frame id of the sensor. Scan messages append scan number (0-3) to this', 'max': '', 'cconsttype': 'const char * const', 'ctype': 'std::string', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'frame_id_prefix', 'edit_method': '', 'default': '/ldmrs', 'level': 3, 'min': '', 'type': 'str'}, {'srcline': 259, 'description': 'Scan messages will use first echo if true, last echo otherwise', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'use_first_echo', 'edit_method': '', 'default': False, 'level': 3, 'min': False, 'type': 'bool'}, {'srcline': 259, 'description': 'high values will smooth time more, low values will track noisy time more', 'max': 1.0, 'cconsttype': 'const double', 'ctype': 'double', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'time_smoothing_factor', 'edit_method': '', 'default': 0.97, 'level': 3, 'min': 0.0, 'type': 'double'}, {'srcline': 259, 'description': 'allowed error (miliseconds) between smooth time and noisy time before step correction is applied, -1 disables time correction', 'max': 500, 'cconsttype': 'const int', 'ctype': 'int', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'time_error_threshold', 'edit_method': '', 'default': 10, 'level': 3, 'min': -1, 'type': 'int'}, {'srcline': 259, 'description': 'Issues a restart with the new parameter value. Note: none of the changes will take effect until this is set', 'max': True, 'cconsttype': 'const bool', 'ctype': 'bool', 'srcfile': '/opt/ros/kinetic/lib/python2.7/dist-packages/dynamic_reconfigure/parameter_generator.py', 'name': 'apply_changes', 'edit_method': '', 'default': False, 'level': 3, 'min': False, 'type': 'bool'}], 'type': '', 'id': 0}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])    
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']
