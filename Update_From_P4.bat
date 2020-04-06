@echo off
rem Update the local perforce directory from the depot
rem *Original from TexMech - C28 

echo ----------------------------------------------------------------------
echo Step 1: Getting latest changes from Perforce
echo ----------------------------------------------------------------------\

set sertver=129.119.63.244:1666
set user=daily_builds
set password=gKv52w!*
set workspace=NightlyBuild_HaberDashers

p4 -p %sertver% -u %user% -P %password% -c %workspace% sync -f
echo:
echo: