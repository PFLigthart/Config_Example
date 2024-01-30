import configparser

config_file_path = "config.ini"
config_obj = configparser.ConfigParser()
config_obj.read(config_file_path)
Params = config_obj["Parameters"]


Param_1 = int(Params["Param_1"])
Param_2 = float(Params["Param_2"])
Var_3 = str(Params["Param_3"])

print(f"Param_1: {Param_1} is type {type(Param_1)}")
print(f"Param_2: {Param_2} is type {type(Param_2)}")
print(f"Param_3: {Var_3} is type {type(Var_3)}")

