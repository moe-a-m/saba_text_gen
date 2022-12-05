
@Echo Off

Set "VIRTUAL_ENV=textgen_venv"

If Not Exist "%VIRTUAL_ENV%\Scripts\activate.bat" (
    pip.exe install virtualenv
    python.exe -m venv %VIRTUAL_ENV%
)

call %VIRTUAL_ENV%\Scripts\activate 
call pip install -r .\requirements.txt
python start.py