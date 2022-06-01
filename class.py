from xmlrpc.client import Transport


class Aircraft(object):
    def __init__(self, role, outline , airframeCharacteristics, examples):
        self.role = role
        self.outline = outline  
        self.airframeCharacteristics = airframeCharacteristics
        self.examples = examples


    
    def details(self, role, type, airframeCharacteristics, examples):
        print("The role of the aircraft is: ", self.role)
        print("What is this role?: ", self.outline)        
        print("The main airframe characteristics of this aircraft are: ", self.airframeCharacteristics)
        print("These are some examples: ", self.examples)

    def description(self):
        print("This program will teach you the seven main roles of aircraft in the Royal Australian Air Force. It will explain, their role type, a breif summary airframe characteristics along with a example")


Fighter = Aircraft("Multi-Role Fighter", "Small aircraft designed to shoot down other fighters Can also be multirole and carry some bombs and air to ground missiles", "Small, short, tapered wings, Narrow fuselage, pointy nose, Single or twin tails", "F-35 Lighting II, F/A-18F Super Hornet, F/A-18A/B Hornet")
print(Fighter.description())
print(Fighter.details(Fighter.role, Fighter.outline, Fighter.airframeCharacteristics, Fighter.examples))
    
Bomber = Aircraft("Bomber", "Large, heavy aircraft designed to carry bombs and missiles internally or externally, Long range", "Large fuel capacity, Maximised for range and load, Not as manoeuvrable as a fighter", "B-52 Stratofortress (US Air Force), B-1B Lancer (US Air Force)")
print(Bomber.description())
print(Bomber.details(Bomber.role, Bomber.outline, Bomber.airframeCharacteristics, Bomber.examples)) 

Transporter = Aircraft("Transporter", "Large, heavy aircraft designed to carry equipment or personnel", "Large fuel capacity, Maximised for range and load, Not as manoeuvrable as a fighter", "C-130J Hercules, C-17A Globemaster, C-27J Spartan")
print(Transporter.description())
print(Transporter.details(Transporter.role, Transporter.outline, Transporter.airframeCharacteristics, Transporter.examples)) 

MaritimePatrol = Aircraft("Maritime Patrol", "Large aircraft with multiple crew onboard and dedicated air to surface sensors", "Usually based on passenger aircraft crew comfort, Multiple sensors and antennas to detect ships, Often has a boom for detecting submarines", "P-8A Poseidon, AP-3C Orion ")
print(MaritimePatrol.description())
print(MaritimePatrol.details(MaritimePatrol.role, MaritimePatrol.outline, MaritimePatrol.airframeCharacteristics, MaritimePatrol.examples))

AirborneSurveillanceAndControl = Aircraft("Airborne Surveillance And Control", "Large aircraft with multiple crew onboard and dedicated air-to-air sensors, Can be airborne for 12-14 hours", "Usually based on passenger aircraft crew comfort, Large antenna or array to see long distances, Can have the ability to refuel while airborne", "E-7A Wedgetail")
print(AirborneSurveillanceAndControl.description())
print(AirborneSurveillanceAndControl.details(AirborneSurveillanceAndControl.role, AirborneSurveillanceAndControl.outline , AirborneSurveillanceAndControl.airframeCharacteristics, AirborneSurveillanceAndControl.examples)) 

AerialRefuelling = Aircraft("Aerial Refuelling", "Large aircraft designed to provide airborne refuelling for other aircraft", "Usually based on passenger aircraft common design and maintenance, Large internal fuel load, Can have boom, probe and drogue refuelling capability, or both", "KC-30A Multirole Tanker Transport (MRTT)")
print(AerialRefuelling.description())
print(AerialRefuelling.details(AerialRefuelling.role, AerialRefuelling.outline , AerialRefuelling.airframeCharacteristics, AerialRefuelling.examples)) 

Trainer = Aircraft("Trainer", "Powered or unpowered, Have a propeller or jet engine, Fixed wing or rotary wing, Pilot trainer or crew trainer", "Seating for student and instructor, Good visibility, Rugged, reliable and simple", "PC-21, Hawk 127 Lead-In Fighter, KA-350 King Air")
print(Trainer.description())
print(Trainer.details(Trainer.role, Trainer.outline , Trainer.airframeCharacteristics, Trainer.examples)) 