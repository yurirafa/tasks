all_tasks = [
    None,
    {'id':1, 'title':'shop', 'details':'Milk'},
    {'id':2, 'title':'post-office', 'details':'Send Letter'},
    {'id':3, 'title':'phone', 'details':'Call Joan'},
    {'id':4, 'title':'kitchen', 'details':'Wash the dishes'},    
]
@app.route("/tasks")
def get_all_tasks():
    return json.dumps(all_tasks)