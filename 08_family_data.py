#my family members
family = {
      "anvar" : {"surname" : "hojaniyazow",
                "b_year" : 1979,
                "job" : "carpenter",
                "hobby" : "animal husbandry"
      },
      "zamira" : {"surname" : "sadadinowa",
                "b_year" : 1985,
                "job" : "housewife",
                "hobby" : "playing sports"
      },
      "mahmut" : {"surname" : "hojaniyazow",
                "b_year" : 2010,
                "job" : "student",
                "hobby" : "playing sports"
      },
      "nuriya" : {"surname" : "hojaniyazowa",
                "b_year" : 2016,
                "job" : "student",
                "hobby" : "dancing"
      },
      "behruz" : {"b_year" : 2008,
                "surname" : "hojaniyazow",
                "job" : "student",
                "hobby" : "reading"
      }
}
for name, info in family.items():
  print(f"\n {name.title()}'s surname is {info['surname'].title()}. "
        
       f"He/She was born in {info['b_year']}, "
       
       f"He/She works as a {info['job']}, "
       
       f"His/Her favourite hobby is {info['hobby']}. "
  )