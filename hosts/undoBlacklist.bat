@ECHO OFF
set hostspath=%windir%\System32\drivers\etc\hosts
del findstr /c: "127.0.0.1 www.facebook.com" >> %hostspath%
if not errorlevel 1 findstr /c: "127.0.0.1 www.facebook.com" goto end
end
echo specified string not found
