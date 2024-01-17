products = [
    "PHILIPS_Boiler_HD4646_2020_09_21_C_1",
    "KENWOOD_KitchenMachine_KVL8300S_2015_09_22_C_3",
    "BOSCH_Blender_MMB65G5M_2016_05_07_C_3",
    "WHIRLPOOL_Microwave_MCP345WH_2019_01_15_C_1",
    "ROSENLEW_Freezer_RPP2330_2017_01_29_C_2",
    "ELECTROLUX_Fridge_ERF4114AOW_2017_11_07_C_2"
]
categories = ["Other", "Small electronics", "Appliances", "Blenders"]

for p in products:
    product= p.split("_")
    print(f"Brand: {product[0]}")
    print(f"Name and model: {product[1]} ({product[2]})")
    print(f"Category: {categories[int(product[len(product)-1])]}")
    print(f"Addition date: {product[5]}.{product[4]}.{product[3]}")
    print()