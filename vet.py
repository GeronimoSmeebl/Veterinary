# Put Training Horse Serial Below
Training_Horse_Serial = 0x0000624A

#
def find_items(item_types, item_serial=Player.Backpack.Serial):
    found_items = []    
    cur_item = Items.FindBySerial(item_serial)
    
    # If the serial does not correspond to an item, no items can be found
    if not cur_item:
        return found_items

    # If I was looking for this item, add this item to the list of found items
    if cur_item.ItemID in item_types:
        found_items.append(cur_item)

    # If the item is not a container, no need to search within item for contained items
    if not cur_item.IsContainer:  
        return found_items

    # Otherwise, search inside of item for contained items
    
    # If current item is an empty container, it does not contain any items
    if len(cur_item.Contains) == 0:
        return found_items
    
    

    # Otherwise, look at all contained items and their potential contents with this same function for the same item types
    for item in cur_item.Contains:
        for contained_in_item in find_items(item_types, item.Serial):
            found_items.append(contained_in_item)
    return found_items
#

#
def get_training_horse():
    horse = Target.PromptTarget("Target a training horse.")
    if Mobiles.FindBySerial(horse).Name == "A Taming Training Horse":
        return horse
    else:
        Player.HeadMessage(30, "Target is not a training horse.")
        return None
#


# Work done here
########################################################
Bandage_Item_Id = 0x0E21
Vet_Bandage_Color = 0x0871

horse = get_training_horse()

while(horse != None):
    vet_bandages = None
    bandages_found = find_items([Bandage_Item_Id])

    for item in bandages_found:
        if item.Hue == Vet_Bandage_Color:
            vet_bandages = item.Serial

    if( vet_bandages != None ):
        Items.UseItem(vet_bandages)
        Target.WaitForTarget(10000, False)
        Target.TargetExecute(horse)
        Misc.Pause(3500)
    else:
        Player.HeadMessage(12, "No vet bandages found.")
        break
########################################################