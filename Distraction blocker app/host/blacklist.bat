@echo off
set hostspath=%windir%\System32\drivers\etc\hosts\
echo 127.0.0.1 www.facebook.com >> %hostspath%
echo 127.0.0.1 www.twitter.com >> %hostspath%
echo 127.0.0.1 www.reddit.com >> %hostspath%
exit