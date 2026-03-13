cars = {
      "toyota" : {"colour" : "black",
                  "p_year" : 2024,
                  "cost" : 5000,
                  "gearbox" : "automatic"
      },
      "bmw" : {"colour" : "black",
              "p_year" : 2007,
              "cost" : 4000,
              "gearbox" : "mechanic"
      },
      "mercedes-benz" : {"colour" : "white",
                        "p_year" : 2020,
                        "cost" : 10000,
                        "gearbox" : 
                          "automatic"
      },
      "tesla" : {"colour" : "white",
                "p_year" : 2025,
                "cost" : 7000,
                "gearbox" : "automatic"
      },
      "opel" : {"colour" : "red",
                "p_year" : 2000,
                "cost" : 1000,
                "gearbox" : "mechanic"
      }
}
for car, info in cars.items():
  print(f"\n {car.title()}'s colour is {info['colour']}. "
        f"The car was produced in {info['p_year']}. "
        f"It costs ${info['cost']}. "
        f"and it is {info['gearbox']}"
  )