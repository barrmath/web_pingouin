from pingouin_app.views import create_app


if __name__ == "__main__":
    #après verification, Gunicorn ne passe pas par la et se mets par defaut en debug=false
    app = create_app()
    app.run(debug=True)
