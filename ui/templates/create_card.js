let card = document.createElement('div');
card.className = 'card'

let header = document.createElement('div');
header.className = 'card-header';

let header_link = document.createElement('a')
header_link.innerHTML = article.title;
header_link.href = '/article/' + article.slug;
header.append(header_link);
card.append(header);

let card_content = document.createElement('div');
card_content.className = 'card-content';

let card_text = document.createElement('p');
card_text.className = 'card-text b3';
card_text.innerHTML = article.text.substr(0,50) + '...';
card_content.append(card_text);

let card_topic = document.createElement('p');
card_topic.innerHTML = 'Topic: ';

let card_topic_link = document.createElement('a');
card_topic_link.innerHTML = article.topic;
card_topic_link.href = '/topic/' + article.topic;

card_topic.append(card_topic_link);
card_content.append(card_topic);

let card_author = document.createElement('p');
card_author.innerHTML = 'Author: ';

let card_author_link = document.createElement('a');
card_author_link.innerHTML = article.author;
card_author_link.href = '/user/' + article.author;

card_author.append(card_author_link);
card_content.append(card_author);

let card_date = document.createElement('p');
let date = new Date(article.created)
let options = {day: 'numeric', month: 'long', year: 'numeric', hour: 'numeric', minute: 'numeric'}
card_date.innerHTML = 'Created: ' + date.toLocaleDateString('en-GB', options);

card_content.append(card_date);
card.append(card_content);

content.append(card)