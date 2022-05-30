import flask
app = flask.Flask("app")

# functions : 

#get page
def get_html(page_name):
  html_file = open(page_name + ".html")
  content = html_file.read()
  html_file.close()
  return content

# Add notes
def add_notes(note_value):
    note = note_value
    file = open("notes.txt", "a")
    file.write("----\n" + str(note) + "\n")
    file.close()

#get notes
def get_notes():
  notedb = open("notes.txt")
  content = notedb.read()
  notedb.close()
  notes = content.split("\n")
  notes.pop(len(notes) - 1)
  return notes


@app.route("/")
def home():
  return get_html("index")


@app.route("/add")
def add():
  note_value = flask.request.args.get("add")
  add_notes(note_value)
  return get_html("index")

@app.route("/search-results")
def search():
  html_page = get_html("search-results")
  query = flask.request.args.get("search")
  notes = get_notes()
  result = ""
  
  for note in notes:
    if note.lower().find(query.lower()) != -1:
      result += "<p>" + str(note) + "</p>"
      
  if result == "":
      result = "<p>No results found</p>"
  return html_page.replace("$$NOTES$$", result)

@app.route("/notes")
def view_all_notes():
  html_page = get_html("notes")
  notes = get_notes()
  result = ""
  for note in notes:
      result += "<p>" + note + "</p>"
      
  if result == "":
      result = "<p>No notes available</p>"
  return html_page.replace("$$NOTES$$", result)
