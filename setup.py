#from setuptools import setup, find_packages
from setuptools import setup



"""
#import imp
#import os

#from jxbase import common_config as cf

# ------------------------
# 这个 for 是用来安装本包的依赖包的
for k,module in enumerate(cf.MODULES_ARR):
	try:
		imp.find_module(module) 				# 这句是到已安装的 python 系统中寻找是否存在已安装的库（或叫包）
	except:
		print('\n\n----No module %s found. Will pip install it now...' % (module))
		os.system('pip install %s' % (module))
		try:
			imp.find_module(module)
		except:
			print("----Can't find %s, may pip install failed." % (module))
		else:
			print('----Find %s after pip install' % (module))
	else:
		print('----%s already exists.' % (module))

"""


setup(
	name='jxbase', 		# 这是安装到 python 目录后的文件名，仅仅是文件名或目录名，不是包名，无法对这个名称进行 import；但如果用 twine upload dist/* 到了 pypi.org 的话，则此处是 pip install 要用到的包名（实际上，pip install 后面跟的是文件名），然后安装到 python 的 lib 之后，依然是文件名，无法用 import 引入。下面那个 packages 参数所指向的包名，才是可以 import 的。
	version='3.1',
	author='Jason Xie',
	author_email='xjxfly@qq.com',
	description='QQ交流群：1001030977',	
	url='https://github.com/xjxflyxx/jxbase',	
	zip_safe=False, 			# 这个参数为 False ，使得安装到目标位置后是平坦的目录文件形式，而非 .egg 形式，这样有助于定位资源文件
	install_requires = [
		# itertools 			# 引入支持排列组合的模块
		# copy
		# from fractions import Fraction 		# 从分数模块中引入分数函数
		#'configobj>=5.0.6',
		#'numpy>=1.10.4',
		#'pandas>=0.18.0',
		#'pytesseract>=0.1.7'
		#'pywinauto>=0.6.8'
		'rsa>=0.0.1', 			# 非对称加解密模块
		'configobj>=0.0.1',
		'numpy>=0.0.1',
		'pandas>=0.0.1',
		'pytesseract>=0.0.1',
		# 以下第三方包在本包中是用不到的，但上层 job.py 中可能会用到，为了方便上层避免手动去下载以下包，暂时在这里声明要求安装并自动安装以下包
		'schedule>=0.0.1'
		#'pywinauto>=0.0.1', 	# 这个库依赖 win平台，所以从本包中移出去了，移到 jxwin 包中了。
		#'pycryptodome>=0.0.1' 	# 包含各种加解密算法的模块
		], 	# 这是本包要用到的依赖包
	packages=['jxbase'], 		# 这是实际待安装的包名，即是个内含 __init__.py 的目录名，可以当作未来的包名引用，如 import jxbase as jxb 等，这里注意，子包必须带上父包前缀才能被找到安装，如 flyx.autotrade 会被找到，但只写 autotrade 不会被找到，虽然他也是包名
	package_data = {'':['*.*']} 				# 表示安装时将上述 packages 指定的每个包下的所有文件都带过去安装。如果没有这句，那只安装所有 py 文件。'' 表示所有上述指定的包，['*.*']表示该包下的所有文件
	)


