shipment_item=input("Choose shipment item: \nletter or parcel\nItem: \n")
weight = int(input("Mailbox Weight: \n"))
shipment_cost ={"letter":[0.5,{0:[0,200], 0.04:[200, 500], 0.07:[500, float('inf')]}], "parcel":[2,{0:[0,200], 0.08:[200, 500], 0.14:[500, float('inf')]}]}
cost=0
if weight>500:
    if input("Does it fit in Mailbox? \nType 'Yes' or 'No':\n")=="No":
        cost=2
for item, weight_per_cost in shipment_cost.items():
    if item==shipment_item:
        cost+=weight_per_cost[0]
        for extra_money, extra_weight_range in weight_per_cost[1].items():
            if weight>=extra_weight_range[0] and weight<=extra_weight_range[1]:
                cost+= extra_money*round((weight/100))
                break
print(f"Total cost for {shipment_item}: {round(cost,2)}€")
