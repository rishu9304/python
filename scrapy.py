import scrapy
import time
#import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#import matplotlib.pyplot as plt  


analyser = SentimentIntensityAnalyzer()

product =  input("Enter the product fullname to get review: ").lower()



class AmazonReview(scrapy.Spider):
	name = 'comment'
	start_urls = ['https://www.amazon.in/']
	allowed_domains = ['amazon.com','amazon.in']

	def parse(self,response):
		print(response.url)
		print("product",product)
		return scrapy.FormRequest.from_response(
            response,
            formdata={'field-keywords': product},
            callback=self.after_login
        )
	def after_login(self,response):
		print(response.url)
		#response.css('h2.a-size-mini')
		for link in response.css('h2.a-size-mini'):
			res = link.css('a.a-link-normal::attr(href)').get()
			span = link.css('span.a-size-medium::text').get()
			print("span",span)
			if product in span.lower():
				print("res",res)
				print('*'*50)
				break
		yield response.follow(res,callback=self.data_fetch)
		#print("working")

	def data_fetch(self,response):
		print("something")
		print('*'*50)
		for div in response.css('div.a-row'):
			link = div.css('a.a-size-base::attr(href)').get()
			print(link)
			#break
		time.sleep(5)
		yield response.follow(link,callback=self.fetch_comment)

	def fetch_comment(self,response):
		total = 0
		neu = 0
		pos = 0
		neg = 0 
		time.sleep(5)
		print("response",response.url)
		print('*'*50)
		for data in response.css('div.review-data'):
			comment = data.css('span::text').getall()
			try:
				for text in comment:
					print("text",text)
					if text != 'Verified Purchase' and text is not None and len(text)>10:
						#with open('data.txt','a') as f:
							#f.write(text+'\n')
						total += 1
						score = analyser.polarity_scores(text)
						if score['compound']>0.05:
							pos+=1
						elif score['compound']>-0.05 and score['compound']<0.05:
							neu+=1
						else:
							neg+=1 
			except:
				print("data is wrong!!")

		page = response.css('li.a-last')
		next_page = page.css('a::attr(href)').get()
		print("next_page",next_page)
		if next_page is not None:
			yield response.follow(next_page,callback=self.fetch_comment)
		else:
			neu_percent =  (neu*100)/total
			pos_percent =  (pos*100)/total
			neg_percent =  (neg*100)/total
			print("neu_percent",neu_percent)
			print("pos_percent",pos_percent)
			print("neg_percent",neg_percent)
			print("total",total)


#print("neu_percent",neu_percent)
#print("pos_percent",pos_percent)
#print("neu_percent",neu_percent)


'''
import matplotlib
import matplotlib.pyplot as plt
#plt.switch_backend("TkAgg")
matplotlib.use('TKAgg')

values = [60, 80, 90, 55, 10, 30]
colors = ['b', 'g', 'r', 'c', 'm', 'y']
labels = ['US', 'UK', 'India', 'Germany', 'Australia', 'South Korea']
explode = (0.2, 0, 0, 0, 0, 0)
plt.pie(values, colors=colors, labels= values,explode=explode,counterclock=False, shadow=True)
plt.title('Population Density Index')
plt.legend(labels,loc=3)
plt.show()
'''
