import importlib.util as ilu
folder = '/.../importTest/folderB'
file = 'myFunction'
spec = ilu.spec_from_file_location(file, folder)
your_lib = ilu.module_from_spec(spec)
spec.loader.exec_module(your_lib)
your_lib.do_something()