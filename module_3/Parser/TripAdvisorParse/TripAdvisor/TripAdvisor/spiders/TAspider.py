import scrapy
import pandas as pd



class TaspiderSpider(scrapy.Spider):

    name = 'TAspider'
    allowed_domains = ['tripadvisor.ru']

    df_train = pd.read_csv('main_task.csv')
    df_test = pd.read_csv('kaggle_task.csv')

    df_train['sample'] = 1
    df_test['sample'] = 0
    df_test['Rating'] = 0

    data = df_test.append(df_train, sort=False).reset_index(drop=True)

    new_urls = data['URL_TA'].apply(lambda x: 'https://www.tripadvisor.ru' + x)
    new_urls = list(new_urls)

    start_urls = new_urls

    counter = 0

    def parse(self, response):
        self.counter += 1
        print(f'{self.counter} processing: ' + response.url)
        rate = response.css('.row_num ::text').extract()
        all_rate = []

        for item in rate[0:5]:
            all_rate.append(int(item))

        yield {
            'url': response.url,
            'rate5': all_rate[0],
            'rate4': all_rate[1],
            'rate3': all_rate[2],
            'rate2': all_rate[3],
            'rate1': all_rate[4]
        }
