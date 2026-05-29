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



"""
🏠 Project 1 — Smart Home AC Controller Simulation

Built a real-world IoT automation logic in Python 
using conditional statements!

🌡️ How it works:
- Temp ≥ 45°C → Critical Heat! Max Power mode
- Temp ≥ 30°C → Checks room occupancy:
   - 5+ people → Turbo Mode activated
   - Less people → Normal Mode (22°C)
- Temp < 20°C → AC turns OFF (energy saving)
- Otherwise → Comfortable, Eco Mode runs

🔹 Concepts Practiced:
✅ Nested if/elif/else conditions
✅ Multiple user inputs
✅ Real-world decision making logic
✅ IoT automation thinking

What I love about this project — it's not just 
code, it's actual logic that smart home devices use!

CS Student @ UET Lahore 🎓
Day [X] of my Python Journey

#Python #SmartHome #IoT #100DaysOfCode
#UETLahore #Programming #ApnaCollege
#ConditionalStatements #BeginnerProjects"""