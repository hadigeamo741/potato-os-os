@echo off
:: إعدادات الشاشة واللون (0E أصفر ذهبي)
title Batata OS Terminal v4.0 - APScell Console
color 0E
cls

:: --- شعار الـ ASCII (APScell) ---
echo.
echo    =======================================================
echo      ____  ____  ____  ____  ____  ____    ____  ____ 
echo     (  _ \(  _ \(  _ \(  _ \(  _ \(  _ \  / ___)(  __)
echo      ) __/ ) _ ( ) __/ ) _ ( ) __/ ) _ (  \___ \ ) _) 
echo     (__)  (___/(__)  (___/(__)  (___/  (____/(____)
echo    =======================================================
echo      KERNEL: STARCH v4.0 // LANGUAGE: APScell ENABLED
echo    =======================================================
echo.
echo [System]: Ready. Type 'help' to see Batata commands.
echo.

:cmd_loop
:: علامة الإدخال مثل لينكس
set /p "cmd=Batata@User:~$ "

:: --- منطق الأوامر ---

:: 1. أوامر بطاطس الخاصة
if "%cmd%"=="help" (
    echo.
    echo  [Linux Style]: ls, clear, pwd, whoami
    echo  [Win Style]:   ip, sysinfo
    echo  [Batata Spec]: hello, version, about, exit
    echo.
    goto cmd_loop
)
if "%cmd%"=="hello" (echo Ahlan! Welcome to the potato world. && goto cmd_loop)
if "%cmd%"=="version" (echo Batata OS Version 4.0 (Stable Build) && goto cmd_loop)
if "%cmd%"=="about" (echo Developed by LENOVO Master - Starch Tech 2024. && goto cmd_loop)

:: 2. أوامر لينكس (Linux Commands)
if "%cmd%"=="ls" (dir /b && goto cmd_loop)
if "%cmd%"=="clear" (cls && goto cmd_loop)
if "%cmd%"=="pwd" (echo %cd% && goto cmd_loop)
if "%cmd%"=="whoami" (echo Current User: Potato_Master && goto cmd_loop)

:: 3. أوامر ويندوز (Windows Commands)
if "%cmd%"=="ip" (ipconfig | findstr "IPv4" && goto cmd_loop)
if "%cmd%"=="sysinfo" (systeminfo | findstr /B /C:"OS Name" /C:"OS Version" && goto cmd_loop)

:: 4. الخروج
if "%cmd%"=="exit" (exit)

:: إذا كان الأمر غير معروف
echo '%cmd%' is not a recognized Batata command. Type 'help'.
goto cmd_loop