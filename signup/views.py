from django.shortcuts import render, redirect
import mysql.connector as sql
from django.http import HttpResponse
from django.contrib.auth.models import User

def signup_method(request):
    if request.method == "POST":
        # Connect to the MySQL database
        m = sql.connect(host='localhost', user='root', passwd='idontknow', database='user_authentication')
        cursor = m.cursor()

        # Get form data from the request
        first_name = request.POST.get("first_name", "")
        last_name = request.POST.get("last_name", "")
        profile_picture = request.POST.get("profile_picture", "")
        user_name = request.POST.get("username", "")
        user_type = request.POST.get("user_type", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")
        confirm_password = request.POST.get("confirm_password", "")
        address_line1 = request.POST.get("address_line1", "")
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        pincode = request.POST.get("pincode", "")

        # Insert data into the database
        query = ("INSERT INTO users (first_name, last_name, profile_picture, username, email_id, password, "
                 "confirm_password, address_line1, city, state, pincode, user_type) VALUES (%s, %s, %s, %s, %s, %s, "
                 "%s, %s, %s, %s, %s, %s)")
        values = (first_name, last_name, profile_picture, user_name, email, password, confirm_password, address_line1, city, state, pincode, user_type)
        cursor.execute(query, values)

        # Commit the transaction
        m.commit()

        # Close the database connection
        m.close()
        return HttpResponse("Account Created! You can Login now!")

    return render(request, 'signup_page.html')
