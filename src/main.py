import src.yt_downloader

print("="*48)
print("main.py")
print("="*48)

class MainMenu:
    def main_menu():
        yt_extractor
        def main_options():
            print("What information are you looking for today?\n\n"
            "1 = Get Video Info \n"
            "2 = Download Dash Stream (highest quality) \n"
            "3 = Download Progressive \n"
            "0 = Cancel & Exit \n")
        
        main_options()
        option = int(input("Input here: "))

        while option != 0:
            if option == 1:
                yt_extractor.get_vid_info()
            elif option == 2:
                yt_extractor.download_dash()
            elif option == 3:
                yt_extractor.download_progressive() 
            else:
                print("\nInvalid response, please try again.\n")

            print("\n")
            main_options()
            option = int(input("Input here: "))

    
    def main():
        yt_downloader = src.yt_downloader
        global yt_extractor
        yt_extractor = yt_downloader.VideoExtractor
        print("\nThis is a simple program that will download YouTube videos for watching at any time.")
        yt_extractor.main()
        MainMenu.main_menu()

if __name__ == '__main__':
    MainMenu.main()

print("="*48)
print("Ending Program. . .")
print("="*48)