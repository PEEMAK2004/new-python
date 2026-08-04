def dispaly_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

dispaly_info(name="Supakorn", age=30, city="Bangkok")
# Output:
# name: Supakorn
# age: 25
# city: Bangkok