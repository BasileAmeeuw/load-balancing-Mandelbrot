from flask import request, jsonify, Flask
import os
import subprocess
import json


app = Flask(__name__)


@app.route('/mandelbrot')
def mandelbrot():
    c={"real":1,"imag":1}
    z={"real":0,"imag":0}
    real = float(request.args.get('real', default=1, type=float))
    imag = float(request.args.get('imag', default=1, type=float))
    max_steps = request.args.get('max_steps', default=10000, type=int)

    c["real"]=real
    c["imag"]=imag
    max = max_steps
    count = 0
    lengthsq=0
    while (count < max):
        if (lengthsq <= 4.0):
            temp = z["real"] * z["real"] - z["imag"] * z["imag"] + c["real"];
            z["imag"] = 2 * z["real"] * z["imag"] + c["imag"];
            z["real"] = temp;
            lengthsq = z["real"] * z["real"] + z["imag"] * z["imag"];
            print(lengthsq);
            count+=1
        else:
            break
    # stream = subprocess.run("getIter.exe " + real + " " + imag)
    # output = stream.stdout()
    # output = stream.read()

    # response = {
    #     "output": output,
    #     "isMandelbrot": output[0],
    #     "iterations": output[1]
    # }
    # if output[0] == 0:
    #     response = {
    #         "isMandelbrot": True,
    #         "iterations": output[1]
    #     }
    # if output[0] == 1:
    #     response = {
    #         "isMandelbrot": False,
    #         "iterations": output[1]
    #     }

    # return jsonify(response)
    return str(count)+","+" serveur 6"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
