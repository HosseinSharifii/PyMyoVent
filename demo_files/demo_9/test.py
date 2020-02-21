import json


#input_file_name = "demo_9_model.json"
#input_file_name = "fenics_input.json"
input_file_name= "example_1.json"
with open(input_file_name,'r') as f:
    json_input = json.load(f)

#print(json_input)
#baro_scheme = json_input["baroreflex"]["baro_scheme"]
gravity = json_input["base_parameters"]["gravity"][0]
#myosim_parameters = json_input["myosim_parameters"]["max_rate"][0]
print(gravity)
#print('output',baro_scheme)
#print(myosim_parameters)
