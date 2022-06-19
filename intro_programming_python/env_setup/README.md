# Windows
1. Install Python: https://www.python.org/downloads/
   1. Make sure `Add Python 3.10 to PATH` is checked ![python_install](images/python_install.png)
1. Install PyCharm
   1. Download here https://www.jetbrains.com/pycharm/download/#section=windows
   1. Select the Community edition ![pycharm_install](images/pycharm_install.png)
1. Create a new PyCharm project
   1. It should auto-detect Python ![new_project](images/new_project.png)
   1. Run the program by clicking on the green arrow on the left-hand side ![run_main](images/run_main.png)
1. Install PowerShell 7: https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.2
1. Make PowerShell run with admin privileges
   1. Search for "Powershell 7" in the start menu ![powershell_start](images/powershell_start.png)
   1. Right-click and select "Open file location" ![powershell_start_file_location](images/powershell_start_file_location.png)
   1. Right-click and select "Properties" ![powershell_properties](images/powershell_properties.png)
   1. Click on "Advanced..." and check "Run as administrator" ![powershell_admin](images/powershell_admin.png)
1. Install packages in PowerShell 7
   1. Install Chocolatey package manager https://chocolatey.org/install
   1. Install git
      ```
      choco install git -y
      ```
   1. Install posh-git
      ```
      choco install poshgit -y
      ```
   1. Auto-import posh-git https://github.com/dahlbyk/posh-git#using-posh-git

# macOS
TODO