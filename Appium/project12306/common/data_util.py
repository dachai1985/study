import yaml

def readyaml(path):
    try:
        with open(path, "r+", encoding="utf-8") as file:
            data=yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"Error: The file at path {path} was not found.")
        raise
    except yaml.YAMLError as exc:
            print(f"Error in parsing YAML file: {exc}")
            raise

# if __name__=='__main__':
#     rootPath = os.path.abspath(os.path.dirname(os.path.dirname(__file__))) #当前文件的上一级的上一级目录
#     print(rootPath)
#     path = os.path.join(rootPath, "config\config.yaml")
#     print(readYaml(path))