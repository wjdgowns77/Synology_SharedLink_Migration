
print("프로그램 시작중입니다..")
print("\n\n\n")

program_info = "SharedLink_CSV_to_Html.py of GhostUser#2863"
program_info = program_info + "\n" + "Ver DSM52_20210922_ES01"
print('Init\n\n')
print('This program is developed for Synology DSM "Shared Link" Migration')
print('You must convert synology Shared Link Database file (/usr/syno/etc/filebrowser/fbsharing.db) to CSV file with "DB Browser for SQLite" program( SET Mode = TAB ) Before run this program!!')

'''
This program is developed for Synology DSM's "Shared Link" Migration
You must convert synology Shared Link Database file (/usr/syno/etc/filebrowser/fbsharing.db) to CSV file with "DB Browser for SQLite" program( SET Mode = TAB ) Before run this program!!
And also, you need to modify "HTML_SRC/SAMPLE.html" file for make new download link.

	1) Download "DB Browser for SQLite" : 
		https://sqlitebrowser.org/dl/ 	<- Click and download "DB Browser for SQLite - .zip (no installer) for 64-bit Windows"
	2) Open : 
		extract the .zip file, and open "DB Browser for SQLite.exe"
	3) export to CSV : 
		1. Click "Open Database" in the top menu.
		2. Choose a database file - pull your database file in synology.
			Connect Synology(or Xpenology) NAS with SSH(use putty or something), with "root" ID, and copy "/usr/syno/etc/filebrowser/fbsharing.db" file.
				I copyed that file to my synology shared folder and downloaded via DSM's file station.
		3. Click "Browse Data"tab, and Check the list is correct.
		4. File > Export > Table(s) as CSV file...
		5. 	Table(s) = sharingLinks								(default)
			Column names in first line = V (checked)			(default)
			Field Separator = Tab 							<== important !!!
			Quote charactor = "									(default)
			New line characters = windows : CR + LF(\r \n)		(default)
	

This program will make new html files autometically, with no extention.
So, you need to set ".htaccss" like this : 
	RewriteEngine On
	RewriteCond %{REQUEST_FILENAME} !-f
	RewriteRule ^([^/]+)/$ $1.php
	RewriteRule ^([^/]+)/([^/]+)/$ /$1/$2.php
	RewriteCond %{REQUEST_FILENAME} !-f
	RewriteCond %{REQUEST_FILENAME} !-d
	RewriteCond %{REQUEST_URI} !(\.[a-zA-Z0-9]{1,5}|/)$
	RewriteRule (.*)$ /$1/ [R=301,L]

'''
try:
	import os
	import shutil
	import time
	import datetime
	from tkinter import filedialog
except:
	print("기본 도구 로딩에 실패했습니다. 프로그램은 작동하지 않습니다. 프로그램을 종료합니다. \n\n")
	exit()
	

ignore_just_make_html_file = 0
skip_and_do_not_make_html_file = 1

# You need to SET this Val...
debug=0


PATH_DEL = ""

'''
		<< GUYS, this is important. It is the SECURITY SEETING. If you have secret files, README!!! >>
	
	You need to set here to {Ignore / Do not ingore} the ACCESS SECURITY settings when you(or someone) creating a shared link.
	Access security includes a file access password(Not a DSM Password), access period, and number of accesses.
	Be careful. This could leak your secret files.
	IF YOU HAVE SECRET FILES, CHECK THE CSV FILE ONE MORE TIME!!!!
'''

# if Password Protected files, than { [ignore_just_make_html_file] or [skip_and_do_not_make_html_file] }
if_file_has_password = skip_and_do_not_make_html_file

# if file have exp-date or Avail-date, than { [ignore_just_make_html_file] or [skip_and_do_not_make_html_file] }
if_file_has_ExpDate = skip_and_do_not_make_html_file
if_file_has_AvailDate = skip_and_do_not_make_html_file

# if orig link is folder, than { [ignore_just_make_html_file] or [skip_and_do_not_make_html_file] }
#						* if you're enabled "directory listing"on your new server, you can use "ignore_just_make_html_file"
#						* or not, just select "skip_and_do_not_make_html_file".
if_file_has_isFolder = ignore_just_make_html_file

# if file have "ValidTime"Settings, than { [ignore_just_make_html_file] or [skip_and_do_not_make_html_file] }
if_file_has_valid_times = skip_and_do_not_make_html_file


changed_RootFilePath_01_src = "/SDA/"
changed_RootFilePath_01_dst = "NEW_SDA/" 
changed_RootFilePath_02_src = "/IM-DRIVE/" 
changed_RootFilePath_02_dst = "" 
changed_RootFilePath_03_src = "I will not use this..." 
changed_RootFilePath_03_dst = "I will not use this..." 
changed_RootFilePath_04_src = "I will not use this..." 
changed_RootFilePath_04_dst = "I will not use this..." 
changed_RootFilePath_05_src = "I will not use this..." 
changed_RootFilePath_05_dst = "I will not use this..." 
changed_RootFilePath_06_src = "I will not use this..." 
changed_RootFilePath_06_dst = "I will not use this..." 
changed_RootFilePath_07_src = "I will not use this..." 
changed_RootFilePath_07_dst = "I will not use this..." 
changed_RootFilePath_08_src = "I will not use this..." 
changed_RootFilePath_08_dst = "I will not use this..." 
changed_RootFilePath_09_src = "I will not use this..." 
changed_RootFilePath_09_dst = "I will not use this..." 
changed_RootFilePath_10_src = "I will not use this..." 
changed_RootFilePath_10_dst = "I will not use this..." 

changed_FileNameOrPath_01_src = "I will not use this..." 
changed_FileNameOrPath_01_dst = "I will not use this..." 
changed_FileNameOrPath_02_src = "I will not use this..." 
changed_FileNameOrPath_02_dst = "I will not use this..." 
changed_FileNameOrPath_03_src = "I will not use this..." 
changed_FileNameOrPath_03_dst = "I will not use this..." 
changed_FileNameOrPath_04_src = "I will not use this..." 
changed_FileNameOrPath_04_dst = "I will not use this..." 
changed_FileNameOrPath_05_src = "I will not use this..." 
changed_FileNameOrPath_05_dst = "I will not use this..." 
changed_FileNameOrPath_06_src = "I will not use this..." 
changed_FileNameOrPath_06_dst = "I will not use this..." 
changed_FileNameOrPath_07_src = "I will not use this..." 
changed_FileNameOrPath_07_dst = "I will not use this..." 
changed_FileNameOrPath_08_src = "I will not use this..." 
changed_FileNameOrPath_08_dst = "I will not use this..." 
changed_FileNameOrPath_09_src = "I will not use this..." 
changed_FileNameOrPath_09_dst = "I will not use this..." 
changed_FileNameOrPath_10_src = "I will not use this..." 
changed_FileNameOrPath_10_dst = "I will not use this..." 



Except_filepath_01_src = "/HDD3" 
Except_filepath_02_src = "/HDD1" 
Except_filepath_03_src = "I will not use this..." 
Except_filepath_04_src = "I will not use this..." 
Except_filepath_05_src = "I will not use this..." 
Except_filepath_06_src = "I will not use this..." 
Except_filepath_07_src = "I will not use this..." 
Except_filepath_08_src = "I will not use this..." 
Except_filepath_09_src = "I will not use this..." 
Except_filepath_10_src = "I will not use this..." 




try:
	csv_file_path=filedialog.askopenfilename( initialdir="/" , title = "Select CSV file",filetypes=( ("csv files","*.csv"),("all files", "*.*") ) )
	csv_file_opener = open(csv_file_path,mode='r',encoding='UTF-8')
	csv_MatchList_Raw = csv_file_opener.readlines()
except Exception as lc_err_msg:
	print("Faild to READ CSV file. Errorcode : " , lc_err_msg)

try:
	out_dir = filedialog.askdirectory(initialdir="/",title='select Output directory')
	out_dir_filelist=os.listdir(out_dir)
except Exception as lc_err_msg:
	print("Faild to get OUT-DIR or SAMPLE-HTML. Errorcode : " , lc_err_msg)

try:
	HTML_SRC_DIR = filedialog.askdirectory(initialdir="/",title='select HTML_SRC directory')
	
	html_file_orig_opener = open(HTML_SRC_DIR + "/SAMPLE.html",mode='r',encoding='UTF-8')
	html_file_orig_lines = html_file_orig_opener.readlines()
	html_file_orig = ""
	for linenow in html_file_orig_lines:
		html_file_orig = html_file_orig + linenow
	
	
except Exception as lc_err_msg:
	print("Faild to get HTML-SRC-DIR. Errorcode : " , lc_err_msg)



password_skip_qty    = 0
ExpDate_skip_qty     = 0
AvailDate_skip_qty   = 0
isFolder_skip_qty    = 0
valid_times_skip_qty = 0


for line in csv_MatchList_Raw:
	line = line.replace("\n","")
	linesplit = line.split("\t")
	
	html_file_mdfy=html_file_orig
	
	if( len(linesplit) != 12 ) : 
		print("Expection : line not expected. ")
		continue
	
	
	
	linkID         = linesplit[ 0] # Shared Link id ( example : http://dsm.example.com/fbsharing/linkID )
	uid            = linesplit[ 1] # We'll not use this...
	filename       = linesplit[ 2] # file name ( example : filename = myfile.zip )
	filepath       = linesplit[ 3] # file path ( example : filepath = /SharedFolderName/myfile.zip )
	password       = linesplit[ 4] # Password ( "" means no password)
	ExpDate        = linesplit[ 5] # Exp-date ( 0 means no exp-date)
	AvailDate      = linesplit[ 6] # Avail-date ( 0 means no Avail-date)
	tmp_username   = linesplit[ 7] # We'll not use this...
	tmp_linkStatus = linesplit[ 8] # We'll not use this...
	isFolder       = linesplit[ 9] # is this folder? ("true" means This is folder right, "flase" means this is just a file.)
	sharing_list   = linesplit[10] # We'll not use this...
	valid_times    = linesplit[11] # Valid-time ( -1 means Infinity)
	
	# Security : skip? not to skip?
	if if_file_has_password:
		if password:
			password_skip_qty = password_skip_qty +1
			continue
	
	if if_file_has_ExpDate:
		if ExpDate!="0":
			ExpDate_skip_qty = ExpDate_skip_qty +1
			continue
	
	if if_file_has_AvailDate:
		if AvailDate!="0":
			AvailDate_skip_qty = AvailDate_skip_qty +1
			continue
	
	if if_file_has_isFolder:
		if isFolder=="true":
			isFolder_skip_qty = isFolder_skip_qty +1
			continue
	
	if if_file_has_valid_times:
		if valid_times!="-1":
			valid_times_skip_qty = valid_times_skip_qty +1
			continue
	
	if ( len(filename) > 23 ) :
		filename_ln1 = filename[:len(filename)//2]
		filename_ln2 = filename[len(filename)//2:]
	else:
		filename_ln1 = filename
		filename_ln2 = " "
	
	
	
	if ( filepath[:len(changed_RootFilePath_01_src)]==changed_RootFilePath_01_src ):
		filepath = changed_RootFilePath_01_dst + filepath[len(changed_RootFilePath_01_src):]
	if ( filepath[:len(changed_RootFilePath_02_src)]==changed_RootFilePath_02_src ):
		filepath = changed_RootFilePath_02_dst + filepath[len(changed_RootFilePath_02_src):]
	if ( filepath[:len(changed_RootFilePath_03_src)]==changed_RootFilePath_03_src ):
		filepath = changed_RootFilePath_03_dst + filepath[len(changed_RootFilePath_03_src):]
	if ( filepath[:len(changed_RootFilePath_04_src)]==changed_RootFilePath_04_src ):
		filepath = changed_RootFilePath_04_dst + filepath[len(changed_RootFilePath_04_src):]
	if ( filepath[:len(changed_RootFilePath_05_src)]==changed_RootFilePath_05_src ):
		filepath = changed_RootFilePath_05_dst + filepath[len(changed_RootFilePath_05_src):]
	if ( filepath[:len(changed_RootFilePath_06_src)]==changed_RootFilePath_06_src ):
		filepath = changed_RootFilePath_06_dst + filepath[len(changed_RootFilePath_06_src):]
	if ( filepath[:len(changed_RootFilePath_07_src)]==changed_RootFilePath_07_src ):
		filepath = changed_RootFilePath_07_dst + filepath[len(changed_RootFilePath_07_src):]
	if ( filepath[:len(changed_RootFilePath_08_src)]==changed_RootFilePath_08_src ):
		filepath = changed_RootFilePath_08_dst + filepath[len(changed_RootFilePath_08_src):]
	if ( filepath[:len(changed_RootFilePath_09_src)]==changed_RootFilePath_09_src ):
		filepath = changed_RootFilePath_09_dst + filepath[len(changed_RootFilePath_09_src):]
	if ( filepath[:len(changed_RootFilePath_10_src)]==changed_RootFilePath_10_src ):
		filepath = changed_RootFilePath_10_dst + filepath[len(changed_RootFilePath_10_src):]
	
	if ( filepath[:len(Except_filepath_01_src)]==Except_filepath_01_src ):
		continue
	if ( filepath[:len(Except_filepath_02_src)]==Except_filepath_02_src ):
		continue
	if ( filepath[:len(Except_filepath_03_src)]==Except_filepath_03_src ):
		continue
	if ( filepath[:len(Except_filepath_04_src)]==Except_filepath_04_src ):
		continue
	if ( filepath[:len(Except_filepath_05_src)]==Except_filepath_05_src ):
		continue
	if ( filepath[:len(Except_filepath_06_src)]==Except_filepath_06_src ):
		continue
	if ( filepath[:len(Except_filepath_07_src)]==Except_filepath_07_src ):
		continue
	if ( filepath[:len(Except_filepath_08_src)]==Except_filepath_08_src ):
		continue
	if ( filepath[:len(Except_filepath_09_src)]==Except_filepath_09_src ):
		continue
	if ( filepath[:len(Except_filepath_10_src)]==Except_filepath_10_src ):
		continue
	
	filepath = filepath.replace(changed_FileNameOrPath_01_src,changed_FileNameOrPath_01_dst)
	filepath = filepath.replace(changed_FileNameOrPath_02_src,changed_FileNameOrPath_02_dst)
	filepath = filepath.replace(changed_FileNameOrPath_03_src,changed_FileNameOrPath_03_dst)
	filepath = filepath.replace(changed_FileNameOrPath_04_src,changed_FileNameOrPath_04_dst)
	filepath = filepath.replace(changed_FileNameOrPath_05_src,changed_FileNameOrPath_05_dst)
	filepath = filepath.replace(changed_FileNameOrPath_06_src,changed_FileNameOrPath_06_dst)
	filepath = filepath.replace(changed_FileNameOrPath_07_src,changed_FileNameOrPath_07_dst)
	filepath = filepath.replace(changed_FileNameOrPath_08_src,changed_FileNameOrPath_08_dst)
	filepath = filepath.replace(changed_FileNameOrPath_09_src,changed_FileNameOrPath_09_dst)
	filepath = filepath.replace(changed_FileNameOrPath_10_src,changed_FileNameOrPath_10_dst)
	
	html_file_mdfy = html_file_mdfy.replace("{OLD_LinkID}",linkID)
	html_file_mdfy = html_file_mdfy.replace("{NEW_FilePATH}",filepath)
	html_file_mdfy = html_file_mdfy.replace( "{filename_line01}" , filename_ln1 )
	html_file_mdfy = html_file_mdfy.replace( "{filename_line02}" , filename_ln2 )
	
	out_filename = linkID
	
	
	htmlout = open(out_dir + "/" + out_filename ,mode='w',encoding='utf-8')
	htmlout.write(html_file_mdfy)
	htmlout.close()


print("end")