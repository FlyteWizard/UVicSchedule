import uvic

def main():
  auth = uvic.Auth()

  # Attempt to open the MyCard page
  auth.load('https://www.uvic.ca/BAN1P/bwskflib.P_SelDefTerm?calling_proc_name=bwskfshd.P_CrseSchdDetl')

if __name__ == "__main__":
  main()
