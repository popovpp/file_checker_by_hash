import hashlib
from sys import argv
import os


def get_hash(hstr, method):

    hash_dict = {'md5':(hashlib.md5(hstr)).hexdigest(),
            'sha1':(hashlib.sha1(hstr)).hexdigest(),
            'sha256':(hashlib.sha256(hstr)).hexdigest()}
    return hash_dict[method]


if __name__=='__main__':
    path1 = None
    path2 = None
    try:
        path1 = argv[1]
        path2 = argv[2]
    except:
        if path2 is None:
            path2 = os.getcwd()
        if path1 is None:
            path1 = os.getcwd()
    filename_to_check_list = [f for f in os.listdir(path1) if f.endswith('.check')]
    if len(filename_to_check_list) > 0:
        for filename_to_check in filename_to_check_list:
            with open(''.join((path1, filename_to_check)), 'r') as f:
                for s in f:
                    filename = s.rsplit()[0]
                    method = s.rsplit()[1]
                    hash_sum = s.rsplit()[2]
                    try:
                        with open(''.join((path2, filename)), 'rb') as f1:
                            hstr = f1.read()
                            f1.close()
                            h1h = get_hash(hstr, method)
                            if h1h == hash_sum:
                                print(filename, 'OK')
                            else:
                                print(filename, 'FAIL')
                    except FileNotFoundError:
                        print(filename, 'NOT FOUND')
    else:
    	print('INPUT FILE WITH EXTENTION ".check" NOT FOUND')
