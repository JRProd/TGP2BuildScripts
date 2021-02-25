# Unreal build/deploy scripts (TGP2)

(What does this do?)

## Setup

You need to have the [Helix Core API for Python](https://www.perforce.com/downloads/helix-core-api-python) installed
on top of a compatible version of a Python installation. For example, the current p4python MSI installer is
`p4python-3.8-x64.msi`, so it requires specifically Python 3.8.x. (A newer version of Python, such as 3.9.x, will
_not_ work!) Install the [correct version of Python](https://www.python.org/downloads/) for current p4python, then
run the p4python MSI. It should detect your python install (e.g. "Use Python 3.8 from registry"), and install on top.

Additionally, you need
- [Inno Setup](https://jrsoftware.org/isdl.php) to actually pack the installer.
- The latest [Steamworks SDK](https://partner.steamgames.com/downloads/steamworks_sdk.zip)
- The Visual Studio components for both "Desktop Development with C++" and ".NET Desktop Development"

Clone the buildscripts into their own folder, _independent_ of your project folder. For example, I have mine at just
`D:\TGP2BuildScripts`. The buildscripts will run from here and clone/build your project.

You will want to set up a P4 workspace just for doing builds, so that builds don't interfere with development.
Additionally, every file that's not required for builds that's mapped into the workspace is another file that has
to be synced over the network, slowing down the process.

## Configuration

In your build scripts folder, create a `config.ini`. This tells the buildscripts specific information about your build.
The basic format is as follows:

```ini
; You can reference other variables as `${Section:setting}`
; Section is optional if referring to the same section
; If you need a literal `$`, escape it as `$$`
; Directory paths should end with a trailing separator

[Game]
; The name of your game
game_name = Game Name
; The project directory to put the game for building (NOT your development folder!)
project_dir = ${Local:base_dir}Project_Files\PigmentPenguins\
; The path to your project's project file
uproject_file = ${project_dir}PigmentPenguins.uproject
; The directory to put build artifacts
builds_dir = ${Local:base_dir}Build_Dir\
; The directory where the latest build ends up
latest_build_dir = ${builds_dir}WindowsNoEditor
; The directory that contains your map files
map_dir = ${project_dir}Content\Levels\Stages\
; A space-separated list of map prefixes to build lighting for
maps = PLVL_


[Perforce]
; Your build account's P4 username
user_name = P4 Name
; Your build account's P4 password
user_password = P4 Password
; Your build account's P4 client/workspace name
client = Workspace Name


[Local]
; Unused drive letter to mount Deleted Nightly
drive_letter = K:
; Base directory for builds
base_dir = D:\AutomatedBuilds\C3X\TGP2\
; Directory to put executable
exe_dir = ${base_dir}Executable\
; Filepath to put executable build script
exe_build_script = ${exe_dir}Executable_Build_Script.iss
; Filepath to Inno Setup command line interface
inno_setup_exe = C:\Program Files (x86)\Inno Setup 6\ISCC.exe
; Directory of the Unreal Engine
ue4_engine_dir = C:\Program Files\Epic Games\UE_4.XX\Engine\
; Directory of UE4's build scripts
ue4_batchfiles_dir = ${ue4_engine_dir}Build\BatchFiles\
; Directory fo UE4's binaries
ue4_binaries_dir = ${ue4_engine_dir}Binaries\Win64\


[SMU]
; Your build account's network username
user_name = Network Name
; Your build account's network password
user_password = Network Password
; The network path of the Deleted Nightly network folder
deleted_nightly_dir = \\smu.edu\files\Guildhall$$\Deleted Nightly\
; The path (on the mapped drive letter) to copy the executables
remote_archive_dir = ${Local:drive_letter}\C3X\TGP2\GameName\Executables\


[Steam]
; Your build account's Steam name
user_name = Steam Name
; Your build account's Steam password
user_password = Steam Password
; The directory of the Steamworks ContentBuilder tool
steam_dir = ${Local:ue4_engine_dir}Source\ThirdParty\Steamworks\Steamv1XX\sdk\tools\ContentBuilder\
; The relative path to the SteamCMD command line tool, from $steam_dir
steam_cmd = .\builder\steamcmd.exe
; The relative path to the Steam build metadata, from $steam_dir
app_build = .\scripts\app_build_1000.vdf
```

## Use

(How do I invoke the scripts?)  
(What arguments are there?)  
(Where are the logs?)
