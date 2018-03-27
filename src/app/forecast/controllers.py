# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  redirect, url_for, session
from app.forecast.forms import ForecastForm, NumInputsForm
from model import Model
import json

forecast = Blueprint('forecast', __name__, url_prefix='/forecast')

WASTE_TYPES = [
    "pig_manure_waste",
    "cassava_waste",
    "fish_waste_water",
    "kitchen_food_waste",
    "municipal_fecal_residue_waste",
    "tea_waste",
    "chicken_litter_waste",
    "bagasse_feed_waste",
    "alcohol_waste",
    "chinese_medicine_waste",
    "energy_grass_waste",
    "banana_fruit_shafts_waste",
    "lemon_waste",
    "percolate_waste",
    "other_waste" ]

model = Model()

def make_data(form):
    xs, ys = [], []
    print(form.entries.data)
    for entry in form.entries.data:
        xs.append(str(entry["month"]) + "/" + str(entry["year"]))
        ys.append([float(str(entry[waste_type])) for waste_type in WASTE_TYPES])
    return xs, ys

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

    print([field for field in form])

    if form.validate_on_submit():
        xs, ys = make_data(form)
        session["data"] = json.dumps({ "xs": xs, "ys": list(model.predict(model.knn_model, ys)) })
        return redirect(url_for("forecast.result"))
    else:
        for i in range(num_inputs):
            form.entries.append_entry()

    return render_template("forecast/input.html", form=form)

@forecast.route('/result/', methods=['GET'])
def result():
    data = session["data"]
    return render_template("forecast/result.html", data=data)
