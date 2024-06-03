# pip install cx-freeze
import cx_Freeze
executaveis = [
               cx_Freeze.Executable(script="main.py")]
cx_Freeze.setup(
    name = "Iron Man",
    options ={
        "build_exe":{
            "packages":["pygame"],
            "include_files":["assets"]
        }
    }, executables = executaveis
)