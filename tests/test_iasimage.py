import os
import sys
import unittest
import subprocess
import filecmp
import shutil

IASIMAGE='iasimage.py'
ENV='/usr/bin/env'

class MyTests(unittest.TestCase):

	def setUp(self):
		pass

	def tearDown(self):

		shutil.rmtree('extract', ignore_errors=True)
		files_to_clean = ['cmdline.txt', 'bzImage.bin', 'initrd.bin', 
		                  'output.bin', 'output.hash', 'output.sig',
		                  'test_key.pem', 'public_key.pem', 'output.signed.bin']
		for f in files_to_clean:
			try:
				os.remove(f)
			except OSError:
				pass

	def test_help(self):
		cmd = [ENV, 'python', IASIMAGE, '-h']
		subprocess.check_call(cmd)

	def test_version(self):
		cmd = [ENV, 'python', IASIMAGE, '-V']
		subprocess.check_call(cmd)

	def test_create_and_extract_then_compare(self):
		with open('cmdline.txt', 'wb') as cmd_f:
			cmd_f.write(b'c' * 128)
		with open('bzImage.bin', 'wb') as bz_f:
			bz_f.write(b'b' * 1024 * 1024 * 2)
		with open('initrd.bin', 'wb') as initrd_f:
			initrd_f.write(b'f' * 1024 * 1024 * 3)
		cmd = [ENV, 'python', IASIMAGE, 'create', '-o', 'output.bin', 
		       '-i', '0x30000', 'cmdline.txt', 'bzImage.bin', 'initrd.bin']
		subprocess.check_call(cmd)

		cmd = [ENV, 'python', IASIMAGE, 'extract', 'output.bin']
		subprocess.check_call(cmd)

		self.assertTrue(filecmp.cmp('cmdline.txt', os.path.join('extract', 'image_0.bin')))
		self.assertTrue(filecmp.cmp('bzImage.bin', os.path.join('extract', 'image_1.bin')))
		self.assertTrue(filecmp.cmp('initrd.bin',  os.path.join('extract', 'image_2.bin')))

	def test_create_then_sign(self):
		with open('cmdline.txt', 'wb') as cmd_f:
			cmd_f.write(b'c' * 128)
		with open('bzImage.bin', 'wb') as bz_f:
			bz_f.write(b'b' * 1024 * 1024 * 2)
		cmd = [ENV, 'python', IASIMAGE, 'create', '-o', 'output.bin', 
		       '-i', '0x30000', 'cmdline.txt', 'bzImage.bin']
		subprocess.check_call(cmd)

		# Get hash
		cmd = ['openssl', 'dgst', '-binary', '-sha256', '-out', 'output.hash', 'output.bin']
		subprocess.check_call(cmd)

		# Create a new test RSA key
		cmd = ['openssl', 'genrsa', '-out', 'test_key.pem', '2048']
		subprocess.check_call(cmd)

		# Get signature from hash and test key
		cmd = ['openssl', 'pkeyutl', '-in', 'output.hash', '-out', 'output.sig',
		       '-sign', '-inkey', 'test_key.pem', '-pkeyopt', 'digest:sha256']
		subprocess.check_call(cmd)

		# Get publick key from test key
		cmd = ['openssl', 'rsa', '-pubout', '-in', 'test_key.pem', '-out', 'public_key.pem']
		subprocess.check_call(cmd)

		# Attach signature to output.bin
		cmd = [ENV, 'python', IASIMAGE, 'sign', '-o', 'output.signed.bin', '-s', 'output.sig',
		       '-k', 'public_key.pem', 'output.bin']
		subprocess.check_call(cmd)


if __name__ == '__main__':
	unittest.main()

