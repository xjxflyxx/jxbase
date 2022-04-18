__all__ = [
		'get_api_list',
		'acquire_redis_lock',
		'release_redis_lock',
		'append_arr_to_df',
		'change_path_style',
		'concat',
		'convert_df_type',
		'delete_api_list',
		'df_to_list',
		'df_to_tuple',
		'df_to_table',
		'df_to_webpage',
		'encrypt',
		'decrypt',
		'file_log',
		'find',
		'ftp_open',
		'ftp_close',
		'ftp_up',
		'ftp_down',
		'get_comment_symbols',
		'get_comment_start_symbol',
		'get_days_step',
		'get_empty_df',
		'get_file_lines',
		'get_file_info',
		'get_line_nums',
		'get_home_dir',
		'get_installed_modules',
		'get_builtin_modules',
		'get_site_modules',
		'get_pyfile_imported_modules',
		'get_pyproject_imported_modules',
		'get_kelly_percent',
		'get_pid_arr',
		'get_pid_name_arr',
		'get_project_lines',
		'get_project_info',
		'get_report_dir',
		'get_today',
		'get_yesterday',
		'get_tomorrow',
		'get_year',
		'get_month',
		'get_day',
		'get_time',
		'get_date',
		'get_date_time',
		'get_current_time',
		'get_hh',
		'get_mm',
		'get_ss',
		'get_arr_add',
		'get_arr_sub',
		'get_arr_multiply',
		'get_arr_divide',
		'get_arr_ratio',
		'get_current_function_name',
		'get_hash',
		'get_lastfile',
		'get_magic_square',
		'get_computer_name',
		'get_page_by_requests',
		'get_page_by_gevent',
		'get_private_ip',
		'get_public_ip',
		'get_mac_address',
		'get_prime_arr',
		'get_count_24',
		'get_randint_arr',
		'get_randint_df',
		'get_rsa_key',
		'get_system_encoding',
		'get_uuid',
		'get_verify_code',
		'hms_to_minutes',
		'hms_to_seconds',
		'hms_to_timestamp',
		'int_to_list',
		'is_number',
		'is_valid_date',
		'is_linux',
		'is_windows',
		'is_weekday',
		'is_weekend',
		'list_to_tuple',
		'make_api',
		'make_header',
		'merge_list',
		'num_to_words',
		'recognize_verify_code',
		'remove_df',
		'retry_command',
		'run_thread',
		'run_process',
		'seconds_to_hms',
		'security_check',
		'send_mail',
		'sort_df_column',
		'strdate_to_pydate',
		'to_path',
		'to_pydate',
		'timestamp_to_hms',
		'time_spend',
		'xround'
		]

#coding=utf-8

"""
作者：xjxfly
邮箱：xjxfly@qq.com

说明：
这是基础包，是一些通用功能（纯函数）的集合。
包内提供了一些接口，具体有哪些接口可用及怎样调用，请用 help(jxbase) 查看。

"""

# -----------------------------
# 下面这个 __all__ , 是定义可以暴露给外部的接口的，把他们都放在 __all__ 中，且外部只有用 from import 引用时才有效，直接 import 的话，这里的 __all__ 不起作用。；
# 另外，python 内置函数 help() 调用包或模块时，如果模块或包内有 __all__，则只返回 __all__ 中列出的接口的使用方法；否则返回全部接口的使用方法。 
# 这句既是给 from import 看的，也是给内置函数 help() 看的
# 另外 PEP8 建议把 __all__ 放在模块注释后，放在除 from future 之外的其他 import 前

		

# -----------------------------
# from . import common_config as cf 		# 引入本包的自定义常量
from jxbase import common_config as cf

import gevent

if cf.MONKEY_PATCH_ALL:
	from gevent import monkey
	monkey.patch_all()

import time
import datetime
import os
import math
import threading
import multiprocessing
import pkg_resources
import pickle
#import itertools 			# 引入支持排列组合的模块
#import copy

from configobj import ConfigObj
#from fractions import Fraction 		# 从分数模块中引入分数函数

import hashlib
import rsa  # 引入非对称加密模块
#import Crypto # 引入知名加解密模块

import numpy as np
import pandas as pd

import random
import re
import smtplib
import sys
import tempfile
import json
import uuid
import requests
import linecache # 读取文件的模块，非常方便
import psutil # 获取进程模块

#import difflib # 引入字符串取交集模块

# from urllib.request import urlopen
try:
	from fake_useragent import UserAgent 		# 引入假用户代理构造，用于构造爬虫请求头
except:
	print('错误：failed execute from fake_useragent import UserAgent')
	pass

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage  
from email.utils import formataddr

from ftplib import FTP 
from PIL import Image

import pytesseract

#from pywinauto import application

import socket
#import win32gui

# --------------








#########=====================================================



#date_step = datetime.timedelta(days=1)




# ########################################################################################################################################################################################################
# ======================================================================================================================================================
# ======================================================================================================================================================
# ======================================================================================================================================================
# ======================================================================================================================================================
# ======================================================================================================================================================
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# public API start （这里开始，到下面的 public API end 为止，之间的所有函数为公开接口，请不要更改函数名、参数、返回值等。要改的话只可以对内部重构！）
# public API start （这里开始，到下面的 public API end 为止，之间的所有函数为公开接口，请不要更改函数名、参数、返回值等。要改的话只可以对内部重构！）
# public API start （这里开始，到下面的 public API end 为止，之间的所有函数为公开接口，请不要更改函数名、参数、返回值等。要改的话只可以对内部重构！）


def get_api_list():
	"""
	功能说明：本函数仅仅用于返回可用接口列表，不在列表中列出的函数或接口等请不要调用，他们一般在内部实现使用，未来可能会改名或调整！！

	Returns
	-------
	返回值：可用接口, list形式

	"""
	return __all__







	
def acquire_redis_lock(lock_name, redis_conn, expire_time=10, timeout=10):
	"""
	功能说明：尝试获取 redis 中指定 lock_name 的锁， 以便对资源进行操作。主要用在分布式环境，因为各分布式电脑可能对 redis 的数据同时修改，所以修改前需要先获得锁，防止混乱。
	Parameters
	----------
		lock_name : TYPE：str
			说明：这是锁名称，实际上就是 redis 的一个 key
		expire_time : TYPE: int, optional
			说明：如果获到了锁，expire_time 是给锁加的超时时间，默认 10 秒，即本次加锁无论是否主动释放，锁都将在10秒后自动释放. The default is 10.
		timeout: type: int
			说明：这是本接口最多尝试的时间，单位秒，如果超过 timeout 还没获取到锁的话，则返回 False

	Returns
	-------
	返回值：如果获取到锁，则返回给锁加的 uuid 值，否则返回 False

	"""
	redis_lock_id = str(get_uuid())
	
	total_time = 0 			# 时间累积
	sleep_time = 0.1 		# 每次睡眠时间
	while True:
		# 以下这两种获取锁的方式都是对的，但第2种具备原子性，所以考虑用第2种。
		"""
		# setnx()只有当 key 不存在时，才会设置成功并返回 True。如果 key 已存在，则永远返回 False
		if redis_conn.setnx(lock_name, pickle.dumps(redis_lock_id)):
			redis_conn.expire(lock_name,expire_time) 		# 设置该锁超时时间
		"""
		# set() 中的参数 nx=True，效果同上面的 setnx()，即只有 key 不存在时才会设置成功并返回 True，否则返回 False
		if redis_conn.set(lock_name, pickle.dumps(redis_lock_id), nx=True, ex=expire_time):
			return redis_lock_id
		
		time.sleep(sleep_time)
		total_time = total_time + sleep_time
		if total_time > timeout:
			break
		
	return False
	
	
	
	
	
	
	
def release_redis_lock(lock_name, lock_id, redis_conn):
	"""
	功能说明：本接口用于释放 redis 锁
	Parameters
	----------
	lock_name : TYPE: str
		说明：这是 redis 锁（本质是 key 名）
	lock_id : TYPE: str
		说明：这是 redis 锁的值，本质是 key 所指向的 value

	Returns
	-------
	返回值：释放成功返回 True，否则返回 False

	"""	
	redis_lock_id = redis_conn.get(lock_name)
	if redis_lock_id is None:
		return True
	else:
		redis_lock_id = pickle.loads(redis_lock_id)
		if redis_lock_id == lock_id:
			return True
		
	return False
	
	
	
	
	
	
	

def append_arr_to_df(df, arr):
	"""
	功能说明：不直接修改传入的 df!!
		把数组形式的 arr （必须是一维）追加到 DataFrame 形式的 df 行末尾，并将 df 返回到主调函数，
		要求 arr 的元素个数及含意与 df 的列数及含义相同；注意：添加行后，将重建索引！
	参数：df: pandas 格式； arr: 一维 list，要求元素个数及含义与 df 的列数及含义相同
	返回值：在原 df 最后一行添加 arr 后生成新的 result_df
	"""
	columns = df.columns
	temp_df = pd.DataFrame(data=[arr], columns=columns)
	result_df = pd.concat([df, temp_df])
	result_df = result_df.reset_index(drop=True)

	return result_df






def change_path_style(xpath=None, style=cf.UNIX_STYLE_ARR[0], end_slash=None):
	"""
	功能说明：转换路径风格
	参数：
		xpath: 为待转换的路径； 
		style： 为目标风格，接受值：'dos','windows','linux','unix', 以及他们的大写，含意与小写相同。默认 unix（linux）风格
		endwith: 表示转换路径后是否确保路径末尾必须有指定符号，默认 None，表示原汁原味，不在末尾添加任何符号，可接受以下符号
			None: 表示不添加任何符号，保持原样
			True: 表示确保路径末尾以'/'或'\\'结尾
			False: 表示确保路径末尾没有'/'或'\\'结尾
	返回值：转换风格后的路径
	"""
	if xpath is None:
		print('没有输入路径')
		return None
	# -------------
	slash = '/' 		# 斜杠
	backslash = '\\' 	# 反斜杠
	
	new_path = None 		# 预设返回路径值为 None
	# 如果转换为 dos 风格，走这里
	if style.upper() in cf.DOS_STYLE_ARR:
		new_path = xpath.replace(slash, backslash)
		# 下面的 end_slash 如果不为 None，表示一定要有或者没有反斜杠结尾
		if end_slash is not None:
			# 下面这个 if 表示要求有反斜杠结尾
			if end_slash:
				# 下面这个 if 表示没有以反斜杠结尾，则给它加上反斜杠
				if not new_path.endswith(backslash):
					new_path += backslash
			if not end_slash:
				if new_path.endswith(backslash):
					new_path = new_path.rstrip(backslash)
				
	# 转换为 unix 风格走这里
	if style.upper() in cf.UNIX_STYLE_ARR:
		new_path = xpath.replace(backslash, slash)
		if end_slash is not None:
			if end_slash:
				if not new_path.endswith(slash):
					new_path += slash
			if not end_slash:
				if new_path.endswith(slash):
					new_path = new_path.rstrip(slash)

	return new_path








def concat(arr):
	"""
	功能说明：本函数模仿 pandas.concat()，但可以接受 None 元素以及任何元素，但只有 df  元素才会被拼接，其他元素都将被忽略。
	参数：
		arr: type: list
			说明：该参数必须是一个 list，其元素为 df （所有 df 的列名和顺序都必须相同）或 None或其他任何数据类型，但只有 df 会被采用，其他元素都会被忽略。			
	Returns
	-------
	返回值：拼接好后的 df. 若传入的 arr 中没有 df，则返回 None

	"""
	func_name = get_current_function_name()
	result_df = None
	if isinstance(arr,list): 
		if len(arr)>0:
			temp_arr = []		
			for k,v in enumerate(arr):
				#if v is not None:
				if isinstance(v,pd.core.frame.DataFrame):
					temp_arr.append(v)
			if len(temp_arr) > 0:
				result_df = pd.concat(temp_arr)
				result_df = result_df.reset_index(drop=True)
	else:
		print(func_name,' 输入给形参 arr 的值必须是一个 list，并且这个 list 的元素应是 df (若是其他值虽不出错，但不会被拼接)')
			
	return result_df
				
			







def convert_df_type(df, xtype=float, column_arr=None):
	"""
	功能说明：不直接修改传入的 df!!
		对传入的 df ，根据传入的字段 column_arr （如果有的话，要是没有的话，则对 df 中所有字段转换），
		从 df 中找到对应的列，将其数据类型转换为 xtype 指定的类型；
		无法转换的数据值将用0填充，请调用者自己注意填 0 后返回去是否符合要求！  若不符合要求就不要调用本函数。
	参数：
		df, 待转换字段类型的 df; 
		xtype, 目标数据类型；
		column_arr，需要转换哪些列
	返回值：转换数据类型后的 df
	"""	
	all_df = df.reset_index(drop=True) 	# 这步生成新的 all_df ，不再指向传入的 df。对 all_df 的修改不影响 df
	all_df = all_df.fillna(0) 			# 将 pandas 的 DataFrame 中的所有 nan 值全部替换成 0
	row_arr = all_df.index.tolist()

	if column_arr is None:
		column_arr = df.columns.tolist()
	# 先把所有数值型的列转成数值表示（原先是字符串形式的），以便参与数学计算
	#for k,col in enumerate(list(set(list(all_df.columns)) - set(['code','name','date','time']))):
	for col in column_arr:
		try:
			all_df[col] = all_df[col].astype(dtype=xtype)
		except:
			for row in row_arr:
				if not is_number(all_df.loc[row,col]):
					#all_df = all_df.drop(v, axis=0) 			# axis=0 表示行操作，这里是删除一行
					all_df.loc[row,col] = 0 					# 非数值单元域，全部填上 0
			try:
				all_df[col] = all_df[col].astype(dtype=xtype)
			except:	
				continue		
	all_df = all_df.reset_index(drop=True)

	return all_df









def delete_api_list(filename):
	"""
	功能说明：对一个 .py 文件，查找其中是否有 __all__ ，有的话将其定义的 list 删除，把删除后剩余的内容写到原文件。

	Parameters
	----------
		filename : TYPE：str
			只接受 .py 文件
	Returns
	-------
	返回值：无。直接把删除 __all__ 定义后的 .py 文件，直接保存到原文件

	"""
	filename = change_path_style(xpath=filename)
	if not filename.endswith('.py'):
		print('警告：本接口 %s 只针对 .py 文件有效，不支持其他文件类型。' % (get_current_function_name()))
		return False
	
	real_filename = filename.split('/')[-1].strip()
	if real_filename.startswith('_'):
		print('警告：为安全起见，本接口 %s 不处理下划线开头的文件。' % (get_current_function_name()))
		return False
		
	lines_arr = linecache.getlines(filename)
	result_dict = get_line_nums(filename=filename, lines_arr=lines_arr)
	#code_nums = result_dict['code_nums'] 			# 这是代码行行号 list
	comment_nums = result_dict['comment_nums'] 		# 这是注释行行号 list
	
	nums_arr = [] 		# 待删除的行号放这里
	found_start_quote = False 	# 表示是否找到了 __all__, 预设 False, 表示没找到
	found_end_quote = False 	# 表示是否找到了 list 的结束符 ']'，预设 False，表示没找到
	
	for num,line in enumerate(lines_arr):
		# 如果当前行是在注释行，则立马循环到下一行。
		if num in comment_nums:
			continue
		
		line = line.strip()
		
		# 如果没找到开始标志，就先找开始标志
		if not found_start_quote:
			# 流程进入这里，说明没找到开始标志 __all__
			if line.startswith('__all__'):
				nums_arr.append(num)
				found_start_quote = True
				end_quote_str = line.split('#')[0].strip() 		# 以注释符 '#' 为分割，提取注释符前面部分
				if end_quote_str.count(']') >= 1:
					found_end_quote = True 		# 找到 list 结束符		
		else: 
			# 流程进入这里，说明找到开始标志 __all__ ,这时找结束标志 ']'
			if not found_end_quote:
				nums_arr.append(num)
				end_quote_str = line.split('#')[0].strip() 		# 以注释符 '#' 为分割，提取注释符前面部分
				if end_quote_str.count(']') >= 1:
					found_end_quote = True 		# 找到 list 结束符
			else:
				# 如果进入这里说明找到了结束标志 ']'，于是结束循环，停止查找。组织好数据并返回
				break
			
	# -------------------------
	# 光 >0 还不行，还得加上 found_end_quote，反例：__all__ = get_api_list()，这行源码有 __all__ ，将导致其下的 nums_arr 不为0，但却找不到 ']', 即 found_end_quote 为 False，
	# 所以要求这两个条件必须同时成立才继续下去。
	if len(nums_arr) > 0 and found_end_quote:	
		# 以下两种方法都是正确的，选一种执行即可，第一种方法是按行号从大到小删，节省内存。第2种办法由于开辟了新的 list，会占用内存。
		# --------------------
		'''
		# 方法1：
		# 下面删除找到的行，先对要删的行号排序，从大到小删，要不然由于被删除行的 list 在不断变小可能导致删除出错。
		nums_arr.sort(reverse=True)
		for num in nums_arr:
			del lines_arr[num]	
		
		'''
		# --------------------
		# 方法2：
		# 把不在 nums_arr 中的行取出来放到一个新的 list 中
		new_line_arr = []
		for num,line in enumerate(lines_arr):
			if num not in nums_arr:
				new_line_arr.append(line)
		
		# 将剩余的行生成字符串，然后写到同名文件中
		content_str = ''.join(new_line_arr)
		fp = open(filename,'w+',encoding='utf-8')
		fp.write(content_str)
		fp.close()
		
	linecache.clearcache() 			# 清除 linecache 读出来的缓存内容
	
		
	
	
	
	
	
	
	
def df_to_list(df,head=False):
	"""
	功能说明：将 df 转成二维数组
	参数：
		df: pandas的 DataFrame数据
		head: type: bool, 表示要不要包含列头，可取以下值：
			True：保留列头
			False 不保留列头（默认）
	返回值：二维数组

	"""
	columns_arr = df.columns.tolist()
	values_arr = df.values.tolist()
	
	if head:
		result_arr = [columns_arr] + values_arr 		# 这是二维 list
	else:
		result_arr = values_arr
		
	return result_arr		










def df_to_tuple(df,head=False):
	"""
	功能说明：将 df 转成二维元组（不包括列名），即整个是元组，里面每一行也是元组
	参数：
		df: pandas的 DataFrame数据
		head: type: bool, 表示要不要包含列头，可取以下值：
			True：保留列头
			False 不保留列头（默认）
	返回值：二维元组

	"""	

	result_tpl = []

	d2_arr = df_to_list(df=df)
	for row in d2_arr:
		result_tpl.append(tuple(row))
	result_tpl = tuple(result_tpl)

	return result_tpl










def df_to_table(df, head=True, align='center', color_flag=False, fore_color1='black', fore_color2='black', bgcolor1="#F5F5DC", bgcolor2="#A7EEFB"):
	"""
	功能说明：将 df 转成 html 的 table 形式，并以字符串形式返回，主要是为了发电子邮件用
	参数：
		df:待转换的 pandas DataFrame数据；
		head: type: bool, 表示要不要保留df 的列名，可取以下值：
			True ：表示保留列头（默认）
			False：表示不要保留
		align:对齐方式，可取值为： 'left','center','right'，默认 'center'；
		color_flag:要不要用前景色背景色装饰表格，取值True或False；
		在 color_flag = True 的前提下，后面这几个参数才有效，
		fore_color1: 前景色1（即定体颜色）；
		fore_color2:前景色2（字体颜色）；
		bgcolor1: 表格行背景色1；
		bgcolor2:表格行背景色2
	返回值：字符串形式的 html table

	"""
	if df is None:
		print('错误！ 没有传入 DataFrame.')
		print(' df_to_table(df) 函数功能是将 pandas 的 DataFrame 转成 html 下的 <table>形式。用法: 参数 df 必须是 pandas 的 DataFrame 格式，不能为空。返回值是字符串形式的 html 下的 <table>，可独立作网页使用，也可拼接到其他 html 页面使用。')
		return None

	d2_arr = df_to_list(df=df, head=head)

	s = """
		<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>
		<div style="text-align:%s;">
		<table width="500" border=1 style="word-break:norawp;">
		""" % (align)
		
	fore_color = 'black'

	for k1,v1 in enumerate(d2_arr):
		# 设置前景色
		if color_flag:
			if k1 % 2 == 0:
				fore_color = fore_color1
			else:
				fore_color = fore_color2

		# 设置前景色
		s += '<tr style="color:%s;">' % (fore_color)
		for k2,v2 in enumerate(v1):
			s += '<td>' + str(v2) + '</td>'
		s += '</tr>'

	s += '</table></div>'

	# 设置背景色
	if color_flag:
		s += """ 
			<script>
			$(document).ready(function(){
			//隔行表色
			$("tr:even").css("background-color", "%s"); //为双数行表格设置背颜色素
			$("tr:odd").css("background-color", "%s");})
			</script>
			""" % (bgcolor1, bgcolor2)

	return s











def df_to_webpage(df, head=True, align='center', color_flag=False, fore_color1='black', fore_color2='black', bgcolor1="#F5F5DC", bgcolor2="#A7EEFB"):
	"""
	功能说明：将 df 转成 html webpage 形式，并以字符串形式返回，主要是为了发电子邮件用
	参数：
		df:待转换的 pandas DataFrame数据；
		head: type: bool, 表示要不要保留df 的列名，可取以下值：
			True ：表示保留列头（默认）
			False：表示不要保留
		align:对齐方式，可取值为： 'left','center','right'，默认 'center'；
		color_flag:要不要用前景色背景色装饰表格，取值True或False；
		在 color_flag = True 的前提下，后面这几个参数才有效，
		fore_color1: 前景色1（即定体颜色）；
		fore_color2:前景色2（字体颜色）；
		bgcolor1: 表格行背景色1；
		bgcolor2:表格行背景色2
	返回值：字符串形式的 html webpage

	"""
	s1 = """
		<html>
		<head>
		<style type="text/css">
		td
		{
			white-space: nowrap;
		}
		</style>
		<script src="https://cdn.bootcss.com/jquery/3.2.1/jquery.min.js"></script>

		</head>
		<body>

		""" 

	s2 = "</body></html>"

	html_table = df_to_table(df=df, head=head, align=align, color_flag=color_flag, fore_color1=fore_color1, fore_color2=fore_color2, bgcolor1=bgcolor1, bgcolor2=bgcolor2)
	if html_table is None:
		return None
	else:
		result_str = s1 + html_table + s2
		return result_str










def encrypt(msg, key=None, key_len=32, xtype='ARC4', **kwargs):
	"""
	功能说明：本接口用来对传入的数据 msg 调用 xtype的加密类型用密钥 key 进行加密
	参数：
		msg: str型或字节流型，必填
			说明：该参数为待加密的字符串，（若是其他类型，可先转成字符串）
		key: str型或bytes型，可选，默认值 None, 
			说明：若参数 xtype='rsa'，则 key必须指定。
		key_len: int型，可选，默认值32
			说明：若参数 key 为 None，则 key_len 起作用，将由接口自动产一个长度为 key_len 的 key
		xtype: str型，可选，默认值: 'ARC4'
			说明：该参数指出用哪种加密方式进行加密，可取以下值（不区分大小写）：
			'rsa': 表示用 rsa 非对称加密（有限长加密）
			'chacha20': 表示用 chacha20 对称加密（流加密）
			'aes': 表示用 aes 对称加密（块加密）
			'arc4': 表示用 arc4 对称加密（流加密），这个加密方法比较简单，只要一个 key 即可加密和解密，所以设成了默认加密方法。
		kwargs: 预留扩展参数用
	返回值：result_arr: 是一个 list, 第一个元素是加密后的信息，字节流类型（不转成 str 型返回是因为有些加密后的字节流在转成 str 过程中要出错，所以保留字节流型返回
			其他元素（若有的话）个数及含义取决于加密类型 xtype
			1. 若加密类型 xtype = 'rsa'，则返回值 result_arr中只有一个元素，即加密后的信息（字节流形式）
			2. 若加密类型 xtype = 'chacha20', 则返回值 result_arr 中有3个元素，第一个元素是加密后的信息（字节流形式），第二个元素是用来解密的 key, 第三个元素是解密要用到的参数 nonce
			3. 若加密类型 xtype = 'aes', 则返回值 result_arr 中有3个元素，第一个元素是加密后的信息（字节流形式），第二个元素是用来解密的 key, 第三个元素是解密要用到的参数 nonce
			4. 若加密类型 xtype = 'arc4', 则返回值 result_arr 中有2 个元素，第一个元素是加密后的信息（字节流形式），第2个元素是用来解密的 key
	
	"""
	result_arr = None
	
	if xtype.upper() == 'RSA':
		if key is None:
			print('错误! 默认是 RSA 加密方式，请传入公钥（字节流形式）给形参 key ')
			return None
		result_arr = rsa_encrypt(msg=msg, public_key=key)
		
	if xtype.upper() == 'CHACHA20':
		result_arr = chacha20_encrypt(msg=msg, key=key, key_len=key_len)
	
	if xtype.upper() == 'AES':
		result_arr = aes_encrypt(msg=msg, key=key, key_len=key_len)
	
	if xtype.upper() == 'ARC4':
		result_arr = arc4_encrypt(msg=msg, key=key, key_len=key_len)
	
	return result_arr
	
	
	
	
	
	





def decrypt(crypt_msg, key=None, xtype='ARC4', **kwargs):
	"""
	功能说明：本接口用来对传入的数据 crypt_msg 调用 xtype 指向的解密类型用相应的密钥 key 进行解密
	参数：
		crypt_msg: 字节流型，必填
			说明：该参数是待解密的字节流型串（原先已加密）
		key: str型或bytes型，可选，默认值 None, 
			说明：若参数 xtype='rsa'，则 key必须指定。大部分解密类型下，key 都必须指定
		xtype: str型，可选，默认值: 'ARC4'
			说明：该参数指出用哪种解密方式进行解密，解密方式取决于当初的加密方式，可取以下值（不区分大小写）：
			'rsa': 表示用 rsa 的私钥进行解密
			'chacha20': 表示用 chacha20 进行解密，需要传入当初用 chacha20 加密后返回的 key 和 nonce 分别给形参 key 和 nonce
			'aes': 表示用 aes 进行解密，需要传入当初用 aes 加密后返回的 key 和 nonce 分别给形参 key 和 nonce
			'arc4': 表示用 arc4 进行解密，需要传入当初用 arc4 加密后返回的 key 给形参 key
		kwargs: 用来传递某些解密方法需要用到却又未在本接口命名的形参，如传递 nonce 给形参 nonce 等
	返回值：msg, str型，即解密后的数据
	"""
	msg = None
	
	if xtype.upper() == 'RSA':
		if key is None:
			print('错误! 默认是 RSA 解密方式，请传入私钥（字节流形式）给形参 key ')
			return None
		msg = rsa_decrypt(crypt_msg=crypt_msg, private_key=key)
			
	if xtype.upper() == 'CHACHA20':
		if key is None or 'nonce' not in list(kwargs.keys()):
			print('错误! 你选择了chacha20解密方式，请传入当初用 chacha20 加密后返回的 key 和 nonce 分别给本接口的形参 key 和 nonce')
			return None
		msg = chacha20_decrypt(crypt_msg=crypt_msg, key=key, nonce=kwargs['nonce'])
			
	if xtype.upper() == 'AES':
		if key is None or 'nonce' not in list(kwargs.keys()):
			print('错误! 你选择了 AES 解密方式，请传入当初用 AES 加密后返回的 key 和 nonce 分别给本接口的形参 key 和 nonce')
			return None
		msg = aes_decrypt(crypt_msg=crypt_msg, key=key, nonce=kwargs['nonce'])
				
	if xtype.upper() == 'ARC4':
		if key is None :
			print('错误! 你选择了 ARC4 解密方式，请传入当初用 ARC4 加密后返回的 key 传给本接口的形参 key')
			return None
		msg = arc4_decrypt(crypt_msg=crypt_msg, key=key)
			
	# --------------------
	if isinstance(msg, bytes):
		msg = msg.decode()
		
	return msg
	
	
	
	
	
	



def file_log(msg,filename=None):
	"""
	功能说明：本接口的作用是把 msg 信息记录到 filename 文件中去（文件位置会由本接口自动指定，一般会指定到 report_dir）

	Parameters
	----------
	msg : TYPE: str
		说明：这是待写到文件的信息
	filename : TYPE：str, optional
		说明：这是文件名。 The default is None.

	Returns
	-------
	返回值：写成功返回 True, 否则返回 False.

	"""
	msg = '\n\n' + get_current_time() + ': \n' + str(msg)

	report_dir = get_report_dir()
	
	if filename is None:
		filename = cf.FILE_LOG
	filename = change_path_style(xpath=filename)
	filename = report_dir + filename.split('/')[-1]
	try:
		fp = open(file=filename, mode='a+')
		fp.write(msg)
		fp.close()
	except:
		print('错误：写文件失败')
		return False
	else:
		return True








def find(xpath,s,case_sensitive=False,out_file=None):
	"""
	功能说明：本接口在指定的 xpath 目录（及子目录）下对所有文本文件中查找指定字符串 s，把所有包含 s 的文件显示出来；
			若指定了 out_file 的话，则将查找结果同时保存到 out_file 中。

	Parameters
	----------
		xpath: type: str, 待查找的目录
		s : TYPE：str, 待查找字符串
		case_sensitive: type:bool, 表示是否大小写敏感，可取值 True 或 False ，分别表示敏感或不敏感（默认 False)
		out_file : TYPE:str, optional
			如果有指定的话，则将查找结果输出到文件. 

	Returns
	-------
	返回值：查找结果所在的文件形成的 list

	"""
	result_arr = [] 		# 初始化一个空 list，用于存放找到的文件路径
	
	xpath = to_path(xpath=xpath)
	
	for root,dir_arr,file_arr in os.walk(xpath):
		root = to_path(xpath=root)
		for filename in file_arr:
			filename = root + filename
			try:
				lines_arr = linecache.getlines(filename)
			except:
				print('警告：%s 无法读取 %s' % (get_current_function_name(),filename))
				continue
			else:
				content_str = ''.join(lines_arr)
				linecache.clearcache()
				# 下面这个 if 表示如果大小写不敏感的话，那将源内容和待找内容全部转成小写，然后再去找
				if not case_sensitive:
					content_str = content_str.lower()
					s = s.lower()
				# 下面开始查找
				if content_str.find(s) >= 0:
					result_arr.append(filename)
					
	if len(result_arr) > 0:
		if out_file is not None:
			file_str = '\n'.join(result_arr)
			try:
				fp=open(out_file,'w+',encoding='utf-8')				
				fp.write(file_str)
				fp.close()
			except:
				pass
			
		print('\n以下文件包含有查找目标 %s:\n' % (s))
		for one_file in result_arr:
			print(one_file)
			
	return result_arr
	
	
	
	
	
	
	
	
def ftp_open(host=None, port=None, username=None, password=None):
	"""
	功能说明：初始化 FTP 连接，返回指向 ftp 服务器的连接符。首先会尝试从传入的参数中读取信息，
		若没传入，则次选从用户的配置文件 user_config.ini 中读取FTP 服务器配置信息，若没有，则第3选择从 py 配置文件中读取，若还是没有，则返回 None
	参数：host: FTP服务器；port: 服务器端口; username: 登录 ftp  的用户名; password: 登录 ftp 的密码
	返回值：成功登录后的 ftp 操作对象（若登录失败则返回 None)
	"""
	if host is None or port is None or username is None or password is None:
		try:
			cfg = ConfigObj('user_config.ini')
		except:
			print('用户没有提供配置文件 user_config.ini，下面尝试从 common_config.py 中读取配置信息')
			try:
				host = cf.FTP_HOST
				port = cf.FTP_PORT
				username = cf.FTP_USERNAME
				password = cf.FTP_PASSWORD
			except:
				print('错误：common_config.py 配置文件中没有FTP服务器信息')	
				return None	
		else:		
			host = cfg['FTP_HOST']
			port = cfg['FTP_PORT']
			username = cfg['FTP_USERNAME']
			password = cfg['FTP_PASSWORD']	

	# --------------
	ftp = FTP()
	ftp.set_debuglevel(2)
	ftp.connect(host=host, port=port)
	ftp.login(username, password)

	return ftp










def ftp_close(ftp):
	"""
	功能说明：关闭FTP 连接
	参数：ftp: 已经连接的 ftp 对象
	返回值：无
	"""

	ftp.set_debuglevel(0)
	ftp.quit()








def ftp_up(ftp, filename):
	"""
	功能说明：该函数用来上传文件到FTP 服务器，
	参数：ftp: 指向 FTP 服务器的连接符；filename: 待上传的文件，可以是windows 格式包含全路径的文件
	返回值：无
	"""
	#print(ftp.getwelcome())
	#ftp.cwd('xxx/www')
	file_handler = open(filename, 'rb')
	ftp.storbinary('STOR %s' % (os.path.basename(filename)), file_handler)
	file_handler.close()

	print('FTP up OK.')










def ftp_down(ftp, filename):
	"""
	功能说明：该函数用来从 FTP 服务器下载文件，
	参数：ftp: 指向 FTP 服务器的连接符；filename: 待下载的文件，可以是windows 格式包含全路径的文件
	返回值：无
	"""	
	#print(ftp.getwelcome())
	#ftp.cwd('xxx/www')
	file_handler = open(filename, 'wb')
	ftp.retrbinary('RETR %s' % (os.path.basename(filename)), file_handler)
	file_handler.close()

	print('FTP down OK.')






	
	
	

def get_comment_symbols():
	"""
	功能说明：定义一个字典，建立文件类型与其注释符对应关系

	Returns
	-------
	返回值：是一个 dict,每个元素的 key 代表源码文件类型（如：.py），value 代表该源码文件的注释符(是一个二维 list，其中每个元素是一维 list，该一维 list 包含两个元素，表示开始注释符和结束注释符)
	"""
	# 注释符 list，表示这个 list 中的符号是相应语言的注释符号，comment_symbol_arr 中的元素也是 list，规定必须成对出现，即这个子 list 必须包含两个元素，分别表示注释的开始和结束	
	comment_symbols = {
		'.py': [['#',''],['"""','"""'],["'''","'''"]], 	# python 代码注释符
		'.c': [['//',''],['/*','*/']], 					# C 语言代码注释符
		'.cpp': [['//',''],['/*','*/']], 				# C++ 语言代码注释符
		'.php': [['//',''],['/*','*/']], 				# php 语言代码注释符
		'.js': [['//',''],['/*','*/']], 				# javascript 语言代码注释符
		'.go': [['//',''],['/*','*/']], 				# go 语言代码注释符
		'.m': [['%{','}%'],['%','']], 					# Matlab 语言代码注释符
		'.pl': [['#',''],['=pod','=cut']], 				# perl 语言代码注释符
		'.lua': [['--[[',']]--'],['--','']], 			# Lua 语言代码注释符
		'.rb': [['#',''],['=begin','=end']], 			# Ruby 语言代码注释符
		'.rs': [['//',''],['/*','*/']], 				# Rust 语言代码注释符
		'.scala': [['//',''],['/*','*/']], 				# Scala 语言代码注释符
		'.java': [['//',''],['/*','*/']] 				# Java 语言代码注释符
		
		}

	return comment_symbols	






	
def get_comment_start_symbol(line, comment_symbol_arr):
	"""
	功能说明：从给定的程序源码行 line 的注释结束符（若有的话）之后的剩余内容中寻找一个有效的注释起始符，注释起始符和结束符配对情况要传给 comment_symbol_arr 
			# 按照 python 语法要求，一行代码中去掉注释结束符后剩余部分的内容，如果有的话，必须以注释起始符开始，否则在注释结束符后的同一行内写有效代码是语法错误。
			# 因此 本接口 对传入的 注释结束符之后的同一行剩余代码，都会检测是不是以注释符起始符开头，若不是，直接返回 None，否则才开始检测注释嵌套。

	Parameters
	----------
		line : TYPE：str，程序源码行（一行）
		comment_symbol_arr : TYPE，二维 list
			这是一个二维 list，每一个元素是一维 list,这一维 list 只包含两个元素，分别是起始注释符和结束注释符
	Returns
	-------
	返回值，找到的有效起始符，若没找到，则返回 None

	"""
	result = None 		# 预设返回的注释起始符为 None
	
	line = line.strip()

	if len(line) > 0:
		for sub_arr in comment_symbol_arr:
			comment_start_symbol = sub_arr[0]
			comment_end_symbol = sub_arr[1]
			# 下面这个 if 检测传入的行是否以注释起始符开头，若不是，直接 break 返回 None	,
			# 只有以注释起始符开始的行，才继续检测（主要是用递归方法）注释符嵌套情况
			if line.startswith(comment_start_symbol):
				result = comment_start_symbol
				if comment_end_symbol == '':
					result = None
				else:
					temp_arr = line.split(comment_start_symbol)[1:]
					new_line = comment_start_symbol.join(temp_arr)
					if new_line.count(comment_end_symbol) >= 1:
						temp_arr = new_line.split(comment_end_symbol)[1:]
						new_line = comment_end_symbol.join(temp_arr)
						result = get_comment_start_symbol(line=new_line, comment_symbol_arr=comment_symbol_arr) 		# 递归调用
				break
	
	return result
	
	
	
	
	
	
	
	


def get_days_step(n=1):
	"""
	功能说明：根据传入的参数n，返回 n天

	Parameters
	----------
	n : TYPE int, optional
		表示天数. The default is 1.

	Returns
	-------
	返回值：python datetime.timedelta() 日期类型的天数

	"""
	days_step = datetime.timedelta(days=n)
	
	return days_step
	
	
	
	
	
	
	
	
		
def get_empty_df(df):
	"""
	功能说明：不直接修改传入的 df!! 根据传入的df, 返回一个由该 df 的列头组成且保持顺序的空的 df

	Parameters
	----------
	df : TYPE: pandas dataframe

	Returns
	-------
	空的 df

	"""
	# 只取 df 的列头，不要数据。 以下两条是等价的，只选一句即可
	empty_df = df.drop(df.index) 		# 只取 df 的列头，不要数据，这个操作不影响 df
	#empty_df = pd.DataFrame(columns=df.columns) 		# # 取 df 的列头，构造一个空的 df
	
	return empty_df
	
	
	
	
	
	
	
	

def get_file_lines(filename, include_blank_line=False):
	"""
	功能说明：统计一个 文件的行数
	参数：
		filename, 表示一个文本文件（可能需全路径）
		include_blank_line: type: bool，表示是否统计空行，默认 False，表示不统计空行
	Returns
	-------
	返回值：该文件的行数
	"""
	xcount = 0 		# 初始化统计总行数为 0 
	# 读取 filename 中的所有行（包括空行）
	try:
		lines_arr = linecache.getlines(filename) 
	except:
		print('无法统计文件：%s' % (filename))
	else:
		if not include_blank_line:
			# '\n' 表示空行，下面给它去掉，保留有实际内容行，注意：这里返回的是一个迭代器，还无法统计行数
			lines_arr = filter(lambda x:x!='\n', lines_arr) 	
		# 下面从迭代器里统计行数
		for x in lines_arr:
			xcount += 1
		
		linecache.clearcache()
		
	return xcount
	
	
	

	
	
	
	
	
def get_file_info(filename):
	"""
	功能说明：统计一个 程序源码文件的有效代码行数，注释行数，空白行数等
	参数：
		filename, 表示一个程序源码文件（可能需全路径）
	Returns
	-------
	返回值：df，该df包含有效代码行数，注释行数，空白行数等。
	"""
	result_dict = get_line_nums(filename=filename)
	
	code_lines = len(result_dict['code_nums'])
	comment_lines = len(result_dict['comment_nums'])		
	blank_lines = len(result_dict['blank_nums'])
	# ----------------------
	# 下面函数定义行和类定义行的统计目前只针对 .py 源码
	func_count = len(result_dict['func_nums'])
	class_count = len(result_dict['class_nums'])
	# 下面构造一个 df，各字段含义分别是：filename(文件名), code_lines(有效代码行数)， comment_lines(注释行数)，blank_lines(空白行数)，file_count(文件数量)
	df = pd.DataFrame(data=[[filename,code_lines,comment_lines,blank_lines,func_count,class_count,1]], columns=['filename','code_lines','comment_lines','blank_lines','func_count','class_count','file_count'])
	
	return df
	
	
	
	
	
	
		
def get_line_nums_backup(filename, lines_arr=None):
	"""
	功能说明：这个函数很重要，本包内的一些其他接口依赖他。
			扫描一个 程序源码文件，生成代码行行号 list, 注释行号 list, 空白行号 list
			返回一个 dict, 有 3 个元素指向 3 个list,
			3 个元素分别是 'code_nums'，表示代码行,'comment_nums'，表示注释行，'blank_nums'，表示空白行
	参数：
		filename, 表示一个程序源码文件（可能需全路径）
		lines_arr: 表示一个源码文件已用 linecache.getlines() 读取出来的结果传进来，如果这个值为 None，则采用 filename，否则先采用 lines_arr，避免重复到 filename 中读大量数据。
	Returns
	-------
	返回值：	返回一个 dict, 有 3 个元素指向 3 个list,
			3 个元素分别是 'code'，表示代码行,'comment'，表示注释行，'blank'，表示空白行

	"""
	
	in_comment_flag = False 	# 表示当前行是否在注释中
	
	comment_start_symbol = None 	# 初始化开始注释符
	comment_end_symbol = None 		# 初始化结束注释符

	
	comment_symbols = get_comment_symbols() 		# 获取语言类型和其注释对应关系的 dict
	file_type_arr = comment_symbols.keys()
	
	code_nums = [] 				# 保存代码行的行号
	comment_nums = [] 			# 保存注释行的行号
	blank_nums = [] 			# 保存空白行的行号
		
	# ----------------------------------
	
	if lines_arr is None:
		# 读取 filename 中的所有行（包括空行）
		try:
			lines_arr = linecache.getlines(filename) 
		except:
			print(f'错误：linecache.getlines({filename}) 失败。')
			return None
	# --------------	
	for file_type in file_type_arr:		
		if filename.endswith(file_type):
			comment_symbol_arr = comment_symbols[file_type]
			in_comment_flag  = False 		# 表示当前是否在注释对中，预设 False，表示不在。该变量的值会随着后续流程的进行而不断变化
			for i,line in enumerate(lines_arr):
				line = line.strip() 		# 先把该行两头的空格及回车符、换行符、制表符等都去掉
				if not in_comment_flag:	
					# 空白行加1
					if line == '':
						blank_nums.append(i)
						continue
					count_to_comment_flag = False 	# 初始化一个标志变量，表示这一行是否统计到注释计数中，预设 False, 表示没有计入注释
					# for 循环查看是不是注释行
					for sub_arr in comment_symbol_arr:
						if not in_comment_flag:
							comment_start_symbol = sub_arr[0]
							comment_end_symbol = sub_arr[1] 
						else:
							if comment_start_symbol == sub_arr[0]:
								comment_end_symbol = sub_arr[1]
							else:
								continue
						if line.startswith(comment_start_symbol):
							comment_nums.append(i)
							count_to_comment_flag = True
							in_comment_flag = True
							# 由于注释结束符和起始不同，下面的 if 只要判断本行是否有注释结束符即可.后经测试这样可能不行，因为注释结束符不一定是一行的最末几个字符，所以不能用 endswith() ，而是要用 re.findall() 来查找
							# if line.endswith(comment_end_symbol):
							if comment_end_symbol == '':
								in_comment_flag = False
							else:
								temp_arr = line.split(comment_start_symbol)[1:] 			# 去掉注释起始符，把剩下的内容生成新的一行
								new_line = comment_start_symbol.join(temp_arr)
								
								if new_line.count(comment_end_symbol) >= 1:
									temp_arr = new_line.split(comment_end_symbol)[1:] 		# 去掉注释结束符，把剩下的内容生成新的一行
									new_line = comment_end_symbol.join(temp_arr)										
									new_comment_start_symbol = get_comment_start_symbol(line=new_line, comment_symbol_arr=comment_symbol_arr) 		# 递归调用
									# 如果在这一行剩余的字符串没有找到匹配后剩下的单个注释起始符的话，说明各种注释起始符和结束符正好是偶数配对，
									# 那么接下去的一行就不应该是注释了，也就是不在注释对中了，所以把 in_comment_flag 设为 False
									if new_comment_start_symbol is None:
										in_comment_flag = False
									else:
										# 流程进入这里，说明对行剩余字符串匹配注释符配对后，仍然返回单个注释起始符，那么说明下一行仍将在注释对中，且新的注释起始符将是这里返回的这个
										comment_start_symbol = new_comment_start_symbol

							break
					# 如果本行没有被记入到注释计数中，那就对普通代码行计数 +1
					if not count_to_comment_flag:
						code_nums.append(i)	
						# 然后处理函数定义行和类定义行								
				else:
					# 流程到这里，说明在注释内，先对该行注释加 1，然后判断该行是否有注释结束符
					comment_nums.append(i)
					# 下面这个 for 根据上面找到的注释起始符去寻找注释结束符
					for temp_arr in comment_symbol_arr:
						if comment_start_symbol == temp_arr[0]:
							comment_end_symbol = temp_arr[1]
							break
						else:
							continue
					if line.count(comment_end_symbol) >= 1:
						temp_arr = line.split(comment_end_symbol)[1:] 		# 去掉注释结束符，把剩下的内容生成新的一行
						new_line = comment_end_symbol.join(temp_arr)										
						new_comment_start_symbol = get_comment_start_symbol(line=new_line, comment_symbol_arr=comment_symbol_arr)
						# 如果在这一行剩余的字符串没有找到匹配后剩下的单个注释起始符的话，说明各种注释起始符和结束符正好是偶数配对，
						# 那么接下去的一行就不应该是注释了，也就是不在注释对中了，所以把 in_comment_flag 设为 False
						if new_comment_start_symbol is None:
							in_comment_flag = False
						else:
							# 流程进入这里，说明对行剩余字符串匹配注释符配对后，仍然返回单个注释起始符，那么说明下一行仍将在注释对中，且新的注释起始符将是这里返回的这个
							comment_start_symbol = new_comment_start_symbol

			break
			
	linecache.clearcache()			

	result_dict = {
		'code_nums':code_nums,
		'comment_nums':comment_nums,
		'blank_nums':blank_nums
		}
	
	return result_dict
	
	
	
	
	
	
	
	
def get_line_nums(filename, lines_arr=None):
	"""
	功能说明：这个函数很重要，本包内的一些其他接口依赖他。
			扫描一个 程序源码文件，生成代码行行号 list, 注释行号 list, 空白行号 list，以及函数定义行号 list, 类定义行号 list（目前函数定义行及类定义行统计只针对 .py 源码）
			返回一个 dict, 有 5 个元素指向 5 个list,
			5 个元素分别是 'code'，表示代码行,'comment'，表示注释行，'blank'，表示空白行
					以及 'func' 表示函数定义所在行，'xclass' 表示类定义所在行。
	参数：
		filename, 表示一个程序源码文件（可能需全路径）
		lines_arr: 表示一个源码文件已用 linecache.getlines() 读取出来的结果传进来，如果这个值为 None，则采用 filename，否则先采用 lines_arr，避免重复到 filename 中读大量数据。
	Returns
	-------
	返回值：	返回一个 dict, 有 5 个元素指向 5 个list,
			5 个元素分别是 'code'，表示代码行,'comment'，表示注释行，'blank'，表示空白行
			以及 'func' 表示函数定义所在行，'xclass' 表示类定义所在行。


	"""
	
	in_comment_flag = False 	# 表示当前行是否在注释中
	
	comment_start_symbol = None 	# 初始化开始注释符
	comment_end_symbol = None 		# 初始化结束注释符

	
	comment_symbols = get_comment_symbols() 		# 获取语言类型和其注释对应关系的 dict
	file_type_arr = comment_symbols.keys()
	
	code_nums = [] 				# 保存代码行的行号
	comment_nums = [] 			# 保存注释行的行号
	blank_nums = [] 			# 保存空白行的行号
	
	func_symbols = get_func_symbols() 				# 获取语言类型和其函数定义关键字及类定义关键定关系的 dict
	func_nums = [] 				# 保存函数定义所在行的行号
	class_nums = [] 			# 保存类定义所在行的行号
	
	# ----------------------------------
	
	if lines_arr is None:
		# 读取 filename 中的所有行（包括空行）
		try:
			lines_arr = linecache.getlines(filename) 
		except:
			print(f'错误：linecache.getlines({filename}) 失败。')
			return None
	# --------------	
	for file_type in file_type_arr:		
		if filename.endswith(file_type):
			comment_symbol_arr = comment_symbols[file_type]
			in_comment_flag  = False 		# 表示当前是否在注释对中，预设 False，表示不在。该变量的值会随着后续流程的进行而不断变化
			for i,line in enumerate(lines_arr):
				line = line.strip() 		# 先把该行两头的空格及回车符、换行符、制表符等都去掉
				if not in_comment_flag:	
					# 空白行加1
					if line == '':
						blank_nums.append(i)
						continue
					count_to_comment_flag = False 	# 初始化一个标志变量，表示这一行是否统计到注释计数中，预设 False, 表示没有计入注释
					# for 循环查看是不是注释行
					for sub_arr in comment_symbol_arr:
						if not in_comment_flag:
							comment_start_symbol = sub_arr[0]
							comment_end_symbol = sub_arr[1] 
						else:
							if comment_start_symbol == sub_arr[0]:
								comment_end_symbol = sub_arr[1]
							else:
								continue
						if line.startswith(comment_start_symbol):
							comment_nums.append(i)
							count_to_comment_flag = True
							in_comment_flag = True
							# 由于注释结束符和起始不同，下面的 if 只要判断本行是否有注释结束符即可.后经测试这样可能不行，因为注释结束符不一定是一行的最末几个字符，所以不能用 endswith() ，而是要用 re.findall() 来查找
							# if line.endswith(comment_end_symbol):
							if comment_end_symbol == '':
								in_comment_flag = False
							else:
								temp_arr = line.split(comment_start_symbol)[1:] 			# 去掉注释起始符，把剩下的内容生成新的一行
								new_line = comment_start_symbol.join(temp_arr)
								
								if new_line.count(comment_end_symbol) >= 1:
									temp_arr = new_line.split(comment_end_symbol)[1:] 		# 去掉注释结束符，把剩下的内容生成新的一行
									new_line = comment_end_symbol.join(temp_arr)
									# 按照 python 语法要求，一行代码中去掉注释结束符后剩余部分的内容，如果有的话，必须以注释起始符开始，否则在注释结束符后的同一行内写有效代码是语法错误。
									# 因为 get_comment_start_symbol() 对传入的 行（不管是不是new_line），都会检测是不是以注释符起始符开头，若不是，直接返回 None，否则才开始检测注释嵌套。
									new_comment_start_symbol = get_comment_start_symbol(line=new_line, comment_symbol_arr=comment_symbol_arr)
									# 如果在这一行剩余的字符串没有找到匹配后剩下的单个注释起始符的话，说明各种注释起始符和结束符正好是偶数配对，
									# 那么接下去的一行就不应该是注释了，也就是不在注释对中了，所以把 in_comment_flag 设为 False
									if new_comment_start_symbol is None:
										in_comment_flag = False
									else:
										# 流程进入这里，说明对行剩余字符串匹配注释符配对后，仍然返回单个注释起始符，那么说明下一行仍将在注释对中，且新的注释起始符将是这里返回的这个
										comment_start_symbol = new_comment_start_symbol

							break
					# 如果本行没有被记入到注释计数中，那就对普通代码行计数 +1
					if not count_to_comment_flag:
						code_nums.append(i)	
						# 然后处理函数定义行和类定义行	
						if file_type in func_symbols.keys():
							if line.startswith(func_symbols[file_type]['func'] + ' '):
								func_nums.append(i)
							if line.startswith(func_symbols[file_type]['xclass'] + ' '):
								class_nums.append(i)
				else:
					# 流程到这里，说明在注释内，先对该行注释加 1，然后判断该行是否有注释结束符
					comment_nums.append(i)
					# 下面这个 for 根据上面找到的注释起始符去寻找注释结束符
					for temp_arr in comment_symbol_arr:
						if comment_start_symbol == temp_arr[0]:
							comment_end_symbol = temp_arr[1]
							break
						else:
							continue
					if line.count(comment_end_symbol) >= 1:
						temp_arr = line.split(comment_end_symbol)[1:] 		# 去掉注释结束符，把剩下的内容生成新的一行
						new_line = comment_end_symbol.join(temp_arr)										
						new_comment_start_symbol = get_comment_start_symbol(line=new_line, comment_symbol_arr=comment_symbol_arr)
						# 如果在这一行剩余的字符串没有找到匹配后剩下的单个注释起始符的话，说明各种注释起始符和结束符正好是偶数配对，
						# 那么接下去的一行就不应该是注释了，也就是不在注释对中了，所以把 in_comment_flag 设为 False
						if new_comment_start_symbol is None:
							in_comment_flag = False
						else:
							# 流程进入这里，说明对行剩余字符串匹配注释符配对后，仍然返回单个注释起始符，那么说明下一行仍将在注释对中，且新的注释起始符将是这里返回的这个
							comment_start_symbol = new_comment_start_symbol

			break
			
	linecache.clearcache()			

	result_dict = {
		'code_nums':code_nums,
		'comment_nums':comment_nums,
		'blank_nums':blank_nums,
		'func_nums':func_nums,
		'class_nums':class_nums
		}
	
	return result_dict
	
	
	
	
	
	
					
def get_home_dir():
	"""
	功能说明：本接口用于获取用户主目录路径。
		在 linux 上执行，获取到的是 home 所在路径；
		在 windows 上执行，获取到的是当前用户的用户目录，类似这样：C:\\Users\\Administrator

	Returns
	-------
	返回值：用户目录所在路径

	"""	
	home_dir = os.path.expanduser('~')
	#home_dir = change_path_style(xpath=home_dir) + '/'
	home_dir = to_path(xpath=home_dir)
	
	return home_dir
	
	






def get_installed_modules():
	"""
	功能说明：返回所有已安装的模块或包组成的 list（包括内置模块或包第3方安装的模块或包）

	Returns
	-------
	返回值：返回所有已安装的模块或包组成的 list（包括内置模块或包第3方安装的模块或包）

	"""
	builtin_modules = get_builtin_modules()
	site_modules = get_site_modules()
	
	modules_arr = builtin_modules + site_modules
	
	modules_arr = list(set(modules_arr))
	modules_arr.sort(reverse=False)
	
	return modules_arr

	
	
	
	
	
	

def get_builtin_modules():
	"""
	功能说明：查找所有已安装的随 python 内置的模块或包，以 list 形式将他们返回。

	Returns
	-------
	返回值：所有已安装的随 python 内置的模块或包组成的 list

	"""	
	modules_arr = list(sys.builtin_module_names)
	modules_arr.sort(reverse=False)		
	
	return modules_arr
		
	
	





def get_site_modules(with_version=False):
	"""
	功能说明：返回所有第3方安装的模块和包

	Returns
	-------
	返回值：所有已安装的第 3方模块和包组成的 list

	"""	
	modules_arr = []	# 初始化返回值
	m_iter = pkg_resources.working_set
	for m in m_iter:
		modules_arr.append(str(m).strip())
		# 如果不要版本号的话，则进入下面的逻辑
		if not with_version:
			temp_arr = modules_arr
			modules_arr = []
			for m in temp_arr:
				modules_arr.append(m.split(' ')[0].strip())
	
	modules_arr.sort(reverse=False)
				
	return modules_arr
			
		
		
	
	
	
	
	
	
def get_pyfile_imported_modules(pyfile):
	"""
	功能说明：返回一个 .py 文件中所有被 import 到的模块及包组成的 list

	Parameters
	----------
		pyfile : TYPE: str  要求输入的一个 .py 文件（含全路径，否则只在当前目录找）

	Returns
	-------
	返回值：返回一个 .py 文件中所有被 import 到的模块及包组成的 list
	"""
	keyword_import = 'import'
	keyword_from = 'from'
	
	pyfile_imported_module_arr = [] 		# 初始化返回值为空 list
	
	if isinstance(pyfile,str):
		if pyfile.endswith('.py'):
			lines_arr = linecache.getlines(pyfile)
			for line in lines_arr:
				line = line.strip() 		# 去掉字符串 line 两头的空格
				for keyword in [keyword_import, keyword_from]:
					if line.startswith(keyword):
						module_str = line.split(keyword)[1].strip() 		# 以'import'或'from'来分割，分割后第1个元素是空串'',包保在第2个元素开始，
						# 去掉 . 开头的模块
						if not module_str.startswith('.'):
							module_str = module_str.split(' ')[0].strip()
							module_str = module_str.split('.')[0].strip()
							pyfile_imported_module_arr.append(module_str)

			linecache.clearcache()									
		
	pyfile_imported_module_arr = list(set(pyfile_imported_module_arr))	
	pyfile_imported_module_arr.sort(reverse=False)
						
	return pyfile_imported_module_arr
			
	
	
	
	
	
	
	
	
def get_pyproject_imported_modules(project_dir, save_to_file=True, out_file='requirements.txt'):
	"""
	功能说明：返回一个 python 项目中的所有 import 到的模块和包构成的 list（不含版本号）,
		如果有指定 out_file 的话，则同时将输出保存到 out_file 所指的文件中，
		在输出文件中所有的包统一附加了版本号 >=0.0.1，使用者若引用输出文件的话，请考虑清楚统一版本号0.0.1 是否适合你，不要盲目引用！！

	Parameters
	----------
		project_dir : type:str 项目路径。如果为 None，则直接取当前目录路径
		save_to_file: type: bool. 表示是否保存到文件，
			取值 True or False，True 表示需要保存到文件， False 表示不需要保存。
			若该值为 True，则下面的 out_file 起作用，否则忽略 out_file
		out_file : TYPE:str, optional
			用于保存结果的文件，一般就是 'requirements.txt' 这个文件名，最好不要更改。

	Returns
	-------
	返回值：项目中所有 import 的到模块或包构成的 list（不含版本号）

	"""
		
	project_dir = to_path(xpath=project_dir)
		
	pyproject_imported_modules_arr = [] 		# 初始化返回值为空 list
	
	file_type_arr = ['.py']
	# 所以如果想处理文件的话，只需对下面返回的 files 进行处理，每一次循环进来，files 都是指向某个目录下的所有文件，当循环结束，所有目录下的文件也遍历完了。
	for root,dir_arr,file_arr in os.walk(project_dir):
		root = to_path(xpath=root) 		# 把路径转成 linux 风格，并且以 / 结尾，以便后续可以添上文件名
		for filename in file_arr:
			filename = root + filename
			if file_type_arr is not None:
				for file_type in file_type_arr:
					if filename.endswith(file_type):
						# 流到了这里，确定了是 .py 文件，下面对文件进行读，以返回 module_arr
						pyfile_imported_module_arr = get_pyfile_imported_modules(pyfile=filename)
						pyproject_imported_modules_arr.extend(pyfile_imported_module_arr)
						break
	
	pyproject_imported_modules_arr = list(set(pyproject_imported_modules_arr))
	# ---------------------------------------------
	# 下面这个 dict 是包名到文件名的映射，表示如果上面扫描到的包名如果匹配到 dict 中的 key 名（即包名）的话，则将其转为 value 指向的名称（即文件名），以便可以 pip install 它。
	change_package_name_dict = {
		'Crypto': 'pycryptodome'
		}
	
	for key in change_package_name_dict.keys():
		if key in pyfile_imported_module_arr:
			pyfile_imported_module_arr[pyfile_imported_module_arr.index(key)] = change_package_name_dict[key]
	# ----------------------------------------------		

	pyproject_imported_modules_arr.sort(reverse=False)	

	if save_to_file:
		temp_arr = [x + '>=0.0.1' for x in pyproject_imported_modules_arr]
		module_str = '\n'.join(temp_arr)
		fp = open(project_dir + out_file,'w+')
		fp.write(module_str)
		fp.close()
	
	return pyproject_imported_modules_arr			
	
	
	
	
	
	
	
	
def get_kelly_percent(p,rl,rw):
	"""
	功能说明：获取用凯利公式计算后的下注百分比（应用凯利公式的前提是数学期望必须大于0，否则用不用凯利公式的结局都是亏！！）
			凯利公式（Kelly Formula）: f = p/rl - q/rw，  (即下注百分比 = 赢的概率/净损失率 - 输的概率/净收益率)
			p:表示赢的概率（必须是达到 rw 的概率）
			q: 表示输的概率（p + q = 1)（必须是达到 rl 的概率）
			rl: 损失率，即输掉时应当支付的百分比，譬如今天炒股亏损 5%， 那这个 rl 就取 5%，而上述的 q，就是指 rl 发生的概率
			rw: 收益率，即赢到的百分比，譬如今天炒股盈利 7%，则 rw 就取 7%，而上述的 p，就是指 rw 发生的概率
			注意：按照凯利公式，p + q 必须为 1， rl 和 rw 也必须是对立事件，不是这个发生就是那个发生。
				赌博不是输就是赢，其模型比较适合凯利公式；而炒股的股价是连续变化，未来股价变化有非常非常多的取值，每一个价格都有一个对应的概率，
				所以，股票模型是个概率分布，不是非此即彼的对立事件，同时，rl 和 rw 也成了概率分布，如此一来，凯利公式无法直接用在股票模型上，
				只有把股票的连续的价格变化通过抽象建模转换成二值对立事件，然后才可以套用凯利公式。
	Parameters
	----------
		p : TYPE: float
			表示赢的概率（必须是达到 rw 的概率）	
		rl : TYPE: float
			损失率，即输掉时应当支付的百分比，譬如今天炒股亏损 5%， 那这个 rl 就取 5%，而上述的 q，就是指 rl 发生的概率
		rw : TYPE: float
			收益率，即赢到的百分比，譬如今天炒股盈利 7%，则 rw 就取 7%，而上述的 p，就是指 rw 发生的概率
	Returns
	-------
	返回值：是一个百分比，表示按照可以承受损失的总本金的这个百分比去下注，会使收益最大化。
		（注意：只有当返回值大于 0 才有意义，如果返回值小于或等于 0，则不赌就是赢！！！！）

	"""	
	q = 1 - p 					# q 表示输的概率, p 表示赢的概率（p 和 q 是对立事件，他们概率之和为 1）
	f = p/rl - q/rw 			# 根据凯利公式求下注百分比
	
	return f
	
	
	
	
	
	

def get_pid_arr(xname=None,accurate=False,include_name=True):
	"""
	功能说明：根据参数 xname 查找相应的进程号，如果xname 为 None，则返回所有进程号

	Parameters
	----------
		xname : TYPE:str, optional，欲查找的进程名称，如果是 None，则返回所有进程id
		accurate: type:bool, default: False, 表示精确查找还是模糊查找，可取以下值：
			True: 表示精确查找，此时，只有进程名和输入的 xname 完全相等才返回进程id
			False: 表示模糊查找，此时，进程名只要包含 xname，则返回进程 id
		include_name: 表示返回的结果中是否需要包含进程名，可取以下值：
			True: 表示需要包含进程名（默认）
			False: 表示不需要包含进程名
	Returns
	-------
	返回值：进程 id 组成的 list

	"""
	pid_arr = [] 		# 初始化返回值 list，用于存放找到的进程号
	
	pid_name_arr = get_pid_name_arr() 		# 获取所有进程（包括进程名称和进程id）
	if len(pid_name_arr) > 0:
		for p_dict in pid_name_arr:
			# 如果 xname 是 None ，则返回所有进程 id
			if xname is None:
				if include_name:
					pid_arr.append(p_dict)
				else:
					pid_arr.append(p_dict['pid'])
			else:
				if accurate:
					if p_dict['name'] == xname:
						if include_name:
							pid_arr.append(p_dict)
						else:
							pid_arr.append(p_dict['pid'])					
				else:
					#match_arr = difflib.SequenceMatcher(a=p_dict['name'], b=xname).get_matching_blocks()
					match_arr = re.findall(xname, p_dict['name'])
					if len(match_arr) > 0: 
						if include_name:
							pid_arr.append(p_dict)
						else:
							pid_arr.append(p_dict['pid'])					
					
	return pid_arr	






def get_pid_name_arr():
	"""
	功能说明：获取所有进程
	Returns
	-------
	返回值：list，其元素是 dict，每个 dict 包含两个 key，分别是 'name', 'pid'，他们指向进程名和进程id
	"""
	p_arr = []
	for proc in psutil.process_iter():
		try:
			p_dict = proc.as_dict(attrs=['name','pid']) 		# 只取 'name' 和 'pid' 字段，将其转化为字典
		except psutil.NoSuchProcess:
			pass
		else:
			p_arr.append(p_dict)
			
	return p_arr
	
	
	
	
	
	
	
	
	
def get_project_lines(project_dir, file_type_str='.py;.c;.cpp;.js;.go;.m;.pl;.lua;.rb;.rs;.scala;.java', include_blank_line=False):
	"""
	功能说明：根据项目所在路径，统计项目所有源码文件总行数
	Parameters
	----------
		project_dir : TYPE:str
			说明：这是一条项目路径，必填。
		file_type: type:str
			说明：表示哪些文件类型需进行统计行数，它是一个字符串，把所有需统计的文件扩展名以点开头添加进这个字符，相互用分号隔开即可
		include_blank_line: type: bool，
			说明：表示是否统计空行，默认 False，表示不统计空行
	Returns
	-------
	返回值：总行数, int 型
	"""	
	project_dir = to_path(xpath=project_dir)
		
	file_type_arr = None
	if isinstance(file_type_str,str) and len(file_type_str)>0:
		file_type_arr = file_type_str.split(';')
		
	xcount = 0 		# 初始化要统计的总行数为 0
	# 下面这个 for 每一次循环进来都是进入 project_dir 下的一个不同目录，相当于自动递归调用，当 for 循环结束，project_dir下的所有目录也遍历完了。
	# 所以如果想处理文件的话，只需对下面返回的 files 进行处理，每一次循环进来，files 都是指向某个目录下的所有文件，当循环结束，所有目录下的文件也遍历完了。
	for root,dir_arr,file_arr in os.walk(project_dir):
		root = to_path(xpath=root) 		# 把路径转成 linux 风格，并且以 / 结尾，以便后续可以添上文件名
		for filename in file_arr:
			filename = root + filename
			if file_type_arr is not None:
				for file_type in file_type_arr:
					if filename.endswith(file_type):
						xcount += get_file_lines(filename=filename, include_blank_line=include_blank_line)
						break
			else:
				xcount += get_file_lines(filename=filename, include_blank_line=include_blank_line)
				
	return xcount			
	
	
	
	
	
	
	
	
def get_project_info(project_dir, file_type_str='.py;.c;.cpp;.js;.go;.m;.pl;.lua;.rb;.rs;.scala;.java'):
	"""
	功能说明：根据项目所在路径，统计项目所有源码文件累计有效代码行数，注释行数，空白行数等，
	Parameters
	----------
		project_dir : TYPE:str
			说明：这是一条项目路径，必填。
		file_type: type:str
			说明：表示哪些文件类型需进行统计行数，它是一个字符串，把所有需统计的文件扩展名以点开头添加进这个字符，相互用分号隔开即可
		include_blank_line: type: bool，
			说明：表示是否统计空行，默认 False，表示不统计空行
	Returns
	-------
	返回值：df，包含有效代码行数，注释行数，空白行数等列
	"""	
	project_dir = to_path(xpath=project_dir)
		
	file_type_arr = None
	if isinstance(file_type_str,str) and len(file_type_str)>0:
		file_type_arr = file_type_str.split(';')
		
	arr = [] 		# 初始化一个 list ，用于存入每个文件返回的 df(含代码行数、注释行数、空白行数等信息)
	# 下面这个 for 每一次循环进来都是进入 project_dir 下的一个不同目录，相当于自动递归调用，当 for 循环结束，project_dir下的所有目录也遍历完了。
	# 所以如果想处理文件的话，只需对下面返回的 files 进行处理，每一次循环进来，files 都是指向某个目录下的所有文件，当循环结束，所有目录下的文件也遍历完了。
	for root,dir_arr,file_arr in os.walk(project_dir):
		root = to_path(xpath=root) 		# 把路径转成 linux 风格，并且以 / 结尾，以便后续可以添上文件名
		for filename in file_arr:
			filename = root + filename
			#filename = filename.lower()
			if file_type_arr is not None:
				for file_type in file_type_arr:
					if filename.endswith(file_type):
						#print(filename)
						df = get_file_info(filename=filename)
						arr.append(df)
						break
			else:
				df = get_file_info(filename=filename)
				arr.append(df)
	# --------------
	df = None
	if len(arr) > 0:
		df = pd.concat(arr)
		df = df.reset_index(drop=True)
				
	return df			
	
	
	
	
	
	
	
	
		
def get_report_dir():
	"""
	说明：该函数用来获取 report/路径，如果没有则创建之。并且以 '/' 结尾
	返回值：report/ 目录在用户目录下完整路径
	"""
	home_dir = get_home_dir()
	report_dir = home_dir + 'report/'
		
	# 判断路径是否存在，若不存在，则创建
	if not os.path.exists(report_dir):
		os.makedirs(report_dir) 		# 创建文件夹。注意：report_dir 必须是全路径
	print('report dir is :',report_dir)

	return report_dir







	
def get_today():
	"""
	功能说明：获取今天日期（python格式）
	参数：无
	返回值：今天日期（python 格式)

	"""
	#today=time.strftime(date_format, time.localtime(time.time()))
	today = datetime.date.today()
	return today







def get_yesterday():
	"""
	功能说明：获取昨天日期（python格式）
	参数：无
	返回值：昨天日期（python 格式）
	"""
	#xstep=datetime.timedelta(days=1)
	yesterday = get_today() - get_days_step(n=1)
	return yesterday







def get_tomorrow():
	"""
	功能说明：获取明天日期（python格式）
	参数：无
	返回值：明天日期（python格式）
	"""
	#xstep=datetime.timedelta(days=1)
	tomorrow = get_today() + get_days_step(n=1)
	return tomorrow







def get_year(xdate=None):
	"""
	功能说明：对传入的日期取年份以数值型返回，
	参数：xdate，表示传入日期，取值可以是YYYY-mm-dd格式，或用 python 构造的日期型，
	返回值：年份（数值型）

	"""
	if xdate is None:
		xdate = get_today()
		return xdate.year

	xyear = None
	xdate = str(xdate)
	date_arr = xdate.split('-')
	if len(date_arr)>=1:
		try:
			xyear = int(date_arr[0])
		except:
			pass

	return xyear







def get_month(xdate=None):
	"""
	功能说明：对传入的日期取月份以数值型返回，
	参数：xdate，表示传入日期，取值可以是YYYY-mm-dd格式，或用 python 构造的日期型，
	返回值：整型月份

	"""
	if xdate is None:
		xdate = get_today()
		return xdate.month

	xmonth = None
	xdate = str(xdate)
	date_arr = xdate.split('-')
	if len(date_arr)>=2:
		try:
			xmonth = int(date_arr[1])
		except:
			pass

	return xmonth









def get_day(xdate=None):
	"""
	功能说明：对传入的日期取日份以数值型返回，
	参数：xdate，表示传入日期，取值可以是YYYY-mm-dd格式，或用 python 构造的日期型，
	返回值：整型日

	"""
	if xdate is None:
		xdate = get_today()
		return xdate.day
		
	xday = None
	xdate = str(xdate)
	date_arr = xdate.split('-')
	if len(date_arr)>=3:
		try:
			xday = int(date_arr[2])
		except:
			pass

	return xday







def get_time(xtime=None, time_format=cf.TIME_FORMAT):
	"""
	功能说明：根据传入的时间戳，取出时间返回
	参数：xtime: 是时间戳，如time.time() 返回的结果
	返回值：返回该时间戳指向的时间部分，以 HH:MM:SS 字符串格式返回。
	"""
	if xtime is None:
		xtime = time.time()
	time_result = time.strftime(time_format, time.localtime(xtime))

	return str(time_result)







def get_date(xtime=None):
	"""
	功能说明：根据传入的时间戳，取出日期返回
	参数：xtime: 是时间戳，如time.time() 返回的结果
	返回值：返回该时间戳指向的日期部分，以YYYY-MM-DD字符串格式返回。
	"""
	xdate = get_time(xtime=xtime, time_format=cf.DATE_FORMAT)

	return str(xdate)







def get_date_time(xtime=None, time_format=cf.DATE_TIME_FORMAT2):
	"""
	功能说明：根据传入的时间戳，取出日期时间返回
	参数：xtime: 是时间戳，如time.time() 返回的结果
	返回值：返回该时间戳指向的日期时间部分，以YYYY-MM-DD - HH:MM:SS 字符串格式返回。
	"""
	date_time = get_time(xtime=xtime, time_format=time_format)
	
	return date_time






def get_current_time(xtime=None, time_format=cf.DATE_TIME_FORMAT2):
	"""
	功能说明：根据传入的时间戳，取出时间返回
	参数：xtime: 是时间戳，如time.time() 返回的结果
	返回值：返回该时间戳指向的时间部分，以HH：MM：SS字符串格式返回。
	"""
	if xtime is None:
		xtime = time.time()
	if time_format.upper() == 'COMPACT': 		# 紧凑型时间格式，例：20191018
		time_format = cf.DATE_TIME_FORMAT3
	current_time = get_time(xtime=xtime, time_format=time_format)
	
	return current_time







def get_hh(xtime=None):
	"""
	功能说明：根据传入的时间 ，返回小时部分（整型）
	参数：xtime，可以是格式为 hh:mm:ss 的时间字符串，也可以是时间戳
	返回值：整型 hh
	"""
	if xtime is None:
		xtime = time.time()

	if is_number(xtime):
		xtime = get_time(xtime=xtime)

	hh = None
	time_arr = xtime.split(':')
	if len(time_arr) >= 1:
		hh = int(time_arr[0])

	return hh
	





def get_mm(xtime=None):
	"""
	功能说明：根据传入的时间 ，返回分钟部分（整型）
	参数：xtime，可以是格式为 hh:mm:ss 的时间字符串，也可以是时间戳
	返回值：整型 mm
	"""
	if xtime is None:
		xtime = time.time()

	if is_number(xtime):
		xtime = get_time(xtime=xtime)

	mm = None
	time_arr = xtime.split(':')
	if len(time_arr) >= 2:
		mm = int(time_arr[1])

	return mm
	






def get_ss(xtime=None):
	"""
	功能说明：根据传入的时间 ，返回秒数部分（整型）
	参数：xtime，可以是格式为 hh:mm:ss 的时间字符串，也可以是时间戳
	返回值：整型 ss
	"""
	if xtime is None:
		xtime = time.time()

	if is_number(xtime):
		xtime = get_time(xtime=xtime)

	ss = None
	time_arr = xtime.split(':')
	if len(time_arr) >= 3:
		ss = int(time_arr[2])

	return ss
	







def get_arr_add(arr1, arr2):
	"""
	功能说明：计算两个数组（相同维度）对应元素（必须数值型）的加法
	参数：arr1, arr2：参加求和的两个 list
	返回值：arr1 和 arr2 对应元素的求和结果（list型）
	"""
	result_arr = None

	if len(arr1) != len(arr2):
		print('错误！  %s 和 %s 维数不相等' % (str(arr1), str(arr2)))
		return None
	else:
		try:
			result_arr = (np.array(arr1) + np.array(arr2)).tolist()
		except:
			print('错误！ 两数组对应元素相加出错，请确保数组元素为数值型。')
			return None

	return result_arr	










def get_arr_sub(arr1, arr2):
	"""
	功能说明：计算两个数组（相同维度）对应元素（必须数值型）的减法(arr1 - arr2)
	参数：arr1, arr2：参加求差的两个 list
	返回值：arr1 和 arr2 对应元素的求差结果（list型）
	"""
	result_arr = None

	if len(arr1) != len(arr2):
		print('错误！  %s 和 %s 维数不相等' % (str(arr1), str(arr2)))
		return None
	else:
		try:
			result_arr = (np.array(arr1) - np.array(arr2)).tolist()
		except:
			print('错误！ 两数组对应元素相加出错，请确保数组元素为数值型。')
			return None

	return result_arr	











def get_arr_multiply(arr1, arr2):
	"""
	功能说明：计算两个数组（相同维度）对应元素（必须数值型）的乘积
	参数：arr1, arr2：参加求积的两个 list
	返回值：arr1 和 arr2 对应元素的求积结果（list型）
	"""
	result_arr = None

	if len(arr1) != len(arr2):
		print('错误！  %s 和 %s 维数不相等' % (str(arr1), str(arr2)))
		return None
	else:
		try:
			result_arr = (np.array(arr1) * np.array(arr2)).tolist()
		except:
			print('错误！ 两数组对应元素相乘出错，请确保数组元素为数值型。')
			return None

	return result_arr	










def get_arr_divide(arr1, arr2):
	"""
	功能说明：计算两个数组（相同维度）对应元素（必须数值型）的除法(arr1 / arr2)
	参数：arr1, arr2：参加求商的两个 list
	返回值：arr1 和 arr2 对应元素的求商结果（list型）	
	"""
	result_arr = None

	if len(arr2) == 0 or len(arr1) != len(arr2):
		print('错误！ %s 为空，或 %s 和 %s 维数不相等' % (str(arr2), str(arr1), str(arr2)))
		return None
	else:
		try:
			result_arr = (np.array(arr1) / np.array(arr2)).tolist()
		except:
			print('计算出错，可能 %s 数组中含有 0 值' % (str(arr2)))
			return None

	return result_arr









def get_arr_ratio(arr1, arr2):
	"""
	功能说明：计算两个等长数值数组 arr2 各元素相对于 arr1 各对应元素的增长幅度，即 (arr2 - arr1 ) / arr1 这个意思，
		具体要用到 numpy ，python 的 list 无法直接这样计算，必须先转成 numpy 的 array 才行。
	参数：arr1, arr2: 两个数值型 list		

	"""
	result_arr = None
	if len(arr1)==0 or len(arr1) != len(arr2):
		print('错误！ %s 为空，或 %s 和 %s 维数不相等' % (str(arr1), str(arr1), str(arr2)))
		return None
	else:
		try:
			result_arr = ((np.array(arr2) - np.array(arr1)) / np.array(arr1)).tolist()
		except:
			print('计算出错，可能 %s 数组中含有 0 值' % (str(arr1)))
			return None

	return result_arr











def get_current_function_name():
	"""
	功能说明：当该函数被调用时，将返回上级函数（即主调函数）的函数名，所以一般用它放在函数内部来获取函数名 
	参数：无
	返回值：主调函数名（字符串形式）
	"""
	# return sys._getframe(0).f_code.co_name 		# 返回本函数名
	return sys._getframe(1).f_code.co_name 			# 返回上级函数名（或模块名）







def get_hash(s, hash_mode='sha512'):
	"""
	功能说明：根据传入的哈希算法对传入的字符串 s 进行哈希计算，并将结果返回
	参数：s: 待计算字符串，hash_mode: 哪种哈希算法
	返回值：哈希计算后的结果（字符串类型）
	"""
	if hash_mode.upper() == 'MD5':
		result = get_hash_md5(s=s)

	if hash_mode.upper() == 'SHA512':
		result = get_hash_sha512(s=s)

	return result






def get_lastfile(xpath):
	"""
	功能说明：从 xpath 目录中找出修改时间为最新的一个文件，并返回给主调函数
	参数：xpath: 表示一条目录路径
	返回值：xpath 目录下修改时间最新的文件。
	"""
	lst = os.listdir(xpath)
	lst.sort(key=lambda fn: os.path.getmtime(xpath + fn) if not os.path.isdir(xpath + fn) else 0)
	#d = datetime.datetime.fromtimestamp(os.path.getmtime(xpath + lst[-1]))
	lastfile = lst[-1]
	#time_end=time.mktime(d.timetuple())
	return lastfile





def get_magic_square(n=3, arr=None):
	"""
	功能说明：该函数用于产生一个幻方，使得每一行、每一列以及对角线，他们各自的和都相等。
	参数：n: 方阵的边长，必须是大于等于 3 的正整数；
		arr（可选）: 是一个 list，表示需要对 arr 中的数求幻方，arr 的长度必须是一个奇数的平方数。
		arr 是可选的，如果输入 arr ，则不考虑 n
	返回值：幻方（df格式）
	"""
	if n is None or n < 3 or not isinstance(n, int):
		print('错误！请输一个大于 2 的正整数')
		return None	

	df = None 			# 初始化
	if n % 2 == 1:
		df = magic_square_odd_df(n=n, arr=arr)
	if n % 4 == 0:
		df = magic_square_4k_df(n=n)
	if n % 4 == 2:
		df = magic_square_4k_2_df(n=n)

	if df is not None:
		# 配上行和列名称
		row_arr = ['r' + str(c) for c in range(1, n + 1)]
		col_arr = ['c' + str(c) for c in range(1, n + 1)]
		df.index = row_arr
		df.columns = col_arr
		
	return df







def get_computer_name():
	"""
	功能说明：该函数用于获取电脑名称
	参数：无
	返回值：电脑名称（字符串类型）
	"""
	#获取本机电脑名
	#computer_name = socket.getfqdn(socket.gethostname())
	computer_name = socket.gethostname()

	return computer_name








def get_page_by_requests(url, header=None):
	"""
	说明：下载（获取）指定 URL 的页面源码。对于静态 html 或网站能直接提供数据的（包括api形式，string 形式，json形式等），
		请优先使用本接口去获取数据，次选上面的 get_page_by_urllib() 接口；
		若网站的数据没有直接给，而是用 js 方式提供的话，则请调用下面的 get_page_by_browser() 方式去获取，它是模拟浏览器的
	参数：url：目标地址; headers: 请求头，若没有传入，则由本函数自己调用请求头。
	返回值：url 指向的 page_source（本函数已经将取到的 page_source  decode() 成字符串形式（纯文本））
	"""
	if header is None:
		header = make_header()
	try:
		response = requests.get(url, headers=header)
	except:
		print('错误！ requests 没有请求到页面。若本机有VPN或开启了代理，请先关闭他们再尝试。')
		return None
	else:
		#charset = response.encoding 			# 从返回的字节流中提取字符编码方式，待会后面可能要用到
		#content = response.content
		#page_source = content.decode(charset)
		# 下面这句和上面注释掉的3句起相同作用
		page_source = response.text 			# 获取纯文本的网页源码
		return page_source  	








def get_page_by_gevent(url_arr, xcount=None):
	"""
	功能说明：调用该函数返回由url_arr 所指向的一堆url所对应的页面源码。
	Parameters
	----------
	url_arr : list
		是 url list，每个元素是一个 url
	xcount : int
		取值正整数或 None，表示url_arr 中完成几个即结束；默认值None ，表示需要完成所有 url 的请求

	Returns
	-------
	是一个 list ，每个元素是 url_arr 中相应 url 的 page_source
	"""
	if xcount is None or xcount <= 0 or xcount > len(url_arr):
		xcount = len(url_arr)
		
	g_arr = [] 		# 存放协程对象
	for url in url_arr:
		g = gevent.spawn(get_page_by_requests, url)
		g_arr.append(g)
	# gevent.wait() 执行 g_arr 中的各个协程对象，count = 1 表示g_arr 中的协程对象只要有一个完成了就立马返回主线程往下走，
	# 即执行 gevent.wait() 后面的代码，而不再等其他几个一起完成才返回主线程
	gevent.wait(g_arr, count=xcount)
	# 下面这个 for , 从上面返回的协程中提取 value.
	page_source_arr = []
	for g in g_arr:
		if g.value is None:
			continue
		else:
			page_source = g.value
			page_source_arr.append(page_source)
		
	return page_source_arr








def get_private_ip():
	"""
	功能说明：获取本机内网ip地址，这是获取到真实的内网IP，应优先使用本函数。
	参数：无
	返回值：本机内网 IP。
	"""
	return get_real_host_ip()






def get_public_ip():
	"""
	功能说明：获取本机公网ip地址
	参数：无
	返回值：本机公网 ip
	"""
	public_ip = None
	"""
	# 这里是同步代码，效率低下
	try:
		public_ip = get_public_ip_from_jsonip()
	except:
		try:
			public_ip = get_public_ip_from_httpbin()
		except:
			try:
				public_ip = get_public_ip_from_ipify()
			except:
				print('无法获取到本机公网 ip')
	"""
	# 下面是异步代码（用 gevent 做异步）
	g1 = gevent.spawn(get_public_ip_from_jsonip)
	g2 = gevent.spawn(get_public_ip_from_httpbin)
	g3 = gevent.spawn(get_public_ip_from_ipify)
	
	g_arr = [g1,g2,g3]
	# t1 = time.time()
	# gevent.wait() 执行 g_arr 中的各个协程对象，count = 1 表示g_arr 中的协程对象只要有一个完成了就立马返回主线程往下走，
	# 即执行 gevent.wait() 后面的代码，而不再等其他几个一起完成才返回主线程
	gevent.wait(g_arr, count=1)
	# time_spend(t1)
	# 下面这个 for , 从上面最早返回的协程中提取 value，并 kill 掉其他还没完成的协程。
	for g in g_arr:
		# print(g.value)
		if g.value is None:
			gevent.kill(g)
		else:
			public_ip = g.value
	
	return public_ip









def get_mac_address(): 
	"""
	功能说明：获取本机 MAC 地址
	"""
	# 先获取本机 MAC 地址（字符串形式的十六进制）
	mac = uuid.UUID(int=uuid.getnode()).hex[-12:]  
	# 将上述 MAC 地址字符串中的字母全部转成大写
	mac = mac.upper() 		
	# 再用冒号切分后返回
	return ":".join([mac[e:e+2] for e in range(0,11,2)])







def get_prime_arr(n=100):
	"""
	功能说明：返回 n 以内的所有素数
	"""
	if n is None or n < 2:
		print('请输入一个大于 2 的正整数')
		return None

	prime_arr = []
	for num in range(2, n + 1):
		if num == 2:
			prime_arr.append(num)
			continue
		if num % 2 == 0:
			continue
		#sqrt_num = int(math.sqrt(num)) + 1
		prime_flag = True

		for prime in prime_arr:
			if num % prime == 0:
				prime_flag = False
				break

			#if prime > sqrt_num:
			if prime * prime > num:
				break

		if prime_flag:
			prime_arr.append(num)

	return prime_arr








def get_count_24(num_arr, result=24, operator_arr=None, times_arr=[0]):
	"""
	功能说明: 根据传入的操作数 num_arr (list形式) 和操作符 operator_arr(list 形式), 每个数用且只用一次, 返回计算结果和 result 一致的表达式
	参数: num_arr: 操作数 list;  operator_arr: 操作符 list; result: 要求计算达到的结果
	返回值: 解的步骤（list 类型），list 中的每个元素（字符串）代表其中一步解
	"""
	if num_arr is None:
		print('错误! 请传入操作数 list')
		return None

	if 0 or '0' in num_arr:
		print('错误! 传入的操作数请不要包含 0, 避免计算过程中出现无穷大.')
		return None

	# 若没有传入操作符 list, 则初始化操作符 list 为加减乘除
	if operator_arr is None:
		operator_arr = ['+','-','*','/'] 		

	N = len(num_arr)
	M = len(operator_arr)
	total = pow(math.factorial(N), 2) / N * pow(M, N - 1)

	print('数据个数 N = %d' % (N))
	print('运算符个数 M = %d' % (M))
	print('最多有 %d 个计算表达式' % (int(total)))

	[procedure_arr,flag] = get_arr_rolling_count(num_arr=num_arr, operator_arr=operator_arr, result=result, times_arr=times_arr)
	#print('耗费 %d / %d 步.' % (times_arr[0], total))
	return procedure_arr







def get_randint_arr(xbegin=1, xend=10):
	"""
	功能说明：调用该函数返回一个在xbegin（含） 和 xend（含）之间的随机整数 list
	参数：xbegin：起始整数；xend: 结束整数
	返回值：随机整数构成的一维 list
	"""
	arr = [x for x in range(xbegin, xend + 1)]
	random.shuffle(arr)

	return arr










def get_randint_df(n=3):
	"""
	功能说明：调用该函数返回一个 n x n 的 元素为不大于 n 的随机整数构成的 df
	"""
	arr=[]
	col_arr = []

	for i in range(0, n):
		temp_arr = get_randint_arr(xend=n)
		arr.append(temp_arr)
		col_arr.append('col' + str(i))

	df = pd.DataFrame(data=arr, columns=col_arr)

	return df






def get_rsa_key(bit=1024):
	"""
	功能说明：本接口用来产生一对rsa public key 和 rsa private key
	参数：
		bit: int型，可选，默认值 1024
			说明：本参数表明密钥长度
		
	返回值：list，共有3个元素，第1个元素是 public key,字节流类型, 第2个元素是 private key，字节流类型；
			第3个元素表示能加密的明文长度，int型。

	"""
	# 计算能加密的最大明文长度
	max_length = int(bit/8) - 11
	pub_key, pri_key = rsa.newkeys(bit) 		# 调用 RSA 模块的 newkeys() 方法产生非对称密钥对，bit表示密钥长度
	# 调用自定义函数将对象型的公钥私钥转成字节流型
	byte_pub_key = rsa_key_to_byte(pub_key) 
	byte_pri_key = rsa_key_to_byte(pri_key)

	rsa_key_arr = [byte_pub_key, byte_pri_key, max_length]	
	
	return rsa_key_arr




	

def get_system_encoding():
	"""
	功能说明：获取操作系统的编码字符集
	"""
	#获取系统字符集
	system_encoding = sys.getfilesystemencoding()

	return system_encoding








def get_uuid():
	"""
	功能说明：该函数用于获取一个 uuid()，其作用是产生一个唯一数，一般用在某种场 合做 ID，并且以时间开头，方便需要时判断
	参数：无
	返回值：生成的十进制 uuid
	"""
	#return int(uuid.uuid1().hex, 16) 	# 调用模块 uuid 的 uuid1()函数，生成一个 uuid ，并转成10进制数返回
	s = get_time(xtime=time.time(), time_format=cf.DATE_TIME_FORMAT3)
	t = str(int(uuid.uuid1().hex, 16)) 	# 调用模块 uuid 的 uuid1()函数，生成一个 uuid ，并转成10进制数
	my_uuid = int(s+t)

	return my_uuid










def get_verify_code(code_image):
	"""
	功能说明：处理验证码，传入的参数 code_image 为待处理的验证码图片（不是图片文件，而是图片数据）
	参数：code_image: 待处理的验证码图片（不是图片文件，而是图片数据）
	返回值：文本验证码

	"""
	image_path = tempfile.mktemp()+'.jpg'
	code_image.capture_as_image().save(image_path)
	time.sleep(0.1)
	vcode = recognize_verify_code(image_path=image_path)

	return vcode











def hms_to_minutes(xtime):
	"""
	功能说明：将传入的 xtime 转为分钟数返回
	参数：xtime，取值可以为 hh:mm:ss 或时间戳
	返回值：分钟数
	"""	
	minutes = None
	hh = get_hh(xtime)
	mm = get_mm(xtime)
	if hh is not None and mm is not None:
		minutes = hh*60 + mm
	
	return minutes









def hms_to_seconds(xtime):
	"""
	功能说明：将传入的 xtime 转为秒数返回
	参数：xtime，取值可以为 hh:mm:ss 或时间戳
	返回值：秒数
	"""		
	seconds = None
	hh = get_hh(xtime)
	mm = get_mm(xtime)
	ss = get_ss(xtime)

	if hh is not None and mm is not None and ss is not None:
		seconds = hh*60*60 + mm*60 + ss
	
	return seconds






def hms_to_timestamp(xtime, xdate=None):
	"""
	功能说明：将输入的日期时间转成时间戳戳（timestamp），
	参数：xdate 可以是字符串形式，也可以是python date 格式，如果没有输入，则取今天
		xtime 是时间，需要 hh:mm:ss 形式
	返回值： 转换后的时间戳
	"""
	if xdate is None:
		xdate = get_today()
	t = str(xdate) + ' ' + str(xtime)
	t_arr = time.strptime(t, cf.DATE_TIME_FORMAT1)
	timestamp = time.mktime(t_arr) 				# 创建时间戳

	return timestamp







def int_to_list(intnum):
	"""
	功能说明：对输入的一个整型数 intnum 以 list形式返回，list 中的每个元素都是整型，他们是原整型数的各个数位
	"""
	s = str(intnum) 			# 将输入整数转成字符串
	arr = list(s) 				# 将字符串转成一个个字符构成的列表
	result_arr = list(map(lambda x:int(x), arr)) 		# 将上述 arr 中的每个字符型元素 map 成一个整型元素，形成列表返回

	return result_arr









def is_number(n):
	"""
	功能说明：测试输入的参数是否为数值型（或数值型字符串），如是则返回 True，否则返回 False
	参数：n: 待检测的数据
	返回值：如是数字则返回 True，否则返回 False
	"""
	if n is None:
		return False
		
	try:
		float(n)
	except ValueError:
		return False
	else:
		return True






def is_valid_date(xdate):
	"""
	功能说明：判断是否日期
	参数：xdate: 表示传入的日期
	返回值：True: 表示传入的的确是日期；False: 表示传入的不是日期
	"""
	try:
		time.strptime(str(xdate), cf.DATE_FORMAT)
	except:
		return False
	else:
		return True








def is_linux():
	"""
	功能说明：判断操作系统是否 linux，是的话返回 True, 否则返回 False

	"""
	os_system = sys.platform 			# 返回系统是哪种操作系统（字符串形式）
	if os_system.upper().find('LINUX') >= 0:
		return True
	else:
		return False






def is_windows():
	"""
	功能说明：判断操作系统是否 windows，是的话返回 True, 否则返回 False

	"""
	os_system = sys.platform 			# 返回系统是哪种操作系统（字符串形式）
	if os_system.upper().find('WIN') >= 0:
		return True
	else:
		return False








def is_weekday(xdate=None):
	"""
	功能说明：该函数用于判断传入的日期（若没传入，则判断今天）是否为周一到周五
	参数：xdate: 日期，取值可以是'-' 分割的字符串日期，也可以是 python 格式的日期
	返回值：如果是周一到周五，则返回True，否则返回 False
	"""
	if xdate is None:
		xdate = get_today()

	# 若是字符串形的日期，则先转化成python格式日期
	if isinstance(xdate, str):
		year = get_year(xdate=xdate)
		month = get_month(xdate=xdate)
		day = get_day(xdate=xdate)
		# 构造 python 日期
		xdate = datetime.date(year, month, day)

	n = xdate.weekday()
	if n >= 0 and n <= 4:
		return True
	else:
		return False








def is_weekend(xdate=None):
	"""
	功能说明：该函数用于判断传入的日期（若没传入，则判断今天）是否为双休日
	参数：xdate: 日期，取值可以是'-' 分割的字符串日期，也可以是 python 格式的日期
	返回值：若是双休日，则返回True，否则返回 False
	"""
	if xdate is None:
		xdate = get_today()

	# 若是字符串形的日期，则先转化成python格式日期
	if type(xdate) == str:
		year = get_year(xdate=xdate)
		month = get_month(xdate=xdate)
		day = get_day(xdate=xdate)
		# 构造 python 日期
		xdate = datetime.date(year, month, day)

	n = xdate.weekday()
	if n == 5 or n == 6:
		return True
	else:
		return False








def list_to_tuple(arr, quote_flag=False):
	"""
	功能说明：该函数用于将 list 转成 tuple，包括只有一个元素的情形 (注意：本函数将 list 转成 tuple 主要是给数据库 sql 用的，用在其他地方不一定合适)
	参数：arr, 待转换的数组，quote_flag 表示是否给转换后的每个元组元素加上单引号，如果是 True 的话就加，加上去主要为了给数据库查询语句 select 用
	返回值：xtuple, 字符串形式的元组
	"""
	#判断只有一个元素时要单独处理，如果直接用 tuple()转，则会在末尾加一个逗号，导致不符合数据库查询要求
	if len(arr) == 0:
		if quote_flag:
			xtuple="('')"

		if not quote_flag:
			xtuple = "()"		

	if len(arr) == 1:	
		if quote_flag:
			xtuple="('" + str(arr[0]) + "')"

		if not quote_flag:
			xtuple = "(" + str(arr[0]) + ")"

	if len(arr) > 1:
		if quote_flag:
			arr1 = [str(x) for x in arr]
			xtuple = tuple(arr1)

		if not quote_flag:
			xtuple = tuple(arr)

	return str(xtuple)









def make_api(dir_or_file, force=False, stop_func='z'):
	"""
	功能说明：本接口对指定的 python 项目或源码文件，生成 API 列表（不是说明文档），
		即相当于给 py 库文件的开头加上 __all__ , 并搜索所有接口定义（函数定义），将有定义的接口名放到 __all__ 这个 list 中，

	Parameters
	----------
		dir_or_file: 表示可以接受文件名或目录名
		force: type:bool, 表示是否重新生成 api list，无论是否已有 api list，可取以下值：
			True: 表示要重新生成 api list，即若有旧的 api list，则先删除它，然后生成新的 api list
			False: 表示如果已经有 api list，则直接返回。 （默认）
		stop_func : TYPE, optional
			是函数名，表示如果遇到了 stop_func，就停止搜索. 缺省函数名为 'z'.

	Returns
	-------
	返回值：无

	"""
	dir_or_file = change_path_style(xpath=dir_or_file) 		# 先转换路径风格到默认的 unix 风格
	# 判断是否文件，经各种测试，它能精准判断
	if os.path.isfile(dir_or_file):
		filename = dir_or_file
		make_pyfile_api(filename=filename, force=force, stop_func=stop_func)
	# 判断是否目录，经各种测试，它能精准判断		
	if os.path.isdir(dir_or_file):
		project_dir = dir_or_file
		project_dir = to_path(project_dir)
		file_type_arr = ['.py']
		# 下面这个 for 每一次循环进来都是进入 project_dir 下的一个不同目录，相当于自动递归调用，当 for 循环结束，project_dir下的所有目录也遍历完了。
		# 所以如果想处理文件的话，只需对下面返回的 files 进行处理，每一次循环进来，files 都是指向某个目录下的所有文件，当循环结束，所有目录下的文件也遍历完了。
		for root,dir_arr,file_arr in os.walk(project_dir):
			root = to_path(xpath=root) 		# 把路径转成 linux 风格，并且以 / 结尾，以便后续可以添上文件名
			for filename in file_arr:
				filename = root + filename
				if file_type_arr is not None:
					for file_type in file_type_arr:
						if filename.endswith(file_type):
							make_pyfile_api(filename=filename, force=force, stop_func=stop_func)
							break
							




	






def make_header():
	"""
	说明：构造一个 http 请求头返回
	"""
	user_agent_str = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
	try:
		ua = UserAgent()
		user_agent_str = ua.random
	except:
		print('警告：UserAgent() does not work or not exists.')
		pass
	# 构造一个 dict 形式的 http 请求头
	header = {
		'Connection': 'Keep-Alive',
		'Accept': 'text/html, application/xhtml+xml, */*',
		'Accept-Language':'zh-CN,zh;q=0.8',
		#'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
		#'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'
		'User-Agent': user_agent_str 			# 使用随机请求头（ua.random 返回的是字符串形式）
		}
	return header







def merge_list(arr,drop_duplicates=False):
	"""
	功能说明：合并 arr 中的元素（也是list）后返回

	Parameters
	----------
		arr: type:list，这是一个二维 list，其元素也是 list
		drop_duplicates: type:bool
			说明：该参数表示是合并 list 后是否去重，默认 False，表示不去重，即纯粹的合并，不做去重。
	Returns
	-------
	返回值：合并后的 list

	"""
	result_arr = []
	if isinstance(arr,list):
		for temp_arr in arr:
			if isinstance(temp_arr,list):
				result_arr += temp_arr
	if drop_duplicates:
		result_arr = list(set(result_arr))
	
	return result_arr
	
	
	
	
	
	
	
def num_to_words(num):
	"""
	功能说明：转换数字为大写（财务）货币格式( format_word.__len__() - 3 + 2位小数 )
	参数：num: 待转换的数字，支持 float, int, long, string 格式
	返回值：财务上的大写金额
	"""
	format_word = ["分", "角", "元",
			   "拾","佰","仟","万",
			   "拾","佰","仟","亿",
			   "拾","佰","仟","万",
			   "拾","佰","仟","兆"]

	format_num = ["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
	if type(num) == str:
		# - 如果是字符串,先尝试转换成float或int.
		if '.' in num:
			try:
				num = float(num)
			except:
				print('无法转换 %s' % (str(num)))
				return None
		else:
			try:
				num = int(num)
			except:
				print('无法转换 %s' % (str(num)))
				return None

	if type(num) == float:
		real_numbers = []
		for i in range(len(format_word) - 3, -3, -1):
			if num >= 10 ** i or i < 1:
				real_numbers.append(int(round(num/(10**i), 2)%10))

	elif isinstance(num, (int)):
		real_numbers = [int(i) for i in str(num) + '00']

	else:
		print('无法转换 %s' % (str(num)))
		return None

	zflag = 0                       #标记连续0次数，以删除万字，或适时插入零字
	start = len(real_numbers) - 3
	change_words = []
	for i in range(start, -3, -1):  #使i对应实际位数，负数为角分
		if 0 != real_numbers[start-i] or len(change_words) == 0:
			if zflag:
				change_words.append(format_num[0])
				zflag = 0
			change_words.append(format_num[real_numbers[start - i]])
			change_words.append(format_word[i+2])

		elif 0 == i or (0 == i%4 and zflag < 3):    #控制 万/元
			change_words.append(format_word[i+2])
			zflag = 0
		else:
			zflag += 1

	if change_words[-1] not in (format_word[0], format_word[1]):
		# - 最后两位非"角,分"则补"整"
		change_words.append("整")

	return ''.join(change_words)







def recognize_verify_code(image_path):
	"""
	功能说明：识别验证码，其中具体调用下面的 recognize_code_by_tesseract() 来识别
	参数：image_path: 图片路径
	返回值：文本形式的验证码

	"""
	#vcode = None
	img = Image.open(image_path) 			# 这里调用后返回 image 对象
	vcode = recognize_code_by_pytesseract(img=img) 			# 调用 tesseract 识别

	return vcode









def remove_df(df,to_be_remove_df):
	"""
	功能说明：不直接修改传入的 df!! 对传入的 df 去除 to_be_remove_df 中的数据后返回

	Parameters
	----------
		df : TYPE: pandas dataframe
			说明：股票信息数据（腾讯实时tick数据为宜，也可接受网易K线数据）
		to_be_remove_df: type: pandas dataframe
			说明：也是df格式的股票数据，这是从 df 中待删除的数据

	Returns
	-------
	返回值：df 去除 to_be_remove_df 中的数据后返回（df格式）
	
	"""
	result_df = None
	# 判断两个集合相等，即各列名相同（但不考虑顺序）
	#if set(df.columns) == set(to_be_remove_df.columns):
	# 下面这个 if 判断两个 list 是否相等，既要求列名相同，也要求各列顺序相同。只有这样才能 concat()，所以应当用这个条件来判断！
	if df.columns.tolist() == to_be_remove_df.columns.tolist(): 			# 记得一定要加 .tolist()，否则就会形成一个 list，其元素为 True 或 False，个数与列数相同。
		result_df = pd.concat([df,to_be_remove_df,to_be_remove_df])
		result_df = result_df.drop_duplicates(keep=False)
	else:
		print('错误！传入的两个 df 的列名、数量、顺序等都必须一致才行。')
		
	return result_df








def retry_command(command, para='', wait_time=None, retry_count=10, auto_wait=True):
	"""
	功能说明：对传入的命令command，尝试执行 retry_count 次, 只要执行到成功，立马返回
	参数：
		command: 传入的命令（对象）；
		para: 字符串形式的参数链，必须完整；
		wait_time: 表示两次尝试之间的等待时间；
		retry_count: 尝试执行次数; 
		auto_wait: 表示在每次尝试失败后是否愿意等待一段时间尝试下一次，True 表示愿意，False 表示不等待。
		如果 wait_time 不为 None ，则直接用 wait_time 而不考虑 auto_wait， 否则考虑 auto_wait, 如果这时 auto_wait为 True，则由系统自己决定等待时间，如果为 False，则采用 0 等待
	返回值：返回一个 list，包含两个元素[command, result], 第一个元素是传进来的 command 对象本身，第2个元素是执行结果。（因为有些执行是直接改变自身的，所以需要把自身改变后的 command 返回给主调函数）
	"""
	func_name = get_current_function_name()
	result = None
	xcount = 1
	while True:
		if xcount > retry_count:
			print(func_name,' 错误！ 已尝试 %d 次没能成功，不再尝试。' % (xcount))
			return None
		try:
			result = eval("command" + para) 				# 这个 "command" 就是指形参中的 command，但在这里必须写成字符串形式，因为是被 eval() 拿去执行的
		except:
			if wait_time is None:
				if auto_wait:
					time.sleep(xcount)
				else:
					time.sleep(0)
			else:
				time.sleep(wait_time) 			# 休息一个 wait_time ，防止爬的过快遭遇网站反爬
			xcount += 1
			continue
		else:
			break
	result_arr = [command,result]
	
	return result_arr






def run_thread(func, start=True, block=False, **kwargs):
	"""
	功能说明：本接口用于运行线程

	Parameters
	----------
		func : 函数名或方法名
			说明：这是待运行的线程（即函数名或方法名）
		start: type: bool, 表示是否在本接口内启动线程，默认 True，表示要启动；若为 False，则将线程返回给主调函数处理
		block: type:bool, 表示是否以阻塞方式运行 func，默认 False，表示非阻塞。
		**kwargs : TYPE: dict
			说明：这是上述线程 func（函数或方法）要用到的参数，字典形式传入

	Returns
	-------
	None.

	"""
	# 以线程方式启动函数 func；注意：参数 kwargs 所指内容是给 func 当参数用的，其他参数是给 Thread() 用的；
	job_thread = threading.Thread(target=func,kwargs=kwargs) 			# 注意：kwargs= 这个kwargs 是 Thread() 的命名参数，不能改名，后面传给它一个字典即可
	if start:
		job_thread.start()
	else:
		return job_thread 			# 如果不启动，则将线程返回给主调函数处理。
	print("%s, %s: 线程 %s 启动成功..." % (get_current_time(),get_current_function_name(),str(func)))
	if block:
		job_thread.join() 	# 这句千万不要使用，要不然将阻塞主线程
	






def run_process(func, name='process1', daemon=False, start=True, block=False, **kwargs):
	"""
	功能说明：本接口用于运行进程

	Parameters
	----------
		func : 函数名或方法名
			说明：这是待运行的进程（即函数名或方法名）
		name: 表示要启动的进程名称，这里随机取一个预设值，这个名称最好由外部传入以表达正确含义
		daemon: 表示子进程是否依赖主进程，如果是，则设置 daemon 为 True，表示子进程必须随主进程退出而退出，避免子进程被启动后而主进程已退出导致子进程成为僵尸进程。
		start: type: bool, 表示是否在本接口内启动进程，默认 True，表示要启动；若为 False，则将进程返回给主调函数处理
		block: type:bool, 表示是否以阻塞方式运行 func，默认 False，表示非阻塞。		
		**kwargs : TYPE: dict
			说明：这是上述进程 func（函数或方法）要用到的参数，字典形式传入

	Returns
	-------
	None.

	"""
	# 以进程方式启动函数 func, 注意：参数 kwargs 所指内容是给 func 当参数用的，其他参数是给 Process() 用的；
	job_process = multiprocessing.Process(target=func, name='process_'+name, kwargs=kwargs) 			# 注意：kwargs= 这个kwargs 是 Process() 的命名参数，不能改名，后面传给它一个字典即可
	job_process.daemon = daemon 			# 如果 daemon 为 True，主进程退出会强迫子进程也退出。False 的话主进程退出不管子进程，默认为 False
	if start:
		job_process.start()
	else:
		return job_process 			# 如果不启动，则将进程返回给主调函数处理。
	print("%s, %s: 进程 %s 启动成功..." % (get_current_time(),get_current_function_name(),str(func)))
	if block:
		job_process.join() 		# 这句一般不要使用，要不然将阻塞主线程
	







def seconds_to_hms(seconds):
	"""
	功能说明：将秒数转为 hms 形式
	参数：seconds，秒数
	返回值：hms, 表示 HH:MM:SS 格式的时间
	"""
	hh = int(seconds / 3600)
	mm = int((seconds % 3600) / 60)
	ss = int((seconds % 3600) % 60)
	# 用字符串内建方法，将原字符串靠右，左侧填'0' ，使得填好后的长度为 2
	hh = str(hh).rjust(2, '0') 			
	mm = str(mm).rjust(2, '0')
	ss = str(ss).rjust(2, '0')

	hms = hh + ":" + mm + ":" + ss

	return hms







def security_check(ip):
	"""
	功能说明：本函数获取本机 公网 ip ，和传入的 ip 比较，以判断程序是否运行在传入的 ip 电脑上，
		若不是，则返回 False 给上层代码，以决定是否退出，这样可防止程序被非法运行在指定 IP 以外的电脑上。
	参数：ip: 本程序能正确运行的电脑的 ip
	返回值：True or False,
	"""
	if ip is None:
		print('请输入本程序能正确运行的电脑 ip.')
		return False

	public_ip = get_public_ip()
	#hash_ip = get_hash(s=public_ip, hash_mode='sha512')

	if public_ip == ip:
		return True
	else:
		return False

	





	
def send_mail(msg_dict, receiver_arr, smtp_server, smtp_port, sender_email, sender_password, mode='inline'):
	"""
	功能说明：自定义发邮件函数，
	参数：
		msg_dict: 为邮件标题和内容构成的字典，只需包含content 和 subject 两项即可，有其他项数据也是可以的; 
			如果要发送图片，则要在 msg_dict 中定义 image_arr，即要定义 msg_dict['image_arr'], 而 image_arr 中的元素都是一条条指向图片的路径。
		receiver_arr: 邮件接收者email 构成的数组,如果是单个接收者也可以是字符串形式的 email地址 ；
		smtp_server: smtp 服务器IP或域名；
		smtp_port: smtp 服务器端口；
		sender_email: 邮件发送者的email 地址；
		sender_passwprd: 发送者的密码；
		mode: 取值为 inline 或 attachment，表示对图片是内嵌方式发还是附件形式发；
		注意，参数 receiver_arr 为数组形式，每个元素是字符串，内容是email 地址，如果有多个收件人，则在数组中以逗号分割; sender: 发件人的邮箱地址，字符串格式。
	返回值：无

	"""
	# 构造邮件信息 
	# 首先要构造 Multipart，有3种参数类型，分别是 mixed, related, alternative. 有效范围依次递减，mixed 级别最大，可以发文件邮件，HTML邮件，内嵌图像，发附件等等 
	msgRoot = MIMEMultipart('mixed')  		# MIMEMultipart 表示允许附件在邮件正文件中直接显示
	msgRoot['Subject'] = msg_dict['subject']
	msgText = MIMEText(msg_dict['content'], 'html', 'utf-8')			# 中文需参数‘utf-8’，单字节字符不需要 
	msgRoot.attach(msgText)

	#msgRoot['From'] = formataddr(['wind', cf.MAIL_SENDER])
	#msgRoot['To'] = formataddr(['Friend',','.join(receiver_arr)])
	msgRoot['From'] = formataddr(['',sender_email])
	msgRoot['To'] = formataddr(['',','.join(receiver_arr)])

	# 如果存在图片要发送，则把图片附加到邮件上
	#if 'image_arr' in msg_dict.keys():
	if msg_dict.get('image_arr') is not None:
		msgRoot = attach_mail_image(msgRoot=msgRoot, image_arr=msg_dict['image_arr'], mode=mode)
		
	if not isinstance(receiver_arr, list):
		receiver_arr = [receiver_arr]

	try:
		# 连接邮件服务器
		smtp = smtplib.SMTP_SSL(smtp_server, smtp_port)
		# 登录
		smtp.login(sender_email, sender_password)
		# 发送
		smtp.sendmail(sender_email, receiver_arr, msgRoot.as_string()) 
	except:
		print("邮件发送失败。")   
	else:
		print('Mail sent to %s successfully.' % (str(receiver_arr)))
		smtp.quit()  			








def sort_df_column(df, column_arr, inplace=False):
	"""
	功能说明：对传入的 df ，将其各列按照 column_arr 中的列顺序排列后形成新的 df 返回。
		1. 若 df 中的列名与 column_arr 没有交集，则返回原 df;
		2. 若 df 中的列名与 column_arr 只有部分交集，则只对 df 中的交集字段按 column_arr 排序，然后放在新 df 的前面，
			df中有而column_arr 中没有的字段统统按原来顺序排在新生成的 df 后面；
		3. 若 df 中的列名是 column_arr 子集，则将 df 中的所有列完全按照 column_arr 中的顺序排列。
	参数：
		df:待（按列）排序的 df; 
		column_arr: 被参照排序的字段 list
		inplace: 表示是否直接修改原 df，默认 False，表示先 copy 一个 df，然后对 copy 的 df 进行修改，inplace 可取以下值：
			True: 表示直接修改传入的 df
			False: 表示生成一个新的 df 进行修改，保持原 df 不变。
	返回值：列排序后的 df
	"""
	if inplace:
		result_df = df
	else:
		result_df = df.reset_index(drop=True) 			# reset_index() 做过后，再修改 result_df 就不影响原来的 df 了
	
	df_column_arr = result_df.columns.tolist() 			# 获取 df 的列名称
	position = 0
	for i,col in enumerate(column_arr):
		if col in df_column_arr:
			result_df.insert(position, col, result_df.pop(col))
			position += 1

	return result_df






def strdate_to_pydate(xdate):
	"""
	功能说明：将字符串形的日期，转化成python datetime.date() 表示的日期
	参数：xdate: 待转换的字符串形式的日期
	返回值：py 形式的日期

	"""
	# 下面这个 if 表示如果 xdate 本身已是 python datetime.date 类型的话，则直接返回，无需再转
	if isinstance(xdate,datetime.date):
		return xdate
	
	py_date=None 		# 如果传进来的日期是有效的，则转化成 datetime.date(y,m,d) 形式，并传递给变量 py_date

	if is_valid_date(xdate):
		xdate = str(xdate)
		temp_arr = xdate.split('-')
		y=int(temp_arr[0]) 		# 获取并转化年
		m=int(temp_arr[1]) 		# 获取并转化月
		d=int(temp_arr[2]) 		# 获取并转化日
		py_date=datetime.date(y,m,d)

	return py_date









def to_path(xpath=None, style=cf.UNIX_STYLE_ARR[0], end_slash=True):
	"""
	功能说明：转换路径风格
	参数：
		xpath: 为待转换的路径； 
		style： 为目标风格，接受值：'dos','windows','linux','unix', 以及他们的大写，含意与小写相同。默认 unix（linux）风格
		endwith: 表示转换路径后是否确保路径末尾必须有指定符号，默认 True，表示路径末尾必须有斜杠或反斜杠
			None: 表示不添加任何符号，保持原样
			True: 表示确保路径末尾以'/'或'\\'结尾
			False: 表示确保路径末尾没有'/'或'\\'结尾
	返回值：转换风格后的路径
	"""
	xpath = change_path_style(xpath=xpath, style=style, end_slash=end_slash)
	
	return xpath







def to_pydate(xdate):
	"""
	功能说明：将字符串形的日期，转化成python datetime.date() 表示的日期
	参数：
		xdate: 待转换的日期，可以是字符串型，py datetime.date() 型，或 df 中含有 date 的列
	返回值：py 形式的日期。如果传入的是 df ，则将 df 中 date列 转换成 py datetime.date() 然后返回 df，若没有 date 列，则将原 df 返回
		无论 df 中有没 'date' 列，返回的 df 的 index 和传入时保持一致。

	"""
	py_date = xdate 		# 预设直接返回传进来的值，即不做任何改动。
	
	if isinstance(xdate,pd.core.frame.DataFrame):
		# 流程进入这里的话，说明 xdate 是个 DataFrame
		if 'date' in xdate.columns:
			#df = xdate.copy(deep=True) 					# 防止对 xdate (df 类型) 的更改影响到函数外，这里copy一份仅在本函数内修改，同时，copy 后也是防止出现警告 "A value is trying to be set on a copy of a slice from a DataFrame"
			df = xdate.reset_index(drop=True) 			# reset_idnex() 做过后再修改，就不会影响原来的 df 了
			df['date'] = pd.to_datetime(df.date)
			df['date'] = df.date.dt.date 				# 解释：df.date.dt.date, 第一个 date 是字段名， 其类型是 datetime, 这种类型有个属性叫 dt，这个属性下有个子属性叫 date
			py_date = df 			# 返回改过后的 df
	else:
		py_date = strdate_to_pydate(xdate=xdate)
		
	return py_date
		
	
	
	
	
def timestamp_to_hms(xtime):
	"""
	功能说明：将时间戳转成 HH:MM:SS格式，丢掉日期部分
	参数：xtime: 时间戳格式
	返回值：HH:MM:SS格式的时间

	"""
	hms = get_time(xtime)
	
	return hms






def time_spend(t1):
	"""
	功能说明：该函数计算t1 到 t2 之间的时间差，并输出信息，一般在程序末尾调用，输出程序执行花了多少时间
	参数：t1： 表示起始时间，需时间戳形式，即秒数
	返回值：无
	"""
	t2 = time.time()
	begin_time = get_time(xtime=t1, time_format=cf.DATE_TIME_FORMAT2)
	end_time = get_time(xtime=t2, time_format=cf.DATE_TIME_FORMAT2)

	print("Begin time:", begin_time)
	print("end time:", end_time)

	# 秒数之差
	second_diff = t2 - t1
	days = int(second_diff / (3600 * 24)) 		# 计算流逝的天数

	second_diff = second_diff % (3600 * 24) 	# 取余数
	hms = seconds_to_hms(second_diff)
	if days == 0:
		s = "Time spend: %s" % (hms)
	else:
		s = "Time spend: %d 天 %s" % (days, hms)

	print(s)









def xround(f, bit=2):
	"""
	功能说明：由于 python3 的  round() 函数返回的结果与我们中国人的常规认识不同，所以自定义一个 xround() 函数 来代替系统提供的 round()
		注意：本函数是通过加一个较小的数（0.0000001） 来达到符合中国习惯的四舍五入目的的，精度为小数点后6位。
		请注意本法是否符合用户的四舍五入要求，若不符合，请不要调用！
	参数：f: 要进行四舍五入的目标数值, 也可以是dataframe 的数值列；bit: 表示保留几位小数
		注意：若是df传给f, 则 df 最好是独立的，否则就是对其它df 的引用，若传其他 df 的引用进来，则会产生slice 警告

	返回值：四舍五入后的数值

	"""
	result = None			# 预设返回值为 None
	alittle=0.0000001 		# 小幅修正值

	# 只有传入的数值的小数部分的长度小于上面的修正值时，才能继续下去，否则返回 None
	if bit <= 6:
		try:
			result=round(f+alittle, bit)
		except:
			print('xround 转换失败')
	else:
		print('错误：本函数最多支持 6 位精度。')

	return result



	





def z():
	"""
	功能说明：这个函数没有实际功能，仅仅是表明上面的公开接口到此为止，下面的函数都是内部私有函数。

	Returns
	-------
	None.

	"""
	print('这个函数没有实际功能，仅仅是表明上面的公开接口到此为止，下面的函数都是内部私有函数。')
	pass








# public API end （公开接口到这里结束！）
# public API end （公开接口到这里结束！）
# public API end （公开接口到这里结束！）
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------------------------------------------------------------------
# ======================================================================================================================================================
# ======================================================================================================================================================
# ======================================================================================================================================================
# ======================================================================================================================================================
# ======================================================================================================================================================
# ########################################################################################################################################################################################################













# ########################################################################################################################################################################################################
# *********************************************************************************************************************************************************************************************
# *********************************************************************************************************************************************************************************************
# *********************************************************************************************************************************************************************************************
# *********************************************************************************************************************************************************************************************
# *********************************************************************************************************************************************************************************************
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# private  private  private  private  private  private private
# 以下为私有函数，他们都是具体实现，只被上面 public API 函数调用，不宜对下面的具体实现直接公开成接口

def attach_mail_image(msgRoot, image_arr, mode='inline'):
	"""
	功能说明：msgRoot 是邮件基信息定义，一般由 email 包下的 MIMEMultipart() 函数的返回值得到，image_arr 是个数组，每个元素是图片文件所在的全路径（含图片文件名），
		该函数的作用是把 image_arr 数组中每条路径上的图片以邮件格式附加到 msgRoot，并把 msgRoot 带回主调函数，mode 表示图片内嵌到正文还是以附件形式。

	"""
	#for k,img_file in enumerate(msg_dict['image_arr']):
	for k,img_file in enumerate(image_arr):
		img_pos = '<p><img src="cid:imgid%d" /></p>' % (k)
		
		msgRoot.attach(MIMEText(img_pos, 'html', 'utf-8'))

		fp = open(img_file, 'rb')
		msgImage = MIMEImage(fp.read())
		fp.close()

		# 图片以内嵌方式发
		if mode == 'inline':
			msgImage.add_header('Content-ID', '<imgid%d>' % (k))
			#msgImage["Content-Disposition"] = 'inline; filename="imgid%s"' % (str(k))

		# 图片以附件方式发
		if mode == 'attachment':
			msgImage.add_header("Content-Disposition", "attachment", filename=os.path.split(img_file)[1])
			#msgImage["Content-Disposition"] = 'attachment; filename="%s"' % (os.path.split(img_file)[1])
			
		msgRoot.attach(msgImage)

	return msgRoot









def get_func_symbols():
	"""
	功能说明：定义一个字典，建立文件类型与其函数名，类名的对应关系	

	Returns
	-------
	返回值：是一个 dict，每个元素的 key 代表源码文件类型（如：.py），value 也是 DICT，value 中的 key func 指向各种语言的函数定义保留字；key xclass 指向类定保留字

	"""
	func_symbols = {
		'.py':{'func':'def',
				 'xclass':'class'}
		}
	
	return func_symbols
	
	
	
	
	

	
def get_hash_md5(s):
	"""
	功能说明：采用 md5 对传入的字符串 s 进行 hash 后返回
	"""
	result = hashlib.md5(str(s).encode('utf-8')).hexdigest()

	return result






def get_hash_sha512(s):
	"""
	功能说明：采用 sha512 对传入的字符串 s 进行 hash 后返回
	"""
	result = hashlib.sha512(str(s).encode('utf-8')).hexdigest()

	return result






def get_host_ip():
	"""
	功能说明：该函数用于获取内网 ip 地址。注意：在多张网卡（包括虚拟网卡）的情形下，取到的内网 IP 可能不是想要的 IP。
		建议使用上面的 get_real_host_ip()
	"""	
	computer_name = get_computer_name()
	#获取本机ip
	private_ip = socket.gethostbyname(computer_name)

	return private_ip






def get_real_host_ip():
	"""
	功能说明：获取本机内网ip地址，这是获取到真实的内网IP，比下面的 get_host_ip() 准确，应优先使用本函数。
	返回值：本机内网 IP。
	"""
	private_ip = None
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 80))
		private_ip = s.getsockname()[0]
	finally:
		s.close()

	return private_ip







def get_public_ip_from_jsonip():
	"""
	功能说明：从 jsonip 网站获取本机公网 ip
	"""
	url = 'https://jsonip.com'
	#header = make_header()
	#public_ip = json.loads(urlopen(url, header).read().decode('utf-8'))['ip']
	# 以下的 get_page_by_requests() 纯粹是取回网页并正确转码后形成字符串（纯文本）形式，他不关心是否为 json，
	page_source = get_page_by_requests(url)	
	public_ip = None
	if page_source is not None:
		# 经判断后这个网址返的数据格式是 json 格式，所以调用下面的 json.loads() 进行解析
		page_source = json.loads(page_source)	
		public_ip = page_source['ip']
	
	return public_ip




def get_public_ip_from_httpbin():
	"""
	功能说明：从 httpbin 网站获取本机公网 ip
	"""
	url = 'http://httpbin.org/ip'
	# header = make_header()
	# public_ip = json.loads(urlopen(url, header).read().decode('utf-8'))['origin']
	page_source = get_page_by_requests(url)
	public_ip = None
	if page_source is not None:
		page_source = json.loads(page_source)			
		public_ip = page_source['origin']

	return public_ip




def get_public_ip_from_ipify():
	"""
	功能说明: 从 ipify 网站获取本机公网 ip
	"""
	url = 'https://api.ipify.org/?format=json'
	# header = make_header()
	# public_ip = json.loads(urlopen(url, header).read().decode('utf-8'))['ip']
	page_source = get_page_by_requests(url)
	public_ip = None
	if page_source is not None:
		page_source = json.loads(page_source)			
		public_ip = page_source['ip']
	
	return public_ip




'''
def get_public_ip_from_sohu():
	"""
	功能说明：从sohu获取本机公网 ip

	"""
	url = "http://txt.go.sohu.com/ip/soip"
	# header = make_header()
	# page_source = urlopen(url, header).read().decode('utf-8')
	page_source = get_page_by_requests(url)
	public_ip = None
	if page_source is not None:
		ip_arr = re.findall('\d+\.\d+\.\d+\.\d+', str(page_source))
		public_ip = ip_arr[0]

	return public_ip
'''





def recognize_code_by_pytesseract(img):
	"""
	功能说明：调用 pytesseract 识别验证码。 pytesseract 识别准确率不是很高，但也够用了
	参数：img:传入的的图片文件路径
	返回值：对图片识别后的文本验证码字符返回

	"""

	# 设置环境变量
	# pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
	# tessdata_dir_config = '--tessdata-dir "D:/Program Files (x86)/Tesseract-OCR/tessdata"'

	try:
		vcode_str = pytesseract.image_to_string(img)
	except:
		print('pytesseract 未安装 或 tesseract-OCR 未安装，或已安装但传给 pytesseract 的参数有问题，验证码无法识别。')
		#return None
		raise

	valid_chars_arr = re.findall('[0-9A-Za-z]', vcode_str, re.IGNORECASE)
	vcode = ''.join(valid_chars_arr)

	return vcode

		
	
	
	
	
	
	

def make_pyfile_api_backup(filename, force=True, stop_func='z'):
	"""
	功能说明：本接口对指定的 python 源码文件，生成 API 列表（不是说明文档），
		即相当于给 py 库文件的开头加上 __all__ , 并搜索所有接口定义（函数定义），将有定义的接口名放到 __all__ 这个 list 中，

	Parameters
	----------
	filename : TYPE:str 
		python 源码文件
	force: type:bool，表示是否强制重新生成API 列表，可取以下值：
		True: 表示如果 API 列表即便已经存以，也会被删掉，然后重新生成 API 列表（默认值）
		False: 表示如果 API 列表已经存在的话，则立马返回，不再重新生成。
	stop_func : TYPE, optional
		是函数名，表示如果遇到了 stop_func，就停止搜索. 缺省函数名为 'z'.

	Returns
	-------
	返回值：无

	"""
	if not filename.endswith('.py'):
		print('错误：本接口 %s 只针对 .py 文件有效，不支持其他文件类型。' % (get_current_function_name()))
		return False
	# 如果强制重新生成 api list 的话，则先删除已有的 api list
	if force:
		delete_api_list(filename=filename)
	
	lines_arr = linecache.getlines(filename)
	
	api_arr = []
		
	found_get_api_list_flag = False 		# 初始化一个变量，表示有没找到 get_api_list() 这个函数
	
	for line in lines_arr:
		line = line.strip()
		# 下面这个 if 表示如果找到 '__all__' ，表示该 .py 文件中已经定义过接口，无需再生成接口列表，于是立即返回。
		if line.startswith('__all__'):
			return None
		# 下面这个 if 寻找函数定义。注间下面两个 def ，一个后面有空格，一个没有，这并不是错误，而是分析实际情形后采取这样做的。
		if line.startswith('def '):
			func_name = line.split('def')[1].strip()
			func_name = func_name.split('(')[0].strip()
			if stop_func is not None and func_name == stop_func:
				break
			else:
				# 下划线开头的函数定义，无论是一根下划线还是两根下划线，都是私有的，不能作为公共接口，要排除掉
				if not func_name.startswith('_'):
					api_arr.append(f"'{func_name}'")
					if func_name == 'get_api_list':
						found_get_api_list_flag = True
				
	# 如果有找到接口
	if len(api_arr) > 0:
		if not found_get_api_list_flag:
			api_arr.insert(0,"'get_api_list'")
			
		api_str = "__all__ = [\n\t\t" + ',\n\t\t'.join(api_arr) + "\n\t\t]"
		
		# 如果源码文件中没有找到 get_api_list() 这个函数，则下面就给它添加上去
		if not found_get_api_list_flag:
			# 注意，下面这个是字符串，不是函数定义，让它在顶格，不要缩进来，要不然把这个函数定义添加到其他.py 文件后也往后面缩了。
			get_api_list_str = '''
def get_api_list():
	"""
	功能说明：本函数仅仅用于返回可用接口列表，不在列表中列出的函数或接口等请不要调用，他们一般在内部实现使用，未来可能会改名或调整！！

	Returns
	-------
	返回值：可用接口, list形式

	"""
	return __all__

			'''

			api_str += '\n\n\n' + get_api_list_str
			
		content_str = api_str + '\n' + ''.join(lines_arr) 			# 中间这个 '\n' 不能少，要不然不停的操作增删 api list 之后，会导致 __all__ 和 get_api_list() 之间的空行不断减少直至最后出错。

		fp = open(filename,'w+',encoding='utf-8') 		# w+ 表示覆盖方式写，不是追加。 encoding='utf-8' 表示采用这个编码打开，否则下面 fp.write() 可能会出错。
		fp.write(content_str)
		fp.close()
		
	linecache.clearcache() 		# 清除 linecache 读出来的缓存内容
		
		
	
	
	
	
	
	
	
	
def make_pyfile_api(filename, force=False, stop_func='z'):
	"""
	功能说明：本接口对指定的 python 源码文件，生成 API 列表（不是说明文档），
		即相当于给 py 库文件的开头加上 __all__ , 并搜索所有接口定义（函数定义），将有定义的接口名放到 __all__ 这个 list 中，

	Parameters
	----------
	filename : TYPE:str 
		python 源码文件
	force: type:bool，表示是否强制重新生成API 列表，可取以下值：
		True: 表示如果 API 列表即便已经存以，也会被删掉，然后重新生成 API 列表
		False: 表示如果 API 列表已经存在的话，则立马返回，不再重新生成。（默认值）
	stop_func : TYPE, optional
		是函数名，表示如果遇到了 stop_func，就停止搜索. 缺省函数名为 'z'.

	Returns
	-------
	返回值：无

	"""
	filename = change_path_style(xpath=filename)
	print(filename)
	
	if not filename.endswith('.py'):
		print('警告：本接口 %s 只针对 .py 文件有效，不支持其他文件类型。' % (get_current_function_name()))
		return False
	
	real_filename = filename.split('/')[-1].strip()
	if real_filename.startswith('_'):
		print('警告：为安全起见，本接口 %s 不处理下划线开头的文件。' % (get_current_function_name()))
		return False

	# 如果强制重新生成 api list 的话，则先删除已有的 api list
	if force:
		delete_api_list(filename=filename)
	
	lines_arr = linecache.getlines(filename)
	result_dict = get_line_nums(filename=filename, lines_arr=lines_arr)
	comment_nums = result_dict['comment_nums'] 			# 这是注释行 list
	
	api_arr = []
		
	found_get_api_list_flag = False 		# 初始化一个变量，表示有没找到 get_api_list() 这个函数
	
	for num,line in enumerate(lines_arr):
		if num in comment_nums:
			continue
		
		line = line.strip()
		# 下面这个 if 表示如果找到 '__all__' ，表示该 .py 文件中已经定义过接口，无需再生成接口列表，于是立即返回。
		if line.startswith('__all__'):
			return None
		# 下面这个 if 寻找函数定义。注意下面两个 def ，一个后面有空格，一个没有，这并不是错误，而是分析实际情形后采取这样做的。
		if line.startswith('def '):
			func_name = line.split('def')[1].strip()
			func_name = func_name.split('(')[0].strip() 		# 提取函数名
			if stop_func is not None and func_name == stop_func:
				break
			else:
				# 下划线开头的函数定义，无论是一根下划线还是两根下划线，都是私有的，不能作为公共接口，要排除掉
				if not func_name.startswith('_'):
					api_arr.append(f"'{func_name}'")
					if func_name == 'get_api_list':
						found_get_api_list_flag = True
				
	# 如果有找到接口
	if len(api_arr) > 0:
		if not found_get_api_list_flag:
			api_arr.insert(0,"'get_api_list'")
			
		api_str = "__all__ = [\n\t\t" + ',\n\t\t'.join(api_arr) + "\n\t\t]"
		
		# 如果源码文件中没有找到 get_api_list() 这个函数，则下面就给它添加上去
		if not found_get_api_list_flag:
			# 注意，下面这个是字符串，不是函数定义，让它在顶格，不要缩进来，要不然把这个函数定义添加到其他.py 文件后也往后面缩了。
			get_api_list_str = '''
def get_api_list():
	"""
	功能说明：本函数仅仅用于返回可用接口列表，不在列表中列出的函数或接口等请不要调用，他们一般在内部实现使用，未来可能会改名或调整！！

	Returns
	-------
	返回值：可用接口, list形式

	"""
	return __all__

			'''

			api_str += '\n\n\n' + get_api_list_str
			
		content_str = api_str + '\n' + ''.join(lines_arr) 			# 中间这个 '\n' 不能少，要不然不停的操作增删 api list 之后，会导致 __all__ 和 get_api_list() 之间的空行不断减少直至最后出错。

		fp = open(filename,'w+',encoding='utf-8') 		# w+ 表示覆盖方式写，不是追加。 encoding='utf-8' 表示采用这个编码打开，否则下面 fp.write() 可能会出错。
		fp.write(content_str)
		fp.close()
		
	linecache.clearcache() 		# 清除 linecache 读出来的缓存内容
		
		
	
	
	
	
	
	
	
	
def magic_square_odd(n=3, arr=None):
	"""
	功能说明：该函数用来产生一个奇数阶方阵，使得横竖斜每条线加起来结果都相等
	参数：n ，必须是一个正的奇数，表示方阵的边长; 
		如果 n 没有输入, 则 arr 必须传入, arr 是一维 list, 元素个数必须是一个奇数的平方,函数表示对 arr 进行做幻方操作
	返回值：是符合要求的方阵（二维数组）
	"""

	if n is None and arr is None:
		print('错误! n 和 arr 必须输入其一')
		return None

	if arr is not None:
		n = int(math.sqrt(len(arr)))
		if pow(n, 2) != len(arr):
			print('错误! 传入的 arr 长度(即元素个数)必须是奇数的平方才行!')
			return None
	else:			
		if n is None or n <=2 or n % 2 != 1:
			print('错误！请输一个正的奇数')
			return None
		else:
			arr = list(range(1, pow(n, 2) + 1))

	result_arr = [[None for i in range(n)] for i in range(n)]

	i = 0
	j = 0
	
	#for num in range(1, pow(n, 2) + 1):
	for num in arr:
		if num == arr[0]:
			i = 0
			j = int(n / 2)
		else:
			if i == 0 and j == n - 1:
				i = 1
			else:
				old_i = i
				old_j = j

				i = i - 1
				j = j + 1

				if i < 0:
					i = n - 1
				if j > n - 1:
					j = 0

				if result_arr[i][j] is not None:
					i = old_i + 1
					j = old_j

		result_arr[i][j] = num

	return result_arr







def magic_square_odd_df(n=3, arr=None):
	"""
	功能说明：该函数用来产生一个奇数阶方阵，使得横竖斜每条线加起来结果都相等
	参数：n ，必须是一个正的奇数，表示方阵的边长; 
		如果 n 没有输入, 则 arr 必须传入, arr 是一维 list, 元素个数必须是一个奇数的平方,函数表示对 arr 进行做幻方操作
	返回值：是符合要求的方阵（df形式）
	"""	
	df = None
	result_arr = magic_square_odd(n=n, arr=arr)
	if result_arr is not None:
		df = pd.DataFrame(data=result_arr)
		df.index = range(0, len(df.index))
		df.columns = range(0, len(df.columns))

	return df









def magic_square_4k_df(n=4):
	"""
	功能说明: 这是双偶阶(4k)幻方.
	算法参考: https://wenku.baidu.com/view/8f81130d168884868662d608.html
	"""

	if n is None or n <=2 or n % 4 != 0:
		print('错误！请输一个正的4的倍数')
		return None

	#d2_arr = [[None for i in range(n)] for i in range(n)]

	d2_arr = get_d2_arr(n=n) 		# 初始化一个 n X n 的二维数组
	df1 = pd.DataFrame(data=d2_arr)

	d2_arr = get_d2_arr(n=n, asscending=False) 		# 初始化一个 n X n 的倒排二维数组
	df2 = pd.DataFrame(data=d2_arr) 		# 生成 DataFrame
	k = int(n / 4)
	# 从倒排的 df (即 df2)中扣取 4 块覆盖到df1 中相应的位置
	# 第 1 块(上块)
	df1.loc[0:(k - 1),k:(3 * k - 1)] = df2.loc[0:(k - 1),k:(3 * k - 1)]
	# 第 2 块(下块)
	df1.loc[(n - k):(n - 1),k:(3 * k - 1)] = df2.loc[(n - k):(n - 1),k:(3 * k - 1)]
	# 第 3 块(左块)
	df1.loc[k:(n - k - 1),0:(k - 1)] = df2.loc[k:(n - k - 1),0:(k - 1)]
	# 第 4 块(右块)
	df1.loc[k:(n - k - 1),(n - k):(n - 1)] = df2.loc[k:(n - k - 1),(n - k):(n - 1)]

	return df1










def magic_square_4k_2_df(n=6):
	"""
	功能说明: 这是单偶阶(4k + 2)幻方, 是3类幻方中最复杂的一种.
	算法参考: https://wenku.baidu.com/view/11402d1af7ec4afe04a1dfde.html
	"""

	if n is None or n <=2 or n % 4 != 2:
		print('错误！请输一个 4 * k + 2 的数(k 取正整数)')
		return None
	# k ，其含义就是 4*k + 2 中的 k 
	k = int(n / 4) 			
	# m,  代表的是 4*k + 2 这种方阵的边长的一半，
	# 因为这种单偶阶方阵是要切成4块大小相同的方阵并把他们放到4个象限中去的，这里 m 代表每个象限中的小方阵的边长
	m = int(n / 2) 			

	arr = list(range(1, pow(n, 2) + 1))
	arr_len = len(arr)

	# 把边长为 4 * k + 2 的单偶阶方阵切成 4 块
	arr1 = arr[0:int(arr_len * 1/4)]
	arr2 = arr[int(arr_len * 1/4):int(arr_len * 2/4)]
	arr3 = arr[int(arr_len * 2/4):int(arr_len * 3/4)]
	arr4 = arr[int(arr_len * 3/4):int(arr_len * 4/4)]

	# 对 4 块中的每一块按奇数阶幻方处理
	df1 = magic_square_odd_df(n=m, arr=arr1) 		# df1 代表象限1 中的数据，填数据顺序中的第 1 块（即 arr1) 数据
	df4 = magic_square_odd_df(n=m, arr=arr2) 		# df4 代表象限4 中的数据，填数据顺序中的第 2 块（即 arr2) 数据
	df2 = magic_square_odd_df(n=m, arr=arr3) 		# df2 代表象限2 中的数据，填数据顺序中的第 3 块（即 arr3) 数据 
	df3 = magic_square_odd_df(n=m, arr=arr4) 		# df3 代表象限3 中的数据，填数据顺序中的第 4 块（即 arr4) 数据


	# 开始交换。注意：pandas 的范围选择是闭区间的，是 [] 效果，而 python 语言的各种选择是首闭尾开区间的，是 [) 效果。
	temp_df = df1.loc[0:(k-1),0:(k-1)]
	temp_df = temp_df.copy(deep=True)
	df1.loc[0:(k-1),0:(k-1)] = df3.loc[0:(k-1),0:(k-1)]
	df3.loc[0:(k-1),0:(k-1)] = temp_df

	temp_df = df1.loc[(k+1):,0:(k-1)]
	temp_df = temp_df.copy(deep=True)
	df1.loc[(k+1):,0:(k-1)] = df3.loc[(k+1):,0:(k-1)]
	df3.loc[(k+1):,0:(k-1)] = temp_df

	temp_df = df1.loc[k,k:(k+(k-1))]
	temp_df = temp_df.copy(deep=True)
	df1.loc[k,k:(k+(k-1))] = df3.loc[k,k:(k+(k-1))]
	df3.loc[k,k:(k+(k-1))] = temp_df


	if k > 1:
		temp_df = df2.loc[:,2:k]
		temp_df = temp_df.copy(deep=True)
		df2.loc[:,2:k] = df4.loc[:,2:k]
		df4.loc[:,2:k] = temp_df

	# 交换完成后进行合并
	left_df = pd.concat([df1,df3])
	right_df = pd.concat([df2,df4])

	magic_df = pd.concat([left_df,right_df],axis=1)
	magic_df.index = range(0, len(magic_df.index))
	magic_df.columns = range(0, len(magic_df.columns))

	return magic_df









def get_d2_arr(n=3, asscending=True):
	"""
	功能说明: 该函数用来产生一个 n X n 的二维数组, asscending = True 表示从小到大, 否则就从大到小
	"""
	if n is None or n <=0:
		print('错误!  请输入一个正整数')
		return None

	d2_arr = []

	d1_arr = list(range(1, pow(n, 2) + 1))

	if not asscending:
		d1_arr.reverse() 				# 翻转排列, 即从大到小

	i = 0 		# 首个元素的下标
	while True:		
		temp_arr = d1_arr[i:i + n]
		if len(temp_arr) > 0:
			d2_arr.append(temp_arr)
		else:
			break

		i += n

	return d2_arr








def quick_sort(arr):    
	"""
	功能说明：对传入的数组进行快速排序，用到了递归
	参数：arr: 待排序的数组
	返回值：排序后的数组
	"""    
	if len(arr) >= 2:  # 递归入口及出口        
		mid = arr[len(arr)//2]  # 选取基准值，也可以选取第一个或最后一个元素        
		left, right = [], []  # 定义基准值左右两侧的列表        
		arr.remove(mid)  # 从原始数组中移除基准值        
		for num in arr:            
			if num >= mid:                
				right.append(num)       	# 大于基准值的，排在右侧      
			else:                
				left.append(num)        	# 小于基准值的，排在左侧
		return quick_sort(left) + [mid] + quick_sort(right) 		# 然后对左侧和右侧列表继续快速排序，即递归
	else:        
		return arr





		



def get_count_result(num1, num2, operator):
	"""
	功能说明: 对传入的 num1 和 num2,按操作符 operator 进行计算, 并把计算结果返回
	"""
	if (operator == '/' or operator =='%') and (num2 == 0 or str(num2) == '0'):
		#print('operator 为除法 / 或模 % 操作时，请确保 num2 不为 0')
		return None

	procedure_arr = [str(num1) + ' ' + operator + ' ' + str(num2)]
	expression = str(num1) + operator + str(num2)

	result = eval(expression)

	return [procedure_arr,result]







def get_arr_rolling_count(num_arr, operator_arr=None, result=24, times_arr=[0]):
	"""
	功能说明: 对传入的操作数 num_arr( list 形式)和 操作符 operator_arr(list 形式),进行运算, 
		目标是计算出 result, 若找到,则返回解法步骤; 若无解, 则返回空.
	"""

	if len(num_arr) == 1 and abs(float(num_arr[0]) - result) <= 0.000001:
		return [[],True]

	if len(num_arr) == 1 and abs(float(num_arr[0]) - result) > 0.000001:
		return [[],False]

	# -------------
	same_value_arr = [] # 保存相同的值对

	plus_arr = [] 		# 加法数组里保存值对
	minus_arr = [] 		# 减法数组里保存值对
	multi_arr = [] 		# 剩法数组里保存值对
	divide_arr = [] 	# 除法数组里保存值对
	# =================
	# 若没有传入操作符 list, 则初始化操作符 list 为加减乘除
	if operator_arr is None:
		operator_arr = ['+','-','*','/'] 		

	# ----------------------------
	for i,num1 in enumerate(num_arr):
		for j,num2 in enumerate(num_arr):
			if j == i:
				continue

			# ----------
			# 遇两个相同数, 后续只要计算一遍即可, 无需交换后再做一遍计算, 以节约时间.
			if num1 == num2:
				if [num1,num2] in same_value_arr:
					continue
				else:
					same_value_arr.append([num1,num2]) 		# 保存值对
			# =============


			# 初始化 一个子数组
			sub_num_arr = []
			for k,v in enumerate(num_arr):
				if k != i and k != j:
					sub_num_arr.append(v)
			
			for operator in operator_arr:
				# ----------------------
				# 遇加法的, 两个数只计算一遍即可, 无需重复计算, 因为两数交换后加法结果是一样的.
				if operator == '+':
					if [num1,num2] in plus_arr or [num2,num1] in plus_arr:
						continue
					else:
						plus_arr.append([num1,num2]) 		# 保存值对

				# 遇减法的, 若相同的被减数和减数已经出现过的话, 则无需重复再做
				if operator == '-':
					if [num1,num2] in minus_arr:
						continue
					else:
						minus_arr.append([num1,num2])

				# 遇乘法的, 两个数只计算一遍即可, 无需重复计算, 因为两数交换后乘法结果是一样的.
				if operator == '*':
					if [num1,num2] in multi_arr or [num2,num1] in multi_arr:
						continue
					else:
						multi_arr.append([num1,num2]) 		# 保存值对

				# 遇除法的, 若相同的被除数和除数已经出现过的话, 则无需重复再做
				if operator == '/':
					if [num1,num2] in divide_arr:
						continue
					else:
						divide_arr.append([num1,num2])

				# ====================
				# 对num1 和 num2 两个操作数按 operator 进行计算，返回的 result_arr 包含两个元素，第1个是表达式，第2个是计算结果值
				result_arr = get_count_result(num1=num1, num2=num2, operator=operator)
				times_arr[0] += 1 			# 这个是计数器, 上述 get_count_result() 每返回一次, 这里就 +1, 表示完成了一次计算
				#print(times_arr[0], end=', ')
				if result_arr is None:
					continue
				else:
					[procedure_arr,middle_result] = result_arr
					#sub_num_arr.append(middle_result) 			# 这句也是正确的, 但为了优先使用中间结果, 所以用下面这一句, 即把中间计算结果插到第一个位置
					sub_num_arr.insert(0, middle_result) 		# 将计算返回的值插入到第一个位置, 即优先使用中间的计算结果, 这样符合人的思维

					# 把上述计算结果放回原队列, 并去掉已经用过的数, 形成一个新的数字队列, 然后递归调用本函数, 直至队列中只剩下一个数据就结束
					[sub_procedure_arr,flag] = get_arr_rolling_count(num_arr=sub_num_arr, operator_arr=operator_arr, result=result, times_arr=times_arr)
					# flag 若为 True，表示子列数组找到了解法步骤并放在了 sub_procedure_arr 中，
					# 这里再插入本步解法步骤 procedure_arr 到 sub_procedure_arr 中当第一步，然后带回给上一级调用者，由上一层再插入他的步骤，层层返回去，
					# 注意：这里 sub_procedure_arr 包含了自本步以下的所有步骤。而 procedure_arr 就是指本步。
					if flag:
						sub_procedure_arr.insert(0, procedure_arr)
						return [sub_procedure_arr,flag]
					else:
						sub_num_arr.pop(0) 			# 如流程进入这里, 表明没有计算到目标值, 则去掉上面插进去的第一个值
						continue

	return [[],False]	
					








def rsa_key_to_byte(rsa_key):
	"""
	功能说明：将非对称加密 RSA 的 对象key(可以是 public key也可以是 private key) 转成 byte 型（即字节流），以便保存到文件
	参数：
		rsa_key，rsa对象型的key，必填
			说明: 该参数是由 rsa.newkeys() 生成的 public key 或 private key 对象
	返回值：转成字节流后的 key

	"""
	byte_key = rsa_key.save_pkcs1() 		# 将 rsa 对象 key 转成字节流
	#str_key = str_key.decode('utf-8') 				# 将字节流解码成字符串
	
	return byte_key







def byte_key_to_rsa(byte_key, xtype):
	"""
	功能说明：将字节流类型的 key 还原成 rsa 对象 key
	参数：
		byte_key，字节流型，必填
			说明: 该参数是字节流，必须是原先由 rsa 的对象 key 转化而来，否则无法还原回去.
		xtype, str型，必填
			说明：该参数是字符串，表明前面的 byte_key 是public key 还是 private key，因为不同性质的 key还原方法不同。可取以下值（不区分大小写）：
			'public': 表示传入的 byte_key 需还原成 rsa public key
			'private': 表示传入的 byte_key 需还原成 rsa private key
			
	返回值：转成 rsa 的 key对象

	"""
	#byte_key = str_key.encode('utf-8')
	
	rsa_key = None
	if xtype.upper() == 'PUBLIC':
		rsa_key = rsa.PublicKey.load_pkcs1(byte_key)
	if xtype.upper() == 'PRIVATE':
		rsa_key = rsa.PrivateKey.load_pkcs1(byte_key)
		
	return rsa_key
		
	
	
	
	
	
	
	
	
	
def rsa_encrypt(msg, public_key):
	"""
	功能说明：本接口是非对称加密。用公钥 public_key （字节流型）对传入的消息 msg （字符串型）进行非对称加密
	参数：
		msg: str型或字节流型，必填
			说明：该参数是待加密的数据，一般是字符串型，也可以是字节流型
		public_key： 字节流型, 必填
			说明：该参数是公开密钥，一般来自上述 get_rsa_key() 
	返回值：对 msg 加密后的数据（字节流型）

	"""	
	
	if isinstance(msg, bytes):
		pass
	else:
		msg = msg.encode()
	
	if isinstance(public_key, bytes):
		pass
	else:
		public_key = public_key.encode() 		# 转成字节流型
		
	rsa_public_key = byte_key_to_rsa(byte_key=public_key, xtype='public')
		
	# rsa 的加密或解密对象必须是 bytes 类型，即字节流型	，加密后也是 bytes 类型
	crypt_msg = rsa.encrypt(msg, rsa_public_key) 		
	
	result_arr = [crypt_msg]
	
	return result_arr







def rsa_decrypt(crypt_msg, private_key):
	"""
	功能说明：用私钥 private_key （字节流型）对传入的消息 crypt_msg （字节流型）进行非对称解密
	参数：
		crypt_msg: 字节流型，必填
			说明：该参数是用public key 加密过的字节流数据
		private_key： 字节流型, 必填
			说明：该参数是私有密钥，一般来自上述 get_rsa_key() 
	返回值：msg ，字节流型，是对 crypt_msg 解密后的数据（字节流型）

	"""	
	if isinstance(crypt_msg, bytes):
		pass
	else:
		crypt_msg = crypt_msg.encode()
		
	if isinstance(private_key, bytes):
		pass
	else:
		private_key = private_key.encode() 			# 转成字节流
		
	rsa_private_key = byte_key_to_rsa(byte_key=private_key, xtype='private')
	# rsa 的加密或解密对象必须是 bytes 类型，即字节流型	， 返回的结果也是字节流
	msg = rsa.decrypt(crypt_msg, rsa_private_key)
	
	return msg




	

def aes_encrypt(msg, key=None, key_len=16):
	"""
	功能说明：本接口是对称加密。用密钥 key （字节流型,长度需是16的倍数）对传入的消息 msg （字符串型）进行对称加密
	参数：
		msg: str型或字节流型，必填
			说明：该参数是待加密的数据，一般是字符串型，也可以是字节流型
		key： 字节流型, 可选，默认值：None
			说明：该参数是密钥，若该参数省略，则由本函数根据 key_len 自动产生 key
		key_len: int型，可选，默认值16
			说明：该参数在 key为None 时起作用，用于产生一个长度为 ken_len 的 key，key_len 必须是 16 或其倍数
	返回值：result_arr, 是一个 list, 第一个元素是对 msg 加密后的数据（字节流型），第二个元素是用于解密的 key, 第3个元素是解密要用到的参数 nonce

	"""	
	from Crypto.Cipher import AES
	#from Crypto.Util.Padding import pad
	from Crypto.Random import get_random_bytes	
	
	# msg 为要加密的内容
	if isinstance(msg, bytes):
		pass
	else:
		msg = msg.encode()
	
	if key is None:
		key = get_random_bytes(key_len)
		
	if isinstance(key, bytes):
		pass
	else:
		key = key.encode() 		# 转成字节流型

	if len(key) % 16 != 0:
		print('错误！输入的 key 长度必须是 16 或其整数倍；若key 没有输入，则参数 key_len 必须是 16 或其整数倍')		
		return None
	
	# 实例化加密套件，使用CTR模式
	cipher = AES.new(key, AES.MODE_CTR)
	nonce = cipher.nonce 		# 先获取随机数，
	# 对内容进行加密，
	crypt_msg = cipher.encrypt(msg)
	
	result_arr = [crypt_msg, key, nonce]
	
	return result_arr







def aes_decrypt(crypt_msg, key, nonce):
	"""
	功能说明：用私钥 key （字节流型）对传入的消息 crypt_msg （字节流型）进行对称解密
	参数：
		crypt_msg: 字节流型，必填
			说明：该参数是用public key 加密过的字节流数据
		key： 字节流型, 必填
			说明：该参数是私有密钥，一般来自相应的加密函数
	返回值：msg ，字节流型，是对 crypt_msg 解密后的数据（字节流型）

	"""	
	from Crypto.Cipher import AES
	
	if isinstance(crypt_msg, bytes):
		pass
	else:
		crypt_msg = crypt_msg.encode()
		
	if isinstance(key, bytes):
		pass
	else:
		key = key.encode() 			# 转成字节流
		
	# 实例化加密套件，使用CTR模式
	cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
	# 对内容进行加密，pad函数用于分组和填充
	msg = cipher.decrypt(crypt_msg)
	
	return msg




	

	

def chacha20_encrypt(msg, key=None, key_len=32):
	"""
	功能说明：本接口是流加密。用密钥 key （字节流型,长度需是16的倍数）对传入的消息 msg （字符串型）进行对称加密
	参数：
		msg: str型或字节流型，必填
			说明：该参数是待加密的数据，一般是字符串型，也可以是字节流型
		key： 字节流型, 必填
			说明：该参数是密钥
		key_len: int型，可选，默认值32
			说明：该参数表示 key 是长度是多少，一般需是16的整数倍
	返回值：是个list, 第一个元素是对 msg 加密后的数据（字节流型），第2个元素是解密要用到的 key, 第3个元素是解密要用到的nonce

	"""	
	from Crypto.Cipher import ChaCha20
	from Crypto.Random import get_random_bytes	
	
	# msg 为要加密的内容
	if isinstance(msg, bytes):
		pass
	else:
		msg = msg.encode()
	
	if key is None:
		key= get_random_bytes(key_len)
		
	if isinstance(key, bytes):
		pass
	else:
		key = key.encode() 		# 转成字节流型
		
	if len(key) % 16 != 0:
		print('错误！输入的 key 长度必须是 16 或其整数倍；若key 没有输入，则参数 key_len 必须是 16 或其整数倍')		
		return None
	# 实例化
	cipher = ChaCha20.new(key=key)
	nonce = cipher.nonce 		# 先获取随机数，
	# 对内容进行加密，
	crypt_msg = cipher.encrypt(msg)
	
	result_arr = [crypt_msg, key, nonce]
	
	return result_arr






def chacha20_decrypt(crypt_msg, key, nonce):
	"""
	功能说明：用私钥 key （字节流型）对传入的消息 crypt_msg （字节流型）进行对称解密
	参数：
		crypt_msg: 字节流型，必填
			说明：该参数是用public key 加密过的字节流数据
		key： 字节流型, 必填
			说明：该参数是私有密钥，一般来自相应的加密时用的那个 key  
		nonce: 解密需的随机数，这个随机数不能凭产生，必须来自相应的加密函数给出的随机数，用来反向解密用的
	返回值：msg ，字节流型，是对 crypt_msg 解密后的数据（字节流型）

	"""	
	from Crypto.Cipher import ChaCha20
	
	if isinstance(crypt_msg, bytes):
		pass
	else:
		crypt_msg = crypt_msg.encode()
		
	if isinstance(key, bytes):
		pass
	else:
		key = key.encode() 			# 转成字节流
		
	cipher = ChaCha20.new(key=key, nonce=nonce)
	# rsa 的加密或解密对象必须是 bytes 类型，即字节流型	， 返回的结果也是字节流
	msg = cipher.decrypt(crypt_msg)
	
	return msg




	

	
def arc4_encrypt(msg, key=None, key_len=32):
	"""
	功能说明：本接口是流加密。用密钥 key （字节流型,长度需是16的倍数）对传入的消息 msg （字符串型）进行对称加密
	参数：
		msg: str型或字节流型，必填
			说明：该参数是待加密的数据，一般是字符串型，也可以是字节流型
		key： 字节流型, 必填
			说明：该参数是密钥
		key_len: int型，可选，默认值32
			说明：该参数表示 key 是长度是多少，一般需是16的整数倍
	返回值：是个 list，第一个元素是对 msg 加密后的数据（字节流型），第2个元素是解密要用的 key

	"""	
	from Crypto.Cipher import ARC4
	from Crypto.Random import get_random_bytes	
	
	# msg 为要加密的内容
	if isinstance(msg, bytes):
		pass
	else:
		msg = msg.encode()
	
	if key is None:
		key= get_random_bytes(key_len)
		
	if isinstance(key, bytes):
		pass
	else:
		key = key.encode() 		# 转成字节流型
		
	if len(key) % 16 != 0:
		print('错误！输入的 key 长度必须是 16 或其整数倍；若key 没有输入，则参数 key_len 必须是 16 或其整数倍')		
		return None
	# 实例化
	cipher = ARC4.new(key=key)
	# 对内容进行加密，
	crypt_msg = cipher.encrypt(msg)
	
	result_arr = [crypt_msg, key]
	
	return result_arr






def arc4_decrypt(crypt_msg, key):
	"""
	功能说明：用私钥 key （字节流型）对传入的消息 crypt_msg （字节流型）进行对称解密
	参数：
		crypt_msg: 字节流型，必填
			说明：该参数是用public key 加密过的字节流数据
		key： 字节流型, 必填
			说明：该参数是私有密钥，一般来自相应的加密时用的那个 key  
		nonce: 解密需的随机数，这个随机数不能凭产生，必须来自相应的加密函数给出的随机数，用来反向解密用的
	返回值：msg ，字节流型，是对 crypt_msg 解密后的数据（字节流型）

	"""	
	from Crypto.Cipher import ARC4
	
	if isinstance(crypt_msg, bytes):
		pass
	else:
		crypt_msg = crypt_msg.encode()
		
	if isinstance(key, bytes):
		pass
	else:
		key = key.encode() 			# 转成字节流
		
	cipher = ARC4.new(key=key)
	# rsa 的加密或解密对象必须是 bytes 类型，即字节流型	， 返回的结果也是字节流
	msg = cipher.decrypt(crypt_msg)
	
	return msg




	

	

	
# 具体实现的私有函数到这里结束！！这些具体实现不宜对外公开成接口！
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# *********************************************************************************************************************************************************************************************
# *********************************************************************************************************************************************************************************************
# *********************************************************************************************************************************************************************************************
# *********************************************************************************************************************************************************************************************
# *********************************************************************************************************************************************************************************************
# ########################################################################################################################################################################################################








if __name__ == "__main__":
	"""
	# ---------------------
	url="https://finance.sina.com.cn/stock/"
	page = get_page_by_requests(url)
	print(page)
	# ===================
	msg = "hello,world! The world is so beautiful!"
	
	result_arr = aes_encrypt(msg)
	
	[crypt_msg, key, nonce] = result_arr
	
	print(crypt_msg)
	print(key)
	print(nonce)
	
	original_msg = aes_decrypt(crypt_msg, key, nonce)
	
	print(original_msg)
	"""
	
	line="'''__all__ = [ """
	
	symbols = get_comment_symbols()
	comment_symbol_arr = symbols['.py']
	
	comment_start_symbol = get_comment_start_symbol(line=line, comment_symbol_arr=comment_symbol_arr)
	
	print(comment_start_symbol)
	
	print('Done.')
	
	