<p>This script checks files by known hash sums. </p>
<p>Information about files must be in a file has extention .check and likes this:</p>
<p>
  file_01.bin md5 aaeab83fcc93cd3ab003fa8bfd8d8906<br>
  file_02.bin md5 6dc2d05c8374293fe20bc4c22c236e2e<br>
file_03.bin md5 6dc2d05c8374293fe20bc4c22c236e2e<br>
файл_04.txt sha1 da39a3ee5e6b4b0d3255bfef95601890afd80709.
</p>
<p>To run script you need do:<br>
python fcbh.py [path to the input file] [path to the directory containing the files to check].</p>
<p>Input files may be more then one: as much as you like.
If arguments are absent, all files and script must be in an one current folder.
If one argument is present, the input file and the files to check must be in an one folder with path is in the argument.</p>
<p>Output will in the stdout likes this:<br>
  file_01.bin OK<br>
  file_02.bin FAIL<br>
  file_03.bin NOT FOUND<br>
  файл_04.txt OK.</p>
