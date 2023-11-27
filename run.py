from pingouin_app import app


if __name__ == "__main__":
    if (type_server == 'local'):
        app.run(debug=True)
    else:
        app.run(debug=False)