from slugify import slugify
from requests_html import HTMLSession


def crawl_one(url):

    with HTMLSession() as session:
        response = session.get(url)

    name = response.html.xpath('//*[@id="big_title"]')[0].text
    content = response.html.xpath('//*[@id="content_col"]/div[3]/div[3]')
    image_url = 'https://www.techcult.ru' + response.html.xpath('//*[@id="content_col"]/div[3]/div[3]/div[1]/div/img/@src')[0]
    pub_date = response.html.xpath('//*[@id="content_col"]/div[3]/div[2]/meta/@content')[0]

    my_content = ''
    short_description = ''
    for element in content:
        my_content +=f'<{element.tag}>' + element.text + f'<{element.tag}>'
        if len(short_description) < 200:
            short_description += element.text + ' '

#    my_content = ''
#    breakpoint()
#    for element in content:
#        my_content += element
    image_name = slugify(name)[:25]
    img_type = image_url.split('.')[-1]

    img_path = f'images/{image_name}.{img_type}'
#    breakpoint()
    with open(f'media/{img_path}', 'wb') as f:
        with HTMLSession() as session:
            response = session.get(image_url)
            f.write(response.content)

    article = {
        'name': name,
        'content': my_content,
        'short_description': short_description.strip(),
        'main_image': img_path,
        'pub_date': pub_date,
    }

    print(article)
#    print(content)
#    print(images)
#    print(pub_date)
