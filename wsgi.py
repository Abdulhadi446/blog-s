from app import create_app

application = create_app(os.environ.get('FLASK_CONFIG', 'production'))

if __name__ == "__main__":
    application.run()