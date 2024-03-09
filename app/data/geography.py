biomes: list = ["PLAIN"]

regions: list = [
    {
        "id": "GREAT_PLAINS",
        "name": "Great Plains",
        "biome": "PLAIN",
        "description": "The expanse of the Great Plains is magestic. The Wide Road crosses this landscape, from the windy peaks of the Highlands to the dank mists of the Marshes. There are plenty of settlements and relics, and all sorts of creatures hiding away off the beaten track.",
        "temperatureModifier": 0,
        "weatherConditions": ["SUNNY", "OVERCAST", "RAINING", "SNOWING", "WINDY"],
        "startingArea": "LOWLANDS",
        "areas": [
            "LOWLANDS",
            "MARSHES",
            "WIDE_PRAIRIE",
            "LAKE_GROTTEN",
            "ESCARPMENT",
            "MIDWAY",
            "RAGGED_MOOR",
            "HIGHLANDS",
            "FOOTHILLS",
            "SLOPE",
            "BLUE_COPSE",
            "LOWER_VALLEY",
        ],
    }
]

areas: list[dict] = [
    {
        "id": "LOWLANDS",
        "name": "Lowlands",
        "temperatureModifier": 1,
        "size": 5,

        "altitude": 50,
        "hasCoastline": False,
        "hasRiver": True,
        "hasLake": True,
        "isUrban": False,
        "isUnderground": False,

        "description": "An area of open grassland at low altitude with plenty of flora and fauna.",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "ESCARPMENT",
            "MARSHES",
            "WIDE_PRAIRIE",
        ],
    },
    {
        "id": "MARSHES",
        "name": "Marshes",
        "temperatureModifier": 3,
        "size": 5,

        "altitude": 50,
        "hasCoastline": False,
        "hasRiver": True,
        "hasLake": True,
        "isUrban": False,
        "isUnderground": False,

        "description": "A wet and smelly place, often flooded completely from the nearby River Claron",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "LOWLANDS",
            "LAKE_GROTTEN",
        ],
    },
    {
        "id": "WIDE_PRAIRIE",
        "name": "Wide Prairie",
        "temperatureModifier": 2,
        "size": 5,
        "description": "An open expanse of grassland stretching to the horizon in all directions.",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "LOWLANDS",
            "LAKE_GROTTEN",
            "FOOTHILLS",
            "MIDWAY",
        ],
    },
    {
        "id": "LAKE_GROTTEN",
        "temperatureModifier": 0,
        "size": 5,
        "name": "Lake Grotten",
        "description": "A large, circular lake known for its plentiful fish stock.",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "MARSHES",
            "WIDE_PRAIRIE",
        ],
    },
    {
        "id": "ESCARPMENT",
        "temperatureModifier": -1,
        "size": 5,
        "name": "Escarpment",
        "description": "A large, steep incline marking the eastern edge of the region.",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "LOWLANDS",
            "MIDWAY",
        ],
    },
    {
        "id": "MIDWAY",
        "name": "Midway",
        "temperatureModifier": -2,
        "size": 5,
        "description": "A long, open area of grassland connecting rising from out of the valleys.",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "ESCARPMENT",
            "WIDE_PRAIRIE",
            "RAGGED_MOOR",
        ],
    },
    {
        "id": "RAGGED_MOOR",
        "name": "Ragged Moor",
        "temperatureModifier": -3,
        "size": 5,
        "description": "A high-altitude secton of moorland with high winds and view over entire region.",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "MIDWAY",
            "FOOTHILLS",
            "HIGHLANDS",
        ],
    },
    {
        "id": "HIGHLANDS",
        "name": "Highlands",
        "temperatureModifier": -5,
        "size": 5,
        "description": "A barren expanse of rock and scrubland, often covered in cloud.",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "RAGGED_MOOR",
            "SLOPE",
        ],
    },
    {
        "id": "FOOTHILLS",
        "name": "Foothills",
        "temperatureModifier": 1,
        "size": 5,
        "description": "A series of rolling hills rising up from the meadows below.",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "RAGGED_MOOR",
            "SLOPE",
            "BLUE_COPSE",
            "WIDE_PRAIRIE",
        ],
    },
    {
        "id": "SLOPE",
        "name": "Slope",
        "temperatureModifier": 0,
        "size": 5,
        "description": "A wide section of grassland rising steeply out of the valleys below.",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "HIGHLANDS",
            "FOOTHILLS",
            "LOWER_VALLEY",
        ],
    },
    {
        "id": "BLUE_COPSE",
        "name": "Blue Copse",
        "temperatureModifier": 2,
        "size": 5,
        "description": "A dense thicket named for the colour the trees appear at twilight.",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "LAKE_GROTTEN",
            "LOWER_VALLEY",
            "FOOTHILLS",
        ],
    },
    {
        "id": "LOWER_VALLEY",
        "name": "Lower Valley",
        "temperatureModifier": 4,
        "size": 5,
        "description": "A wide, sweeping valley with an abundance of meadows.",
        "region": "GREAT_PLAINS",
        "connectedAreas": [
            "SLOPE",
            "BLUE_COPSE",
            "FOOTHILLS",
        ],
    }
]

maps: list = [
    {
        "region": "GREAT_PLAINS",
        "map": """
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒
▒▒   Escarpment  ▒▒▒▒▒▒     Midway    ▒▒▒▒▒▒  Ragged Moor  ▒▒▒▒▒▒   Highlands   ▒▒
▒▒               ▒▒▒▒▒▒               ▒▒▒▒▒▒               ▒▒▒▒▒▒               ▒▒
▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
        ▒▒▒                  ▒▒▒                  ▒▒▒                  ▒▒▒        
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒
▒▒    Lowlands   ▒▒▒▒▒▒     Wide      ▒▒▒▒▒▒   Foothills   ▒▒▒▒▒▒     Slope     ▒▒
▒▒               ▒▒▒▒▒▒    Prairie    ▒▒▒▒▒▒               ▒▒▒▒▒▒               ▒▒
▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒  
        ▒▒▒                  ▒▒▒                  ▒▒▒                  ▒▒▒        
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒
▒▒    Marshes    ▒▒▒▒▒▒      Lake     ▒▒▒▒▒▒      Blue     ▒▒▒▒▒▒     Lower     ▒▒
▒▒               ▒▒▒▒▒▒    Grotten    ▒▒▒▒▒▒     Copse     ▒▒▒▒▒▒     Valley    ▒▒
▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒  ▒▒▒             ▒▒▒
 ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒    ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ 
"""
    }
]
