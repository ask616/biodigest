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
    pig_manure_waste = bio_input_field("Pig manure waste")
    cassava_waste = bio_input_field("Cassava waste")
    fish_waste_water = bio_input_field("Fish waste water")
    kitchen_food_waste = bio_input_field("Kitchen food waste")
    municipal_fecal_residue_waste = bio_input_field("Municipal fecal residue waste")
    tea_waste = bio_input_field("Tea waste")
    chicken_litter_waste = bio_input_field("Chicken litter waste")
    bagasse_feed_waste = bio_input_field("Bagasse feed waste")
    alcohol_waste = bio_input_field("Alcohol waste")
    chinese_medicine_waste = bio_input_field("Chinese medicine waste")
    energy_grass_waste = bio_input_field("Energy grass waste")
    banana_fruit_shafts_waste = bio_input_field("Banan afruit shafts")
    lemon_waste = bio_input_field("Lemon waste")
    percolate_waste = bio_input_field("Percolate waste")
    other_waste = bio_input_field("Other waste")

class ForecastForm(FlaskForm):
    entries = FieldList(FormField(DataForm))
