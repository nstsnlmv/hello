echo "# hello" >> README.md

git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/nstsnlmv/hello.git
git push -u origin master

…or push an existing repository from the command line
git remote add origin https://github.com/nstsnlmv/hello.git
git push -u origin master







<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<!-- saved from url=(0028)http://www.school661.spb.ru/ -->
<html><head><meta http-equiv="Content-Type" content="text/html; charset=windows-1251">
<script type="text/javascript" src="http://esir.gov.spb.ru/static/widget/js/widget.js" charset="utf-8"></script>
<script type="text/javascript">
  var total_pics_num = 28; // колличество изображений
  var interval = 5000;    // задержка между изображениями
  var time_out = 1;       // задержка смены изображений
  var i = 0;
  var timeout;
  var opacity = 100;
  function fade_to_next() {
    opacity--;
    var k = i + 1;
    var image_now = 'image_' + i;
    if (i == total_pics_num) k = 1;
    var image_next = 'image_' + k;
    document.getElementById(image_now).style.opacity = opacity/100;
    document.getElementById(image_now).style.filter = 'alpha(opacity='+ opacity +')';
    document.getElementById(image_next).style.opacity = (100-opacity)/100;
    document.getElementById(image_next).style.filter = 'alpha(opacity='+ (100-opacity) +')';
    timeout = setTimeout("fade_to_next()",time_out);
    if (opacity==1) {
      opacity = 100;
      clearTimeout(timeout);
    }
  }
  setInterval (
    function() {
      i++;
      if (i > total_pics_num) i=1;
      fade_to_next();
    }, interval
  );
</script>


<title>Школа 661 » Сведения об ОО</title>
<link href="css/style.css" rel="stylesheet" type="text/css">
<style type="text/css">
<!--
.стиль1 {
	font-family: Arial, Helvetica, sans-serif;
	font-size: 14px;
}
-->
</style>
<title>Многоуровневое раскрывающееся меню | Горизонтальные компоненты навигации на базе списков</title> 

<style> 
<!-- 


body { 
   margin : 0; 
   padding : 10px; 
   font-family: Verdana, Tahoma, arial, geneva, Helvetica, sans-serif; 
   behavior: url(csshover.htc); 
   background-color: #ffffff; 
} 

/* Горизонтальное меню */ 

div#menunav { 
   width: 100%; /* задаем ширину для div */ 
   float: center;  /* добавляем список в div */ 
   //border-top: 1px  solid  #ffffff;  /* рисуем линию поверх div */ 
   //border-bottom: 1px solid #ffffff; /* рисуем линию снизу div */ 
   font-size: 11px;  /* задаем размер шрифта */ 
   //background-color: #b3b3b3;  /* фоновый цвет div */ 
   padding: 0 0 0 30px;  /* отступ ul от края контейнера */ 
} 
div#menunav ul { 
   margin: 0px; 
   padding: 0px; 
} 
* html div#menunav ul { 
   float: left;  /* заставляет ul вместить все li */ 
   border-left: 1px solid #ffffff;  /* добавляет левую вертикальную черту к ul */ 
   margin-left: 15px;  /* IE удваивает заданное значение */ 
} 
div#menunav li { 
   float: left;   /* располагаем список по горизонтали */ 
   position: relative;  /* контекст позиционирования для раскрывающегося меню с абсолютным позиционированием */    
   list-style-type: none;  /* удаляем маркеры */ 
   background-color: #ff8100;  /* задаем фоновый цвет элементов меню */ 
   border-right: 1px solid #ffffff;  /* создаем разделительные линии между элементами li */ 
} 
div#menunav li:first-child { 
   border-left: 1px solid #ffffff;  /* первая вертикальная линия в меню */ 
} 
div#menunav a { 
   display: block;  /* пункты вложенного меню выделяются при наведении указателя */ 
   text-decoration: none;  /* удаляем подчеркивание ссылок */ 
   padding: 0px 10px 0px 10px;  /* создаем пространство с обеих сторон текста пункта меню */ 
   color: #ffffff;  /* задаем цвет шрифта */ 
} 
div#menunav a:hover { 
   color: #ff3333; 
} 
div#menunav li:hover { 
   background-color: #ffffff;  /* задает фон пунктов списка */ 
} 

/* Раскрывающееся меню */ 

div#menunav ul li ul { 
   margin: 0px; 
   position: absolute;  /* размещает выпадающий ul относительно родительского li */ 
   left: -1px;  /* выравнивает раскрывающееся меню */ 
   width: 10em; 
} 
div#menunav ul li ul li  { 
   width: 100%;  /* элементы списка заполняют контейнер (ul) */ 
   border-left: 1px solid #ffffff;  /* три стороны каждого пункта раскрывающегося меню */ 
   border-bottom: 1px solid #ffffff; 
   border-right: 1px solid #ffffff; 
} 
div#menunav ul li ul li:first-child { 
   border-top: 1px solid #ffffff;  /* верхний край раскрывающегося меню */ 
} 
body div#menunav ul li ul { 
   display: none; 
} 
div#menunav ul li:hover ul, div#menunav ul li ul:hover { 
   display: block; 
} 
* html div#menunav ul li ul {  /* добавляет верхнюю границу раскрывающегося меню для IE*/ 
   border-top: 1px solid #ffffff; 
   border-left: 0рх;  /* устраняет наследование границ ul раскрывающимся меню */ 
} 

/* Многоуровневое раскрывающееся меню */ 

body div#menunav ul li ul li ul   { 
   visibility: hidden;  /* идентично display: none */ 
   top: -1px;  /* выровнено по верхей границе пункта списка */ 
   left: 10em; 
} 
div#menunav ul li ul li:hover ul { 
   visibility: visible;  /* идентично display: block */ 
} 
div#menunav ul li ul li:hover ul li ul { 
   visibility: hidden; 
} 
div#menunav ul li ul li ul li:hover ul { 
   visibility: visible; 
} 
.стиль4 {
	font-size: 12px;
	font-weight: bold;
	color: #FFFFFF;
}

.стиль35 {
	font-weight: bold;
	color: #000000;
}
#apDiv1 {
	
	
	

}
.стиль43 {color: #000000}
.стиль44 { color: #ffffff}
.стиль45 { font-weight: bold;color: #FF8100}
.стиль47 {
	font-size: 10px;
	font-weight: bold;
	color: #FFFFFF;
}
.стиль48 {font-size: 12px}
.стиль50 {font-weight: bold; color: #FFFFFF; }
.стиль55 {font-weight: bold}
.стиль56 {font-weight: bold; color: #FF6600; }
.стиль57 {font-weight: bold; font-size: 12px;}

--> 
</style> 

<TITLE> Смена картинки</TITLE>

<SCRIPT type="text/javascript">

function up06()

{
document.mypic06.src="images/rollower/up06.gif"


}

function down06()

{

document.mypic06.src="images/rollower/cart1_06.gif"

}
function up03()

{
document.mypic03.src="images/rollower/up03.gif"


}

function down03()

{

document.mypic03.src="images/rollower/cart1_03.gif"

}

function up14()

{
document.mypic14.src="images/rollower/up14.gif"


}

function down14()

{

document.mypic14.src="images/rollower/cart1_14.gif"

}
function up10()

{

document.mypic10.src="images/rollower/up10.gif"


}

function down10()

{
document.mypic10.src="images/rollower/cart1_10.gif"

}



</SCRIPT>
</head>
<body>
<table width="998" height="3" align="center" bgcolor="ff8100">
<tr></tr>
<table></table>
<div align="center"><a href="about/dostup.html"><http://school661.spb.ru/img src="images/22.png" width="998" height="101"></a>
  
</div>
<tr> </tr>
<table cellspacing="0" cellpadding="0" class="top_bg" align="center">
<tr>
<td  valign="top" align="center"></td>
</tr>

 
</table>



<table width="998" height="43" align="center" bgcolor="ff8100">
<tr>
<td>
<div id="menunav" align="center"> 
   <ul> 
   <li><a href="http://school661.spb.ru/index.html"><strong>Главная</strong></a>  
   <ul> 
               <li><a href="http://school661.spb.ru/about/news.html">Новости</a></li> 
   </ul> 
     </li>
      <li><a href="#"><strong>Сведения об ОО</strong></a> 
            <ul> 
               <li><a href="http://school661.spb.ru/svedenya.html">Основные сведения</a></li> 
               <li><a href="http://school661.spb.ru/svedenya/struktura.html">Структура и органы управления ОУ</a></li> 
               <li><a href="http://school661.spb.ru/about/documents.html">Документы</a></li> 
               <li><a href="http://school661.spb.ru/svedenya/obrazovanie.html">Образование</a></li>
               <li><a href="http://school661.spb.ru/parents/fgos.html">Образовательные стандарты</a></li>
                <li><a href="http://school661.spb.ru/parents/administration.html">Руководство. Педагогический  (научно-педагогический состав)</a></li>
               <li><a href="http://school661.spb.ru/about/info.html">Материально-техническое обеспечение и оснащенность образовательного процесса</a> 
              <li><a href="http://school661.spb.ru/about/mt.html">Стипендии и иные виды мат. поддержки </a></li>
                     <li><a href="http://school661.spb.ru/club/odod.html">Платные образовательные услуги</a></li>
                     <li><a href="http://school661.spb.ru/about/fd.html">Финансово-хозяйственная деятельность</a></li> 
                     <li><a href="http://school661.spb.ru/about/informatizacia.html">Вакантные места</a></li>
                                       
                </li> 
                 </li>
                
                
                
                   
                
              
              
                
               <li><a href="http://school661.spb.ru/informatizacia.html">Информатизация</a></li>
           </ul> 
     </li> 
      <li><a href="#"><strong>Учебная работа</strong></a> 
            <ul> 
               
               
               <li><a href="http://school661.spb.ru/parents/gia.html"> ГИА Итоговая аттестация</a>
                  <ul> 
                     <li><a href="http://school661.spb.ru/parents/9gia.html">9 классы</a></li> 
                     <li><a href="http://school661.spb.ru/parents/11gia.html">11 классы</a></li> 
                     <li><a href="http://school661.spb.ru/parents/1gia.html">Выпускникам прошлых лет</a> 
                     <li><a href="http://school661.spb.ru/parents/sochgia.html">Итоговое сочинение</a>
                  </ul> </li>
               
               <li><a href="http://school661.spb.ru/dsad/dsad.html" onFocus="href=&quot;http://school661.spb.ru/dsad/dsad.html">Отделение дошкольного образования детей</a> 
               <ul>
               <li><a href="http://school661.spb.ru/dsad/strvosp.html" >Страницы воспитателей</a></li>
<li><a href="http://school661.spb.ru/dsad/first.html">Будущему первокласснику</a></li>
<li><a href="http://school661.spb.ru/dsad/exibition.html">Новости</a></li>
<li><a href="http://school661.spb.ru/dsad/prog.html">Программы</a></li>
<li><a href="http://school661.spb.ru/dsad/dsad.html" class="active">Информация</a></li>
               
               </ul>
               </li>
               
               <li><a href="http://school661.spb.ru/elementary/schedule.html">Начальная школа</a></li> 
               <li><a href="http://school661.spb.ru/5-9/info.html">Основная школа</a></li> 
               <li><a href="http://school661.spb.ru/10-11/schedule.html">Средняя школа</a></li> 
               <li><a href="http://school661.spb.ru/about/dist.html">Дистанционное обучение</a></li>
               <li><a href="http://school661.spb.ru/about/dostup.html">Доступная среда</a></li>
               <li><a href="http://school661.spb.ru/club/club.html">Отделение дополнительного образования детей</a></li>
               
               
               <li><a href="http://school661.spb.ru/about/rezults.html">Конкурсы и олимпиады</a></li>
               <li><a href="http://school661.spb.ru/about/rezults.html">Достижения</a></li>
            </ul> 
     </li> 
      <li><a href="http://school661.spb.ru/parents/vospitanie.html"><strong>Воспитательная работа</strong></a> 
            <ul> 
               <li><a href="http://school661.spb.ru/parents/vospitanie.html">Воспитание</a>
               <ul> 
                     <li><a href="http://school661.spb.ru/neva_wawe/index.html">ДОО Невская волна</a></li> 
                     <li><a href="http://school661.spb.ru/parents/kalendar.html">Календарь знаменательных дат</a></li> 
                     <li><a href="http://school661.spb.ru/parents/mchs.html">МЧС</a> 
               </ul>
               </li> 
               <li><a href="http://school661.spb.ru/parents/zdorovie.html">Служба здоровья</a></li>
                <li><a href="http://school661.spb.ru/lager.html">Лагерь "Бригантина"</a></li>
               <li><a href="http://school661.spb.ru/parents/sochsluzba.html">Социальная служба</a></li> 
               <li><a href="http://school661.spb.ru/parents/support.html">Служба сопровождения</a></li> 
               <li><a href="http://school661.spb.ru/parents/proforient.html">Профориентация</a></li> 
            </ul> 
     </li> 
      <li><a href="#"><strong>Ученик</strong></a> 
            <ul> 
               <li><a href="http://school661.spb.ru/about/mode.html">Внутренний распорядок</a></li> 
               <li><a href="http://school661.spb.ru/parents/pozbez.html">Пожарная безопасность</a></li> 
               <li><a href="http://school661.spb.ru/parents/infobez.html">Информационная  безопасность</a></li> 
               <li><a href="http://school661.spb.ru/parents/obrazovres.html">Образовательные ресурсы</a></li> 
               
            </ul> 
     </li> 
   
   <li><a href="http://school661.spb.ru/parents/classes.html"><strong>Родители</strong></a> 
            <ul> 
            <li><a href="http://school661.spb.ru/about/ureg.html">Урегулирование споров</a></li>
               <li><a href="http://school661.spb.ru/elementary/priem.html">Прием в школу</a></li> 
               <li><a href="http://school661.spb.ru/elementary/1class.html">Прием в 1 класс</a></li> 
               <li><a href="http://school661.spb.ru/parents/prava.html">Права и обязанности</a></li> 
               <li><a href="http://school661.spb.ru/parents/forma.html">Школьная форма</a></li>
               <li><a href="http://school661.spb.ru/parents/diet.html">Школьное питание</a></li> 
               <li><a href="http://school661.spb.ru/about/dnevnik.html">Электронный дневник</a></li>
               <li><a href="http://school661.spb.ru/parents/sochsluzba.html">Соц. поддержка</a></li>               
               <li><a href="http://school661.spb.ru/about/anti.html">Антикоррупция</a></li>
            </ul> 
     </li>
   <li><a href="#"><strong>Учитель</strong></a> 
            <ul> 
               <li><a href="http://school661.spb.ru/parents/teachers.html">Коллектив школы</a></li> 
               <li><a href="http://school661.spb.ru/teachers/attestacia.html">Аттестация</a></li> 
               <li><a href="http://school661.spb.ru/teachers/mo.html">МО</a></li> 
               <li><a href="http://school661.spb.ru/teachers/strteacher.html">Страницы учителей</a></li> 
            </ul> 
     </li>
   <li><a href="http://school661.spb.ru/about/museum.html"><strong>Музей</strong></a> </li>
           
     
   <li><a href="http://school661.spb.ru/kontakt.html"><strong>Контакты</strong></a>  </li>
    
   </ul> 
</div> 
</td>
</tr>
</table>
</td>
</tr>
</tbody></table>

<table width="985" align="center" cellpadding="0" cellspacing="0" class="content_bg">
<tbody><tr>
<td width="223" valign="top" class="menu"><p class="стиль55 стиль6 стиль12 стиль11">&nbsp;</p>
<p align="center" class="стиль8 стиль4"><a href="http://school661.spb.ru/about/znak.html" class="стиль45">МОНИТОРИНГ УДОВЛЕТВОРЕННОСТИ</a></p>
<p align="center" class="стиль8 стиль4"><em><br>
  </em></p>
<p align="center" class="стиль43"><strong class="стиль45">осенние каникулы</strong><span class="стиль45"> -</span>  <span class="стиль35">26.10.19 - 02.11.19</span></p>
<p align="center" class="стиль43"><strong class="стиль45">зимние каникулы</strong> - <span class="стиль35">28.12.19 - 11.01.20</span></p>
<p align="center" class="стиль43"><span class="стиль45">весенние каникулы -</span> <span class="стиль35">21.03.20- 28.03.20</span></p>
<p align="center" class="стиль45">доп. каникулы первоклассников </p>
<p align="center" class="стиль35">03.02.20 - 09.02.20</p>
<p align="center" class="стиль43"><strong class="стиль45">Учебный год заканчивается </strong><span class="стиль35">25.05.2020</span></p>
<p class="стиль8 стиль4"><a href="http://school661.spb.ru/kontakt.html"><img src="./images/box.png"></a></p>
<p align="center" class="стиль8 стиль4"><a href="kontakt.html" class="стиль45">электронная приемная</a></p>
<p class="стиль8 стиль4">&nbsp;</p>
<p align="center" class="стиль8 стиль4" ><span ><a href="http://k-obr.spb.ru/page/632/  "class="стиль45">Комитет по образованию Санкт-Петербурга </a></span></p>
<table width="70%" border="1">
  <tr>
    <td bgcolor="#FFFFFF" class="стиль45"><div align="center" class="стиль48">электронная библиотека школы</div></td>
  </tr>
  <tr>
    <td bgcolor="#FF8100"><div align="center"><span class="стиль47">1класс</span></div></td>
  </tr>
  <tr>
    <td bgcolor="#FF8100" class="стиль47"><div align="center">2класс</div></td>
  </tr>
  <tr>
    <td bgcolor="#FF8100" class="стиль47"><div align="center">3класс</div></td>
  </tr>
  <tr>
    <td bgcolor="#FF8100" class="стиль47"><div align="center">4класс</div></td>
  </tr>
  <tr>
    <td bgcolor="#FF8100" class="стиль47"><div align="center"><a href="library/5.html" class="стиль47">5класс</a></div></td>
  </tr>
  <tr>
    <td bgcolor="#FF8100" class="стиль47"><div align="center"><a href="library/6.html" class="стиль47">6класс</a></div></td>
  </tr>
  <tr>
    <td bgcolor="#FF8100" class="стиль47"><div align="center">7класс</div></td>
  </tr>
  <tr>
    <td bgcolor="#FF8100" class="стиль47"><div align="center"><a href="library/8.html" class="стиль47">8класс</a></div></td>
  </tr>
  <tr>
    <td bgcolor="#FF8100" class="стиль47"><div align="center"><a href="library/9.html" class="стиль47">9класс</a></div></td>
  </tr>
  <tr>
    <td bgcolor="#FF8100" class="стиль47"><div align="center"><a href="library/10.html" class="стиль47">10класс</a></div></td>
  </tr>
  <tr>
    <td bgcolor="#FF8100" class="стиль47"><div align="center"><a href="library/11.html" class="стиль47">11класс</a></div></td>
  </tr>
</table>
<p>&nbsp;</p>
</td>







<td width="760" valign="top" class="content">
  <div style="border-width:thick; border-style:groove; padding:0
px; border-color:#ff8100"><div class="стиль1" style="text-align: center;">
    <div style="border-width:thick; border-style:groove; padding:0
px; border-color:#ff8100">
      <div class="стиль1" style="text-align: center;">
        <p class="стиль45">&nbsp;</p>
        <p class="стиль45"><a href="https://rospotrebnadzor.ru/region/korono_virus/spec.php" class="стиль45">Информация короно-вирус</a></p>
        <p class="стиль45">____________________________________________________________________________</p>
        <p align="center" class="стиль45"><strong>РЕГИОНАЛЬНЫЕ</strong><br>
            <strong>ТРЕНИРОВОЧНЫЕ  МЕРОПРИЯТИЯ ГИА-9</strong> <br>
          Письмо КО СПб  №03-28-10352/19-0-0  от 03.12.2019</p>
        <table border="1" cellspacing="0" cellpadding="0">
          <tr>
            <td width="312" valign="top" class="стиль45"><br>
              ТМ ГИА-9 </td>
            <td width="350" valign="top"><p align="left" class="стиль45">Дата проведения</p></td>
          </tr>
          <tr>
            <td width="312" valign="top"><p>обществознание</p></td>
            <td width="350" valign="top"><p>22.01.2020</p></td>
          </tr>
          <tr>
            <td width="312" valign="top"><p>биология</p></td>
            <td width="350" valign="top"><p>29.01.2020</p></td>
          </tr>
          <tr>
            <td width="312" valign="top"><p>математика</p></td>
            <td width="350" valign="top"><p>06.02.2020</p></td>
          </tr>
          <tr>
            <td width="312" valign="top"><p>география</p></td>
            <td width="350" valign="top"><p>26.02.2020</p></td>
          </tr>
          <tr>
            <td width="312" valign="top"><p>русский    язык</p></td>
            <td width="350" valign="top"><p>03.03.2020</p></td>
          </tr>
          <tr>
            <td width="312" valign="top"><p>химия</p></td>
            <td width="350" valign="top"><p>12.03.2020</p></td>
          </tr>
        </table>
        <p>По русскому языку и математике ТМ обязательны для всех <a name="_GoBack"></a>обучающихся 9 классов.<br>
          По предметам - обществознание, биология, география, химия только для тех  обучающихся, которые выбрали данные предметы на ОГЭ.<br>
          Мероприятия проводятся в своих ОУ. </p>
        <p class="стиль45">__________________________________________________________________________________</p>
        <p align="center" class="стиль45">&nbsp;</p>
        <p class="стиль45"><img src="about/docs/2020/ВПР_3.jpg" alt="" width="600" height="410" /></p>
        <p align="left" class="стиль43">____________________________________________________________________________________________<br>
        </p>
        <p class="стиль45">Контингент учащихся школы</p>
        <p align="center" class="стиль35">на 01.01.2020г.- <span class="стиль45">806</span> учащихся:</p>
        <p align="center" class="стиль35">начальное общее образование(1-4)-<span class="стиль45">401</span> учащихся.</p>
        <p align="center" class="стиль35">основное общее образование(5-9)-<span class="стиль45">331</span> учащихся.</p>
        <p align="center" class="стиль35">среднее общее образование(10-11)-<span class="стиль45">74</span>  учащийся.</p>
        <p align="center" class="стиль35">Детский сад-<span class="стиль45">  134 человека. </span></p>
        <p align="center" class="стиль35">&nbsp;</p>
        <p align="center" class="стиль35">&nbsp;</p>
        </div>
    </div>
   
    <table width="704" height="502" border="0">
      <tr>
        <td>
        <div style="text-align: center;">                    <img src='http://school661.spb.ru/images/galery/1g.jpg' id="image_1" style="position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/2g.jpg' id="image_2" style="opacity: 0; filter: alpha(opacity=0);position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/3g.jpg' id="image_3" style="opacity: 0; filter: alpha(opacity=0);position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/4g.jpg' id="image_4" style="opacity: 0; filter: alpha(opacity=0);position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/5g.jpg' id="image_5" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/6g.jpg' id="image_6" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/7g.jpg' id="image_7" style="opacity: 0; filter: alpha(opacity=0); position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/8g.jpg' id="image_8" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/9g.jpg' id="image_9" style="opacity: 0; filter: alpha(opacity=0); position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/10g.jpg' id="image_10" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/11g.jpg' id="image_11" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/12g.jpg' id="image_12" style="opacity: 0; filter: alpha(opacity=0); position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/13.jpg' id="image_13" style="opacity: 0; filter: alpha(opacity=0); position: absolute; " />
            
                    <img src='http://school661.spb.ru/images/galery/14g.jpg' id="image_14" style="opacity: 0; filter: alpha(opacity=0);position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/15g.jpg' id="image_15" style="opacity: 0; filter: alpha(opacity=0); position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/16g.jpg' id="image_16" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/17g.jpg' id="image_17" style="opacity: 0; filter: alpha(opacity=0); position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/18g.jpg' id="image_18" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/19g.jpg' id="image_19" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/20g.jpg' id="image_20" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/21g.jpg' id="image_21" style="opacity: 0; filter: alpha(opacity=0);position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/22g.jpg' id="image_22" style="opacity: 0; filter: alpha(opacity=0); position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/23g.jpg' id="image_23" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/24g.jpg' id="image_24" style="opacity: 0; filter: alpha(opacity=0); position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/25g.jpg' id="image_25" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                    <img src='http://school661.spb.ru/images/galery/26g.jpg' id="image_26" style="opacity: 0; filter: alpha(opacity=0); position: absolute;" />
                    <img src='http://school661.spb.ru/images/galery/27g.jpg' id="image_27" style="opacity: 0; filter: alpha(opacity=0);position: absolute; " />
                <img src='http://school661.spb.ru/images/galery/28g.jpg' name="image_28" align="top" id="image_28" style="opacity: 0; filter: alpha(opacity=0);position: relative; " />                  </div>      </td></tr>
    </table>
   
    </div>
  </div>
  <div style="border-width:thick; border-style:groove; padding:0
px; border-color:#ff8100">
    <div class="стиль1" style="text-align: center;">
      <p align="center" class="стиль45">ПРИЕМ в 1 класс на 2020 - 2021г.</p>
      <p align="center" class="стиль35"><strong><a href="about/docs/2019/Разъяснение Прокуратуры по приему в первые классы от 22.01.2019.pdf" class="стиль45">Разъяснение Прокуратуры по приему в первые классы от 22.01.201</a></strong><a href="about/docs/2019/Разъяснение Прокуратуры по приему в первые классы от 22.01.2019.pdf" class="стиль45">9</a></p>
      <p class="стиль45"><a href="about/docs/2019/ozdorovlenie 2019.pdf" class="стиль45">Разъяснение по вопросу оздоровления детей и бесплатных путевок в  2019</a></p>
      <p class="стиль45">По плану на 2020-2021 учебный год</p>
      <p class="стиль45">набирается -  50 человек.</p>
      <p class="стиль45">на 02.03.20 - зачислено 50 человек.</p>
      <p class="стиль45">перевод из детского сада - 15</p>
      <p class="стиль45">на 02.03.20 -вакантных мест- 0</p>
      <p>&nbsp;</p>
    </div>
  </div>  
  <div style="border-width:thick; border-style:groove; padding:0
px; border-color:#ff8100">
    <div class="стиль1" style="text-align: center;">
      <div></div>
      <p class="стиль45"><strong>Уважаемые  ребята и родители, педагоги!</strong></p>
      <p class="стиль57">В нашей школе стартует проект к 75-летию  Великой Победы «Я-помню! Я-горжусь!». <br>
        По итогам проекта будет создана  школьная книга Памяти «Я-помню! Я-горжусь», в которой будут собраны рассказы учеников,  их родителей и учителей о героях, родственниках, защищавших нашу Родину во  время Великой Отечественной войны. <br>
        Для участия в проекте необходимо  выполнить работу по одной из предложенных тем:<br>
        - «Письма с фронта» (фотографии  документальных материалов, фронтовых треугольников, которые хранятся во многих  семейных архивах, рассказы о людях, которые их посылали, судьбе писем);<br>
        - «Войной опаленные строки» (стихи  собственного сочинения, проиллюстрирован<a name="_GoBack"></a>ные рисунком или  фотографией);<br>
        - «Они были ленинградцами» (истории о  судьбе и подвигах героев-ленинградцев, принимавших участие в Великой  Отечественной войне. К работе можно приложить фотографию героя рассказа);<br>
        - «Фронтовые дневники» (рассказы из  жизни жителей в период оккупации, плена, глубокого тыла, партизанских отрядов,  концлагерей и пр.);<br>
        - «У войны не детское лицо» (рассказы о  судьбе детей, участников боевых действий, участников трудового тыла);<br>
        - «Письма Победы» (сочинения, рассказы,  очерки, эссе, в произвольной форме, рассказывающие о Великой Отечественной  войне, о мужестве и героизме, о подвигах солдат и простых людей);<br>
        -   «Я рисую Победу!» (рисунки, выполненные на любом материале (ватман,  картон, холст и т.д.) и исполнены в любой технике рисования (масло, акварель,  гуашь, цветные карандаши, мелки, компьютерная графика и т. д.). На конкурс  направлять фотографию(ии) рисунка(ов) или отсканированный вариант.<br>
        В работе обязательно указывается имя и фамилия, возраст и класс автора  (группы авторов), а также название и тема сочинения.<br>
        Требования к оформлению:<br>
        К рассмотрению принимаются работы,  соответствующие завяленной тематике и выполненные в соответствии с  оформительскими требованиями:<br>
        Текст объемом до 2,5 тыс. знаков с  пробелами набирается в программе MS Word шрифтом TimesNewRoman, 14 кегль. Обязательно  наличие заголовка.<br>
        Требования к иллюстрациям: архивные фотоматериалы или иллюстрации  вертикальной, или горизонтальной ориентации должны быть отсканированы, а не  сфотографированы. Формат фотографий или иллюстраций — jpeg, png или tiff.<br>
        Работы принимаются до 20 марта 2020 года.</p>
      <p><span class="стиль57"><br>
        </span><br>
        <br>
        <br>
        <br>
        <br>
        <br>
      </p>
      <p><span class="стиль45"><br>
      </span></p>
      <p>&nbsp;</p>
    </div>
  </div></td>
</tr>
</tbody></table>

<table height="199" align="center" cellpadding="0" cellspacing="0" bgcolor="#FF8100"  class="bottom_bg">
<tbody><tr>
<td valign="top"><a href="karta.html" class="стиль50">Карта сайта</a><br>
  <table width="100%" style="border:#003366">
    <tbody>
      <tr>
        <td  valign="top" width="20%"  ><a href="http://минобрнауки.рф//"><img src="../images/mon.gif" alt="4"></a></td>
        <td  valign="top" width="20%"  ><a href="http://petersburgedu.ru///"><img src="../images/peterobr.jpg" alt="5"></a></td>
        <td  valign="top" width="20%"  ><a href="http://www.spbtolerance.ru//"><img src="../images/spbtolerance.jpg" alt="9" width="120" height="60
  "></a></td>
        <td  valign="top" width="20%"  ><a href="http://www.obrnadzor.gov.ru//"><img src="../images/ron.gif" alt="7"></a></td>
        <td  valign="top" width="20%"  ><a href="http://www.primpms.ru//"><img src="../images/primpms.png" alt="6"></a></td>
      <tr>
        <td  valign="top" width="20%"  ><a href="http://www.spbdeti.org//"><img src="../images/upolnom.gif" alt="11"></a> </td>
        <td  valign="top" width="20%"  ><a href="http://www.rustest.ru//"><img src="../images/f-obr.jpg" alt="3"></a> </td>
        <td  valign="top" width="20%"  ><a href="http://www.ege.spb.ru//"><img src="../images/ege_spb.jpg" alt="2" width="120" height="60"></a></td>
        <td  valign="top" width="20%"  ><a href="http://www.gu.spb.ru//"><img src="../images/ege.jpg" alt="1"></a> </td>
        <td  valign="top" width="20%"  ><a href="http://www.ya-roditel.ru//"><img src="../images/teldover2.jpg" alt="10"></a></td>
      </tr>
    </tbody>
  </table>  
  <p><span style="color: #ffffff
; "><span class="стиль35 стиль43"><a href="mailto:sunela@yandex.ru">Copyright © 1996- 2<span class="стиль44">8</span>.0<span class="стиль44">2</span>.201<span class="стиль44">9</span> | Школа 661</a></span></span></p>  </td>
</tr>
</tbody></table>
</table>


</body></html>

Process finished with exit code 0
