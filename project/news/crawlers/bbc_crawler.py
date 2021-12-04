from requests_html import HTMLSession


def crawl_one(url):

    with HTMLSession() as session:
        response = session.get(url)

    name = response.html.xpath('//*[@id="Z1TST2R1z1d"]/div/div/div[1]/h1/text()')[0]

    content = response.html.xpath('//*[@id="Z1TST2R1z1d"]/div/div/p/text()')
    images = response.html.xpath('//*[@id="Z1TST2R1z1d"]/div/div/figure[1]')
    pub_date = response.html.xpath('//*[@id="Z1TST2R1z1d"]/div/div/div[1]/div/div/time')[0].text

    my_content = ''
#    breakpoint()
    for element in content:
        my_content += element

    article = {
        'name': name,
        'content': my_content,
        'images': images,
        'pub_date': pub_date,
    }

    print(article)
