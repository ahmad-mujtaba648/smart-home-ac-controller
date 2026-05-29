# ==========================================
# SMART HOME AC CONTROLLER SIMULATION
# ==========================================
# Real-world IoT automation logic based on temperature and room occupancy

temperature = int(input("Please enter your room temperature: "))

if(temperature >= 45):
    print("Critical Heat! AC running at Maximum Power.")
elif(temperature >= 30):
    people_count = int(input("How many people are in the room: "))
    if(people_count < 0):
        print("Invalid number of people!")
    elif(people_count>= 5):
        print("Turbo Mode Activated (High Occupancy)!")
    else:
        print("Normal Mode (22°C) Activated.")
elif(temperature < 20):
    print("AC turned OFF automatically to save energy.")
else:
    print("Room temperature is comfortable. AC running in Eco Mode.")




