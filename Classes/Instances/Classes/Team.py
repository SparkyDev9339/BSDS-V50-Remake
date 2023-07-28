class Team:
    TeamID = [0, 1]
    roomType = 0
    mapID = 7
    PlayersCount = 1
    Members = {}
    ChatData = []

    def createTeamData(calling_instance, fields):
        DBData = {
            'TeamID': fields['TeamID'],
            'roomType': fields['roomType'],
            'mapID': fields['mapID'],
            'PlayersCount': fields['PlayersCount'],
            'Members': {str(calling_instance.player.ID[1]): {'HighID': calling_instance.player.ID[0], 'LowID': calling_instance.player.ID[1], 'King': 1, 'Name': calling_instance.player.Name, 'BrawlerID': calling_instance.player.SelectedBrawlers[0], 'SkinID': 0, 'BrawlerTrophies': calling_instance.player.OwnedBrawlers[f'{calling_instance.player.SelectedBrawlers[0]}']['Trophies'], 'BrawlersTrophiesForRank': calling_instance.player.OwnedBrawlers[f'{calling_instance.player.SelectedBrawlers[0]}']['HighestTrophies'], 'NameColor': calling_instance.player.Namecolor, 'Thumbnail': calling_instance.player.Thumbnail}},
            'ChatData': []
        }
        return DBData