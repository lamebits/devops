import webscraping
import datamanupilation
import emailsending

def run_all_tasks():
    print("Starting the Main Process...")
    webscraping.webscraping_main()
    datamanupilation.datamanupilation_main()
    emailsending.mailsending_main()
    print("Stoping the Main Process...")
    
if __name__ == "__main__":
    run_all_tasks()