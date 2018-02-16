цвет_фона = "#54aec7"
название_страницы = "резюме"
заголовок_1 = "Мой сайт портфолио"
заголовок_2 = "Мои контакты"
заголовок_3 = "Я в интернете"
ссылка_вк = '"https://vk.com/id260089130"' 
ссылка_githab = '"https://github.com/pupokbomzha/013"'
нижний_заголовок_2 = "Обо мне"
ссылка_картинка = '"http://lorempixel.com/400/200/sports"'
нижний_заголовок_3 = "Моя биография"
параграф_1 = "Происхождение Александра Сергеевича Пушкина идёт от разветвлённого нетитулованного дворянского рода Пушкиных, восходившего по генеалогической легенде к «мужу честну» РатшеПушкин неоднократно писал о своей родословной в стихах и прозе; он видел в своих предках образец истинной «аристократии», древнего рода, честно служившего отечеству, но не снискавшего благосклонности правителей и «гонимого»."
параграф_2 = "Дед по отцу Лев Александрович — артиллерии полковник, гвардии капитан. Отец — Сергей Львович Пушкин (1770—1848), светский острослов и поэт-любитель. Мать Пушкина — Надежда Осиповна (1775—1836), внучка Ганнибала. Дядя по отцу, Василий Львович (1766—1830), был известным поэтом круга Карамзина. Из детей Сергея Львовича и Надежды Осиповны, кроме Александра, выжили дочь Ольга (в замужестве Павлищева, 1797—1868) и сын Лев (1805—1852"

print("<!DOCTIPE>")

print("<html>")

print("<head>")
print('    <title>',название_страницы, '</title>')
print("</head>")

print('<body style="background-color:', цвет_фона, '">')
print("    <h1>", заголовок_1, "</h1>")
print("    <div>")
print("        <h2>", заголовок_2, "</h2>")
print("        <div>")
print("            <h3>", заголовок_3, "</h3>")
print("            <ul>")
print('                <li><a href=', ссылка_вк, '>Я в ВК</a></li>')
print('                <li><a href=', ссылка_githab, '>Moй репозиторий</a></li>')
print("            </ul>")
print("        </div>")
print("    </div>")
print("    <div>")
print("        <h2>", нижний_заголовок_2, "</h2>")
print("         <div>")
print("             <img src=", ссылка_картинка, 'alt="чёт картинка не грузится">')
print("         </div>")
print("         <div>")
print("             <h3>", нижний_заголовок_3, "</h3>")
print("             <p>", параграф_1, "</p>")
print("             <p>", параграф_2, "</p>")
print("         </div>")
print("    </div>")
print("</body>")
print("</html>")

