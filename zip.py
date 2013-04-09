import zipfile
f = zipfile.ZipFile('ziptest.zip', 'w')
f.write('changelog')
f.write('install.py')
f.close()
