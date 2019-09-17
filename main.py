#!/usr/bin/env python
from flask import Flask, render_template, request, jsonify, make_response
from flask_wtf import Form
from wtforms import StringField, SelectField
from wtforms.validators import InputRequired
from flask_bootstrap import Bootstrap
from pit import * 


DEBUG = True
app = Flask(__name__)
Bootstrap(app)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


# Format number with thousand separator
def place_value(number): 
    return ("{:,}".format(number)) 

class PITForm(Form):
    gross = StringField('Thu nhập hàng tháng (lương, các khoản phụ cấp, làm ngoài giờ...)', validators=[InputRequired()], default=0)
    contract = StringField('Lương hợp đồng (căn cứ đóng bảo hiểm)', validators=[InputRequired()], default=0)
    dependant = StringField('Số người phụ thuộc', validators=[InputRequired()], default=0)
    region = SelectField(
        'Chọn vùng',
        choices = [
            ('1', 'Vùng 1 Hà Nội, Quảng Ninh, Đà Nẵng, Tp.HCM, Bình Dương, Đồng Nai, Vũng Tàu'), 
            ('2', 'Vùng 2 Hải Phòng, Vĩnh Phúc, Thái Nguyên, Khánh Hoà, Bình Phước, Tây Ninh, Long An, An Giang, Cần Thơ, Cà Mau.'), 
            ('3', 'Vùng 3 Hà Tây, Bắc Ninh, Hải Dương, Hưng Yên, Huế, Bình Định, Gia Lai, Đắc Lắc, Lâm Đồng, Ninh Thuận, Bình Thuận, ĐồngTháp, Tiền Giang, Vĩnh Long, Bến Tre, Kiên Giang, Hậu Giang, Sóc Trăng, Bạc Liêu'), 
            ('4', 'Vùng 4 các tỉnh còn lại.')]
    )


@app.route('/index')
@app.route('/', methods=['GET', 'POST'])
def index():
    form = PITForm()

    if request.method == 'GET':
        return render_template('index.html', form=form)

    elif request.method == 'POST':
        gross = int(request.form['gross'])
        contract = int(request.form['contract'])
        dependant = int(request.form['dependant'])
        region = int(request.form['region'])

        income = PersonalMonthlyIncome(gross,contract,dependant,region)
        #return str(income.personal_income_tax()), 200

        data = [
            {'Name':'Thu nhập trong tháng (lương, phụ cấp, ...)', 'Value':place_value(income.gross)},
            {'Name':'Lương hợp đồng (căn cứ tính bảo hiểm)', 'Value':place_value(income.contract)},
            {'Name':'Mức lương tối thiểu theo vùng', 'Value':place_value(income.minimum_salary())},
            {'Name':'Mức tối đa đóng BHXH (8%), BHYT (1.5%)', 'Value':place_value(income.insurance_based_calculation())},
            {'Name':'Mức tối đa đóng BHTN (1%)', 'Value':place_value(income.unemployment_based_calculation())},
            {'Name':'Bảo hiểm xã hội', 'Value':place_value(income.social_insurance())},
            {'Name':'Bảo hiểm y tế', 'Value':place_value(income.health_insurance())},
            {'Name':'Bảo hiểm thất nghiệp', 'Value':place_value(income.unemployment())},
            {'Name':'Giảm trừ cá nhân', 'Value':place_value(income.personal_deduction())},
            {'Name':'Giảm trừ người phụ thuộc', 'Value':place_value(income.dependant_deduction())},
            {'Name':'Thu nhập chịu thuế', 'Value':place_value(income.taxable_income())},
            {'Name':'Thuế thu nhập cá nhân', 'Value':place_value(income.personal_income_tax())},
            {'Name':'Tiền lương thực nhận (net income)', 'Value':place_value(income.net_income())}
        ]

        return render_template('index.html', data=data, form=form)


if __name__=='__main__':
    app.run(host= '0.0.0.0', port=8000, debug=True)