from csgo_manager import CSGOMarket

api_key = ''


if __name__ == '__main__':
    connect = CSGOMarket(api_key)
    weapon = connect.get_weapon_price(weapon_name='AK-47 | Redline (Field-Tested)')
    print(weapon)
