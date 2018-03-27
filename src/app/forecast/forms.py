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
    pig_manure_waste = bio_input_field("Pig manure")
    cassava_waste = bio_input_field("Cassava")
    fish_waste_water = bio_input_field("Fish waste water")
    kitchen_food_waste = bio_input_field("Kitchen food")
    municipal_fecal_residue_waste = bio_input_field("Municipal fecal residue")
    tea_waste = bio_input_field("Tea")
    chicken_litter_waste = bio_input_field("Chicken litter")
    bagasse_feed_waste = bio_input_field("Bagasse feed")
    alcohol_waste = bio_input_field("Alcohol")
    chinese_medicine_waste = bio_input_field("Chinese medicine")
    energy_grass_waste = bio_input_field("Energy grass")
    banana_fruit_shafts_waste = bio_input_field("Banana fruit shafts")
    lemon_waste = bio_input_field("Lemon")
    percolate_waste = bio_input_field("Percolate")
    other_waste = bio_input_field("Other")

class ForecastForm(FlaskForm):
    entries = FieldList(FormField(DataForm))
