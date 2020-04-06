@echo off

echo ----------------------------------------------------------------------
echo Step 1: Getting latest changes from Perforce
echo ----------------------------------------------------------------------\

set sertver=129.119.63.244:1666
set user=daily_builds
set password=gKv52w!*
set workspace=NightlyBuild_TexMech

p4 -p %sertver% -u %user% -P %password% -c %workspace% sync -f
echo:
echo: