from flask import Flask, render_template

app=Flask("__name__")

@app.route("/")
def object():
    names = ["ayse", "veli", "zeki"]
    return render_template("body.html", object=names)










if __name__ == "__main__":
    app.run(debug=True)