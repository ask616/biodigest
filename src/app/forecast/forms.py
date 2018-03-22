from flask_wtf import FlaskForm
from wtforms.fields import IntegerField, DecimalField, FieldList, FormField
from wtforms.validators import Required, NumberRange

any_month = NumberRange(min=1, max=12, message="Invalid month")
any_year = NumberRange(min=1, message="Invalid year")
geq_zero = NumberRange(min=0.0, message="Invalid value")

def bio_input_field(name):
    return DecimalField(name, [geq_zero], default=0.0)

class NumInputsForm(FlaskForm):
    num_inputs = IntegerField("Number of inputs", [geq_zero, Required(message="Missing number of inputs")])

class DataForm(FlaskForm):
    month = IntegerField("Month", [any_month, Required(message="Missing month")])
    year = IntegerField("Year", [any_year, Required(message="Missing year")])
    kitchen_waste = bio_input_field("Kitchen waste")
    fruit_veg_waste = bio_input_field("Fruit and vegetable waste")
    bread_paste_waste = bio_input_field("Bread paste waste")
    diesel_waste_water = bio_input_field("Diesel waste water")
    oil_waste = bio_input_field("Oil waste")
    other_waste = bio_input_field("Other waste")

class ForecastForm(FlaskForm):
    entries = FieldList(FormField(DataForm))
