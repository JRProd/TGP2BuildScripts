@echo off

set base_dir=C:\AutomatedBuilds\C28\TGP3\Tex_Mechs\
set executable_dir=%base_dir%Executable\
set executable_build_script="%executable_dir%Executable_Build_Script.iss"
set initial_executable_file="%executable_dir%Tex-Mechs.exe"
set archive_dir=%base_dir%Archived_Builds\

set network_dir=\\smu.edu\files\Guildhall$\Deleted Nightly\C28_Capstone\Tex-Mechs\Executable

rem Yay, the build was a success!
rem Step 3 Time to make an installer using the created archive
rem I don't believe this step can fail, as I never had it fail, but you could check this return code too
echo ----------------------------------------------------------------------
echo Step 3: Building installer executable
echo ----------------------------------------------------------------------
call "C:\Program Files (x86)\Inno Setup 5\ISCC.exe" %executable_build_script%
echo:
echo: