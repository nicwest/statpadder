from distutils.core import setup
import py2exe, sys, os

data_path = 'C:\\Users\\Nic\\PycharmProjects\\statpadder\\data\\'

sys.argv.append('py2exe')
setup(
    options={
       "py2exe" : {
           "includes" : ["sip",],
           "bundle_files": 3,
           "optimize": 2,
       }
    },
    windows = [{'script': "statpadder.py", "icon_resources": [(1, os.path.join(data_path, "logo.ico"))]}],

    data_files = [
        ('imageformats', [r'C:\Python27\Lib\site-packages\PyQt4\plugins\imageformats\qico4.dll']),
        ('data', [
            os.path.join(data_path, 'logo.ico'),
            os.path.join(data_path, 'maps.json'),
            os.path.join(data_path, 'settings.png'),
            os.path.join(data_path, 'structures_10.json'),
            os.path.join(data_path, 'structures_17.json'),
            os.path.join(data_path, 'structures_18.json'),
            os.path.join(data_path, 'structures_20.json'),
            os.path.join(data_path, 'structures_22.json'),
            os.path.join(data_path, 'structures_24.json'),
            os.path.join(data_path, 'structures_26.json'),
            os.path.join(data_path, 'structures_27.json'),
            os.path.join(data_path, 'structures_28.json'),
            os.path.join(data_path, 'structures_29.json'),
            os.path.join(data_path, 'structures_65.json'),
            os.path.join(data_path, 'structures_69.json'),
            os.path.join(data_path, 'tanks.json'),
        ])
    ]
)