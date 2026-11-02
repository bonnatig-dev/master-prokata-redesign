# -*- coding: utf-8 -*-
exec(open('data.py').read())
def head(title,cur):
    nav="".join(f'<a href="{u}"{" class=on" if n==cur else ""}{" target=_blank rel=noopener" if u.startswith("http") else ""}>{n}</a>' for n,u in MENU)
    return f'''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600&family=Oswald:wght@300;400;500;600&display=swap&subset=cyrillic" rel="stylesheet">
<link rel="stylesheet" href="style.css"></head><body><div class="grain" aria-hidden="true"></div>
<div class="top"><div class="wrap">
<a href="tel:+375336916916">Победы, 22 / <b>+375 (33) 691-69-16</b></a>
<a href="tel:+375298846451">Ржаная, 18 / <b>+375 (29) 884-64-51</b></a>
<a href="tel:+375297375799">Гаспадарчая, 22 / <b>+375 (29) 737-57-99</b></a>
<a href="tel:+375333539539">Для юрлиц / <b>+375 (33) 353-95-39</b></a>
<span class="sp"></span><span>Пн-сб / воскресенье выходной</span>
<div class="call"><span>Гродно / 3 пункта проката</span><a href="contacts.html"><b>Позвонить</b></a></div></div></div>
<header class="hdr"><div class="wrap"><a class="logo" href="index.html"><img src="assets/img/logo.png" alt="Мастер проката"></a>
<nav class="nav">{nav}</nav><a class="btn red" href="catalog.html">Каталог</a><button class="burger" aria-label="Меню" aria-expanded="false"><span></span><span></span><span></span></button></div></header>'''
FOOT=f'''<footer class="ftr"><div class="wrap"><div class="g" data-g>
<div class="about" data-r><img src="assets/img/logo.png" alt="Мастер проката"><p>Прокат строительного и садового инструмента в Гродно. Три пункта: Девятовка и Вишневец.</p></div>
<div data-r><h4>Разделы</h4><ul><li><a href="catalog.html">Каталог</a></li><li><a href="usloviya.html">Условия проката</a></li><li><a href="{LIVE}/akcii/">Акции</a></li><li><a href="about.html">О нас</a></li><li><a href="{LIVE}/news/">Новости</a></li><li><a href="{LIVE}/baza-znanii/">Важно знать</a></li><li><a href="contacts.html">Контакты</a></li></ul></div>
<div data-r><h4>Пункты</h4><ul><li>ул. Ржаная, 18</li><li>ул. Победы, 22</li><li>ул. Гаспадарчая, 22</li></ul></div>
<div data-r><h4>Связь</h4><ul><li><a href="tel:+375298846451">+375 (29) 884-64-51</a></li><li><a href="tel:+375333539539">+375 (33) 353-95-39 / юрлица</a></li><li><a href="mailto:office@master-prokata.by">office@master-prokata.by</a></li><li><a href="https://www.instagram.com/masterprokata_grodno/" target="_blank" rel="noopener">Instagram</a></li></ul></div></div>
<div class="word" aria-hidden="true"><div class="wt"><span class="wg"><span class="wi">Мастер <em>проката</em><i>/</i></span><span class="wi">Мастер <em>проката</em><i>/</i></span><span class="wi">Мастер <em>проката</em><i>/</i></span><span class="wi">Мастер <em>проката</em><i>/</i></span></span><span class="wg"><span class="wi">Мастер <em>проката</em><i>/</i></span><span class="wi">Мастер <em>проката</em><i>/</i></span><span class="wi">Мастер <em>проката</em><i>/</i></span><span class="wi">Мастер <em>проката</em><i>/</i></span></span></div></div>
<div class="legal"><span>ЧУП «Мастер Проката» / УНП 591040896 / г. Гродно, ул. Коммунальная, 32А, каб. 19</span><span>Демо-версия редизайна</span></div></div></footer>
<script src="main.js"></script></body></html>'''
def w(fn,s): open(fn,"w").write(s)
def shead(n,h,extra=""): return f'<div class="shead" data-g><div class="num-l" data-r>({n})</div><div><h2 data-r>{h}</h2>{extra}</div></div>'
CONTACTS=f'''<section class="sec dark"><div class="wrap" data-g><div class="meta" data-r>Звоните в пункт, куда удобнее приехать / пн-сб</div>
<a class="bigtel" data-r href="tel:+375298846451">+375 29 <em>884-64-51</em></a>
<div class="ccols"><div data-g><h3 data-r style="font-size:28px;margin-bottom:10px">Проверим наличие и забронируем</h3><p class="mute" data-r style="margin-bottom:26px">Назовите инструмент и дату. Бронь действует после подтверждения менеджером.</p>
<a class="cbtn red" data-r href="tel:+375298846451"><span><small>Ржаная, 18 / Девятовка</small><b>+375 (29) 884-64-51</b></span></a>
<a class="cbtn" data-r href="tel:+375336916916"><span><small>Победы, 22 / Вишневец</small><b>+375 (33) 691-69-16</b></span></a>
<a class="cbtn" data-r href="tel:+375297375799"><span><small>Гаспадарчая, 22 / Девятовка</small><b>+375 (29) 737-57-99</b></span></a>
<a class="cbtn" data-r href="tel:+375333539539"><span><small>Для юридических лиц</small><b>+375 (33) 353-95-39</b></span></a></div>
<div class="kv" data-g><div data-r><span>Ржаная, 18</span><b>пн-пт 8:30-18:00 / сб 9:00-18:00</b></div><div data-r><span>Победы, 22</span><b>пн-пт 8:00-18:00 / сб 9:00-16:00</b></div><div data-r><span>Гаспадарчая, 22</span><b>пн-пт 8:30-18:00 / сб 9:00-18:00</b></div><div data-r><span>Воскресенье</span><b>выходной</b></div><div data-r><span>Почта</span><b><a href="mailto:office@master-prokata.by">office@master-prokata.by</a></b></div></div></div></div></section>'''
ROWS=[("Перфораторы","BULL, Makita, P.I.T., WORTEX, ДИОЛД: 23 модели, от одного до трёх режимов","от 13 руб.","perforatory.html"),
("Строительные леса","ЛРСП-300, минимальный срок аренды 5 суток","2,5 руб.","catalog.html"),
("Вышки-тура","Для работ на высоте, минимальный срок 48 часов","от 15 руб.","catalog.html"),
("Мотоблоки","Skiper для участка и огорода","40 руб.","catalog.html"),
("Бензогенераторы","Skiper LT 4000, когда на участке нет света","16,5 руб.","catalog.html"),
("Моющие пылесосы","Karcher SE 6.100 для ковров и мебели","30 руб.","catalog.html")]
rows="".join(f'<a class="row" data-r href="{u}"><span class="num-l" style="color:var(--muteD)">{i+1:02d}</span><span class="t">{t}</span><span class="d">{d}</span><span class="p"><small>за сутки</small><b>{p}</b></span><span class="circle">→</span></a>' for i,(t,d,p,u) in enumerate(ROWS))
def trow(i,n,p,old):
    o=f"<s>{old}</s>" if old else ""
    l="item-bull-bh-3201.html" if i=="2" else "tel:+375298846451"
    return f'<div class="r" data-r><img src="assets/p/{i}.jpg" alt="{n}" loading="lazy"><span class="n">{n}</span><span class="pr">{o}{p}<small> руб.</small></span><a class="lnk" href="{l}">{"Подробнее" if i=="2" else "Забронировать"}</a></div>'
TBL='<div class="tbl" data-g><div class="h meta"><span></span><span>Модель</span><span style="text-align:right">Сутки</span><span></span></div>'+"".join(trow(*x) for x in P)+'</div>'
STEPS=[("Позвоните","Расскажите, какую работу нужно сделать. Менеджер подскажет инструмент и проверит наличие."),("Забронируйте","Выберите дату и время. Бронь действует после подтверждения менеджером."),("Приезжайте с паспортом","Паспорт РБ или вид на жительство. Водительские права для договора не подходят."),("Проверка и инструктаж","Вместе проверим исправность и комплектацию, расскажем про технику безопасности."),("Договор и оплата","Оформляем на месте и оплачиваете весь срок аренды сразу."),("Возврат","Привозите в тот же час, в который забрали. Нужно дольше? Позвоните до конца срока.")]
steps="".join(f'<div class="step" data-r><b>{i+1:02d}</b><h3>{t}</h3><p>{d}</p></div>' for i,(t,d) in enumerate(STEPS))
FAQ=[("Какие документы нужны?","Паспорт гражданина РБ или вид на жительство в РБ. Водительское удостоверение не подходит: по нему нельзя оформить договор."),
("Какой минимальный срок аренды?","Одни сутки. Для вышек-тура и некоторого оборудования 48 часов, для строительных лесов 5 суток. Даже если вернёте инструмент через час, оплачиваются полные сутки."),
("Что будет, если я задержусь с возвратом?","До 1 часа без доплаты. От 1 до 3 часов +30% суточной стоимости, от 3 до 6 часов +50%, больше 6 часов +100%. О задержке обязательно сообщите менеджеру."),
("Как продлить аренду?","Позвоните по номеру +375 (29) 884-64-51 до окончания оплаченного срока, назовите фамилию и примерную дату возврата. Оплатить продление нужно в пункте проката в течение недели."),
("Можно вернуть деньги, если инструмент не понадобился?","Нет. Внесённая арендная плата не возвращается, даже при форс-мажоре. Планируйте работу заранее."),
("Работаете с организациями?","Да. Для юрлиц стоимость на 10% выше обычного прайса, новые организации вносят 100% предоплату за весь срок. Телефон для юрлиц +375 (33) 353-95-39.")]
def faq(items): return '<div class="faq" data-g>'+"".join(f'<details data-r{" open" if i==0 else ""}><summary><span class="num-l">{i+1:02d}</span>{q}</summary><div class="a">{a}</div></details>' for i,(q,a) in enumerate(items))+'</div>'

w("index.html",head("Мастер проката / прокат инструмента в Гродно","Главная")+f'''
<section class="hero"><img class="bg" src="assets/img/generator.jpg" alt="Бензогенератор Skiper на газоне у дома">
<div class="price" data-g><div class="meta" data-r style="color:var(--onD)">Строительные леса ЛРСП-300</div><b data-r>2,5<small> руб.</small></b><span data-r>за секцию в сутки</span></div>
<div class="wrap"><div class="col" data-g><div class="meta" data-r style="color:var(--muteD);margin-bottom:26px">Сеть пунктов проката / с 2013 года</div>
<h1 data-r><span>Прокат</span><span><em>в Гродно</em></span></h1></div>
<div class="base" data-g><p data-r>Строительный и садовый инструмент на сутки и дольше. Перфоратор, леса, мотоблок, генератор: берёте на нужный срок и возвращаете в пункт.</p>
<div class="acts" data-r><a class="btn red" href="catalog.html">Каталог и цены</a><a class="btn ghost" href="tel:+375298846451">Позвонить</a></div></div>
<div class="metas meta" data-r><span>Ржаная, 18 / Победы, 22 / Гаспадарчая, 22</span><span>Пн-сб / воскресенье выходной</span></div></div></section>
<section class="sec"><div class="wrap"><div class="shead" data-g><div class="num-l" data-r>(01) О прокате</div><p class="state" data-r>Не нужно покупать перфоратор ради трёх отверстий. Берёте инструмент на сутки, <em>работаете</em>, возвращаете. Обслуживание, щётки и масло <mark>остаются на нас.</mark></p></div>
<div class="stats" data-g><div data-r><b>2013</b><span class="mute">год, с которого работаем</span></div><div data-r><b>350+</b><span class="mute">позиций инструмента</span></div><div data-r><b>150</b><span class="mute">организаций среди клиентов</span></div><div data-r><b>3</b><span class="mute">пункта проката в Гродно</span></div></div></div></section>
<section class="sec dark"><div class="wrap">{shead("02","Что чаще <em>берут</em>")}<div class="rows" data-g>{rows}</div></div></section>
<section class="sec"><div class="wrap split"><div class="side" data-g><div class="meta" data-r>(03) Прайс</div><h2 data-r>Перфораторы <em>на сутки</em></h2><p class="mute" data-r style="font-size:16px">Чем дольше срок аренды, тем дешевле обходятся сутки. Цену на день обращения уточняйте у менеджера.</p>
<div class="box" data-r><h3>Работаете от организации?</h3><p>Договор, документооборот, отчётность. Стоимость для юрлиц +10% к прайсу.</p><a class="btn red" href="tel:+375333539539">+375 (33) 353-95-39</a></div></div>{TBL}</div></section>
<section class="sec" style="background:#fff"><div class="wrap">{shead("04","От звонка <em>до возврата</em>")}<div class="steps" data-g>{steps}</div></div></section>
<section class="sec dark"><div class="wrap">{shead("05","Наш инструмент. <em>Наши фото.</em>")}<div class="gal" data-g><img data-r src="assets/img/lesa.jpg" alt="Строительные леса" loading="lazy"><img data-r src="assets/img/motoblok.jpg" alt="Мотоблок Skiper" loading="lazy"><img data-r src="assets/img/benzobur.jpg" alt="Бензобур" loading="lazy"><img data-r src="assets/img/pylesos.jpg" alt="Моющий пылесос" loading="lazy"></div></div></section>
<section class="sec"><div class="wrap">{shead("06","Частые <em>вопросы</em>")}{faq(FAQ)}</div></section>
<section class="sec s" style="padding-top:0"><div class="wrap">{shead("07","Прокат инструмента <em>в Гродно</em>")}<div class="cols mute" data-g><div data-r><p>«Мастер проката» работает в Гродно с 2013 года. В наличии больше 350 позиций: перфораторы и болгарки, строительные леса и вышки-тура, бетономешалки, виброплиты, генераторы, мотоблоки, мойки, пылесосы и садовая техника.</p><p>Каталог можно смотреть по названию или по типу работ: бетонные, кровельные, фасадные, уход за газоном и ещё два десятка направлений.</p></div><div data-r><p>Пункты проката на Ржаной, 18 и Гаспадарчей, 22 (Девятовка) и на Победы, 22 (Вишневец). Работаем без обеда, воскресенье выходной.</p><p>Постоянным клиентам действует дисконтная программа со скидкой от 5 до 30%. Условия на странице <a href="{LIVE}/akcii/" style="color:var(--ink);border-bottom:1px solid">акций</a>.</p></div></div></div></section>
'''+CONTACTS+FOOT)

def phead(crumb,h,p=""): return f'<section class="phead"><div class="wrap" data-g><div class="crumbs" data-r><a href="index.html">Главная</a> / {crumb}</div><h1 data-r>{h}</h1>{f"<p data-r>{p}</p>" if p else ""}</div></section>'
chips="".join(f'<a class="chip" data-r href="{LIVE}/catalog/">{n}</a>' for n in WORK)
az="".join(f'<a data-r href="{"perforatory.html" if n=="Перфораторы" else LIVE+"/catalog/"}"><span>{i+1:02d}</span>{n}</a>' for i,n in enumerate(AZ))
w("catalog.html",head("Каталог / Мастер проката","Каталог")+phead("Каталог","Каталог <em>инструмента</em>","Ищите по задаче, если не знаете, как называется нужный инструмент. Или по названию, если знаете.")+f'''
<section class="sec s"><div class="wrap">{shead("01","По типу <em>работ</em>")}<div class="chips" data-g>{chips}</div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap">{shead("02",f"По названию / <em>{len(AZ)} групп</em>")}<div class="az" data-g>{az}</div></div></section>'''+CONTACTS+FOOT)

w("perforatory.html",head("Перфораторы / Мастер проката","Каталог")+phead('<a href="catalog.html">Каталог</a> / Перфораторы',"Перфораторы <em>напрокат</em>","Для сквозных отверстий в стенах, глухих под анкеры, штробления под проводку и трубы, демонтажа старой штукатурки.")+f'''
<section class="sec"><div class="wrap split"><div class="side" data-g><div class="meta" data-r>12 моделей с ценой / за сутки</div><h2 data-r>Какой <em>выбрать?</em></h2><div class="kv l" data-g style="margin-top:20px"><div data-r><span>Однорежимный</span><b>только сверление</b></div><div data-r><span>Двухрежимный</span><b>сверление с ударом</b></div><div data-r><span>Трёхрежимный</span><b>сверление, удар, долбление</b></div></div>
<div class="box" data-r><h3>Не знаете, какой нужен?</h3><p>Расскажите, что сверлить и в каком материале. Менеджер подберёт модель.</p><a class="btn red" href="tel:+375298846451">Позвонить</a></div></div>{TBL}</div></section>'''+CONTACTS+FOOT)

spec="".join(f'<div data-r><span>{a}</span><b>{b}</b></div>' for a,b in SPEC)
w("item-bull-bh-3201.html",head("Перфоратор BULL BH 3201 / Мастер проката","Каталог")+phead('<a href="catalog.html">Каталог</a> / <a href="perforatory.html">Перфораторы</a> / BULL BH 3201',"Перфоратор <em>BULL BH 3201</em>")+f'''
<section class="sec"><div class="wrap item"><div class="ph" data-r><img src="assets/p/2.jpg" alt="Перфоратор BULL BH 3201"></div>
<div data-g><div class="meta" data-r>Профессиональный / сеть 220 В</div><div class="bignum" data-r style="font-size:96px;line-height:1;color:var(--ink);margin:18px 0 6px">23<span style="font-size:30px"> руб.</span></div><div class="mute" data-r>за сутки / цену на день обращения уточняйте у менеджера</div>
<p data-r style="font-size:16px;margin:28px 0">Двигатель 1500 Вт и удар 7 Дж: сверление, сверление с ударом и режим отбойного молотка. Vario-lock фиксирует зубило в 12 положениях, гашение вибрации снимает часть нагрузки с рук.</p>
<div data-r style="display:flex;gap:12px;flex-wrap:wrap"><a class="btn red" href="tel:+375298846451">Забронировать по телефону</a><a class="btn ghost" href="tel:+375333539539">Для юрлиц</a></div>
<div class="kv l" data-g style="margin-top:44px">{spec}</div></div></div></section>'''+CONTACTS+FOOT)

w("usloviya.html",head("Условия проката / Мастер проката","Условия проката")+phead("Условия проката","Условия <em>проката</em>","Коротко о документах, сроках и деньгах. Полный текст на действующем сайте.")+f'''
<section class="sec s"><div class="wrap"><div class="stats" data-g style="margin-top:0"><div data-r><b>1 сутки</b><span class="mute">минимальный срок аренды</span></div><div data-r><b>48 ч</b><span class="mute">минимум для вышек-тура</span></div><div data-r><b>5 суток</b><span class="mute">минимум для строительных лесов</span></div><div data-r><b>+10%</b><span class="mute">к прайсу для юрлиц</span></div></div></div></section>
<section class="sec" style="padding-top:0"><div class="wrap">{shead("01","Ответы <em>по пунктам</em>")}{faq(FAQ)}
<div class="note" data-r style="margin-top:40px">Сутки считаются с часа выдачи: взяли в 12:00, вернуть нужно в 12:00 последнего дня аренды. <a href="{LIVE}/yslovia-prokata/" style="border-bottom:1px solid">Полный текст условий</a></div></div></section>'''+CONTACTS+FOOT)

w("about.html",head("О нас / Мастер проката","О нас")+phead("О нас","О <em>нас</em>")+f'''
<section class="sec"><div class="wrap"><div class="shead" data-g><div class="num-l" data-r>(01) Дмитрий Вильк, директор</div><p class="state" data-r>«Цены на прокат я отслеживаю <em>лично</em>, чтобы предложение оставалось выгодным. Работаем без обеда, с раннего утра, а с организациями у нас <mark>налажен документооборот.</mark>»</p></div>
<div class="stats" data-g><div data-r><b>2013</b><span class="mute">год основания</span></div><div data-r><b>350+</b><span class="mute">позиций</span></div><div data-r><b>150</b><span class="mute">организаций</span></div><div data-r><b>3</b><span class="mute">пункта проката</span></div></div></div></section>
<section class="sec dark"><div class="wrap">{shead("02","Зачем брать <em>напрокат</em>")}<div class="rows" data-g>
{"".join(f'<div class="row" data-r style="grid-template-columns:60px 1fr 1fr"><span class="num-l" style="color:var(--muteD)">{i+1:02d}</span><span class="t">{t}</span><span class="d">{d}</span></div>' for i,(t,d) in enumerate([("Экономия","Не нужно покупать дорогой инструмент ради одной работы."),("Место","Не нужно искать, где хранить технику после ремонта."),("Обслуживание","Масло, щётки и подшипники меняем мы."),("Ремонт","Поломки от износа больше не ваша забота."),("Проба","Возьмите модель напрокат перед покупкой и решите, подходит ли она.")]))}</div></div></section>'''+CONTACTS+FOOT)

w("contacts.html",head("Контакты / Мастер проката","Контакты")+phead("Контакты","Три пункта <em>в Гродно</em>","У каждого пункта свой телефон. Звоните туда, куда удобнее приехать.")+CONTACTS+f'''
<section class="sec"><div class="wrap">{shead("02","Реквизиты <em>для юрлиц</em>")}<div class="kv l" data-g><div data-r><span>Организация</span><b>ЧУП «Мастер Проката»</b></div><div data-r><span>УНП</span><b>591040896</b></div><div data-r><span>Юр. адрес</span><b>230029, г. Гродно, ул. Коммунальная, 32А, каб. 19</b></div><div data-r><span>Почтовый адрес</span><b>230003, г. Гродно, а/я 9</b></div><div data-r><span>Р/с</span><b>BY45 ALFA 3012 2C59 5700 1027 0000</b></div><div data-r><span>Банк</span><b>ЗАО «Альфа-Банк», БИК ALFABY2X</b></div><div data-r><span>Телефон</span><b><a href="tel:+375333539539">+375 (33) 353-95-39</a></b></div></div></div></section>'''+FOOT)
