# SIMULATED GDP DATA GENERATOR
# 1960–2020, Top 20 countries each year
# For learning / visualization only (NOT real GDP)

countries = [
    "United States", "China", "Japan", "Germany", "United Kingdom",
    "France", "Italy", "Canada", "India", "Russia",
    "Brazil", "Australia", "South Korea", "Spain", "Mexico",
    "Indonesia", "Netherlands", "Saudi Arabia", "Turkey", "Switzerland"
]

base_gdp_1960 = [
    543e9, 120e9, 95e9, 88e9, 72e9,
    65e9, 62e9, 58e9, 52e9, 56e9,
    48e9, 45e9, 40e9, 38e9, 36e9,
    34e9, 32e9, 30e9, 28e9, 26e9
]

growth_rates = [
    0.035, 0.075, 0.045, 0.03, 0.028,
    0.03, 0.029, 0.031, 0.055, 0.025,
    0.04, 0.032, 0.05, 0.033, 0.036,
    0.052, 0.03, 0.034, 0.038, 0.029
]

output_file = "gdp_1960_2020_simulated.txt"

with open(output_file, "w", encoding="utf-8") as f:
    for year in range(1960, 2021):
        year_data = []
        for i in range(20):
            gdp = base_gdp_1960[i] * ((1 + growth_rates[i]) ** (year - 1960))
            year_data.append((countries[i], int(gdp)))

        # sort by GDP descending
        year_data.sort(key=lambda x: x[1], reverse=True)

        for country, gdp in year_data:
            f.write(f"{year},{country},{gdp}\n")
print(f"File generated: {output_file}")
