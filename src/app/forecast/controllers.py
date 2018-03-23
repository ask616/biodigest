# Import flask dependencies
from flask import Blueprint, request, render_template, \
                  redirect, url_for, session
from app.forecast.forms import ForecastForm, NumInputsForm
from model import Model
import json

forecast = Blueprint('forecast', __name__, url_prefix='/forecast')

waste_types = [
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
    data = []
    print(form.entries.data)
    for entry in form.entries.data:
        data.append([float(str(entry[waste_type])) for waste_type in waste_types])
    return data

def get_xs(form):
    xs = []
    for entry in form.entries.data:
        xs.append(str(entry["month"]) + "/" + str(entry["year"]))
    return xs

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
        session["data"] = json.dumps({ "ys": list(model.predict(model.knn_model, make_data(form))), "xs": get_xs(form) })
        return redirect(url_for("forecast.result"))
    else:
        for i in range(num_inputs):
            form.entries.append_entry()

    return render_template("forecast/input.html", form=form)

@forecast.route('/result/', methods=['GET'])
def result():
    data = session["data"]
    return render_template("forecast/result.html", data=data)
