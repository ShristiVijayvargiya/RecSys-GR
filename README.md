![Tripadvisor Scraper Featured Image](https://raw.githubusercontent.com/omkarcloud/tripadvisor-scraper/master/images/tripadvisor-scraper-featured-image.png)

<div align="center" style="margin-top: 0;">
  <h1>✨ Tripadvisor Scraper 🚀</h1>
  <p>💦 Find websites, contact details, title, description of hotels and restaurants from TripAdvisor. 💦</p>
</div>
<em>
  <h5 align="center">(Programming Language - Python 3)</h5>
</em>
<p align="center">
  <a href="#">
    <img alt="tripadvisor-scraper forks" src="https://img.shields.io/github/forks/omkarcloud/tripadvisor-scraper?style=for-the-badge" />
  </a>
  <a href="#">
    <img alt="Repo stars" src="https://img.shields.io/github/stars/omkarcloud/tripadvisor-scraper?style=for-the-badge&color=yellow" />
  </a>
  <a href="#">
    <img alt="tripadvisor-scraper License" src="https://img.shields.io/github/license/omkarcloud/tripadvisor-scraper?color=orange&style=for-the-badge" />
  </a>
  <a href="https://github.com/omkarcloud/tripadvisor-scraper/issues">
    <img alt="issues" src="https://img.shields.io/github/issues/omkarcloud/tripadvisor-scraper?color=purple&style=for-the-badge" />
  </a>
</p>
<p align="center">
  <img src="https://views.whatilearened.today/views/github/omkarcloud/tripadvisor-scraper.svg" width="80px" height="28px" alt="View" />
</p>

<p align="center">
  <a href="https://gitpod.io/#https://github.com/omkarcloud/tripadvisor-scraper">
    <img alt="Open in Gitpod" src="https://gitpod.io/button/open-in-gitpod.svg" />
  </a>
</p>
  
---

## Disclaimer for Tripadvisor Scraper Project

> By using Tripadvisor Scraper, you agree to comply with all applicable local and international laws related to data scraping, copyright, and privacy. The developers of Tripadvisor Scraper will not be held liable for any misuse of this software. It is the user's sole responsibility to ensure adherence to all relevant laws regarding data scraping, copyright, and privacy, and to use Tripadvisor Scraper in an ethical and legal manner, in line with both local and international regulations.

We take concerns related to the Tripadvisor Scraper Project very seriously. If you have any inquiries or issues, please contact Chetan Jain at [chetan@omkar.cloud](mailto:chetan@omkar.cloud). We will take prompt and necessary action in response to your emails.

## 👉 Explore Our Other Awesome Products

- ✅ [BOTASAURUS](https://github.com/omkarcloud/botasaurus): The All-in-One Web Scraping Framework with Anti-Detection, Parallelization, Asynchronous, and Caching Superpowers.

- ✅ [GOOGLE MAPS SCRAPER](https://github.com/omkarcloud/google-maps-scraper): Discover Search Results from Google Maps.

<!-- - ✅ [GOOGLE SCRAPER](https://github.com/omkarcloud/google-scraper): Discover Search Results from Google. -->

---

Discover search results of hotels and restaurants from TripAdvisor.


## 🚀 Getting Started

1️⃣ **Clone the Magic 🧙‍♀:**
```shell
git clone https://github.com/omkarcloud/tripadvisor-scraper
cd tripadvisor-scraper
```
2️⃣ **Install Dependencies 📦:**
```shell
python -m pip install -r requirements.txt
```
3️⃣ **Let the Rain of DATA_NAME3 Begin 😎**:
```shell
python main.py
```

Find your Tripadvisor Data in the `output` directory.

![Tripadvisor Scraper CSV Result](https://raw.githubusercontent.com/omkarcloud/tripadvisor-scraper/master/images/tripadvisor-scraper-csv-result.png)

*Note: If you don't have Python installed. Follow this Simple FAQ [here](https://github.com/omkarcloud/tripadvisor-scraper/blob/master/advanced.md#-i-dont-have-python-installed-how-can-i-run-the-scraper) and you will have your Tripadvisor data in next 5 Minutes*

## 🤔 FAQs
### ❓ How to Scrape Hotels and Restaurants from Tripadvisor?

1. Open the `main.py` file.
2. Update the `locations` list with the locations you are interested in. For example:

```python
locations = [
  "New York",
  "Los Angeles",
  "Chicago",
  "Washington DC",
]

Tripadvisor.search(locations, type=Tripadvisor.HOTEL, max=100)
```

3. Run it.

```bash
python main.py
```

Then find your Tripadvisor data in the `output` directory.

![Tripadvisor Scraper CSV Result](https://raw.githubusercontent.com/omkarcloud/tripadvisor-scraper/master/images/tripadvisor-scraper-csv-result.png)

Also, to scrape restaurants, use the following example:

```python
locations = [
  "New York",
  "Los Angeles",
  "Chicago",
  "Washington DC",
]

Tripadvisor.search(locations, type=Tripadvisor.RESTAURANT, max=100)
```


### ❓ How to scrape all cities in my country?

The following example demonstrates how to scrape 100 hotels from 10 cities in UnitedStates.

```python
locations = Tripadvisor.Cities.UnitedStates()[0:10]
Tripadvisor.search(locations, type=Tripadvisor.HOTEL, max=100) 
```

After running the code, an `united-states-cities.json` file will be generated in the `output` directory with a list of all American cities.

You can prioritize certain cities by editing the cities JSON file in the output folder and moving them to the top of the list.

See the list of all supported countries [here](https://github.com/omkarcloud/tripadvisor-scraper/blob/master/countries.md). 

### ❓ How to Scrape All The Hotels in My Target Location?

To search for all hotels in your target location, remove the `max` parameter. This will scrape all the hotels available in the specified locations.

```python
locations = [
  "Detroit",
]

Tripadvisor.search(locations, type=Tripadvisor.HOTEL)
```

### ❓ How to Scrape More Tripadvisor Listings Using Your Tripadvisor API?

To scrape additional locations, follow these steps to use our Tripadvisor API with the Free Plan. You can make 50 requests for free, allowing you to scrape 1500 (50 * 30) listings at no cost:
1. Sign up on RapidAPI by visiting [this link](https://rapidapi.com/auth/sign-up).

<!-- ![Sign Up on RapidAPI](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/sign-up.png) -->

2. Then, subscribe to our Free Plan by visiting [this link](https://rapidapi.com/Chetan11dev/api/tripadvisor-scraper/pricing).

![Subscribe to Free Plan](https://raw.githubusercontent.com/omkarcloud/tripadvisor-scraper/master/images/tripadvisor-free-subscription.png)

3. Now, copy the API key.

![Copy the API Key](https://raw.githubusercontent.com/omkarcloud/tripadvisor-scraper/master/images/tripadvisor-api-key.png) 

4. Use it in the scraper as follows:
```python
Tripadvisor.search("Atlanta", type=Tripadvisor.HOTEL, max=100, key="YOUR_API_KEY")
```

5. Run the script, and you'll find hotels in Amritsar in the `output` folder.
```bash
python main.py
```   

The first 50 requests are free. After that, you can upgrade to the Pro Plan, which will get you 30,000 listings (1000 requests * 30) for just $9.


### ❓ How did you build it?

We used Botasaurus Framework, Botasaurus is an All-in-One Web Scraping Framework with Anti-Detection, Parallelization, Asynchronous, and Caching Superpowers.

Botasaurus helped us cut down the development time by 50% and helped us focus only on the core extraction logic of the scraper.

If you are a Web Scraper, you should learn about Botasaurus [here](https://github.com/omkarcloud/botasaurus), because Botasaurus will save you countless hours in your life as a Web Scraper.

<p align="center">
  <a href="https://github.com/omkarcloud/botasaurus">
  <img src="https://raw.githubusercontent.com/omkarcloud/botasaurus/master/images/mascot.png" alt="botasaurus" />
</a>
</p>

### ❓ Need More Help or Have Additional Questions?

For further help, contact us on WhatsApp. We'll be happy to help you out.

[![Contact Us on WhatsApp about Tripadvisor Scraper](https://raw.githubusercontent.com/omkarcloud/google-maps-scraper/master/screenshots/mwa.png)](https://api.whatsapp.com/send?phone=918295042963&text=Hi,%20I%20would%20like%20to%20learn%20more%20about%20your%20products.)

## Love It? [Star It! ⭐](https://github.com/omkarcloud/tripadvisor-scraper/stargazers)

## Made with ❤️ using [Botasaurus Web Scraping Framework](https://github.com/omkarcloud/botasaurus)