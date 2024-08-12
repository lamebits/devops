from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)


@app.route('/')
def home():
  return '<h1>Create Rest API</h1> <p>Example Url : /api/v1/usd-jpy</p>'


def get_currency(in_currency, out_currency):
  url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount=1'
  content = requests.get(url, verify=False).text
  soup = BeautifulSoup(content, 'html.parser')
  rate = soup.find("span", class_="ccOutputRslt").get_text()
  rate = float(rate[:-4])
  return rate


@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
  rate = get_currency(in_cur, out_cur)
  result_dict = {
      'input_currency': in_cur,
      'output_currency': out_cur,
      'rate': rate
  }
  return jsonify(result_dict)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
