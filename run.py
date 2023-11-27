from pingouin_app import app


if __name__ == "__main__":
    #après verification, Gunicorn ne passe pas par la et se mets par defaut en debug=false
    app.run(debug=True)
