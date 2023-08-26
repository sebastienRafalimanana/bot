
def generate_pharmacies_attachement(sender_id, pharmacies, bot):
    if len(pharmacies) > 7:
        pharmacie_partition = regrouper_liste(pharmacies,10)
        for partition in pharmacie_partition:
            response = {
                "recipient": {"id": sender_id},
                "message": {
                    "attachment": {
                        "type": "template",
                        "payload": {
                            "template_type": "generic",
                            "elements": [
                                {
                                    "title": f"Pharmacie {pharmacy['pharmacie']}",
                                    "subtitle": f"\n{pharmacy['adresse']} ,\nTel:{pharmacy['contact']}",
                                    "image_url": "https://www.vol-direct.net/wp-content/uploads/2023/02/pharmacie-de-garde.jpg",
                                    "buttons": [
                                        {
                                            "type": "postback",
                                            "title": f"Detail",
                                            "payload": f"{pharmacy['pharmacie']};{pharmacy['adresse']};{pharmacy['contact']}"
                                        }]
                                } for pharmacy in partition
                            ]
                        }
                    }
                }
            }
            bot.send_raw(response)
        return
    else:
        response = {
            "recipient": {"id": sender_id},
            "message": {
                "attachment": {
                    "type": "template",
                    "payload": {
                        "template_type": "generic",
                        "elements": [
                                {
                                    "title": f"Pharmacie {pharmacy['pharmacie']}",
                                    "subtitle": f"\n{pharmacy['adresse']} ,\nTel:{pharmacy['contact']}",
                                    "image_url": "https://www.vol-direct.net/wp-content/uploads/2023/02/pharmacie-de-garde.jpg",
                                    "buttons": [
                                        {
                                            "type": "postback",
                                            "title": f"Detail",
                                            "payload": f"{pharmacy['pharmacie']};{pharmacy['adresse']};{pharmacy['contact']}"
                                        }]
                                } for pharmacy in pharmacies
                        ]
                    }
                }
            }
        }
        bot.send_raw(response)
        return

def generate_pharmacy_choice(sender_id, code, bot):
    response = {
        "recipient": {"id": sender_id},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": f"Pharmacie de garde\n 24h/24",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": f"Consulter",
                                    "payload": f'choice;permanant;{code};Pharmacie de garde 24h/24'
                                }]
                        },
                        {
                            "title": f"Pharmacie de garde\n hebdomadaire",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": f"Consulter",
                                    "payload": f'choice;hebdo;{code};Pharmacie de garde hebdomadaire'
                                }]
                        }
                    ]

                }
            }
        }
    }
    bot.send_raw(response)


def generate_menu_attachement(sender_id, bot):
    all_region = getLocalization()
    response = {
        "recipient": {"id": sender_id},
        "message": {
            "attachment": {
                "type": "template",
                "payload": {
                    "template_type": "generic",
                    "elements": [
                        {
                            "title": "Pharmacie de garde à Madagascar",
                            "image_url": "https://www.1min30.com/wp-content/uploads/2018/05/Logo-Pharmacie-500x263.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": f"{all_region[1]}",
                                    "payload": f"{1}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[2]}",
                                    "payload": f"{2}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[3]}",
                                    "payload": f"{3}"
                                },
                            ]
                        },
                        {
                            "title": "Pharmacie de garde à Madagascar",
                            "image_url": "https://www.1min30.com/wp-content/uploads/2018/05/Logo-Pharmacie-500x263.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": f"{all_region[4]}",
                                    "payload": f"{4}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[5]}",
                                    "payload": f"{5}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[6]}",
                                    "payload": f"{6}"
                                },
                            ]
                        },
                        {
                            "title": "Pharmacie de garde à Madagascar",
                            "image_url": "https://www.1min30.com/wp-content/uploads/2018/05/Logo-Pharmacie-500x263.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": f"{all_region[7]}",
                                    "payload": f"{7}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[8]}",
                                    "payload": f"{8}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[9]}",
                                    "payload": f"{9}"
                                },
                            ]
                        },
                        {
                            "title": "Pharmacie de garde à Madagascar",
                            "image_url": "https://www.1min30.com/wp-content/uploads/2018/05/Logo-Pharmacie-500x263.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": f"{all_region[10]}",
                                    "payload": f"{10}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[11]}",
                                    "payload": f"{11}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[12]}",
                                    "payload": f"{12}"
                                },
                            ]
                        },
                        {
                            "title": "Pharmacie de garde à Madagascar",
                            "image_url": "https://www.1min30.com/wp-content/uploads/2018/05/Logo-Pharmacie-500x263.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": f"{all_region[13]}",
                                    "payload": f"{13}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[14]}",
                                    "payload": f"{14}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[15]}",
                                    "payload": f"{15}"
                                },
                            ]
                        },
                        {
                            "title": "Pharmacie de garde à Madagascar",
                            "image_url": "https://www.1min30.com/wp-content/uploads/2018/05/Logo-Pharmacie-500x263.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": f"{all_region[16]}",
                                    "payload": f"{16}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[17]}",
                                    "payload": f"{17}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[18]}",
                                    "payload": f"{18}"
                                },
                            ]
                        },
                        {
                            "title": "Pharmacie de garde à Madagascar",
                            "image_url": "https://www.1min30.com/wp-content/uploads/2018/05/Logo-Pharmacie-500x263.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": f"{all_region[19]}",
                                    "payload": f"{19}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[20]}",
                                    "payload": f"{20}"
                                },
                                {
                                    "type": "postback",
                                    "title": f"{all_region[21]}",
                                    "payload": f"{21}"
                                },
                            ]
                        },
                        {
                            "title": f"Pharmacie de garde à Madagascar",
                            "image_url": "https://www.1min30.com/wp-content/uploads/2018/05/Logo-Pharmacie-500x263.jpg",
                            "buttons": [
                                {
                                    "type": "postback",
                                    "title": f"{all_region[22]}",
                                    "payload": f"{22}"
                                },

                            ]
                        },
                    ]
                }
            }
        }
    }
    bot.send_raw(response)


def quick_response(sender_id, bot):
    response = {
      "recipient": {"id": sender_id},
      "messaging_type": "RESPONSE",
      "message":{
        "text": "...",
        "quick_replies":[
         {
            "content_type":"text",
            "title":"Pharmacie de garde",
            "payload":"pharmacie",
            "image_url":"https://png.pngtree.com/png-vector/20220611/ourmid/pngtree-pharmacy-icon-png-image_4962052.png"
          }
        ]
      }
    }
    bot.send_raw(response)

def getLocalization(button=False):
    bottons_region = []
    localization_key = [
        '___Code region___',
        'Ambatondrazaka',
        'Ambositra',
        'Antananarivo',
        'Fenerive Est',
        'Ambovombe Androy',
        'Tôlagnaro',
        'Toliara',
        'Farafangana',
        'Toamasina',
        'Mahevatanana',
        'Mahajanga',
        'Tsiroanomandidy',
        'Antsiranana',
        'Fianarantsoa',
        'Ihosy',
        'Miarinarivo',
        'Maitirano',
        'Morondava',
        'Sambava',
        'Antsohihy',
        'Antsirabe',
        'Manakara'
    ]

    for key in range(1, len(localization_key)):
        bottons_region.append({
            "type": "postback",
            "title": localization_key[key],
            "payload": key
        }, )
    if button:
        return bottons_region
    return localization_key


def filter_pharmacies_by_date(pharmacies, date, format_date, hebdo=True, permanent=True):
    import bisect
    import datetime
    from config import Config

    date = datetime.datetime.strptime(date, format_date).date()
    filtered_pharmacy = []
    permanent_pharmacy = []
    sorted_pharmacies = sorted(pharmacies,
                               key=lambda x: datetime.datetime.strptime(x['start_date'].strip().replace(' ', ''), format_date).date())
    start_dates = [datetime.datetime.strptime(pharmacy['start_date'].strip(), format_date).date() for pharmacy in
                   sorted_pharmacies]
    end_dates = [datetime.datetime.strptime(pharmacy['end_date'].strip().replace(' ', ''), format_date).date() for pharmacy in
                 sorted_pharmacies]
    #pour la pharmacie de la semaine
    if hebdo:
        index = bisect.bisect_left(start_dates, date)
        if not start_dates[index] <= date and index != 0:
            index = bisect.bisect_left(start_dates, start_dates[index - 1])
        for i in range(index, len(start_dates)):
            if index < len(start_dates) and start_dates[i] <= date < end_dates[i]:
                filtered_pharmacy.append(sorted_pharmacies[i])
            elif start_dates[i] > date:
                break
    #pour le pharmacie 24h/24
    if permanent:
        index = bisect.bisect_left(start_dates, datetime.datetime.strptime(Config.PASS_DATE, format_date).date())
        for i in range(index, len(start_dates)):
            if index < len(start_dates) and start_dates[i] == datetime.datetime.strptime(Config.PASS_DATE, format_date).date():
                permanent_pharmacy.append(sorted_pharmacies[i])
            elif start_dates[i] != date:
                break
    return filtered_pharmacy, permanent_pharmacy

def regrouper_liste(liste, taille_groupe):
    groupes = [liste[i:i + taille_groupe] for i in range(0, len(liste), taille_groupe)]
    return groupes