# Learning-With-AI

this an ai based student teacher application to learn something based on a roadmap provided by user

## How to use:

- to use this application you need to get a `google-gemini` api key.\
  the manual is here : [gemini api key guide](https://ai.google.dev/gemini-api/docs/api-key)
- put that in `.env` file in the root directory of this project as:\

  ```bash
  API_KEY="your gemini api key"
  DOCUMENT_ID=
  ```

- put your learning roadmap in
  ```bash
  asset/.prompt/learning_roadmap.md
  ```
- then check if you have `python` in your machine _like:_\
   **type in teminal:**
  ```bash
    python --version
  ```
  or
  ```bash
  python3 --version
  ```
  **Or** _download_ it from: [downlaod](https://www.python.org/ftp/python/3.13.5/Python-3.13.5.tar.xz)
- create a virtual environment for python in the root directory of this project.
  **guideline:** [create venv](https://www.geeksforgeeks.org/python/creating-python-virtual-environment-windows-linux/)\
   _follow_ it based on your os `widows/linux/mac`
- after **activating** the _virtual environment_ ,\
  run those command in root directory:

  ```powershell
  pip install -r requirement.txt
  ```

  or

  ```powershell
  pip3 install -r requirement.txt
  ```

  then

  ```powershell
  python -m webassets.api
  ```

  or

  ```powershell
  python3 -m webassets.api
  ```

  then you will see something like this:

  ```powershell
  * Serving Flask app 'api'
  * Debug mode: on
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
  * Running on http://127.0.0.1:5000
  Press CTRL+C to quit
  * Restarting with stat
  * Debugger is active!
  * Debugger PIN: 136-864-940
  ```

- click on this :
  ```powershell
  * Running on http://127.0.0.1:5000
  ```
  or copy and paste it to the browser , then you are good to go.
