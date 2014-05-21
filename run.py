# -*- coding: utf-8 -*-
from app import app
  
if __name__ == "__main__":
    print("Host ip is: " + app.config['HOST_IP'])
    app.run(debug=app.config.get('DEBUG'), host=app.config.get('HOST_IP'))
