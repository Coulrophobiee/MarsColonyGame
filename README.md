# MarsColony Game

A Python-based grid strategy game where you build and manage a colony on Mars. This project was developed as part of an Advanced Programming course for a Bachelor's degree.

## Game Overview

MarsColony is a survival strategy game where players must build and manage a sustainable colony on Mars. The goal is to grow your population to 200 inhabitants while managing resources and surviving environmental hazards like meteorite impacts.

## Objective

- **Win Condition**: Reach 200 inhabitants
- **Lose Condition**: Food count drops below zero
- Survive meteorite impacts and manage your resources wisely

## Buildings

### Resource Generating Buildings
- **Bio Dome**: Generates 12 food per day (requires power and manpower)
- **Ore Mine**: Generates 10 metal per day (requires power and manpower)

### Infrastructure Buildings
- **Solar Park**: Provides power to buildings within a 5-cell radius
- **Living Compartment**: Houses 10 inhabitants and provides manpower within a 3-cell radius

All buildings cost 2 metal to construct.

## Environmental Features

- **Mars Rocks**: Natural obstacles blocking construction
- **Volcanoes**: Impassable terrain features
- **Meteorites**: Random events that can destroy buildings or create craters
- **Day/Night Cycle**: Resources are generated every 20 seconds (1 game day)

## Controls

- **Left Click**: Select buildings from sidebar or place them on the grid
- **Grid Click**: 
  - With building selected: Place building (if resources available)
  - Without building selected: View cell information
- **Building Selection**: Click on building names in sidebar to select/deselect

## Technical Requirements

### Dependencies
```bash
pip install pygame
```

### File Structure
```
MarsColonyGame/
├── buildings/
│   ├── building.py
│   ├── generating_building.py
│   ├── radius_building.py
│   ├── biodome.py
│   ├── ore_mine.py
│   ├── living_compartment.py
│   └── solar_park.py
├── environment/
│   ├── blockading_elements.py
│   ├── environmental_generator.py
│   ├── mars_rock.py
│   ├── meteorite.py
│   └── volcano.py
├── ui_elements/
│   ├── cell.py
│   ├── grid.py
│   ├── sidebar.py
│   ├── screen.py
│   ├── popup.py
│   ├── console_log.py
│   └── sidebar_elements/
├── utils/
│   ├── icon_manager.py
│   └── pane.py
├── icons/
│   ├── solar-panel.png
│   ├── living_compartment.png
│   ├── bio-dome.png
│   ├── ore-mine.png
│   ├── mars-rock.png
│   ├── volcano.png
│   ├── meteorite.png
│   └── dust.png
├── colony.py
└── main.py
```

## How to Run

1. Ensure Python 3.x and pygame are installed
2. Clone or download the project
3. Navigate to the project directory
4. Run the game:
```bash
python main.py
```

## Game Mechanics

### Resource Management
- **Metal**: Used for construction, generated by Ore Mines
- **Food**: Consumed daily by inhabitants, generated by Bio Domes
- **Population**: Provided by Living Compartments

### Power System
- Buildings need power (from Solar Parks) and manpower (from Living Compartments) to function
- Buildings within the radius of power/manpower sources will operate efficiently

### Environmental Hazards
- Meteorites spawn randomly with increasing frequency over time
- Meteorites can destroy buildings or create temporary craters
- Living Compartments and Solar Parks are immune to meteorite damage

### Starting Conditions
- Game begins with 3 buildings: 1 Ore Mine, 1 Living Compartment, 1 Solar Park
- These are automatically placed in a cluster to ensure initial functionality

## Credits

### Icons
All icons used in this project are from [Flaticon](https://www.flaticon.com/) under their free license:

- [Solar Panel icon by Freepik](https://www.flaticon.com/free-icon/solar-panel_649802)
- [Living Compartment icon by Freepik](https://www.flaticon.com/free-icon/city_8598658)
- [Bio Dome icon by Freepik](https://www.flaticon.com/free-icon/nature_14470701)
- [Ore Mine icon by Freepik](https://www.flaticon.com/free-icon/coal-factory_1847379)
- [Mars Rock icon by Freepik](https://www.flaticon.com/free-icon/canyon_5241298)
- [Volcano icon by Freepik](https://www.flaticon.com/free-icons/volcano)
- [Meteorite icon by Freepik](https://www.flaticon.com/free-icons/asteroid)
- [Dust icon by Freepik](https://www.flaticon.com/free-icon/dust_4383809)

## Educational Context

This game was developed as a project for an Advanced Programming course at university level. It demonstrates:

- **Object-Oriented Programming**: Inheritance hierarchies, abstract classes
- **Game Development**: Event-driven programming, real-time updates
- **UI Design**: Grid-based interfaces, sidebar management
- **Resource Management**: Game balance and progression systems
- **Threading**: Asynchronous operations for visual effects

## Key Programming Concepts Used

- Abstract Base Classes (ABC)
- Inheritance and Polymorphism
- Event-driven architecture
- Grid-based coordinate systems
- Threading for time-based effects
- Pygame for graphics and user input

## License

This project uses icons from Flaticon under their free license. Please ensure proper attribution is maintained if reusing this code.

---

*Developed as part of Advanced Programming coursework - demonstrating game development principles and object-oriented design patterns.*