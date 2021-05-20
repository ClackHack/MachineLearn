import datetime
import requests
from datetime import timezone
start = datetime.datetime(2010,1,1).replace(tzinfo=timezone.utc).timestamp()
end=datetime.datetime.now().replace(tzinfo=timezone.utc).timestamp()
url=f"http://history.openweathermap.org/data/2.5/history/city?q=Columbus,1&type=hour&start=1262304000&end={str(int(end))}&appid=43ca5bfeca593927711983778455035a"
page=requests.get(url)
print(page.json())
