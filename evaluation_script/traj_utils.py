# Author: Xinshuo Weng
# email: xinshuo.weng@gmail.com

import copy, os, sys

def isstring(string_test):
	if sys.version_info[0] < 3:
		return isinstance(string_test, basestring)
	else:
		return isinstance(string_test, str)

def safe_path(input_path, warning=True, debug=True):
    '''
    convert path to a valid OS format, e.g., empty string '' to '.', remove redundant '/' at the end from 'aa/' to 'aa'

    parameters:
    	input_path:		a string

    outputs:
    	safe_data:		a valid path in OS format
    '''
    if debug: assert isstring(input_path), 'path is not a string: %s' % input_path
    safe_data = copy.copy(input_path)
    safe_data = os.path.normpath(safe_data)
    return safe_data

def fileparts(input_path, warning=True, debug=True):
	'''
	this function return a tuple, which contains (directory, filename, extension)
	if the file has multiple extension, only last one will be displayed

	parameters:
		input_path:     a string path

	outputs:
		directory:      the parent directory
		filename:       the file name without extension
		ext:            the extension
	'''
	good_path = safe_path(input_path, debug=debug)
	if len(good_path) == 0: return ('', '', '')
	if good_path[-1] == '/':
		if len(good_path) > 1: return (good_path[:-1], '', '')	# ignore the final '/'
		else: return (good_path, '', '')	                          # ignore the final '/'
	
	directory = os.path.dirname(os.path.abspath(good_path))
	filename = os.path.splitext(os.path.basename(good_path))[0]
	ext = os.path.splitext(good_path)[1]
	return (directory, filename, ext)

class AverageMeter(object):     
  """Computes and stores the average and current value"""    
  def __init__(self):   
    self.reset()
  
  def reset(self):
    self.val = 0
    self.avg = 0
    self.sum = 0
    self.count = 0    
    self.list = list()
  
  def update(self, val, n=1): 
    self.val = val    
    self.sum += val * n     
    self.count += n
    self.avg = self.sum / self.count  
    self.list.append(val)

def islist(list_test):
	return isinstance(list_test, list)

def safe_list(input_data, warning=True, debug=True):
	'''
	copy a list to the buffer for use

	parameters:
		input_data:		a list

	outputs:
		safe_data:		a copy of input data
	'''
	if debug: assert islist(input_data), 'the input data is not a list'
	safe_data = copy.copy(input_data)
	return safe_data

def remove_list_from_list(input_list, list_toremove_src, warning=True, debug=True):
	'''
	remove a list "list_toremove_src" from a list "list_src" if found, skip if not found

	parameteters:
		input_list:				a list to be removed from
		list_toremove_src:		a list to be removed

	outputs:
		list_remained:			a list of remaining elements after removal
		list_removed:			a list of elements to be successfully removed 
								(as some elements in list_toremove_src may not found in list_src, where the removal fails)
	'''
	list_remained = safe_list(input_list, warning=warning, debug=debug)
	list_toremove = safe_list(list_toremove_src, warning=warning, debug=debug)
	list_removed = []
	for item in list_toremove:
		try:
			list_remained.remove(item)
			list_removed.append(item)
		except ValueError:
			if warning: print('Warning!!!!!! Item to remove is not in the list. Remove operation is not done.')

	return list_remained, list_removed

def remove_unique_item_from_list(input_list, item, warning=True, debug=True):
	'''
	remove all instances of a single item from a list

	parameters:
		input_list:				a list to be removed from

	outputs:
		list_remained:			a list of remaining elements after removal
		count_removal:			number of times the requested item to be removed
	'''
	list_remained = safe_list(input_list, warning=warning, debug=debug)
	count_removal = 0
	while 1:
		try: 
			list_remained.remove(item)
			count_removal += 1
		except ValueError:
			if warning and count_removal == 0: print('Warning!!!!!! Item to remove is not in the list. Remove operation is not done.')
			break

	return list_remained, count_removal