@echo off

echo --------------------
echo Step 1.5: Build lighting
echo --------------------

set base_dir=C:\AutomatedBuilds\C28\TGP3\Tex_Mechs\
set project_dir=%base_dir%Project_Files\TexMechs\
set uproject_file="%project_dir%TexMechs.uproject"
set level_dir=%project_dir%Content\Levels\
set build_maps="/Game/Levels/UI_MainMenu+/Game/Levels/MechBay+/Game/Levels/PLVL_Canyon_Alpha"

rem this is tedious, there should be a better way to do this.
set files_check_out= %level_dir%UI_MainMenu.umap %level_dir%UI_MainMenu_BuiltData.uasset %level_dir%MechBay.umap %level_dir%MechBay_BuiltData.uasset %level_dir%PLVL_Canyon_Alpha.umap %level_dir%PLVL_Canyon_Alpha_BuiltData.uasset %level_dir%PLVL_Canyon_Alpha.umap %level_dir%PLVL_Canyon_Alpha_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_1.umap %level_dir%SLVL_Canyon_Alpha_1_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_1_Logic.umap %level_dir%SLVL_Canyon_Alpha_1_Logic_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_2.umap %level_dir%SLVL_Canyon_Alpha_2_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_2_LogicLD.umap %level_dir%SLVL_Canyon_Alpha_2_LogicLD_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_3.umap %level_dir%SLVL_Canyon_Alpha_3_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_3_Logic.umap %level_dir%SLVL_Canyon_Alpha_3_Logic_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_4.umap %level_dir%SLVL_Canyon_Alpha_4_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_4_Extra.umap %level_dir%SLVL_Canyon_Alpha_4_Extra_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_4_Logic.umap %level_dir%SLVL_Canyon_Alpha_4_Logic_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_5.umap %level_dir%SLVL_Canyon_Alpha_5_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_5_Extra.umap %level_dir%SLVL_Canyon_Alpha_5_Extra_BuiltData.uasset %level_dir%SLVL_Canyon_Alpha_5_Logic.umap %level_dir%SLVL_Canyon_Alpha_5_Logic_BuiltData.uasset 
rem p4 workspace
set sertver=129.119.63.244:1666
set user=daily_builds
set password=gKv52w!*
set workspace=NightlyBuild_TexMech


p4 -p %sertver% -u %user% -P %password% -c %workspace% edit -c default %files_check_out%
call "C:\Program Files\Epic Games\UE_4.22\Engine\Binaries\Win64\UE4Editor-Cmd.exe" %uproject_file% -verbose -p4 -submit -run=resavepackages -buildlighting -quality=Production -allowcommandletrendering -map=%build_maps%

set light_month=%date:~4,2%
set light_day=%date:~7,2%
set light_hour=%time:~0,2%
set light_minute=%time:~3,2%
if %light_hour% lss 10 set hour=0%light_hour:~1,2%


p4 -p %sertver% -u %user% -P %password% -c %workspace% submit -f submitunchanged -d TexMechs_Auto_lighting_%light_month%_%light_day%_%light_hour%_%light_minute%
echo:
echo:
