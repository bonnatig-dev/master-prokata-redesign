# -*- coding: utf-8 -*-
LIVE="https://master-prokata.by"
MENU=[("Главная","index.html"),("Каталог","catalog.html"),("Условия проката","usloviya.html"),("Акции",LIVE+"/akcii/"),("О нас","about.html"),("Новости",LIVE+"/news/"),("Важно знать",LIVE+"/baza-znanii/"),("Контакты","contacts.html")]
def head(title,cur):
    nav="".join(f'<a href="{u}"{" class=on" if n==cur else ""}{" target=_blank rel=noopener" if u.startswith("http") else ""}>{n}</a>' for n,u in MENU)
    return f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600&family=Oswald:wght@500;600&display=swap&subset=cyrillic" rel="stylesheet">
<link rel="stylesheet" href="style.css"></head><body><div class="grain" aria-hidden="true"></div>
<div class="top"><div class="wrap">
<a href="tel:+375336916916">Победы, 22 / <b>+375 (33) 691-69-16</b></a>
<a href="tel:+375298846451">Ржаная, 18 / <b>+375 (29) 884-64-51</b></a>
<a href="tel:+375297375799">Гаспадарчая, 22 / <b>+375 (29) 737-57-99</b></a>
<a href="tel:+375333539539">Для юрлиц / <b>+375 (33) 353-95-39</b></a>
<span class="sp"></span><span>Пн-сб, воскресенье выходной</span>
<div class="call"><span>Гродно / 3 пункта проката</span><a href="contacts.html"><b>Позвонить</b></a></div>
</div></div>
<header class="hdr"><div class="wrap"><a class="logo" href="index.html"><img src="assets/img/logo.png" alt="Мастер проката"></a>
<nav class="nav">{nav}</nav><button class="burger" aria-label="Меню" aria-expanded="false"><span></span><span></span><span></span></button></div></header>'''
FOOT=f'''<footer class="ftr"><div class="wrap"><div class="g" data-g>
<div data-r><a class="logo" href="index.html"><img src="assets/img/logo.png" alt="Мастер проката"></a><div class="cap">Сеть пунктов проката в Гродно</div><p class="big" style="margin:18px 0 24px">Инструмент<br>на сутки<br>и дольше</p><a class="pill acc" href="tel:+375298846451">+375 (29) 884-64-51</a></div>
<div data-r><h4>Разделы</h4><ul><li><a href="catalog.html">Каталог</a></li><li><a href="usloviya.html">Условия проката</a></li><li><a href="{LIVE}/akcii/">Акции</a></li><li><a href="about.html">О нас</a></li><li><a href="{LIVE}/news/">Новости</a></li><li><a href="{LIVE}/baza-znanii/">Важно знать</a></li><li><a href="contacts.html">Контакты</a></li></ul></div>
<div data-r><h4>Пункты</h4><ul><li>ул. Ржаная, 18<br><span class="cap">Девятовка</span></li><li>ул. Победы, 22<br><span class="cap">Вишневец</span></li><li>ул. Гаспадарчая, 22<br><span class="cap">Девятовка</span></li></ul></div>
<div data-r><h4>Связь</h4><ul><li><a href="mailto:office@master-prokata.by">office@master-prokata.by</a></li><li><a href="tel:+375333539539">+375 (33) 353-95-39 / юрлица</a></li><li><a href="https://www.instagram.com/masterprokata_grodno/" target="_blank" rel="noopener">Instagram</a></li></ul></div>
</div><div class="legal"><span>ЧУП «Мастер Проката» / УНП 591040896 / г. Гродно, ул. Коммунальная, 32А, каб. 19</span><span>Демо-версия редизайна</span></div></div></footer>
<script src="main.js"></script></body></html>'''
P=[("1","Перфоратор BULL BH 2602","15.00",None),("2","Перфоратор BULL BH 3201","23.00",None),("3","Перфоратор BULL BH 4002 SDS-MAX","35.00",None),("4","Перфоратор Makita HR 2470","15.00",None),("5","Перфоратор P.I.T. PBH26-C4","20.00",None),("6","Перфоратор P.I.T. РВН28","15.00",None),("7","Перфоратор WORTEX RH 2629","15.00",None),("8","Перфоратор WORTEX RH 2829","15.00",None),("9","Перфоратор WORTEX RH 2831","15.00",None),("10","Перфоратор аккумуляторный Wosai S9","20.00","25.00"),("11","Перфоратор ДИОЛД ПРЭВ-32-01","18.00",None),("12","Перфоратор ДИОЛД ПРЭГ-26-01","15.00",None)]
def pcard(i,n,p,old):
    href="item-bull-bh-3201.html" if i=="2" else LIVE+"/katalog-instrumenta/perforatoryi/"
    t='<span class="pill sm acc tag">Распродажа</span>' if old else ''
    o=f'<s>{old}</s>' if old else ''
    return f'<a class="card" data-r href="{href}">{t}<div class="ph prod"><img src="assets/p/{i}.jpg" alt="{n}" loading="lazy"></div><div class="bd"><div class="nm">{n}</div><div class="pr">{o}{p}<small>руб / сутки</small></div></div></a>'
POP=[("pylesos.jpg","Моющий пылесос Karcher SE 6.100","30","руб / сутки"),("benzobur.jpg","Бензобур Chempion AG252","32,5","руб / сутки"),("motoblok.jpg","Мотоблок Skiper","40","руб / сутки"),("generator.jpg","Бензогенератор Skiper LT 4000","16,5","руб / сутки"),("paroochist.jpg","Пароочиститель Karcher SC 2 Premium","30","руб / сутки"),("lesa.jpg","Строительные леса ЛРСП-300","2,5","руб / секция в сутки"),("lesa2.jpg","Вышки-тура","от 15","руб / сутки"),("hero.jpg","Перфораторы","от 13","руб / сутки")]
def popcard(img,n,p,u): return f'<a class="card" data-r href="catalog.html"><div class="ph"><img src="assets/img/{img}" alt="{n}" loading="lazy"></div><div class="bd"><div class="nm">{n}</div><div class="pr">{p}<small>{u}</small></div></div></a>'
def w(fn,s): open(fn,"w").write(s)

w("index.html",head("Мастер проката / прокат инструмента в Гродно","Главная")+f'''
<section class="hero"><img class="bg" src="assets/img/hero.jpg" alt="Сотрудник проката с перфоратором"><div class="wrap"><div class="col" data-g>
<div class="cap" data-r>Сеть пунктов проката / Гродно / с 2013 года</div>
<h1 class="grad" data-r>Прокат<br>в Гродно</h1>
<p data-r>Строительный и садовый инструмент на сутки и дольше. Перфоратор, леса, мотоблок, генератор: берёте на нужный срок и возвращаете в пункт.</p>
<div class="acts" data-r><a class="pill acc" href="catalog.html">Открыть каталог</a><a class="pill" href="tel:+375298846451">Позвонить на Ржаную</a></div></div></div>
</section>
<section class="sec tight"><div class="wrap"><div class="nums" data-g>
<div class="num" data-r><b>2013</b><span class="cap">работаем с этого года</span></div>
<div class="num" data-r><b>350<i>+</i></b><span class="cap">позиций инструмента</span></div>
<div class="num" data-r><b>150</b><span class="cap">организаций среди клиентов</span></div>
<div class="num" data-r><b>1 <i>сутки</i></b><span class="cap">минимальный срок аренды</span></div></div></div></section>
<section class="sec"><div class="wrap asym" data-b><div class="head" data-g><div class="cap" data-r>Популярное</div><h2 class="grad" data-r>Что чаще<br>всего берут</h2><p class="lead" data-r>Цены за сутки. Чем дольше срок, тем дешевле обходится каждый день: точный тариф подскажет менеджер.</p><div class="acts" data-r style="margin-top:28px"><a class="pill" href="catalog.html">Весь каталог</a></div></div>
<div class="grid top4" style="grid-template-columns:repeat(2,1fr)" data-g>{"".join(popcard(*x) for x in POP[:4])}</div></div>
<div class="wrap" style="margin-top:16px"><div class="grid" data-g>{"".join(popcard(*x) for x in POP[4:])}</div></div></section>
<section class="sec"><div class="wrap"><div class="asym" style="margin-bottom:60px" data-g><div><div class="cap" data-r>Как это работает</div><h2 class="grad" data-r style="margin-top:18px">Шесть шагов<br>от звонка до возврата</h2></div><p class="lead" data-r style="align-self:end">Возьмите с собой паспорт гражданина РБ или вид на жительство. Водительское удостоверение для договора не подходит.</p></div>
<div class="steps" data-g>
<div class="step" data-r><b>01</b><h3>Звонок</h3><p>Расскажите менеджеру, какую работу нужно сделать. Он подскажет, какой инструмент подойдёт.</p></div>
<div class="step" data-r><b>02</b><h3>Бронь</h3><p>Закрепите инструмент на удобную дату и время. Бронь действует после подтверждения менеджером.</p></div>
<div class="step" data-r><b>03</b><h3>Проверка</h3><p>При выдаче менеджер проверяет исправность, комплектацию и внешний вид вместе с вами.</p></div>
<div class="step" data-r><b>04</b><h3>Инструктаж</h3><p>Если берёте впервые, расскажем, как работать безопасно и не перегрузить технику.</p></div>
<div class="step" data-r><b>05</b><h3>Договор и оплата</h3><p>Оформляем договор на месте и оплачиваете весь срок аренды сразу.</p></div>
<div class="step" data-r><b>06</b><h3>Возврат</h3><p>Возвращаете в тот же час, в который забрали. Нужно дольше? Позвоните до конца срока.</p></div></div></div></section>
<section class="sec"><div class="wrap split" data-b><div class="ph" data-r><img src="assets/img/lesa.jpg" alt="Строительные леса у дома" loading="lazy"></div>
<div class="tx" data-g><div class="cap" data-r>Для юридических лиц</div><h2 class="grad" data-r>Договор,<br>документы,<br>отчётность</h2><p class="lead" data-r>Работаем с организациями по отдельному номеру. Стоимость аренды для юрлиц на 10% выше обычного прайса, новые организации вносят 100% предоплату за весь срок.</p>
<div class="rows" data-r><div>Телефон для юрлиц<b>+375 (33) 353-95-39</b></div><div>Почта<b>office@master-prokata.by</b></div></div>
<div data-r><a class="pill" href="usloviya.html">Условия проката</a></div></div></div></section>
<section class="sec"><div class="wrap"><div class="asym" style="margin-bottom:60px" data-g><div><div class="cap" data-r>Пункты проката</div><h2 class="grad" data-r style="margin-top:18px">Три адреса<br>в Гродно</h2></div><p class="lead" data-r style="align-self:end">Работаем без обеда, воскресенье выходной. Наличие конкретной модели лучше уточнить по телефону пункта.</p></div>
<div class="points" data-g>
<div class="point" data-r><img src="assets/img/generator.jpg" alt="" loading="lazy"><div class="glass"><span class="cap">Девятовка</span><h3>ул. Ржаная, 18</h3><a class="tel" href="tel:+375298846451">+375 (29) 884-64-51</a><span class="cap">пн-пт 8:30-18:00 / сб 9:00-18:00</span></div></div>
<div class="point" data-r><img src="assets/img/motoblok.jpg" alt="" loading="lazy"><div class="glass"><span class="cap">Вишневец</span><h3>ул. Победы, 22</h3><a class="tel" href="tel:+375336916916">+375 (33) 691-69-16</a><span class="cap">пн-пт 8:00-18:00 / сб 9:00-16:00</span></div></div>
<div class="point" data-r><img src="assets/img/lesa2.jpg" alt="" loading="lazy"><div class="glass"><span class="cap">Девятовка</span><h3>ул. Гаспадарчая, 22</h3><a class="tel" href="tel:+375297375799">+375 (29) 737-57-99</a><span class="cap">пн-пт 8:30-18:00 / сб 9:00-18:00</span></div></div></div></div></section>
<section class="sec"><div class="wrap split" style="grid-template-columns:39fr 61fr" data-b><div class="tx" data-g style="justify-content:center"><div class="cap" data-r>Дисконтная программа</div><h2 class="grad" data-r>Скидка<br>от 5 до 30%</h2><p class="lead" data-r>Карта постоянного клиента даёт −5% уже с первой аренды. Подробные условия и действующие акции на странице акций.</p><div data-r><a class="pill" href="{LIVE}/akcii/" target="_blank" rel="noopener">Акции и скидки</a></div></div>
<div class="ph" data-r><img src="assets/img/vip.jpg" alt="VIP-карта Мастера проката" loading="lazy"></div></div></section>
'''+FOOT)

AZ="Аккумуляторный инструмент/Аэраторы/Бензобуры (мотобуры)/Бензогенераторы/Бензопилы/Бензорезы/Бетоносмесители/Болгарки (УШМ)/Виброплиты (трамбовки)/Высечные ножницы (по металлу)/Вышки-тура/Газонокосилки (триммеры)/Гидравлические подъемники/Глубинные вибраторы/Гравировальные машинки/Детекторы проводки/Дрели/Клеевые пистолеты/Компрессоры/Краскораспылители/Лазерные дальномеры/Лазерные нивелиры/Леса строительные/Лестницы и стремянки/Лобзики/Миксер-дрели/Мойки высокого давления/Мотоблоки/Мотопомпы/Моющие пылесосы/Насосы/Оптические нивелиры/Оснастка/Отбойные молотки/Паяльник для полипропилена/Перфораторы/Плиткорезы/Подмости/Полировальные машины/Пресс-клещи/Рохли/Рубанок/Сабельные пилы (ножовки)/Садовые валики/Садовые пылесосы/Сварочное оборудование/Строительные пылесосы/Тачки строительные/Тепловые пушки/Торцовочные пилы/Удлинители/Ультразвуковые ванны/Фены промышленные/Фрезеры/Хоппер-ковши/Циркулярные пилы/Шлифмашины/Штроборезы (бороздоделы)".split("/")
WORK="Бетонные работы/Благоустройство участка/Демонтажные работы/Дорожные работы/Измерительные работы/Кровельные работы/Монтажные работы/Отделочные работы/Покрасочные работы/Работы на высоте/Работы с камнем и плиткой/Облицовка плиткой/Работы с деревом/Работы с металлом/Ремонт авто/Ремонт в квартире/Сантехнические работы/Сварочные работы/Уборочные работы/Установка заборов/Уход за газоном/Фасадные работы/Шлифовка пола и паркета/Штукатурные работы/Электромонтажные работы/Отопительное оборудование".split("/")
az="".join(f'<a data-r href="{"perforatory.html" if n=="Перфораторы" else LIVE+"/catalog/"}">{n}</a>' for n in AZ)
wk="".join(f'<a class="pill sm" data-r href="{LIVE}/catalog/">{n}</a>' for n in WORK)
w("catalog.html",head("Каталог / Мастер проката","Каталог")+f'''
<section class="phead"><div class="wrap" data-g><div class="crumbs" data-r><a href="index.html">Главная</a> / Каталог</div><h1 class="grad" data-r>Каталог</h1><p class="lead" data-r>Ищите по задаче, если не знаете, как называется нужный инструмент. Или по названию, если знаете.</p></div></section>
<section class="sec tight"><div class="wrap asym"><div class="head" data-g><div class="cap" data-r>По типу работ</div><h2 class="grad" data-r style="font-size:44px">Что нужно<br>сделать?</h2></div><div class="pills" data-g>{wk}</div></div></section>
<section class="sec"><div class="wrap asym"><div class="head" data-g><div class="cap" data-r>По названию / {len(AZ)} групп</div><h2 class="grad" data-r style="font-size:44px">От А до Ш</h2></div><div class="az" data-g>{az}</div></div></section>'''+FOOT)

w("perforatory.html",head("Перфораторы / Мастер проката","Каталог")+f'''
<section class="phead"><div class="wrap asym" data-b><div data-g><div class="crumbs" data-r><a href="index.html">Главная</a> / <a href="catalog.html">Каталог</a> / Перфораторы</div><h1 class="grad" data-r style="font-size:clamp(48px,6vw,88px)">Перфораторы</h1></div>
<div data-g style="align-self:end"><p class="lead" data-r>Для сквозных отверстий в стенах, глухих под анкеры, штробления под проводку и трубы, демонтажа старой штукатурки. Модели от одного до трёх режимов: сверление, сверление с ударом, долбление.</p><div class="pills" data-r style="margin-top:20px"><span class="pill sm">Бетонные работы</span><span class="pill sm">Демонтаж</span><span class="pill sm">Ремонт в квартире</span></div></div></div></section>
<section class="sec tight" style="padding-top:0"><div class="wrap"><div class="cap" style="margin-bottom:24px">12 моделей с ценой / цена за сутки</div><div class="grid" data-g>{"".join(pcard(*x) for x in P)}</div></div></section>'''+FOOT)

SPEC=[("Мощность","1500 Вт"),("Энергия удара","7 Дж"),("Патрон","SDS-plus"),("Режимов","4"),("Холостой ход","950 об/мин"),("Частота ударов","4500 уд/мин"),("Бетон","до 32 мм"),("Сталь","до 13 мм"),("Дерево","до 40 мм"),("Кабель","3 м"),("Вес","5 кг"),("Упаковка","кейс")]
spec="".join(f'<div data-r><span>{a}</span><b>{b}</b></div>' for a,b in SPEC)
w("item-bull-bh-3201.html",head("Перфоратор BULL BH 3201 / Мастер проката","Каталог")+f'''
<section class="phead"><div class="wrap"><div class="crumbs"><a href="index.html">Главная</a> / <a href="catalog.html">Каталог</a> / <a href="perforatory.html">Перфораторы</a> / BULL BH 3201</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap item" data-b><div class="ph" data-r><img src="assets/p/2.jpg" alt="Перфоратор BULL BH 3201"></div>
<div data-g><div class="cap" data-r>Профессиональный / сеть 220 В</div><h1 class="grad" data-r>Перфоратор<br>BULL BH 3201</h1>
<div class="price" data-r>23.00<small>руб / сутки</small></div>
<p class="lead" data-r style="margin:24px 0">Мощный двигатель 1500 Вт и удар 7 Дж: сверление, сверление с ударом и режим отбойного молотка. Vario-lock фиксирует зубило в 12 положениях, гашение вибрации снимает часть нагрузки с рук.</p>
<div class="acts" data-r style="display:flex;gap:12px;flex-wrap:wrap"><a class="pill acc" href="tel:+375298846451">Забронировать по телефону</a><a class="pill" href="tel:+375333539539">Для юрлиц</a></div>
<p class="cap" data-r style="margin-top:20px">Актуальную цену на день обращения уточняйте у менеджера</p></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap asym"><div class="head" data-g><div class="cap" data-r>Характеристики</div><h2 class="grad" data-r style="font-size:44px">Что внутри</h2></div><div class="spec" data-g>{spec}</div></div></section>'''+FOOT)

w("usloviya.html",head("Условия проката / Мастер проката","Условия проката")+'''
<section class="phead"><div class="wrap" data-g><div class="crumbs" data-r><a href="index.html">Главная</a> / Условия проката</div><h1 class="grad" data-r>Условия<br>проката</h1></div></section>
<section class="sec tight"><div class="wrap"><div class="nums" data-g><div class="num" data-r><b>1 <i>сутки</i></b><span class="cap">минимальный срок аренды</span></div><div class="num" data-r><b>48 <i>ч</i></b><span class="cap">минимум для вышек-тура</span></div><div class="num" data-r><b>5 <i>суток</i></b><span class="cap">минимум для строительных лесов</span></div><div class="num" data-r><b>+10<i>%</i></b><span class="cap">к прайсу для юрлиц</span></div></div></div></section>
<section class="sec"><div class="wrap asym"><div class="head" data-g><div class="cap" data-r>Что взять с собой</div><h2 class="grad" data-r style="font-size:44px">Паспорт</h2></div><div class="prose" data-g>
<p data-r>Для договора нужен паспорт гражданина РБ или вид на жительство в РБ. Водительское удостоверение не подходит. Договор и расчёт оформляются только в вашем присутствии, в момент получения инструмента.</p>
<p data-r>При выдаче менеджер проверяет технику на исправность, комплектацию и внешний вид и рассказывает правила работы и технику безопасности.</p>
<h3 data-r>Стоимость</h3><p data-r>Тариф зависит от срока: чем дольше аренда, тем дешевле сутки. Даже если вернёте инструмент через час, оплачиваются полные сутки. Новые организации вносят 100% предоплату за весь срок.</p>
<div class="note" data-r>Внесённая арендная плата не возвращается, в том числе при форс-мажоре: отключили свет, перенесли работы или инструмент не понадобился.</div>
<h3 data-r>Расчётный час</h3><p data-r>Сутки считаются с часа выдачи: взяли в 12:00, вернуть нужно в 12:00 последнего дня аренды. О задержке обязательно сообщите менеджеру.</p>
<div class="rows" data-r><div>Меньше 1 часа<b>без доплаты</b></div><div>От 1 до 3 часов<b>+30% суток</b></div><div>От 3 до 6 часов<b>+50% суток</b></div><div>Больше 6 часов<b>+100% суток</b></div></div>
<h3 data-r>Продление</h3><p data-r>Позвоните по номеру +375 (29) 884-64-51 до окончания оплаченного срока, назовите фамилию и примерную дату возврата. Оплатить продление нужно в пункте проката в течение недели.</p>
<p data-r>Полный текст условий, включая возврат инструмента, на <a href="https://master-prokata.by/yslovia-prokata/" style="color:var(--acc)">действующем сайте</a>.</p></div></div></section>'''+FOOT)

w("about.html",head("О нас / Мастер проката","О нас")+'''
<section class="phead"><div class="wrap" data-g><div class="crumbs" data-r><a href="index.html">Главная</a> / О нас</div><h1 class="grad" data-r>О нас</h1></div></section>
<section class="sec tight"><div class="wrap split" data-b><div class="ph" data-r><img src="assets/img/hero.jpg" alt="Работа с перфоратором"></div><div class="tx" data-g>
<div class="cap" data-r>Дмитрий Вильк / директор сети</div>
<p class="lead" data-r >«Мастер проката» в Гродно работает без обеда, с раннего утра. Цены на прокат я отслеживаю лично, чтобы предложение оставалось выгодным для клиентов. С организациями у нас налажен документооборот и своевременная отчётность.</p>
<p class="lead" data-r>Менеджеры помогут подобрать инструмент под задачу, покажут, как им пользоваться, и подскажут, на чём можно сэкономить.</p>
<div class="nums" data-g style="grid-template-columns:1fr 1fr"><div class="num" data-r><b>2013</b><span class="cap">год основания</span></div><div class="num" data-r><b>350<i>+</i></b><span class="cap">позиций</span></div><div class="num" data-r><b>150</b><span class="cap">организаций</span></div><div class="num" data-r><b>3</b><span class="cap">пункта проката</span></div></div></div></div></section>'''+FOOT)

w("contacts.html",head("Контакты / Мастер проката","Контакты")+'''
<section class="phead"><div class="wrap" data-g><div class="crumbs" data-r><a href="index.html">Главная</a> / Контакты</div><h1 class="grad" data-r>Контакты</h1><p class="lead" data-r>У каждого пункта свой телефон. Звоните в тот, куда удобнее приехать: там проверят, есть ли нужный инструмент.</p></div></section>
<section class="sec tight" style="padding-top:0"><div class="wrap"><div class="points" data-g>
<div class="point" data-r><img src="assets/img/generator.jpg" alt=""><div class="glass"><span class="cap">Девятовка</span><h3>ул. Ржаная, 18</h3><a class="tel" href="tel:+375298846451">+375 (29) 884-64-51</a><span class="cap">пн-пт 8:30-18:00 / сб 9:00-18:00 / вс выходной</span></div></div>
<div class="point" data-r><img src="assets/img/motoblok.jpg" alt=""><div class="glass"><span class="cap">Вишневец</span><h3>ул. Победы, 22</h3><a class="tel" href="tel:+375336916916">+375 (33) 691-69-16</a><span class="cap">пн-пт 8:00-18:00 / сб 9:00-16:00 / вс выходной</span></div></div>
<div class="point" data-r><img src="assets/img/lesa2.jpg" alt=""><div class="glass"><span class="cap">Девятовка</span><h3>ул. Гаспадарчая, 22</h3><a class="tel" href="tel:+375297375799">+375 (29) 737-57-99</a><span class="cap">пн-пт 8:30-18:00 / сб 9:00-18:00 / вс выходной</span></div></div></div></div></section>
<section class="sec"><div class="wrap asym"><div class="head" data-g><div class="cap" data-r>Юридическим лицам</div><h2 class="grad" data-r style="font-size:44px">Реквизиты</h2><a class="pill acc" data-r style="margin-top:24px" href="tel:+375333539539">+375 (33) 353-95-39</a></div>
<div class="rows" data-g><div data-r><span>Организация</span><b>ЧУП «Мастер Проката»</b></div><div data-r><span>УНП</span><b>591040896</b></div><div data-r><span>Юридический адрес</span><b>230029, г. Гродно, ул. Коммунальная, 32А, каб. 19</b></div><div data-r><span>Почтовый адрес</span><b>230003, г. Гродно, а/я 9</b></div><div data-r><span>Р/с</span><b>BY45 ALFA 3012 2C59 5700 1027 0000</b></div><div data-r><span>Банк</span><b>ЗАО «Альфа-Банк», БИК ALFABY2X</b></div><div data-r><span>E-mail</span><b><a href="mailto:office@master-prokata.by">office@master-prokata.by</a></b></div></div></div></section>'''+FOOT)
