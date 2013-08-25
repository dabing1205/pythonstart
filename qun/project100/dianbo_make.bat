@echo off
set ids=%1
set weburl=%2
set username=%3
set password=%4
set curl=%5
::echo %ids%, %weburl%, %username%, %password%, %curl%
%curl% -s -D cookie.txt -o login.html -d "input_name=%username%&input_pwd=%password%&input_rem=true" -A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"  -e "%weburl%/admini5/index.asp?action=login"  "%weburl%/admini5/index.asp?action=check"

%curl% -s -b cookie.txt -o caiji.html -d "ac=select&rid=5&ids=%ids%"  -A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"  -e "%weburl%/admini5/admin_20131001.asp?ac=list&rid=5"  "%weburl%/admini5/admin_20131001.asp"

%curl% -s -b cookie.txt -o makehtml.html -d "m_id=%ids%" -A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"  -e "%weburl%/admini5/admin_20131001.asp?ac=list&rid=5"  "%weburl%/admini5/admin_makehtml.asp?action=selected"
