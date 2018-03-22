# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  redirect, url_for, session
from app.forecast.forms import ForecastForm, NumInputsForm
import json

forecast = Blueprint('forecast', __name__, url_prefix='/forecast')

def make_data(form):
    data = []
    for entry in form.entries.data:
        data.append({
            "other_waste": float(str(entry["other_waste"])),
            "kitchen_waste": float(str(entry["kitchen_waste"])),
            "bread_paste_waste": float(str(entry["bread_paste_waste"])),
            "diesel_waste_water": float(str(entry["diesel_waste_water"])),
            "fruit_veg_waste": float(str(entry["fruit_veg_waste"])),
            "oil_waste": float(str(entry["oil_waste"]))
        })
    return data

@forecast.route('/', methods=['GET', 'POST'])
def num_inputs():
    form = NumInputsForm(request.form)
    if form.validate_on_submit():
        return redirect(url_for("forecast.input", num_inputs=form.num_inputs.data))
    return render_template("forecast/index.html", form=form)

@forecast.route('/input/', methods=['GET', 'POST'])
def input():
    if "num_inputs" in request.args:
        num_inputs = int(request.args["num_inputs"])
    else:
        num_inputs = 1

    form = ForecastForm(request.form)

    if form.validate_on_submit():
        session["data"] = json.dumps(make_data(form))
        return redirect(url_for("forecast.result"))
    else:
        for i in range(num_inputs):
            form.entries.append_entry()

    return render_template("forecast/input.html", form=form)

@forecast.route('/result/', methods=['GET'])
def result():
    data = session["data"]
    return render_template("forecast/result.html", data=data)
