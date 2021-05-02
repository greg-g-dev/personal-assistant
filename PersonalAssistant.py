class PersonalAssistant:
  def __init__(self, todos):
    self.contacts = {'ann': 'Marketing Coordinator', 'chelsea': 'Software Developer', 'nichole': 'Sales Representative', 'max': 'Technical Writer'}
    self.birthdays = {'homer':'04/01/1950','marge':'05/01/1951','lisa':'06/01/1971','bart':'07/04/1973'}
    self.todos = todos

  def get_contact(self, name):
    lower_name = name.lower()
    if lower_name in self.contacts:
      return self.contacts[lower_name]
    else:
      return "not a contact."

  def add_contact(self, name, position):
    lower_name = name.lower()
    if lower_name in self.contacts:
      return "Contact already exists!"
    else:
      self.contacts[lower_name] = position

  def remove_contact(self, name):
    lower_name = name.lower()
    if lower_name in self.contacts:
      self.contacts.pop(lower_name, None)
    else:
      return "That contact isn't saved."

  def add_todo(self, new_item):
    lower_new_item = new_item.lower()
    self.todos.append(lower_new_item)

  def remove_todo(self, todo_item):
    # Checks if todo_item is in todos list
    lower_todo_item = todo_item.lower()
    if lower_todo_item in self.todos:
      # Gets the todo_item index in list
      index = self.todos.index(lower_todo_item)
      # pop the index for todo_item in todos list
      self.todos.pop(index)
    else:
      return "To-do is not in list."

  def get_todo(self):
    return self.todos

  # Gets a birthday from the dictionary
  def get_birthday(self, name):
    lower_name = name.lower()
    if lower_name in self.birthdays:
      return self.birthdays[lower_name]
    else:
      return "not saved!"

  def add_birthday(self, name, birthday):
    lower_name = name.lower()
    if lower_name in self.birthdays:
      return "Birthday for " + name + " already exists. Birthday not added."
    else:
      self.birthdays[lower_name] = birthday

  def remove_birthday(self, name):
    lower_name = name.lower()
    if lower_name in self.birthdays:
      self.birthdays.pop(lower_name)
    else:
      return "Birthday for " + name + " does not exist. Birthday not removed."
