from flask import Flask, render_template, redirect, url_for, request, session, abort, flash

from app import app

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about-us.html")
	
@app.route('/solutions')
def solutions():
    return render_template("solutions.html")

@app.route('/e-commerce_dev')
def e_commerce_dev():
    return render_template("e-commerce_dev.html")
	
@app.route('/web_design_services')
def web_design_services():
    return render_template("web_design_services.html")
	
@app.route('/seo_services')
def seo_services():
    return render_template("seo_services.html")
	
@app.route('/advantages-of-having-online-shop-over-your-traditional-retail')
def advantages_of_having_online_shop_over_your_traditional_retail():
    return render_template("advantages-of-having-online-shop-over-your-traditional-retail.html")
	
@app.route('/5-must-have-features-of-a-modern-website-design')
def must_have_features_of_a_modern_website_design():
    return render_template("5-must-have-features-of-a-modern-website-design.html")
	
@app.route('/tips-for-choosing-a-web-designer-in-kenya')
def tips_for_choosing_a_web_designer_in_kenya():
    return render_template("tips-for-choosing-a-web-designer-in-kenya.html")
	
@app.route('/school-management-system')
def school_management_system():
    return render_template("school-management-system.html")
	
@app.route('/document-management-system')
def document_management_system():
    return render_template("document-management-system.html")
	
@app.route('/project-management-system')
def project_management_system():
    return render_template("project-management-system.html")
	
@app.route('/property-management-system')
def property_management_system():
    return render_template("property-management-system.html")
	
@app.route('/human-resource-management-system')
def human_resource_management_system():
    return render_template("human-resource-management-system.html")
	
@app.route('/inventory-management-system')
def inventory_management_system():
    return render_template("inventory-management-system.html")

@app.route('/services')
def services():
   return render_template("services.html")
	

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True
            flash('Successful login.')
            return redirect(url_for('index'))
    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))
