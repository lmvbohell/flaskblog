from flaskblog import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

#  $env:FLASK_APP = "flaskblog" pga powershell!!!
