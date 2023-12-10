from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import mysql.connector as sql

def login_method(request):
    if request.method == "POST":
        user_type = request.POST.get("user_type", "")
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        try:
            with sql.connect(host='localhost', user='root', passwd='idontknow', database='user_authentication') as m:
                cursor = m.cursor()
                c = 'SELECT * FROM users WHERE email_id=%s AND password=%s'
                cursor.execute(c, (email, password))
                user_data = cursor.fetchone()

                if user_data:
                    context = {
                        'user_name': user_data[4],
                        'user_type': user_data[-1],
                        'first_name': user_data[1],
                        'last_name': user_data[2],
                        'email': user_data[5],
                        'address_line1': user_data[8],
                        'city': user_data[9],
                        'state': user_data[10],
                        'pincode': user_data[11],
                        'profile_picture': user_data[3],
                    }
                    return render(request, 'doctor_dashboard.html', context)
                else:
                    return render(request, 'error.html', {'error_message': 'Invalid credentials'})

        except Exception as e:
            return render(request, 'error.html', {'error_message': str(e)})

    return render(request, 'login_page.html')

