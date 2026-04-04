from datetime import datetime

def period(effect_from_date,maturity_date):
    start_date = datetime.strptime(effect_from_date, "%Y-%m-%d")
    end_date = datetime.strptime(maturity_date, "%Y-%m-%d")

    # Convert to tuple-style format
    start_tuple = (start_date.year, start_date.month, start_date.day)
    end_tuple = (end_date.year, end_date.month, end_date.day)

    print("Start:", start_tuple)
    print("End:", end_tuple)

    difference = end_date - start_date
#    period_def = difference.days

    return difference.days

 #   print(f"difference = {period}")

  #  print("Difference in days:", difference.days)
  #  print("Difference in weeks:", difference.days // 7)
  #  print("Timedelta object:", difference)