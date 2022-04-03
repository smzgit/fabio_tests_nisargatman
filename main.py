from wiki_app import  app
from wiki_app import  LOG
from wiki_app import controller
if __name__ == '__main__':
    LOG.info("Starting the flask app")
    app.run(host='0.0.0.0', port=5000, debug=True)
    LOG.info("Finished the flask app")