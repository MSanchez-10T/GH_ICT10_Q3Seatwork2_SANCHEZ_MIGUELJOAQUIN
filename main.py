from pyscript import display, document # type:ignore


def check_team(event):
    # 1. Clear previous output so messages don't pile up
    document.getElementById('output').innerHTML = ""
    
    # 2. Get the Radio Buttons (Registration)
    # We use querySelector to find which one is checked
    reg_choice = document.querySelector('input[name="reg_status"]:checked')
    
    # 3. Get the Radio Buttons (Medical)
    med_choice = document.querySelector('input[name="med_status"]:checked')

    # 4. Get Dropdown Values using the correct IDs (s1 and s2)
    grade_val = document.getElementById('s1').value
    section_val = document.getElementById('s2').value

    # --- VALIDATION LOGIC ---

    # Check if the user actually clicked the radio buttons
    if not reg_choice:
        display("Please select Yes or No for Online Registration.", target='output')
        return
    if not med_choice:
        display("Please select Yes or No for Medical Clearance.", target='output')
        return

    # Check Registration Status
    if reg_choice.value == "no":
        display("Please fill out the online registration first.", target='output')
        return  # Stop here, don't check the rest
    
    # Check Medical Status
    if med_choice.value == "no":
        display("Please process your medical clearance.", target='output')
        return # Stop here

    # --- TEAM ASSIGNMENT LOGIC ---
    
    # Check Grade
    valid_grades = ['7', '8', '9', '10']
    
    if grade_val == '0':
        display("Please select a valid Grade level.", target='output')
        return
    
    # Check Section
    valid_sections = ['Topaz', 'Sapphire', 'Emerald', 'Ruby']
    
    if section_val == '01':
        display("Please select a valid Section.", target='output')
        return

    # If all checks pass
    if grade_val in valid_grades and section_val in valid_sections:
        display("Congratulations! You are eligible to join the RedBulldogs.", target='output')