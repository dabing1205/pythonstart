@echo off
set curl=C:\Program Files\curl\curl-7.17.1\curl.exe
set ids=%1
%curl% -D cookie.txt -o login.html -d "input_name=admin1782&input_pwd=520123&input_rem=true" -A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"  -e "http://www.1782.cc/admini5/index.asp?action=login"  "http://www.1782.cc/admini5/index.asp?action=check"

%curl% -b cookie.txt -o caiji.html -d "ac=select&rid=5&ids=%ids%"  -A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"  -e "http://www.1782.cc/admini5/admin_20131001.asp?ac=list&rid=5"  "http://www.1782.cc/admini5/admin_20131001.asp"

%curl% -b cookie.txt -o makehtml.html -d "m_id=%ids%" -A "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0)"  -e "http://www.1782.cc/admini5/admin_20131001.asp?ac=list&rid=5"  "http://www.1782.cc/admini5/admin_makehtml.asp?action=selected"
