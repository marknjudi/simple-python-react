# Simplest Python/React App

by Mark Wallace, Feb 2019

## To configure

If you don't have python flask already:

	pip install flask

## To run

	set FLASK_APP=app.py
	set FLASK_ENV=development
	flask run

Open your browser to:

	http://127.0.0.1:5000/

## What it does

In this example, the simple client calls the server to get the server's IP address.

The server calls out to another service, https://httpbin.org/ip, to get the server's external IP address.

Since this service takes a little while (on my computer), you get a chance to see the React-based GUI render initially, then render again when the data data becomes available (the `tbd` is replaced by the real IP address). 