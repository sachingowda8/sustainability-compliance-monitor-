@echo off
set JAVAC="C:\Users\sachi\.antigravity\extensions\redhat.java-1.54.0-win32-x64\jre\21.0.10-win32-x86_64\bin\javac.exe"
set JAVA="C:\Users\sachi\.antigravity\extensions\redhat.java-1.54.0-win32-x64\jre\21.0.10-win32-x86_64\bin\java.exe"

echo 🛠️ Compiling AiServiceClientStandard.java...
%JAVAC% -d . src/main/java/com/sustainability/client/AiServiceClientStandard.java

if %ERRORLEVEL% EQU 0 (
    echo ✅ Compilation Successful!
    echo 🚀 Running Client (Ensure Flask app is running)...
    %JAVA% com.sustainability.client.AiServiceClientStandard
) else (
    echo ❌ Compilation Failed.
)
pause
