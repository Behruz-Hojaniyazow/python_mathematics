import sys
      
def add_contact():
  """Collect contact information from the user and store it in a list"""
  
  contacts = []
  order = 1
  
  # Start collecting contact information
  while True:
    print(f"{order}-Enter information about a person!")
    name = input("Name: or type(stop) to stop adding contacts: ").strip()
    
    # Stop adding contacts
    if name.lower() == 'stop':
      print("Adding contacts stopped")
      break
    
    # Validate name input
    if not name:
      print("❌️Name cannot be empty!")
      continue
    
    phone_num = input("Phone Number: ").strip()
    
    # Validate phone number
    if not phone_num:
      print("❌️ Phone number cannot be empty!")
      continue
    
    if not phone_num.isdigit():
      print("❌️ Phone number must contain only digits!")
      continue
    
    # Create Contact dictionary
    contact = {
      'name' : name,
      'phone' : phone_num
    }
    
    # Save contact
    contacts.append(contact)
    order += 1
    
    print("✅️\nContact saved successfully!")
  
  return contacts