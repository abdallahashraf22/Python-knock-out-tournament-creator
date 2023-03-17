from metadata.tournament import Tournament


def main():
    tournament = Tournament("./names.csv")
    tournament.start_tournament()


if __name__ == '__main__':
    main()
    
