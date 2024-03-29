import json
import requests
import time
import os

## the "def Data" code is taken from the ROBLOX forums. ##

API_ENDPOINT = "https://users.roblox.com/v1/usernames/users"
GAMEPASS_ENDPOINT = "https://inventory.roblox.com/v1/users/{}/items/GamePass/{}"
BADGE_ENDPOINT = "https://inventory.roblox.com/v1/users/{}/items/2/{}/is-owned"
INVENTORY_ENDPOINT = "https://inventory.roblox.com/v1/users/{}/can-view-inventory"
DETAILEDPLR_ENDPOINT = "https://users.roblox.com/v1/users/{}"
CATALOGGEAR_ENDPOINT = "https://catalog.roblox.com/v1/search/items?category=Accessories&includeNotForSale=true&limit=10&salesTypeFilter=1&subcategory=Gear&Keyword={}"
CATALOG_ENDPOINT = "https://catalog.roblox.com/v1/search/items?category={}&keyword={}&limit=10&salesTypeFilter=1"

def Data(hi):

    requestPayload = {
        "usernames": [
            hi
        ],

        "excludeBannedUsers": False
    }

    responseData = requests.post(API_ENDPOINT, json=requestPayload)

    assert responseData.status_code == 200

    data = responseData.json()["data"][0]["requestedUsername"]
    dataa = responseData.json()["data"][0]["hasVerifiedBadge"]
    dataaa = responseData.json()["data"][0]["id"]
    dataaaa = responseData.json()["data"][0]["name"]
    dataaaaa = responseData.json()["data"][0]["displayName"]

    print(f'Data retreieved!\n\n   requested username: {data}\n   is verified: {dataa}\n   ID: {dataaa}\n   name: {dataaaa}\n   Display Name: {dataaaaa}')
    return data

def checkgamepass(userid, gamepassid):

    response = requests.get(GAMEPASS_ENDPOINT.format(userid, gamepassid))

    ginfo = response.json()["data"]
    print(f'\n"[]" = the player does not own the gamepass / wrong IDs entered. (if gamepass data is shown they own it)\n\n   {ginfo}')
    return ginfo

def checkbadge(useid, badid):

    responsedata = requests.get(BADGE_ENDPOINT.format(useid, badid))

    info = responsedata.json()
    print(f'badge owned: {info}')
    return info

def inv(yo):

    responseyo= requests.get(INVENTORY_ENDPOINT.format(yo))

    inventory = responseyo.json()

    print(f'Data retreieved!\n\n   {inventory}')
    return inventory

def plr(roadblox):

    responseData = requests.get(DETAILEDPLR_ENDPOINT.format(roadblox))

    datab = responseData.json()["description"]
    databc = responseData.json()["created"]
    databcd = responseData.json()["isBanned"]
    databcde = responseData.json()["hasVerifiedBadge"]
    databcdef = responseData.json()["id"]
    databcdefg = responseData.json()["name"]
    databcdefgh = responseData.json()["displayName"]

    print(f'Data retreieved!\n\n   description: {datab}\n\n   creation date: {databc}\n   isBanned: {databcd}\n \n   verified: {databcde}\n   ID: {databcdef}\n   name: {databcdefg}\n   display: {databcdefgh}')
    return datab

def catalog(gear):

    responseData = requests.get(CATALOGGEAR_ENDPOINT.format(gear))

    data = responseData.json()["data"][0]["id"]

    print(f'Gears retreieved!\n\n   gear ID: {data}')
    return data

def catalog10(gears):

    responseData = requests.get(CATALOGGEAR_ENDPOINT.format(gears))

    data = responseData.json()["data"]

    print(f'\n   {data}')
    return data

def start():
    os.system("cls")
    print(
        "██████   ██████  ██████  ██       ██████  ██   ██\n"
        "██   ██ ██    ██ ██   ██ ██      ██    ██  ██ ██\n"
        "██████  ██    ██ ██████  ██      ██    ██   ███\n"
        "██   ██ ██    ██ ██   ██ ██      ██    ██  ██ ██\n"
        "██   ██  ██████  ██████  ███████  ██████  ██   ██\n"
    )
    print("@ycxo on discord                                  | ROBLOX users:")
    print("guns.lol/cxo                                      | 3cxos - creator")
    print("(thanks to @decryptionite for help)               | Dekryptionite - helper")
    print("___________________________________")

start()

while True:

    print("")
    print("1 - get user info                                 |requires player ID. (scrape their info using option 1 first)")
    print("2 - gamepass checker  <---------------------------|")
    print("3 - badge checker  <------------------------------|")
    print("4 - check if users inventory can be viewed  <-----|")
    print("5 - detailed account info on a player  <----------|")
    print("6 - gear ID scraper                               |")
    print("")


    inputs = input("What will it be? ")

    print("")
    if inputs == "1":
     abc = input("username: ")
     print("")
     Data(abc)
     print("")
     time.sleep(1)
     tostart = input("press [ENTER] to return to the start menu. ")
     start()

    if inputs == "2":
        uid = input("player ID: ")
        print("")
        print("default gamepass IDs you can use:")
        print("")
        print("66254 - Kohls admin house [NBC] perm admin")
        print("35748 - Kohls admin house [NBC] person299 admin")
        print("")
        print("64354 - Kohls admin house [BC] perm admin")
        print("37127 - Kohls admin house [BC] person299 admin")
        print("")
        print("96651 - Prison Life [OLD] riot pass")
        print("643697197 - Prison Life [NEW] riot pass")
        print("")
        gid = input("gamepass ID: ")
        checkgamepass(uid, gid)
        time.sleep(1)
        print("")
        tostart = input("press [ENTER] to return to the start menu. ")
        start()

    if inputs == "3":
        usid = input("player ID: ")
        print("")
        print("default badge IDs you can use:")
        print("")
        print("2124510987 - Flex your account age welcome badge - good for spotting PGed accounts")
        print("")
        print("123092900 - Kohls admin house [NBC] visitor 2013")
        print("140970516 - Kohls admin house [NBC] visitor 2014")
        print("123009394 - Kohls admin house [NBC] easter egg")
        print("127566163 - Kohls admin house [NBC] easter egg 2")
        print("")
        print("123093322 - Kohls admin house [BC] visitor 2013")
        print("140970605 - Kohls admin house [BC] visitor 2014")
        print("123012804 - Kohls admin house [BC] easter egg")
        print("127566446 - Kohls admin house [BC] easter egg 2")
        print("")
        bid = input("badge ID: ")
        checkbadge(usid, bid)
        time.sleep(1)
        print("")
        tostart = input("press [ENTER] to return to the start menu. ")
        start()

    elif inputs == "4":
            when = input("player ID: ")
            print("")
            inv(when)
            time.sleep(1)
            print("")
            tostart = input("press [ENTER] to return to the start menu. ")
            start()

    elif inputs == "5":
            hate = input("player ID: ")
            print("")
            plr(hate)
            time.sleep(1)
            print("")
            tostart = input("press [ENTER] to return to the start menu. ")
            start()

    elif inputs == "6":
            forsure = input("Gear name: ")
            print("")
            catalog(forsure)
            time.sleep(1)
            print("")
            ask = input("Would you like to scrape 9 other gear IDs of the same query? Y/N: ")
            if ask.lower() == "y" or ask.upper() == "Y":
                catalog10(forsure)
                print("")
                time.sleep(1)
                tostart = input("press [ENTER] to return to the start menu. ")
                start()

            elif ask.lower() == "n" or ask.upper() == "N":
                    print("")
                    time.sleep(1)
                    tostart = input("press [ENTER] to return to the start menu. ")
                    start()
