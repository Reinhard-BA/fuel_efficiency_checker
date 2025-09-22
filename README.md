# 🚗 Fuel Efficiency Checker

A Python program to check vehicle **fuel efficiency** using EPA data (2010–2025).  
Users can enter a brand, model, and year to get results in different formats:  

- MPG (miles per gallon)  
- km/l (UK & US)  
- L/100km  

---

## 🚀 Quickstart

```bash
git clone https://github.com/Reinhard-BA/fuel_efficiency_checker.git
cd fuel_efficiency_checker
python fuel_efficiency_checker.py

Enter the vehicle brand here: -> toyota
Enter vehicle model here: -> camry
Enter year here: -> 2020

-----------------------------------------
    Metric     |        Value        
-----------------------------------------
Combined MPG   |       28.00 mpg
km/l (UK)      |        9.93 km/l
km/l (US)      |       11.90 km/l
L/100km        |        8.40 L/100km
-----------------------------------------

**✨ Features**

Partial model name search (camry → matches camry LE, camry SE, etc.)

Choose between multiple trims if found

Clean table output with units

**🛠️ Tech**

Python 3.8+

Built-in modules only (csv, sys)