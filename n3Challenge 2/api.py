import os
import glob
from flask import Flask, request, jsonify, send_from_directory
from flask_api import status

UPLOAD_DIRECTORY = os.getcwd() #current working directory

api = Flask(__name__)

@api.route("/files/<path:path>")
def get_file(path):
    """Download a file."""
    with open("new"+path+'.csv', 'w') as outfile:

        for infile in sorted(glob.glob(os.path.join(UPLOAD_DIRECTORY,path+"__"+"*"))):
            with open(infile) as f:
                outfile.write(f.read())

    return send_from_directory(UPLOAD_DIRECTORY, "new"+path+'.csv' ,as_attachment=True)


@api.route("/multiple-files-upload", methods=["POST"])
def post_file():
    # import pdb;pdb.set_trace()
    """Upload a file."""

    if 'files[]' not in request.files:
        return jsonify(status=status.HTTP_400_BAD_REQUEST,Message="No file part in the request")
    all_files =request.files.getlist('files[]') #getting multiple files
    try:
        for single_file in all_files:
            count=0
            if not "." in single_file.filename: #checking extenion 
                return jsonify(status=status.HTTP_400_BAD_REQUEST,Message="Please use some extensions")
            with open(os.path.join(UPLOAD_DIRECTORY, single_file.filename),'rb') as fp:
                chunk_size = 512
                while True:
                    count +=1
                    chunk = fp.read(chunk_size) # reading data into chunks
                    if len(chunk) == 0:
                        break
                    # creating new file and writing data into it.
                    with open(os.path.join(UPLOAD_DIRECTORY, single_file.filename.split(".")[0] + "__"+str(count))+".csv", "wb") as f:
                        f.write(chunk) 
        headers = {'content-type': 'application/json'}
        return jsonify(status=status.HTTP_201_CREATED,Message="successfully created API",headers=headers)
    except Exception as e:
        return jsonify(status=status.HTTP_400_BAD_REQUEST,Message=e)




if __name__ == "__main__":
    api.run(debug=True, port=5000)