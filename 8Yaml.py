import yaml
import json 

# https://pyyaml.org/wiki/PyYAMLDocumentation
def create_json():
    with open(".\SecurityPolicies.yaml","r") as yaml_doc:
        yaml_to_dict=yaml.load(yaml_doc,Loader=yaml.FullLoader)
        # write this dictionary as json object 
        with open("document.json","w") as json_doc:
            json.dump(yaml_to_dict,json_doc)
    print("yaml file is converted to json")

create_json()

