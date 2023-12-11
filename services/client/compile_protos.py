import proto_files
import os
import subprocess
import sys

sys.path.append(".")


COMMAND = "python -m grpc_tools.protoc -I ../../protobufs --python_out=./proto/ --proto_path=. --grpc_python_out=./proto/ ../../protobufs/{file_name}"


REMOVE_PROTOS_COMMAND = "rm ./proto/*pb2*"

try:
    subprocess.run([REMOVE_PROTOS_COMMAND], check=True)
except (subprocess.CalledProcessError, FileNotFoundError):
    pass

for proto_file in proto_files.PROTO_FILES:
    os.system(COMMAND.format(file_name=proto_file))
